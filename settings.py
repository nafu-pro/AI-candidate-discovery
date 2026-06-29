import streamlit as st

st.title("⚙️ Settings")
st.subheader("TalentIQ AI Configuration")

st.markdown("---")

st.header("🎨 Appearance")

theme = st.selectbox(
    "Choose Theme",
    ["Dark", "Light"]
)

st.write("Current Theme:", theme)

st.markdown("---")

st.header("🤖 AI Settings")

model = st.selectbox(
    "AI Model",
    [
        "TalentIQ AI v1",
        "GPT-4",
        "Gemini",
        "Claude"
    ]
)

threshold = st.slider(
    "Minimum Match Score",
    0,
    100,
    75
)

st.markdown("---")

st.header("📁 Resume Parser")

parser = st.checkbox(
    "Enable Resume Parsing",
    value=True
)

st.header("📄 Job Description")

jd = st.checkbox(
    "Enable Job Description Analysis",
    value=True
)

st.markdown("---")

if st.button("💾 Save Settings"):
    st.success("Settings Saved Successfully!")