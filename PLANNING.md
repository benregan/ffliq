# 🏈 FFLIQ – Fantasy Football League IQ

## 🔄 Project Awareness & Context

- **Project Name**: FFLIQ (Fantasy Football League IQ)
- **Read this file at the beginning of every session** to understand the project's structure and priorities.
- **Use GitLab Issues for all task tracking** (no `TASK.md`).
- All architecture, naming, and coding conventions defined here must be followed by all agents and contributors.
- This project will scale over time, so **modularity and clarity** are paramount from day one.

---

## 🎯 MVP Goals

Build a fully functional MVP fantasy football companion app that:

- Provides **AI-powered draft, waiver, and lineup advice**.
- Pulls news from multiple sources and **summarizes key updates**.
- Offers a **browser extension** to assist with **live ESPN drafts**.
- Provides **trend detection and "What-if" roster simulations**.
- Has a **modern, user-friendly UI** built for eventual cross-platform deployment (web + mobile).

---

## 🧱 Tech Stack

### Frontend

- **Framework**: Next.js 15.x (App Router)
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS
- **Data/State**: React Query (TanStack), Axios

### Backend

- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL + `pgvector`
- **ORM**: SQLAlchemy 2.0
- **AI**:
  - Embeddings via `sentence-transformers`
  - Optional local LLM via Ollama (e.g., Mistral, LLaMA 2)
  - RAG and summarization via LangChain (or custom Python modules)
- **Testing**: Pytest, Black, Ruff

### Browser Extension

- **Target**: ESPN live draft interface
- **Structure**:
  - `content.js`: parses DOM
  - `background.js`: sends draft data to backend
  - `ui/`: renders assistant panel inline
- **Build Tools**: Vite or simple JS/TS bundler

### Infrastructure

- **Local Dev**: Docker + `docker-compose`
- **CI/CD**: GitLab CI
- **Hosting**:
  - Frontend: Vercel
  - Backend: Fly.io or Railway
  - DB: Supabase (Postgres)

---
## 🔧 Project Management Reference

- Please refer to `WORKFLOW_GUIDE.md` for all GitLab Issue conventions, task naming patterns, label use, merge request expectations, and AI contributor behavior.

---

## 📁 File Structure

<pre>
/frontend
  /src
    /components      → UI components
    /features        → Feature-specific components
    /pages           → App Router views
    /services        → Axios API logic
    /hooks           → React hooks
    /context         → React Context for global state
    /styles          → Tailwind + theme setup

/backend
  /app
    /api             → FastAPI routes
    /models          → Data models and schemas
    /services        → Business logic
    /db              → SQLAlchemy models + sessions
    /ai              → LLM access, embeddings, RAG logic

/extension
  manifest.json      → Chrome extension config
  content.js         → DOM scraping logic for ESPN draft
  background.js      → Messaging + API interaction
  /ui                → HTML/CSS UI for draft overlay

/infra
  docker-compose.yml → Containerized dev stack
  nginx.conf         → Optional reverse proxy setup

/docs
  /planning          → Design references
  /ai                → AI configs, prompt examples

/tests
  __tests__/         → Unit + integration test suites
</pre>

---

## 🧪 Testing & Code Quality

- **Minimum coverage target**: 80%
- **Linting tools**:
  - Frontend: ESLint + Prettier
  - Backend: Black + Ruff
- **Test frameworks**:
  - Frontend: Jest + React Testing Library
  - Backend: Pytest
- **All tests go in `__tests__` folders adjacent to source**

---

## 🔌 Live Draft Helper – Chrome Extension

**Goal**: Automatically read ESPN live draft data and feed it to the backend for real-time recommendations.

### Functionality:

- Activates only on `https://fantasy.espn.com/*draft*`
- Reads:
  - Current nomination
  - Teams' rosters
  - Drafted player history
  - Available player list
- Sends parsed state to `/api/draft/state` endpoint
- Displays AI advice in a floating overlay component

---

## 🧠 AI & RAG Architecture

- Use **Retrieval-Augmented Generation (RAG)** for chatbot + recommendations
- Knowledge base:
  - Manually curated + optionally transcribed content
  - Stored in a vector DB (`pgvector` or `ChromaDB`)
- Embeddings:
  - Sentence Transformers (all-MiniLM or similar)
- AI options:
  - API: OpenAI (fallback)
  - Local: Ollama + Mistral (dev/test)
- Backed by FastAPI routes like:
  - `/api/chat/query`
  - `/api/lineup/suggest`
  - `/api/waivers/suggest`

---

## 📦 Git + CI Workflow

