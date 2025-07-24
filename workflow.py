# workflow.py
import re
import streamlit as st
import requests
import io

# Import functions from other modules
from gemini_api import query_model
from prompts import (
    format_research_ideas_prompt,
    format_literature_summary_prompt,
    format_properties_prediction_prompt,
    format_final_response_prompt,
    format_refine_idea_prompt,
    format_follow_up_question_prompt,
    format_search_queries_prompt # New import
)
from chemical_lookup import fetch_chemical_info

def generate_research_ideas_from_ai(topic, goal, data):
    """
    Calls the AI model to generate research ideas and parses them into a list.
    """
    prompt = format_research_ideas_prompt(topic, goal, data)
    raw_ideas_text = query_model(prompt)

    if "⚠️ Error:" in raw_ideas_text:
        st.error(raw_ideas_text)
        return []

    # Parse the numbered list into individual ideas
    ideas_list = re.findall(r'^\d+\.\s*(.*)', raw_ideas_text, re.MULTILINE)
    if not ideas_list:
        st.warning("Could not parse ideas into a list. Displaying raw AI output.")
        return [raw_ideas_text]
    return ideas_list

def refine_single_idea_from_ai(original_idea, refinement_feedback, topic, goal, data):
    """
    Calls the AI model to refine a single research idea based on feedback.
    """
    prompt = format_refine_idea_prompt(original_idea, refinement_feedback, topic, goal, data)
    refined_idea_text = query_model(prompt)
    if "⚠️ Error:" in refined_idea_text:
        st.error(refined_idea_text)
        return original_idea # Return original if refinement fails
    return refined_idea_text

def answer_follow_up_question_from_ai(approved_idea, literature_summary, properties, user_question):
    """
    Calls the AI model to answer a follow-up question based on the current context.
    """
    prompt = format_follow_up_question_prompt(approved_idea, literature_summary, properties, user_question)
    response = query_model(prompt)
    if "⚠️ Error:" in response:
        st.error(response)
        return "Error answering question."
    return response

def suggest_search_queries_from_ai(research_idea, literature_summary):
    """
    Calls the AI model to suggest search queries based on the research idea and summary.
    """
    prompt = format_search_queries_prompt(research_idea, literature_summary)
    raw_queries_text = query_model(prompt)

    if "⚠️ Error:" in raw_queries_text:
        st.error(raw_queries_text)
        return []

    # Parse the numbered list into individual queries
    queries_list = re.findall(r'^\d+\.\s*(.*)', raw_queries_text, re.MULTILINE)
    if not queries_list:
        st.warning("Could not parse search queries into a list. Displaying raw AI output.")
        return [raw_queries_text]
    return queries_list


def generate_literature_summary_from_ai(idea):
    """
    Calls the AI model to generate a literature summary.
    """
    prompt = format_literature_summary_prompt(idea)
    summary = query_model(prompt)
    if "⚠️ Error:" in summary:
        st.error(summary)
        return "Error generating summary."
    return summary

def generate_properties_from_ai(idea):
    """
    Calls the AI model to generate properties/predictions.
    """
    prompt = format_properties_prediction_prompt(idea)
    props = query_model(prompt)
    if "⚠️ Error:" in props:
        st.error(props)
        return "Error generating properties."
    return props

def compile_final_response_from_ai(idea, literature_summary, properties):
    """
    Calls the AI model to compile the final response.
    """
    prompt = format_final_response_prompt(idea, literature_summary, properties)
    final_response_text = query_model(prompt)
    if "⚠️ Error:" in final_response_text:
        st.error(final_response_text)
        return "Error compiling final response."
    return final_response_text

def perform_chemical_lookup(name_or_cas):
    """
    Performs a chemical lookup using the chemical_lookup module.
    Also fetches the image bytes if an image URL is found.
    """
    cid, image_url, source, matched_name = fetch_chemical_info(name_or_cas)
    image_bytes = None
    if image_url:
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            image_bytes = response.content
        except requests.exceptions.RequestException as e:
            st.warning(f"Could not download chemical image from {image_url}: {e}")
            image_bytes = None
    return cid, image_url, source, matched_name, image_bytes
