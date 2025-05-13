# 📘 FFLIQ Reference Guide

*This document captures the vision, technical strategy, and development guidelines for the FFLIQ project. It serves as a comprehensive reference for project direction.*

## 1. Market & Competitive Analysis

**Core Observations**
- **Platform Giants:** ESPN/Yahoo offer hosting but generally lack deep, integrated analytical insights.
- **Sleeper:** Praised for great UX and social features, but analysis depth can be limited.
- **Specialized Tools:** FantasyPros/Rotowire offer projections and analysis but often require subscriptions and can have clunky UIs.
- **AI Usage:** Currently rare in mainstream platforms and usually shallow.
- **Positioning:** FFLIQ aims to be a *premium*, AI-powered application giving users a competitive edge through superior UX and actionable, personalized insights.

## 2. Core Feature Analysis

- **Team Management**
  - Manual entry of fantasy team roster (MVP)
  - Viewing players and point tracking
  - Future: Multi-user leagues and automated import

- **Real-Time Updates**
  - Integration with NFL data API
  - Real-time scores and player stats
  - Support for quick, strategic decisions

- **AI-Powered Recommendations**
  - Optimal lineup suggestions (start/sit)
  - Waiver wire pickups
  - Trade targets
  - Considers user's roster, player projections, matchup data
  - Machine learning models with LLM capabilities

- **AI Assistant (RAG Chatbot)**
  - Conversational AI for user Q&A
  - Personalized advice
  - Uses LLM grounded by knowledge base via RAG
  - Vector database stores embeddings of player info, historical data, stats, news

- **News Aggregator**
  - Aggregates from RSS, APIs
  - NLP for tagging players, teams, injury status
  - Personalized news feeds

- **Draft Strategy Assistant**
  - Supports common strategies (Zero RB, Hero RB, etc.)
  - Integrates Average Draft Position data
  - Scenario testing

- **Waiver Wire + Trend Alerts**
  - Real-time alerts for trending pickups
  - Identifies potential sleepers
  - Roster-aware recommendations

- **Live Draft Helper**
  - Chrome extension for ESPN drafts
  - Real-time AI recommendations during draft

## 3. Technical Architecture

- **Overall Architecture**
  - Client-Server model (React/TypeScript frontend, FastAPI/Python backend)
  - RESTful API endpoints
  - Containerized using Docker
  - Modular design with separation of concerns

- **RAG Architecture & AI Integration**
  - RAG pattern for AI Assistant
  - Vector Database (ChromaDB or pgvector)
  - Embedding Model: SentenceTransformers
  - LLM Integration: Open-source models (Llama 2, Mistral)
  - Prompt Engineering: Carefully crafted templates

- **Frontend Technologies**
  - React with TypeScript
  - Next.js 15.x with App Router
  - Tailwind CSS for styling
  - React Context + React Query for state
  - Jest + React Testing Library for testing

- **Backend Technologies**
  - FastAPI (Python 3.11+)
  - PostgreSQL with pgvector
  - SQLAlchemy 2.0 with Pydantic
  - Pytest for testing
  - Alembic for migrations

- **Development Environment**
  - Docker Compose for local development
  - VS Code Dev Containers
  - GitLab CI/CD pipeline
  - ESLint/Prettier for frontend, Black/Ruff for backend

## 4. ESPN Live Draft Helper Design

- **Mechanism:** Chrome Extension reads ESPN draft page DOM
- **Data Extraction:** Content script extracts live data
- **Communication:** Data sent to FFLIQ backend API
- **AI Recommendation:** Backend processes draft state and provides real-time recommendations
- **Display:** Recommendations shown as overlay in ESPN interface

## 5. Legal & Data Considerations

- **Data Sources:** Free APIs, RSS feeds, possibly ESPN unofficial endpoints
- **Analyst Content:** Requires licensing for expert projections
- **User Privacy:** Encryption for sensitive data, secure authentication
- **Browser Extension:** Review ESPN Terms of Service
- **AI Development:** Avoid sending sensitive internal details to third-party AI assistants

## 6. Database Schema Design

- **NFLPlayer**
  - Master list of NFL players (single source of truth)
  - Fields: id, name, position, nfl_team, jersey_number, headshot_url, global_player_id, provider_player_ids (JSON mapping provider:id pairs), active_flag, season_year, status (active, injured, retired, etc.)

