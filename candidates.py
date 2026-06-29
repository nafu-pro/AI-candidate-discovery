import streamlit as st

st.title("👥 AI Candidate Discovery")

st.write("Browse AI-ranked candidates matched with your Job Description.")

st.markdown("---")

candidates = [
    {
        "name":"Sarah Johnson",
        "role":"Data Scientist",
        "score":96,
        "experience":"4 Years",
        "skills":["Python","Machine Learning","SQL","TensorFlow"]
    },
    {
        "name":"Michael Brown",
        "role":"AI Engineer",
        "score":93,
        "experience":"3 Years",
        "skills":["Python","PyTorch","Deep Learning","AWS"]
    },
    {
        "name":"Emily Davis",
        "role":"Data Analyst",
        "score":91,
        "experience":"2 Years",
        "skills":["Excel","Power BI","SQL","Python"]
    },
    {
        "name":"David Wilson",
        "role":"Backend Developer",
        "score":88,
        "experience":"5 Years",
        "skills":["Python","Django","Docker","PostgreSQL"]
    }
]

for candidate in candidates:

    with st.container():

        col1,col2=st.columns([1,4])

        with col1:
            st.image(
                "https://api.dicebear.com/7.x/initials/png?seed="+candidate["name"],
                width=90
            )

        with col2:

            st.subheader(candidate["name"])
            st.write(candidate["role"])

            st.metric("🤖 AI Match",f'{candidate["score"]}%')

            st.progress(candidate["score"]/100)

            st.write("💼 Experience :",candidate["experience"])

            st.write("### Skills")

            skill_cols=st.columns(len(candidate["skills"]))

            for i,skill in enumerate(candidate["skills"]):
                skill_cols[i].success(skill)

            colA,colB=st.columns(2)

            with colA:
                st.button(
                    "👁 View Profile",
                    key="view_"+candidate["name"]
                )

            with colB:
                st.button(
                    "⭐ Shortlist",
                    key="short_"+candidate["name"]
                )

        st.markdown("---")