# 🚀 Initial Development Tasks

## ✅ Project Initialization
- [x] Set up GitLab Repository (monorepo: frontend/backend folders)
- [x] Create initial `docker-compose.yml` for local dev (frontend, backend, Postgres)
- [x] Initialize React/Next.js 15.x project (TypeScript, Tailwind CSS) in `/frontend`
- [x] Initialize FastAPI project (Python 3.11, requirements.txt) in `/backend`

## 📡 Backend Setup
- [x] Configure FastAPI project with basic health endpoint (`/health`)
- [x] Set up database connection (PostgreSQL, SQLAlchemy)
- [x] Create initial DB models and update them based on revised schema
- [x] Set up migrations with Alembic

## 🖥️ Frontend Setup
- [x] Set up basic frontend routing (Next.js App Router)
- [ ] Create reusable React component structure (`/components`)
- [ ] Set up initial UI layout (Nav, Footer, placeholder dashboard page)
- [ ] Implement API service layer with Axios

## 🤖 AI Initial Setup
- [ ] Set up Python backend AI module (`/backend/app/ai`)
- [ ] Configure vector database setup (ChromaDB or pgvector)
- [ ] Set up sentence-transformers for embeddings
- [ ] Implement RAG system basic structure
- [ ] Create test endpoint for AI functionality

## 🛠️ Tools & Workflow Setup
- [x] Configure ESLint and Prettier (`frontend`)
- [x] Configure Black, Ruff/Flake8 (`backend`)
- [ ] Add initial Jest test (frontend) and Pytest test (backend)
- [ ] Set up CI pipeline in GitLab

## 📊 Database Implementation
- [ ] Implement NFLPlayer model with provider mapping
- [ ] Implement User, League, and Team models
- [ ] Implement Roster and GameSchedule models
- [ ] Implement PlayerStats model with normalized stat fields
- [ ] Implement PlayerProjection and PlayerNews models
- [ ] Create scoring service for calculating fantasy points based on league settings
- [ ] Implement PlayerPoints caching system
- [ ] Set up data migration and seed data for testing

## 📱 UI Components
- [ ] Create design system/component library
- [ ] Implement responsive layout components
- [ ] Create data visualization components for stats
- [ ] Build form components for team/league settings

---

## 🌟 Discovered During Work (Add tasks here as you identify them)
- Review and update database schema for compatibility with multiple league providers
- Consider creating a data normalization layer for different fantasy platforms
- Investigate available NFL data APIs for real-time stats