- **User**
  - User account information
  - Fields: id, username, email, hashed_password, created_at, updated_at, provider_credentials (encrypted JSON for API tokens)

- **League**
  - Fantasy league information
  - Fields: id, name, description, season_year, settings (JSON with detailed scoring schema - see below), settings_source (e.g., "espn", "manual"), last_sync_time, sync_frequency, created_by, created_at, updated_at, status

- **Team**
  - User's fantasy team
  - Fields: id, name, user_id, league_id, provider_team_id (external ID), logo_url, created_at, updated_at

- **Roster**
  - Players on a team
  - Fields: id, team_id, nfl_player_id, roster_position (QB, RB1, RB2, BENCH, etc.), week_number, is_starter, last_updated

- **GameSchedule**
  - NFL game scheduling
  - Fields: id, nfl_team_home, nfl_team_away, week_number, season_year, game_time, status (scheduled, active, completed)

- **PlayerStats**
  - Actual player performance
  - Fields: id, nfl_player_id, week_number, season_year, normalized stat fields (passing_yards, passing_tds, interceptions, rushing_yards, rushing_tds, receptions, receiving_yards, receiving_tds, fumbles_lost, kicking stats, defensive stats, etc.), provider_id, raw_stats (JSON), last_updated

- **PlayerProjection**
  - Projected performance
  - Fields: Similar to PlayerStats plus projection_source, created_at

- **PlayerPoints**
  - Cached calculated fantasy points
  - Fields: id, nfl_player_id, league_id, week_number, season_year, points, calculated_at

- **PlayerNews**
  - Player news and updates for AI recommendations
  - Fields: id, nfl_player_id, title, content, source, source_url, published_at, sentiment_score (optional)

### League Settings JSON Schema Example
```json
{
  "scoring": {
    "passing": {
      "yards": 0.04,
      "tds": [
        {"range": [0, 9], "points": 4},
        {"range": [10, 19], "points": 4},
        {"range": [20, 29], "points": 4},
        {"range": [30, 39], "points": 4},
        {"range": [40, 49], "points": 5},
        {"range": [50, null], "points": 7}
      ],
      "interceptions": -2,
      "completions": 1,
      "attempts": 0,
      "bonuses": [
        {"threshold": 300, "type": "yards", "points": 5}
      ]
    },
    "rushing": {
      "yards": 0.1,
      "tds": 6,
      "attempts": 0,
      "bonuses": [
        {"threshold": 100, "type": "yards", "points": 2}
      ]
    },
    "receiving": {
      "yards": 0.1,
      "tds": 6,
      "receptions": 1.0,
      "bonuses": [
        {"threshold": 100, "type": "yards", "points": 2}
      ]
    },
    "kicking": {
      "fg_made": [
        {"range": [1, 29], "points": 3},
        {"range": [30, 39], "points": 3},
        {"range": [40, 49], "points": 4},
        {"range": [50, null], "points": 5}
      ],
      "extra_points_made": 1
    },
    "defense": {
      "points_allowed": [
        {"range": [0, 0], "points": 10},
        {"range": [1, 6], "points": 7},
        {"range": [7, 13], "points": 4},
        {"range": [14, 20], "points": 1},
        {"range": [21, 27], "points": 0},
        {"range": [28, 34], "points": -1},
        {"range": [35, null], "points": -4}
      ],
      "sacks": 1,
      "interceptions": 2,
      "fumble_recoveries": 2,
      "defensive_tds": 6,
      "safeties": 2
    },
    "misc": {
      "fumbles_lost": -2
    }
  },
  "roster": {
    "positions": {
      "QB": 1,
      "RB": 2,
      "WR": 2,
      "TE": 1,
      "FLEX": 1,
      "K": 1,
      "DST": 1,
      "BENCH": 6
    }
  }
}

## 7. Future Expansion

- Support for Yahoo, Sleeper, CBS
- OAuth league sync
- Native mobile app (React Native)
- Paid premium tiers
- Ad-supported free tier
- Auto-sync team data

## 8. Development Best Practices

- Type safety (TypeScript/Python type hints)
- Test coverage (minimum 80% for critical paths)
- Separation of concerns
- Comprehensive documentation
- Conventional commit messages
- Code review for all changes
- Modular, scalable architecture

This document serves as a living reference and should be updated as the project evolves.