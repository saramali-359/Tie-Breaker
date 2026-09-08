import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client securely using Streamlit Secrets
client = OpenAI(api_key=st.secrets["API_KEY"])

st.set_page_config(page_title="The Tiebreaker", page_icon="⚖️")

st.title("⚖️ The Tiebreaker")
st.markdown("Enter your dilemma and let AI break the tie with data-driven analysis.")

# --- UI Inputs ---
with st.sidebar:
    st.header("Decision Context")
    decision = st.text_area("What decision are you facing?", placeholder="e.g., Moving to NYC vs. staying in Austin")
    priorities = st.text_input("What are your top priorities?", placeholder="e.g., Cost of living, Career growth")
    submit = st.button("Analyze Decision")

if submit and decision:
    with st.spinner("Processing your options..."):
        # 1. Generate Pros & Cons
        res_list = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"Create a detailed pros and cons list for: {decision}. Focus on these priorities: {priorities}."}]
        )

        # 2. Generate Comparison Table
        res_table = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"Create a markdown comparison table for: {decision}. Include rows for {priorities}."}]
        )

        # 3. Generate SWOT Analysis
        res_swot = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"Perform a SWOT analysis for: {decision}. Format it as Strengths, Weaknesses, Opportunities, and Threats."}]
        )

        # --- Display Results ---
        tab1, tab2, tab3 = st.tabs(["Pros & Cons", "Comparison Table", "SWOT Analysis"])
        
        with tab1:
            st.markdown(res_list.choices[0].message.content)
        
        with tab2:
            st.markdown(res_table.choices[0].message.content)
            
        with tab3:
            st.markdown(res_swot.choices[0].message.content)

        st.success("Analysis complete! Which way are you leaning?")
else:
    st.info("Enter your dilemma in the sidebar to get started.")
