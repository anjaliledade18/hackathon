from agents.orchestrator import run_pipeline

lead = {
    "name": "Sia jon",
    "company": "TechGig",
    "interest": "Looking for AI automation for sales",
    "budget": "High",
    "timeline": "Immediate"
}

result = run_pipeline(lead)

print("\n FINAL OUTPUT")
print(result)
