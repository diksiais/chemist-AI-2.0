# prompts.py

def format_research_ideas_prompt(topic, goal, data, uploaded_text_context=None):
    """
    Formats the user's input into a prompt for generating research ideas.
    Includes optional uploaded text context.
    """
    context_section = ""
    if uploaded_text_context:
        context_section = f"""
    --- Additional Context from Uploaded Papers ---
    {uploaded_text_context}
    --- End of Additional Context ---

    Please carefully read and incorporate the information from the "Additional Context from Uploaded Papers"
    into your idea generation.
    """

    prompt_text = f"""
    You are an AI research assistant specializing in chemistry.
    Your task is to generate innovative research ideas based on the provided information.

    Research Topic: {topic}
    Research Goal: {goal}
    Existing Data: {data}
    {context_section}

    Please provide 3-7 distinct, detailed, and actionable research ideas.
    Format your response as a numbered list.
    Example:
    1. Idea one description.
    2. Idea two description.
    3. Idea three description.
    """
    return prompt_text

def format_refine_idea_prompt(original_idea, refinement_feedback, topic, goal, data, uploaded_text_context=None):
    """
    Formats a prompt for refining a specific research idea based on user feedback.
    Includes optional uploaded text context.
    """
    context_section = ""
    if uploaded_text_context:
        context_section = f"""
    --- Additional Context from Uploaded Papers ---
    {uploaded_text_context}
    --- End of Additional Context ---

    Please carefully read and consider the information from the "Additional Context from Uploaded Papers"
    when refining the idea.
    """

    prompt_text = f"""
    You are an AI research assistant specializing in chemistry.
    A user wants to refine a previously generated research idea.

    Original Research Topic: {topic}
    Original Research Goal: {goal}
    Original Existing Data: {data}
    {context_section}

    Original Research Idea to Refine:
    {original_idea}

    User's Refinement Feedback:
    {refinement_feedback}

    Please refine the "Original Research Idea to Refine" based on the user's feedback.
    Provide the refined idea as a single, detailed paragraph. Focus on incorporating the feedback
    while maintaining the scientific rigor and actionable nature of the idea.
    """
    return prompt_text


def format_literature_summary_prompt(research_idea, uploaded_text_context=None):
    """
    Formats a prompt for generating a literature summary for a given research idea.
    Includes optional uploaded text context.
    """
    context_section = ""
    if uploaded_text_context:
        context_section = f"""
    --- Additional Context from Uploaded Papers ---
    {uploaded_text_context}
    --- End of Additional Context ---

    Please carefully read and use the information from the "Additional Context from Uploaded Papers"
    as primary reference for the literature summary. Synthesize it with your general knowledge.
    """

    prompt_text = f"""
    Based on the following research idea, provide a concise literature summary.
    Focus on key existing research, relevant methodologies, and potential gaps this idea addresses.
    {context_section}
    Research Idea: {research_idea}

    Please provide a summary of approximately 200-300 words.
    """
    return prompt_text

def format_properties_prediction_prompt(research_idea):
    """
    Formats a prompt for predicting properties or suggesting experimental details for a research idea.
    """
    prompt_text = f"""
    For the following research idea, suggest potential chemical properties (e.g., CAS numbers of key compounds, predicted reactivity, stability)
    or outline a conceptual approach for performance prediction. If applicable, suggest new ligands or materials.

    Research Idea: {research_idea}

    Provide your response in a structured format, perhaps using bullet points or clear headings for different aspects.
    """
    return prompt_text

def format_final_response_prompt(idea, literature_summary, properties):
    """
    Formats a prompt to compile a final research proposal summary.
    """
    prompt_text = f"""
    Based on the following approved research idea, literature summary, and predicted properties,
    compile a concise final research proposal overview.

    Research Idea: {idea}
    Literature Summary: {literature_summary}
    Predicted Properties/Approach: {properties}

    The final response should be a comprehensive overview suitable for a preliminary proposal,
    covering the need, solution, differentiation, and benefit (NSDB).
    Also, suggest what kind of experimental details and analysis data in graphs would be relevant.
    """
    return prompt_text

def format_follow_up_question_prompt(approved_idea, literature_summary, properties, user_question, uploaded_text_context=None):
    """
    Formats a prompt for answering a follow-up question based on the current research context.
    Includes optional uploaded text context.
    """
    context = f"""
    Current Research Context:
    Approved Research Idea: {approved_idea}
    Literature Summary: {literature_summary}
    Predicted Properties/Approach: {properties}
    """
    
    context_section = ""
    if uploaded_text_context:
        context_section = f"""
    --- Additional Context from Uploaded Papers ---
    {uploaded_text_context}
    --- End of Additional Context ---

    Please prioritize information from the "Additional Context from Uploaded Papers" if relevant to the question.
    """

    prompt_text = f"""
    You are an AI research assistant specializing in chemistry.
    A user has a follow-up question regarding their ongoing research.

    Please consider the following context from the user's research:
    {context}
    {context_section}

    User's Question: {user_question}

    Please provide a concise and helpful answer to the user's question, drawing upon the provided context and general chemical knowledge.
    If the question is outside the scope of the provided context or general chemistry, please state that.
    """
    return prompt_text

def format_search_queries_prompt(research_idea, literature_summary, uploaded_text_context=None):
    """
    Formats a prompt to suggest relevant search queries for external databases.
    Includes optional uploaded text context.
    """
    context_section = ""
    if uploaded_text_context:
        context_section = f"""
    --- Additional Context from Uploaded Papers ---
    {uploaded_text_context}
    --- End of Additional Context ---

    Consider the terminology and key concepts found in the "Additional Context from Uploaded Papers"
    when formulating the queries.
    """

    prompt_text = f"""
    You are an AI research assistant specializing in chemistry.
    Based on the following research idea and its preliminary literature summary,
    and potentially additional context from uploaded papers,
    suggest 3-5 specific and effective search queries that a chemist could use
    on academic databases like PubMed, Scopus, or Google Scholar to find more
    relevant papers.

    Research Idea: {research_idea}
    Preliminary Literature Summary: {literature_summary}
    {context_section}

    Provide the queries as a numbered list. Each query should be a concise string.
    Example:
    1. "MOF CO2 capture selectivity"
    2. "post-synthetic modification amine functionalization"
    3. "zeolitic imidazolate frameworks gas separation"
    """
    return prompt_text
