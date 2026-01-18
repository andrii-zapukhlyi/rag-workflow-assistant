# Multi-Agent Workflow Assistant

![Project Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

A comprehensive Multi-Agent Workflow Assistant designed to streamline enterprise tasks, information retrieval, and process automation. This project leverages Large Language Models (LLMs), Retrieval Augmented Generation (RAG), and a Multi-Agent architecture to unify company knowledge (Confluence documents) and operational workflows (Jira, Expert Discovery) into a single, satisfying chat experience.

## Live Demo
**[www.workflowassistant.app](https://www.workflowassistant.app)**

## Tech Stack
- **Backend:** Python, LangChain, FastAPI, Huggingface (Embeddings), SQLAlchemy (ORM)
- **Database:** PostgreSQL
- **Vector DB:** Qdrant
- **Frontend:** Next.js, React, TypeScript
- **Deployment:** Docker Compose, Azure Container Registry, Azure Virtual Machine, Nginx
- **CI/CD:** GitHub Actions
- **Authentication:** JWT, Refresh Tokens
- **Testing:** Pytest
- **Integrations:** Confluence API, Supabase API, Groq API
- **Package Manager:** Poetry

## The Challenge
Modern enterprises struggle with **fragmented knowledge and workflows**. Critical information and tasks are scattered across multiple systems: Confluence, Jira, Slack, email, and often locked inside individual employees' heads. This leads to:

* **Information Silos:** Data and knowledge are separated, making it hard to find answers quickly.
* **Wasted Time:** Employees spend significant time searching, waiting for approvals, or figuring out processes.
* **Complex Workflows:** Onboarding or completing multi-step tasks often requires juggling multiple tools and human interactions.

## The Solution
The **Multi-Agent Workflow Assistant** acts as a "central hub" for enterprise knowledge and workflows. By orchestrating multiple specialized agents, it streamlines both information retrieval and task execution:

1. **Intelligent Q&A:** Uses **RAG (Retrieval-Augmented Generation)** to fetch, synthesize, and cite information from company documentation.
2. **Workflow Automation (Planned):** Agents can create Jira tickets, track tasks, and automate routine processes directly from chat.
3. **Expert Discovery (Planned):** Identify and connect with the right colleagues who have the knowledge or authority to help.
4. **Future Expansion (Planned):** Additional agents can coordinate multi-step workflows, trigger notifications, or integrate with other enterprise systems.

This approach reduces time spent searching, accelerates task completion, and unifies previously fragmented knowledge and workflows into a single conversational interface.


## Local Setup
Follow these steps to download and run the project locally.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/andrii-zapukhlyi/workflow-assistant.git
   cd workflow-assistant
   ```

2. **Configure Environment:**
   Navigate to the backend folder and create your `.env` file.
   ```bash
   cd backend

   # Linux/macOS:
   cp .env.example .env
   
   # Windows CMD:
   copy .env.example .env
   ```
   *Note: You will need to populate `.env` with your API keys (Confluence, Groq, Huggingface, etc.).*

3. **Run with Docker:**
   Return to the root directory and start the application.
   ```bash
   cd ..
   docker compose up --build
   ```
   *Note: Be sure to have Docker installed and running on your machine.*
   
   The application will be accessible at:
   `http://localhost`

## Future Plans
- **Expert Finder Agent:** Implementation of an agent to help employees find experts within the company for specific tools or technologies.
- **Process Starter Agent:** Integration with Jira API to facilitate task management and process initiation through the chatbot.
- **Future Expansion:** Additional agents can coordinate multi-step workflows, trigger notifications, or integrate with other enterprise systems.