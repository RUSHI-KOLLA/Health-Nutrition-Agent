# Health Nutrition Advisor Agent (Google ADK)

AI-powered health nutrition assistant built using Google ADK and Gemini models.
Provides diet suggestions and basic guidance based on user-reported symptoms.

# Features
```
-> Acts as a Nutrition Advisor
-> Provides diet suggestions for conditions like:
-> Fever
-> Acidity
-> Digestion issues
-> Low iron
-> Low sodium
-> Uses Google Search Tool (via ADK) to fetch updated information
-> Maintains session memory
-> Supports a clean ADK-based architecture
-> Includes a web UI for interaction
```

# How It Works
```
-> This agent is built on Google ADK Framework and uses:
-> Gemini Model for reasoning & diet suggestions
-> Search Tool for real-time retrieval
-> Session Memory to remember previous user inputs
-> CLI & ADK Web UI for easy access

```

# Installation
```
pip install -r requirements.txt

```

# Running the Agent
```
CLI:
   python -m adkagents.agenthealth.cli_runner
Web:
   adk web

```

# APIs & Services Used

```
-> This project uses the following APIs and services:

-> Gemini API (Google AI Studio)
     Used to generate diet suggestions, health reasoning, and intelligent responses based on user input.

-> Google CSE ID (Custom Search Engine ID)
     Used to configure and authenticate the custom search engine inside ADK for retrieving accurate real-time health and nutrition information.

-> Google Search API
     Accessed through ADK’s Search Tool to fetch relevant data, articles, and dietary insights from the web.
# Project Structure
```

```
Health-Nutrition-Agent/
│
├── adkagents/
│   └── agenthealth/
│        ├── agent.py
│        ├── cli_runner.py
│        ├── __init__.py
│
├── LICENSE
├── README.md
├── requirements.txt
└── .gitignore
```

# CLI Output - Sample interaction
<img width="1073" height="551" alt="Screenshot 2025-11-19 135159" src="https://github.com/user-attachments/assets/04d0805e-c0c5-4ec8-8d9d-edbc8775bbe7" />
<img width="1067" height="439" alt="Screenshot 2025-11-19 135147" src="https://github.com/user-attachments/assets/91b79155-2fad-4a81-8887-4cc5b838f584" />



# ADK Web - Demo Video 

https://github.com/user-attachments/assets/ea6b67d0-e9fe-4962-961a-6af67d59bffe




# Author

**Kolla Rushikesh**
GitHub: @RUSHI-KOLLA


