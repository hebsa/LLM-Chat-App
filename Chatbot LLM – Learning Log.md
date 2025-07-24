# SEQATO LLM Awareness and Portfolio Development Program - Learning Log

## Introduction

This document captures the detailed learning log and technical experiences encountered during the SEQATO LLM Awareness and Portfolio Development Program. It focuses on Phase 1 projects with a hands-on walkthrough of the Local LLM Chat App using Streamlit, FastAPI, and Ollama. This log provides insights into setup, development, troubleshooting, and successful implementation.

## Phase 1: Project 1 – Local LLM Chat App (Ollama + Streamlit)

### Setup and Tools

* Installed Python, Streamlit, FastAPI, and Ollama.
* Set up the project folder with essential files:

  * `app.py` (frontend)
  * `backend.py` (FastAPI backend)
  * `requirements.txt`
  * `README.md`

### First Attempt to Run Backend

* Faced a **500 Internal Server Error**.
* Issue caused by improper handling of Ollama’s response.
* Initially tried to parse streaming output as static JSON, leading to failures.

### Understanding Ollama Behavior

* Used `ollama run mistral`, which led to terminal locking up.
* Realized `ollama serve` is required for API access, running in background API mode on port `11434`.

### Streamlit and Backend Integration

* Configured Streamlit to send user input to the FastAPI backend.
* Backend calls Ollama and returns a JSON response with the `reply` field.
* Added error handling to ensure robust communication.

### Fixing API Call and JSON Parsing

* Enabled `stream=False` in backend requests to Ollama.
* Used `.get('response', '')` to safely parse outputs and avoid `JSONDecodeError`.

### Resolved Port and Server Errors

* Encountered **port already in use** errors.
* Identified Ollama was already running and avoided restarting `ollama serve` again.
* Confirmed stable backend and LLM communication.

### Successful End-to-End Chat App

* Completed a functional chat app with a Streamlit-based UI and FastAPI backend.
* Tested queries and received responses from the local model (Mistral).
* Project confirmed as working.

## Conclusion

Phase 1 of the SEQATO LLM Program enabled practical exposure to integrating Large Language Models in real-time applications. The Local LLM Chat App project provided experience in working with Streamlit, FastAPI, and local inference engines like Ollama. This learning path included system setup, error analysis, debugging, and deploying a functional AI chatbot—all critical for future LLM-based solution design.
