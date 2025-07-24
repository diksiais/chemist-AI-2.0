# session_state_manager.py
import streamlit as st

def initialize_session_state():
    """
    Initializes all necessary Streamlit session state variables.
    This function should be called once at the start of the app.
    """
    if 'idea_index' not in st.session_state:
        st.session_state.idea_index = 0
    if 'ideas' not in st.session_state:
        st.session_state.ideas = []
    if 'approved_idea' not in st.session_state:
        st.session_state.approved_idea = None
    if 'literature_summary' not in st.session_state:
        st.session_state.literature_summary = None
    if 'properties' not in st.session_state:
        st.session_state.properties = None
    if 'final_response' not in st.session_state:
        st.session_state.final_response = None
    if 'stage' not in st.session_state:
        st.session_state.stage = 'input_details' # Initial stage for user input

    # Session states for chemical lookup
    if 'chemical_query_input' not in st.session_state:
        st.session_state.chemical_query_input = ""
    if 'chemical_cid' not in st.session_state:
        st.session_state.chemical_cid = None
    if 'chemical_image_url' not in st.session_state:
        st.session_state.chemical_image_url = None
    if 'chemical_source' not in st.session_state:
        st.session_state.chemical_source = None
    if 'chemical_matched_name' not in st.session_state:
        st.session_state.chemical_matched_name = None
    if 'chemical_image_bytes' not in st.session_state:
        st.session_state.chemical_image_bytes = None
    if 'chemical_lookup_attempted' not in st.session_state:
        st.session_state.chemical_lookup_attempted = False
    if 'chemical_lookup_success' not in st.session_state:
        st.session_state.chemical_lookup_success = False

    # Session states for search history
    if 'search_history_data' not in st.session_state:
        st.session_state.search_history_data = []
    if 'selected_history_id' not in st.session_state:
        st.session_state.selected_history_id = None

    # Store initial research details for refinement context
    if 'current_topic' not in st.session_state:
        st.session_state.current_topic = ""
    if 'current_goal' not in st.session_state:
        st.session_state.current_goal = ""
    if 'current_data' not in st.session_state:
        st.session_state.current_data = ""

    # Session states for follow-up questions
    if 'follow_up_question' not in st.session_state:
        st.session_state.follow_up_question = ""
    if 'follow_up_response' not in st.session_state:
        st.session_state.follow_up_response = None

    # New: Session state for AI-suggested search queries
    if 'suggested_search_queries' not in st.session_state:
        st.session_state.suggested_search_queries = []
