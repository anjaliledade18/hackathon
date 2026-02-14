from services.llm_service import ask_llm

def create_crm_summary(lead, qualification):

    prompt = f"""
    Create a CRM-ready summary.

    Lead: {lead}
    Qualification: {qualification}

    Include:
    - Lead intent
    - Priority
    - Suggested action
    """

    return ask_llm(prompt)
