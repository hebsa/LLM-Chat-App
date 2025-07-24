Introduction
This document captures the detailed learning log and technical experiences encountered during the SEQATO LLM Awareness and Portfolio Development Program. It focuses on Phase 1 projects with a hands-on walkthrough of the Local LLM Chat App using Streamlit, FastAPI, and Ollama. This log provides insights into setup, development, troubleshooting, and successful implementation.
Phase 1: Project 1 – Local LLM Chat App (Ollama + Streamlit)
Setup and Tools
Installed Python, Streamlit, FastAPI, and Ollama. Set up the project folder with essential files: app.py (frontend), backend.py (FastAPI backend), requirements.txt, and README.md.
First Attempt to Run Backend
Faced a 500 Internal Server Error. Discovered the issue was due to improper handling of Ollama’s response. Initially tried to parse streaming output as static JSON, which caused failures.
Understanding Ollama Behavior
Used `ollama run mistral`, which led to the terminal locking up. Realized that for API access, `ollama serve` is required to run Ollama in background API mode on port 11434.
Streamlit and Backend Integration
Configured Streamlit to send user input to the FastAPI backend, which then called Ollama. Added error handling and made sure the backend returns a proper JSON response with the 'reply' field.
Fixing API Call and JSON Parsing
Enabled `stream=False` in the backend request to Ollama. Used `.get('response', '')` to safely parse the output and avoid JSONDecodeErrors.
Resolved Port and Server Errors
Faced port already in use errors. Identified Ollama was already running, so avoided restarting `ollama serve` again. Confirmed backend and LLM communication worked properly.
Successful End-to-End Chat App
Completed the functional chat app with UI built in Streamlit and backend served via FastAPI. Tested queries and received responses from the local model (Mistral). Project confirmed working.
Conclusion
Phase 1 of the SEQATO LLM Program enabled practical exposure to integrating Large Language Models in real-time applications. The Local LLM Chat App project provided experience in working with Streamlit, FastAPI, and local inference engines like Ollama. This learning path included system setup, error analysis, debugging, and deploying a functional AI chatbot—all critical for future LLM-based solution design.
