import streamlit as st
import ollama

# --- APP CONFIGURATION ---
# Setting up the page title and professional icon
st.set_page_config(page_title="DataBuddy AI", page_icon="💻", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main {
        background-color: #fafafa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONFIGURATION ---
st.sidebar.title("Settings")
st.sidebar.info("Engine: Gemma 4")
st.sidebar.markdown("""
**DataBuddy AI** An advanced tutor designed to bridge the gap between academic theory and industry-level Data Engineering.
""")

# --- MAIN INTERFACE ---
st.title("💻 DataBuddy AI")
st.write(
    "Optimize your data scripts with frontier intelligence. Paste your code for deep analysis on performance, logic, and scalability.")

# --- INPUT AND OUTPUT COLUMNS ---
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📥 Source Code")
    language = st.selectbox("Select Language", ["Python", "Java", "SQL", "C#"])
    code_input = st.text_area(f"Input {language} script:", height=400, placeholder="Paste your code here...")

# --- PROCESSING ENGINE ---
if st.button("Analyze Code"):
    if code_input:
        with st.spinner("Gemma 4 is processing your request..."):
            try:
                # System Prompt: Defining a global, expert persona
                system_prompt = (
                    "You are an expert Data Engineer and Computer Science Mentor. "
                    "Analyze the code provided for: \n"
                    "1. Logic and syntax errors.\n"
                    "2. Algorithmic efficiency (Time/Space Complexity).\n"
                    "3. Data Engineering best practices (Vectorization, Memory management).\n"
                    "4. Statistical validity.\n"
                    "Provide clear, actionable feedback with code examples where necessary."
                )

                # Interacting with the local Gemma 4 model via Ollama
                response = ollama.chat(model='gemma4', messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': f"Language: {language}\nCode:\n{code_input}"},
                ])

                with col2:
                    st.markdown("### 🚀 Professional Feedback")
                    st.success("Analysis Complete")
                    st.markdown(response['message']['content'])

            except Exception as e:
                st.error(f"Connection Error: {str(e)}")
                st.info("Check if the Gemma 4 model download in your terminal is complete and Ollama is running.")
    else:
        st.warning("Please provide code to analyze.")

# --- FOOTER ---
st.divider()
st.caption("Gemma 4 Good Hackathon Submission | Global Impact through AI Education")