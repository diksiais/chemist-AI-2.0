import streamlit as st

# Import functions from our new modules
from prompts import (
    format_research_ideas_prompt,
    format_literature_summary_prompt,
    format_properties_prediction_prompt,
    format_final_response_prompt
)
from gemini_api import query_model
from workflow import (
    generate_research_ideas_from_ai,
    generate_literature_summary_from_ai,
    generate_properties_from_ai,
    compile_final_response_from_ai,
    perform_chemical_lookup
)
from database import init_db, save_search_history, load_search_history, delete_search_history_entry, clear_all_search_history

# Import the new session state manager and UI sections
from session_state_manager import initialize_session_state
from ui_sections import (
    render_input_details_stage,
    render_review_ideas_stage,
    render_literature_summary_stage,
    render_properties_prediction_stage,
    render_final_compilation_stage
)


# --- Streamlit UI Setup ---
st.set_page_config(page_title="AI Research Agent", page_icon="🔬", layout="centered")

st.title("🔬 AI Research Agent for Chemists")
st.markdown("Unlock new research avenues with AI-powered idea generation and workflow management.")

# Initialize the database and session state on app startup
init_db()
initialize_session_state()

# --- UI Flow based on st.session_state.stage ---

if st.session_state.stage == 'input_details':
    render_input_details_stage()
elif st.session_state.stage == 'review_ideas':
    render_review_ideas_stage()
elif st.session_state.stage == 'literature_summary':
    render_literature_summary_stage()
elif st.session_state.stage == 'properties_prediction':
    render_properties_prediction_stage()
elif st.session_state.stage == 'final_compilation':
    render_final_compilation_stage()

st.markdown("---")
st.markdown("Developed with Streamlit and Google Gemini API.")
