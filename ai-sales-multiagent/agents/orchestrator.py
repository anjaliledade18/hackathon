from agents.lead_qualifier import qualify_lead
from agents.followup_agent import generate_followup
from agents.reminder_agent import create_reminder
from agents.crm_agent import create_crm_summary
from services.crm_storage import save_to_crm

def run_pipeline(lead):

    print("Qualifying lead...")
    qualification = qualify_lead(lead)

    print("Generating follow-up...")
    followup = generate_followup(lead, qualification)

    print("Creating reminder...")
    reminder = create_reminder(qualification)

    print("Creating CRM summary...")
    crm_summary = create_crm_summary(lead, qualification)

    record = {
        "lead": lead,
        "qualification": qualification,
        "followup": followup,
        "reminder": reminder,
        "crm_summary": crm_summary
    }

    save_to_crm(record)

    return record