- **Repo**: Monorepo (hosted on GitLab)
- **Branches**: `main`, `dev`, `feature/*`, `fix/*`
- **Commits**: Conventional Commits
- **CI Pipelines**:
  - Lint → Test → Build
- **All changes linked to GitLab Issues**
  - Windsurf + MCP enabled
  - `PLANNING.md` guides architecture
  - Issues define tasks

---

## 💬 Style & Dev Conventions

- **TypeScript + strict types** everywhere
- **Separation of concerns**:
  - No business logic in components
  - No database logic in routes
- **Comments required** for complex logic
- **JSDoc-style annotations** for public functions/components
- **README.md, CHANGELOG.md** and `/docs` must be kept up to date

---

## 🔔 Feature Checklist (MVP)

- [x] App name selected: **FFLIQ**
- [ ] Customizable fantasy news feed (RSS + summaries)
- [ ] Draft strategy assistant (0RB, Hero RB, Auction planner)
- [ ] Lineup suggestions with "floor/upside" mode
- [ ] Waiver wire recommendations + trend detection
- [ ] ESPN Draft Helper (via Chrome extension)
- [ ] Chatbot (RAG w/ public analyst content)
- [ ] Team analyzer w/ "What if I trade/pick up X?" support
- [ ] Basic alert system for roster issues (e.g. inactive players)

---

## 🏀 Database Model Structure

- **NFLPlayer**: Reference table for all NFL players (single source of truth)
  - id, name, position, nfl_team, jersey_number, headshot_url
  - global_player_id, provider_player_ids (JSON mapping provider:id pairs)
  - active_flag, season_year, status (active, injured, retired, etc.)

- **User**: User account information
  - id, username, email, hashed_password, created_at, updated_at
  - provider_credentials (encrypted JSON for API access tokens)

- **League**: Fantasy league information
  - id, name, description, season_year
  - settings (JSON for scoring rules - detailed schema for passing/rushing/receiving points, bonuses, etc.)
  - settings_source (e.g., "espn", "manual")
  - last_sync_time, sync_frequency
  - created_by (user_id), created_at, updated_at, status

- **Team**: User's fantasy team
  - id, name, user_id, league_id
  - provider_team_id (ID in external system)
  - logo_url, created_at, updated_at

- **Roster**: Players on a team
  - id, team_id, nfl_player_id
  - roster_position (QB, RB1, RB2, BENCH, etc.)
  - week_number, is_starter
  - last_updated

- **GameSchedule**: NFL game scheduling
  - id, nfl_team_home, nfl_team_away
  - week_number, season_year, game_time
  - status (scheduled, active, completed)

- **PlayerStats**: Actual player performance
  - id, nfl_player_id, week_number, season_year
  - Normalized stats fields:
    - passing_yards, passing_tds, interceptions, passing_completions, passing_attempts
    - rushing_yards, rushing_tds, rushing_attempts
    - receiving_yards, receiving_tds, receptions, targets
    - fumbles_lost, fg_made_1_29, fg_made_30_39, fg_made_40_49, fg_made_50_plus
    - extra_points_made, sacks, defensive_interceptions, fumble_recoveries, defensive_tds
  - provider_id, raw_stats (JSON for provider-specific data)
  - last_updated

- **PlayerProjection**: Projected performance
  - Similar structure to PlayerStats
  - projection_source (e.g., "espn", "our AI model")
  - created_at

- **PlayerPoints**: Cached calculated fantasy points
  - id, nfl_player_id, league_id, week_number, season_year
  - points, calculated_at
  
- **PlayerNews**: Player news and updates (for AI recommendations)
  - id, nfl_player_id, title, content
  - source, source_url, published_at
  - sentiment_score (optional, for AI analysis)

---

## 🌍 Future-Ready Planning

- Support for other platforms (Yahoo, Sleeper, CBS)
- OAuth league sync (if APIs permit)
- Native mobile app (via React Native)
- Paid tiers: premium insights, AI trade review, weekly reports
- Ad-supported free tier (minimally intrusive)
- Auto-sync team data via extension + league ID

---

## 🔥 Tagline & Branding

- **Name**: FFLIQ
- **Tagline**: *"Smarter Drafts. Sharper Lineups. Dominant Teams."*
- **Alt Slogan**: *"Fantasy Football League IQ. It's not cheating... it's just smarter."*
- **Logo concepts**: brain + football icon, FFLIQ meter, double-F monogram
- **Domains to register**:
  - `ffliq.com`
  - `ffliq.ai`
- **Social handles**:
  - `@ffliq` on Twitter, IG, TikTok (available as of initial check)