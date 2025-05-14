# 🏈 FFLIQ – Fantasy Football League IQ

FFLIQ is an AI-powered fantasy football assistant built for serious players and casual competitors alike. It helps you dominate your draft, optimize lineups, and outsmart your opponents with smart, personalized recommendations.

## 🚀 MVP Features

* Smart news aggregation + summarization
* Draft planner with AI strategy modeling
* Lineup optimizer with floor/upside modes
* Live draft assistant (via ESPN Chrome extension)
* Trade/waiver trend tracking + "what-if" roster scenarios

## 🧱 Tech Stack

* **Frontend**: Next.js 15.x + Tailwind CSS + TypeScript
* **Backend**: FastAPI + PostgreSQL + Python 3.11+
* **AI**: Vector DB (pgvector/ChromaDB), sentence-transformers, Llama 2/Mistral models
* **Infra**: Docker, GitLab CI/CD, Supabase, Vercel/Fly.io

## 🔧 Getting Started

1. Clone the repository
```bash
git clone https://github.com/your-username/ffliq.git
cd ffliq
```

2. Start the Docker containers
```bash
docker-compose up -d
```

3. Apply database migrations to create the tables
```bash
docker-compose exec backend alembic upgrade head
```

4. Access the application
- Frontend: http://localhost:3000
- Backend API docs: http://localhost:8000/docs

1. Clone the repo
2. Run `docker-compose up` to start backend and frontend images
3. Open the app at `http://localhost:3000`
4. Backend API docs available at `http://localhost:8000/docs`

## 📜 Project Planning

See `PLANNING.md` for detailed technical design, conventions, file layout, and feature roadmap.

## 🧭 Contributor Guide

For implementation workflow, task management, and how AI agents should interact with issues and merge requests, please see `WORKFLOW_GUIDE.md`.

## 🧠 AI Architecture

FFLIQ uses Retrieval-Augmented Generation (RAG) to provide accurate, up-to-date fantasy football advice. Our AI system combines:

* **Vector Database**: Stores embeddings of player information, stats, and news
* **Embedding Model**: Converts text to vector representations for semantic search
* **LLM Integration**: Uses open-source models to generate recommendations and analysis

## 📊 Current Development Status

* Initial project structure and environment setup complete
* Database models implemented, Docker setup complete
* Frontend and backend scaffolding in place

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
