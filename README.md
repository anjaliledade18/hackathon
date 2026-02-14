## Project Explanation

The AI Multi-Agent Sales Pipeline Assistant is a collaborative AI system designed to automate repetitive sales workflows. 

In traditional sales processes, teams spend significant time manually qualifying leads, drafting follow-up emails, scheduling reminders, and updating CRM systems. This project simulates a real sales team using specialized AI agents that work together under an orchestrator.

The system accepts lead information through a FastAPI endpoint and automatically:

- Qualifies leads based on intent and urgency
- Generates personalized follow-up communication
- Creates intelligent follow-up reminders
- Produces structured CRM-ready summaries

An Orchestrator Agent coordinates communication between agents, enabling an automated and intelligent workflow that reduces manual effort and improves lead conversion efficiency.

I have added demo video file inside docs folder


##  Tech Stack

- Python 3.11 — Core programming language
- FastAPI — Backend API framework
- OpenAI API — LLM-powered reasoning and content generation
- Multi-Agent Architecture— Specialized AI agents coordinated by an orchestrator
- JSON Storage — Lightweight CRM simulation
- Uvicorn — ASGI server for running FastAPI
- Git & GitHub — Version control and collaboration


## How to Run the Project

### Clone the repository

#```bash
git clone https://github.com/anjaliledade18/hackathon.git

cd hackathon/ai-sales-multiagent

##Create virtual environment:

python3 -m venv venv
source venv/bin/activate   # Mac/Linux

##Install dependencies
pip install -r requirements.txt

##Add environment variables


#Create a .env file: 


OPENAI_API_KEY=your_openai_api_key
FASTAPI_SECRET_KEY=your_fastapi_secret_key

#Run API Server
uvicorn api:app --reload

#Open API Docs
#Visit
http://127.0.0.1:8000/docs

#Run the endpoint: 
POST /run-sales-pipeline