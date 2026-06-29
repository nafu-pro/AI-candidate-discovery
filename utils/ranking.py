from difflib import SequenceMatcher


def calculate_match_score(job_description, resume_text):
    """
    Returns similarity percentage between Job Description and Resume.
    """

    if not job_description or not resume_text:
        return 0

    score = SequenceMatcher(
        None,
        job_description.lower(),
        resume_text.lower()
    ).ratio()

    return round(score * 100, 2)