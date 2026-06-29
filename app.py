import streamlit as st

st.set_page_config(
    page_title="TalentIQ AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background:#0F172A;
}

.hero{
    background:linear-gradient(135deg,#2563EB,#7C3AED);
    padding:35px;
    border-radius:20px;
    color:white;
    text-align:center;
    margin-bottom:25px;
}

.card{
    background:#1E293B;
    padding:20px;
    border-radius:15px;
    border:1px solid #334155;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Hero ----------------

st.markdown("""
<div class="hero">

<h1>🤖 TalentIQ AI</h1>

<h3>AI Powered Candidate Discovery Platform</h3>

<p>Upload • Analyze • Rank • Hire</p>

</div>
""", unsafe_allow_html=True)

# ---------------- Metrics ----------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("👥 Candidates","248","+18")

with c2:
    st.metric("🎯 AI Accuracy","96%","+2%")

with c3:
    st.metric("🏢 Companies","35","+5")

with c4:
    st.metric("⚡ Hiring Time","72% Faster")

st.markdown("---")

st.subheader("🚀 Platform Overview")

left,right=st.columns([2,1])

with left:

    st.info("""
TalentIQ AI helps recruiters

✅ Upload Job Description

✅ Upload Candidate Resumes

✅ AI Resume Parsing

✅ Skill Extraction

✅ Candidate Ranking

✅ AI Recommendation
""")

with right:

    st.success("🤖 AI Ready")

    st.success("📄 Resume Parsing")

    st.success("🏆 Candidate Ranking")

    st.success("📊 Analytics")

st.markdown("---")

st.subheader("📌 Quick Start")

st.write("""
1️⃣ Open **Dashboard**

2️⃣ Upload Job Description

3️⃣ Upload Resumes

4️⃣ Analyze Candidates

5️⃣ View Analytics

6️⃣ Select Best Candidate
""")

st.markdown("---")

st.success("🎉 Welcome to TalentIQ AI")

st.markdown("---")
st.caption("Developed by Nafisa Anjum | TalentIQ AI | Hack2Skill 2026")