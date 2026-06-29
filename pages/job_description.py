import streamlit as st
from utils.parser import extract_text_from_pdf

st.title("📄 Job Description Analysis")
st.subheader("Upload and Analyze Job Description")

st.markdown("---")

uploaded_jd = st.file_uploader(
    "📂 Upload Job Description (PDF)",
    type=["pdf"]
)

st.markdown("### OR")

job_text = st.text_area(
    "✍️ Paste Job Description Here",
    height=220,
    placeholder="Paste the complete job description..."
)

st.markdown("---")

if uploaded_jd is not None:

    jd_text = extract_text_from_pdf(uploaded_jd)

    st.success("✅ Job Description Uploaded Successfully!")

    st.subheader("📄 Extracted Text")

    st.text_area(
        "",
        jd_text,
        height=250
    )

elif job_text:

    st.success("✅ Job Description Added!")

    st.subheader("📄 Job Description")

    st.text_area(
        "",
        job_text,
        height=250
    )

st.markdown("---")

st.subheader("🧠 Required Skills")

skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "Pandas",
    "Scikit-learn",
    "Communication"
]

for skill in skills:
    st.success(f"✔ {skill}")