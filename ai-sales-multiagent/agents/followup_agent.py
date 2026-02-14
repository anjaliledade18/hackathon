from services.llm_service import ask_llm

def generate_followup(lead, qualification):

    prompt = f"""
    Write a professional sales follow-up email.

    Lead: {lead}
    Qualification: {qualification}

    Keep it short and friendly.
    """

    return ask_llm(prompt)
