# 🤖 Multi-Step Autonomous AI Task Agent

## Overview

**Multi-Step Autonomous AI Task Agent** is an Agentic AI application that autonomously plans, executes, and summarizes complex user-defined tasks using **LangGraph, LangChain, Groq LLM, ChromaDB, and Streamlit**.
The system follows a multi-step workflow where an AI planner decomposes a high-level goal into actionable tasks, executes them sequentially, leverages Retrieval-Augmented Generation (RAG) for contextual understanding, and generates a final consolidated report.

---

## Problem Statement

Traditional LLM applications typically provide single-step responses and struggle with handling complex tasks that require:

- Planning and task decomposition
- Context retention across multiple steps
- Reasoning over external knowledge sources
- Structured report generation

Users often need to manually break down goals, search documents, maintain context, and combine findings into a final output. This process is inefficient and time-consuming.

---

## Objective

The primary objective of this project is to build an autonomous AI system capable of:

- Understanding a user's high-level goal
- Automatically generating a sequence of relevant tasks
- Executing tasks independently while maintaining context
- Retrieving information from uploaded documents using RAG
- Producing accurate, context-aware responses
- Generating a structured final summary

---

## Tech Stack

### Programming Language
- Python

### LLM & Agent Framework
- LangChain
- LangGraph
- Groq API
- Llama 3.3 70B Versatile

### Retrieval-Augmented Generation (RAG)
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers

### Document Processing
- PyPDFLoader
- Recursive Character Text Splitter

### Frontend
- Streamlit

### Environment Management
- Python Dotenv

---

## Workflow

### Step 1: User Input
The user enters a goal through the Streamlit interface and optionally uploads a PDF document.

### Step 2: Knowledge Base Creation
If a PDF is uploaded:

- PDF is loaded using PyPDFLoader
- Text is split into chunks
- Embeddings are generated
- Chunks are stored in ChromaDB

### Step 3: Context Retrieval
Relevant document chunks are retrieved using semantic similarity search.

### Step 4: Planner Agent
The Planner Agent analyzes:

- User Goal
- Retrieved Context

It generates 3–5 sequential tasks required to accomplish the objective.

### Step 5: Executor Agent
The Executor Agent:

- Executes one task at a time
- Uses retrieved document context
- References previous task outputs
- Stores results in workflow memory

### Step 6: State Management
LangGraph maintains:

- User Goal
- Retrieved Context
- Planned Tasks
- Completed Tasks
- Task Outputs
- Current Task

This enables stateful multi-step reasoning.

### Step 7: Summarizer Agent
After all tasks are completed, the Summarizer Agent combines outputs and generates a final report.

### Step 8: Result Display
The application displays:

- Task Outputs
- Execution Results
- Final Summary

through the Streamlit interface.

---

## Outcome

The project successfully demonstrates:

- Autonomous task planning and execution
- Multi-step reasoning using LangGraph workflows
- Context-aware response generation through RAG
- Stateful agent orchestration
- Semantic document retrieval using vector databases
- Automated report generation

The system transforms a single user goal into a complete autonomous workflow.

---

## Challenges

### Context Preservation
Maintaining consistency across multiple execution stages required robust state management using LangGraph.

### Retrieval Quality
Optimizing chunk size, overlap, and embeddings was necessary to improve retrieval accuracy.

### Structured Output Parsing
LLM-generated JSON responses occasionally produced formatting issues, requiring fallback handling and validation.

### Sequential Reasoning
Ensuring tasks leveraged previous outputs without context drift or hallucinations was a key challenge.

---

## 📂 Project Structure

```text
autonomous-task-agent/
│
├── app.py
├── planner.py
├──  executor.py
├── summarizer.py
├──  vectorstore.py
├──  retriever.py
├── state.py
├──  workflow.py
├── chroma_db/
├── llm.py
├── .env
├── requirements.txt
└── README.md
