from services.llm_service import ask_llm

def qualify_lead(lead):

    prompt = f"""
    You are a sales qualification expert.

    Lead details:
    {lead}

    Classify as:
    - Hot
    - Warm
    - Cold

    Give short reasoning.
    """

    result = ask_llm(prompt)
    return result
