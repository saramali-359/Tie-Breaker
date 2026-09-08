import streamlit as st
import google.generativeai as genai

# Initialize the Google Gemini client securely using Streamlit Secrets
genai.configure(api_key=st.secrets["API_KEY"])

st.set_page_config(page_title="The Tiebreaker", page_icon="⚖️")

st.title("⚖️ The Tiebreaker")
#st.warning(f"🔍 Diagnostic: My API key has {len(st.secrets['API_KEY'])} characters and starts with {st.secrets['API_KEY'][:4]}")
st.markdown("Enter your dilemma and let AI break the tie with data-driven analysis.")

# --- UI Inputs ---
with st.sidebar:
    st.header("Decision Context")
    decision = st.text_area("What decision are you facing?", placeholder="e.g., Moving to NYC vs. staying in Austin")
    priorities = st.text_input("What are your top priorities?", placeholder="e.g., Cost of living, Career growth")
    submit = st.button("Analyze Decision")

if submit and decision:
    with st.spinner("Processing your options..."):
        # Initialize the free-tier Gemini model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 1. Generate Pros & Cons
        res_list = model.generate_content(f"Create a detailed pros and cons list for: {decision}. Focus on these priorities: {priorities}.")

        # 2. Generate Comparison Table
        res_table = model.generate_content(f"Create a markdown comparison table for: {decision}. Include rows for {priorities}.")

        # 3. Generate SWOT Analysis
        res_swot = model.generate_content(f"Perform a SWOT analysis for: {decision}. Format it as Strengths, Weaknesses, Opportunities, and Threats.")

        # --- Display Results ---
        tab1, tab2, tab3 = st.tabs(["Pros & Cons", "Comparison Table", "SWOT Analysis"])
        
        with tab1:
            st.markdown(res_list.text)
        
        with tab2:
            st.markdown(res_table.text)
            
        with tab3:
            st.markdown(res_swot.text)

        st.success("Analysis complete! Which way are you leaning?")
else:
    st.info("Enter your dilemma in the sidebar to get started.")
