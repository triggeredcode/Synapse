# views/main_view.py
import streamlit as st

def render_field_mixer():
    """Renders the UI for Step 1: Adding and selecting example fields."""
    # This function remains the same as before
    st.write("### Step 1: Mix Your Fields of Study")
    col1, col2 = st.columns([3, 1])
    with col1:
        new_field = st.text_input("Add a scientific field to the mix:", placeholder="e.g., Artificial Intelligence", label_visibility="collapsed")
    with col2:
        if st.button("Add Field", use_container_width=True):
            if new_field and new_field not in st.session_state.fields:
                st.session_state.fields.append(new_field)
                st.rerun()

    if st.session_state.fields:
        st.write("#### Current Mix:")
        # Render fields in a more compact way
        field_cols = st.columns(6)
        for i, field in enumerate(st.session_state.fields):
            with field_cols[i % 6]:
                if st.button(f"❌ {field}", key=f"remove_{i}", use_container_width=True):
                    st.session_state.fields.pop(i)
                    st.rerun()
    
    st.divider()
    st.write("##### Or, try an example mix:")
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8 = st.columns(2)

    with col1:
        if st.button("Neuroscience + LLMs", use_container_width=True):
            st.session_state.fields = ["Neuroscience", "Large Language Models"]; st.rerun()
    with col2:
        if st.button("Marine Biology + Robotics", use_container_width=True):
            st.session_state.fields = ["Marine Biology", "Robotics"]; st.rerun()
    with col3:
        if st.button("Nutrition + Epigenetics + ML", use_container_width=True):
            st.session_state.fields = ["Nutrition", "Epigenetics", "Machine Learning"]; st.rerun()
    with col4:
        if st.button("Quantum Physics + AI", use_container_width=True):
            st.session_state.fields = ["Quantum Physics", "Artificial Intelligence"]; st.rerun()
    with col5:
        if st.button("Climate Science + Genomics", use_container_width=True):
            st.session_state.fields = ["Climate Science", "Genomics"]; st.rerun()
    with col6:
        if st.button("Genomics + AI Ethics", use_container_width=True):
            st.session_state.fields = ["Genomics", "AI Ethics"]; st.rerun()
    with col7:
        if st.button("Synthetic Biology + AI + Robotics", use_container_width=True):
            st.session_state.fields = ["Synthetic Biology", "Artificial Intelligence", "Robotics"]; st.rerun()
    with col8:
        if st.button("Cognitive Science + Robotics", use_container_width=True):
            st.session_state.fields = ["Cognitive Science", "Robotics"]; st.rerun()


def render_step2_selection():
    """Renders the UI for Step 2, now with a file uploader for context."""
    
    st.write("### 💡 Select an Idea & Add Context")
    
    st.session_state.selected_idea = st.radio(
        "Which hypothesis sparks your interest the most?",
        options=st.session_state.ideas,
        index=None,
        key="idea_selection"
    )

    st.divider()
    
    st.write("#### Add Your Context (Optional)")
    st.write(
        "Provide your own knowledge to guide the analysis. "
        "You can either upload a text/markdown file or paste directly into the box below."
    )

    # The new file uploader widget
    uploaded_file = st.file_uploader(
        "Upload a context file", 
        type=['txt', 'md'],
        label_visibility="collapsed"
    )

    # The text area for context. We give it a unique key.
    # Its content will be our "source of truth".

    initial_text = st.session_state.get('context_area', '')
    
        # 2. If a new file is uploaded, its content overrides the initial text.
    if uploaded_file is not None:
        try:
            initial_text = uploaded_file.getvalue().decode("utf-8")
            st.info("✅ File content loaded into the text area.")
        except Exception as e:
            st.error(f"Error reading file: {e}")

    # 3. Draw the text_area ONCE, with the correct value.
    # The return value of the widget updates the state for the *next* run.
    st.session_state.user_context = st.text_area(
        "Paste context here, or edit the content from your uploaded file:",
        value=initial_text, # Use the determined initial value
        key='context_area',
        height=200
    )

def render_step3_results():
    """Renders the UI for Step 3 using containers for a card-like layout."""
    
    st.write("### 📜 Your Detailed Research Proposal")
    
    with st.container(border=True):
        st.markdown(st.session_state.deep_dive_text)
        st.download_button(
            "📄 Download Analysis", 
            st.session_state.deep_dive_text, 
            file_name="synapse_analysis.md"
        )
    
    st.write("### 🔬 The Crucible: Strengthen Your Idea")
    
    # Feature 1: Skeptical Scientist
    with st.container(border=True):
        st.subheader("Red Team Analysis (Peer Review)")
        st.write("Find potential flaws, hidden assumptions, and weaknesses in your proposal.")
        if st.button("Critique this Hypothesis", key="skeptic_button", use_container_width=True):
            # Logic is in app.py
            pass
        if st.session_state.critique_text:
            st.info(st.session_state.critique_text)

    # Feature 2: Dream Team Builder
    with st.container(border=True):
        st.subheader("Assemble Your 'Dream Team'")
        st.write("Identify the key experts you'll need to turn this idea into reality.")
        if st.button("Suggest Collaborators", key="team_button", use_container_width=True):
            # Logic is in app.py
            pass
        if st.session_state.team_text:
            st.success(st.session_state.team_text)