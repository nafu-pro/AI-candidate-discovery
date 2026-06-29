import streamlit as st
import pandas as pd

st.title("📊 Analytics Dashboard")
st.subheader("AI Recruitment Analytics")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Match Score", "92%")

with col2:
    st.metric("Total Candidates", "248")

with col3:
    st.metric("Selected", "15")

st.markdown("---")

st.subheader("📈 Skills Distribution")

skills = pd.DataFrame({
    "Skill": ["Python", "Machine Learning", "SQL", "Java", "C++"],
    "Candidates": [90, 72, 65, 45, 58]
})

st.bar_chart(skills.set_index("Skill"))

st.markdown("---")

st.subheader("📅 Monthly Hiring")

monthly = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Candidates": [25, 40, 60, 95, 120]
})

st.line_chart(monthly.set_index("Month"))

st.success("✅ Analytics Loaded Successfully")