# app.py
import streamlit as st
from views.main_view import render_field_mixer, render_step2_selection, render_step3_results
from views.style_view import load_css
from modules.gemini import get_gemini_response

from modules.prompts import (
    INITIAL_IDEAS_PROMPT, DEEP_DIVE_PROMPT, 
    SKEPTICAL_SCIENTIST_PROMPT, DREAM_TEAM_PROMPT
)

# --- Page Configuration ---
st.set_page_config(page_title="Synapse", page_icon="💡", layout="wide")
load_css()

# --- Session State Initialization ---
def initialize_session_state():
    # Using a loop for cleaner initialization
    keys_to_init = {
        'step': "GENERATE_IDEAS",
        'fields': [],
        'ideas': [],
        'selected_idea': None,
        'user_context': "",
        'deep_dive_text': "",
        'critique_text': "",
        'team_text': "",
        'context_area' : "",
    }
    for key, default_value in keys_to_init.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

initialize_session_state()

# --- Sidebar Rendering ---
with st.sidebar:
    st.title("Synapse 💡")
    st.info("Your AI partner for scientific brainstorming and analysis.")
    st.header("Settings")
    api_key = None

    try:
        if st.secrets.get("GEMINI_API_KEY"):
            api_key = st.secrets["GEMINI_API_KEY"]
            st.success("✅ API Key loaded automatically!")
    except Exception:
        pass

    if not api_key:
        st.warning("API Key not found. Please enter it below.")
        api_key = st.text_input("Enter your Google Gemini API Key", type="password", help="Get your free key from Google AI Studio")

    model_name = st.selectbox("Choose your AI Model", (
        "gemini-2.5-flash-preview-04-17",
        "gemini-2.5-flash-preview-05-20",
        "gemini-2.5-pro-preview-06-05",
        "gemini-2.5-pro-preview-05-06",
        "gemini-2.0-flash",
        "gemini-2.0-flash-lite",
        "gemini-1.5-pro",
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
        ))
    st.divider()
    if st.button("Start Over"):
        # Clear all session state to reset the app
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
    st.subheader("Built by:")
    st.write("[TriggeredCode]")

# --- Main App Controller ---
st.title("Synapse: Your AI Science Partner")

# ========= CONTROLLER FOR STEP 1 =========
if st.session_state.step == "GENERATE_IDEAS":
    render_field_mixer()
    if st.button("Spark Initial Hypotheses", type="primary", use_container_width=True):
        if not api_key:
            st.warning("Please enter your Gemini API key in the sidebar.")
        elif len(st.session_state.fields) < 2:
            st.warning("Please add at least two fields to the mix.")
        else:
            with st.spinner("Synapse is sparking ideas... ✨"):
                fields_list_str = ", ".join(st.session_state.fields)
                prompt = INITIAL_IDEAS_PROMPT.format(fields_list=fields_list_str)
                response = get_gemini_response(prompt, model_name, api_key)
                if response:
                    try:
                        clean_response = response.replace("```python", "").replace("```", "").strip()
                        st.session_state.ideas = eval(clean_response)
                        st.session_state.step = "SELECT_IDEA"
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error parsing ideas. AI response might be malformed. Error: {e}")

# ========= CONTROLLER FOR STEP 2 =========
elif st.session_state.step == "SELECT_IDEA":
    render_step2_selection()
    if st.button("Dive Deep on This Idea", type="primary", use_container_width=True):
        if not st.session_state.selected_idea:
            st.warning("Please select an idea first!")
        else:
            with st.spinner("Performing deep dive analysis... 🔬"):
                prompt = DEEP_DIVE_PROMPT.format(
                    selected_idea=st.session_state.selected_idea,
                    user_context=st.session_state.user_context if st.session_state.user_context else "None"
                )
                response = get_gemini_response(prompt, model_name, api_key)
                if response:
                    st.session_state.deep_dive_text = response
                    st.session_state.step = "SHOW_RESULT"
                    st.rerun()

# ========= CONTROLLER FOR STEP 3 =========
elif st.session_state.step == "SHOW_RESULT":
    render_step3_results()
    
    # Logic for the buttons inside the 'render_step3_results' view
    if st.session_state.get('skeptic_button'):
        with st.spinner("Hiring a skeptical scientist... 🤔"):
            prompt = SKEPTICAL_SCIENTIST_PROMPT.format(deep_dive_text=st.session_state.deep_dive_text)
            response = get_gemini_response(prompt, model_name, api_key)
            if response:
                st.session_state.critique_text = response
                st.rerun()

    if st.session_state.get('team_button'):
        with st.spinner("Assembling your dream team... 🤝"):
            prompt = DREAM_TEAM_PROMPT.format(deep_dive_text=st.session_state.deep_dive_text)
            response = get_gemini_response(prompt, model_name, api_key)
            if response:
                st.session_state.team_text = response
                st.rerun()