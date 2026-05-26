# 🤖 Autonomous AI Task Agent

An Agentic AI workflow system built using **LangGraph**, **Groq LLM**, and **Streamlit** that autonomously plans, executes, and summarizes multi-step tasks from a single high-level user goal.

---

# 🚀 Features

- Multi-step autonomous task execution
- AI-powered task planning
- Stateful workflow orchestration using LangGraph
- Context-aware execution pipeline
- Dynamic task routing
- Final response summarization
- Streamlit UI for interactive execution
---

# 🧠 Problem Statement

Traditional AI chatbots typically respond to a single prompt without:
- planning
- memory
- workflow orchestration
- multi-step reasoning

This project solves that by building an autonomous AI agent capable of:

1. Understanding a high-level user goal
2. Breaking it into structured tasks
3. Executing tasks sequentially
4. Maintaining contextual memory
5. Generating a consolidated final response

---

# 🏗️ Architecture

```text
User Goal
   ↓
Planner Agent
   ↓
Task List
   ↓
Execution Agent Loop
   ↓
Shared State Updates
   ↓
Summarization Agent
   ↓
Final Output
