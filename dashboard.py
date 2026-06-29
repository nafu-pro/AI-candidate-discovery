import streamlit as st
import pandas as pd

st.title("🏠 Dashboard")

st.markdown("## 👋 Welcome to TalentIQ AI")
st.write("AI Powered Candidate Discovery Platform")

st.markdown("---")

# ---------------- Metrics ----------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Candidates", "248", "+18")

with col2:
    st.metric("🎯 AI Accuracy", "96%", "+2%")

with col3:
    st.metric("🏢 Companies", "35", "+5")

with col4:
    st.metric("⚡ Hiring Speed", "-72%", "Faster")

st.markdown("---")

# ---------------- Charts ----------------

left, right = st.columns([2,1])

with left:

    st.subheader("📈 Candidate Growth")

    growth = pd.DataFrame({
        "Month":[
            "Jan","Feb","Mar","Apr","May","Jun"
        ],
        "Candidates":[
            20,45,80,120,180,248
        ]
    })

    st.line_chart(
        growth.set_index("Month")
    )

with right:

    st.subheader("🤖 AI Features")

    st.success("Resume Parsing")
    st.success("Skill Extraction")
    st.success("Candidate Ranking")
    st.success("Analytics")
    st.success("Job Description Matching")

st.markdown("---")

# ---------------- Upload ----------------

st.subheader("📄 Upload Job Description")

uploaded = st.file_uploader(
    "Choose PDF",
    type=["pdf"]
)

if uploaded:
    st.success("Job Description Uploaded Successfully!")

st.markdown("---")

# ---------------- Recent Activity ----------------

st.subheader("📝 Recent Activity")

st.info("📄 Job Description Uploaded")

st.info("👨 5 Candidate Resumes Uploaded")

st.info("🏆 2 Candidates Shortlisted")

st.info("📊 AI Analysis Completed")

st.markdown("---")

# ---------------- Top Candidate ----------------

st.subheader("🏆 Top Candidate")

col1, col2 = st.columns([1,3])

with col1:
    st.metric("AI Match", "96%")

with col2:

    st.success("""
### Rahul Sharma

✅ Python

✅ SQL

✅ Machine Learning

⭐⭐⭐⭐⭐ Highly Recommended
""")

st.markdown("---")

st.success("🚀 TalentIQ AI Dashboard Ready")