"""
Database models for FFLIQ backend.
Includes all models as defined in PLANNING.md with proper relationships and fields.
"""
from sqlalchemy import (
    Column, Integer, String, ForeignKey, Boolean, DateTime, 
    Float, JSON, Table, Enum, Text, func
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
import enum

Base = declarative_base()

class TimestampMixin:
    """Mixin to add created_at and updated_at columns to models."""
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class StatusEnum(str, enum.Enum):
    """Status enum for various status fields."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    COMPLETED = "completed"
    SCHEDULED = "scheduled"

class NFLPlayer(Base):
    """
    Master list of NFL players (single source of truth).
    """
    __tablename__ = "nfl_players"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False, index=True)
    nfl_team = Column(String, nullable=False, index=True)
    jersey_number = Column(Integer, nullable=True)
    headshot_url = Column(String, nullable=True)
    
    # Global identifiers
    global_player_id = Column(String, unique=True, nullable=False)
    provider_player_ids = Column(JSON, nullable=True)  # e.g. {"espn": "123", "sleeper": "456"}
    
    # Status and metadata
    active_flag = Column(Boolean, default=True, nullable=False)
    season_year = Column(Integer, nullable=False, index=True)
    status = Column(String, nullable=True)  # active, injured, retired, etc.

    # Relationships
    stats = relationship("PlayerStats", back_populates="player")
    projections = relationship("PlayerProjection", back_populates="player")
    news = relationship("PlayerNews", back_populates="player")

class User(TimestampMixin, Base):
    """
    User account information.
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    provider_credentials = Column(JSON, nullable=True)  # encrypted JSON for API tokens
    
    # Relationships
    leagues_created = relationship("League", back_populates="created_by")
    teams = relationship("Team", back_populates="user")

class League(TimestampMixin, Base):
    """
    Fantasy league information.
    """
    __tablename__ = "leagues"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    season_year = Column(Integer, nullable=False, index=True)
    
    # External provider information
    provider_id = Column(Integer, nullable=True)  # Foreign key to future LeagueProvider table
    provider_league_id = Column(String, nullable=True)  # ID in the external system
    
    # League configuration
    settings = Column(JSON, nullable=True)  # JSON schema for scoring rules
    settings_source = Column(String, nullable=True)  # e.g., "espn", "manual"
    
    # Synchronization
    last_sync_time = Column(DateTime, nullable=True)
    sync_frequency = Column(Integer, nullable=True)  # in minutes
    
    # Status
    status = Column(String, nullable=False, default=StatusEnum.ACTIVE)  # active, completed, etc.
    
    # Relationships
    created_by_id = Column(Integer, ForeignKey("users.id"))
    created_by = relationship("User", back_populates="leagues_created")
    teams = relationship("Team", back_populates="league")

class Team(TimestampMixin, Base):
    """
    User's fantasy team.
    """
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # Relationships
    user_id = Column(Integer, ForeignKey("users.id"))
    league_id = Column(Integer, ForeignKey("leagues.id"))
    
    # External information
    provider_team_id = Column(String, nullable=True)  # ID in external system
    logo_url = Column(String, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="teams")
    league = relationship("League", back_populates="teams")
    rosters = relationship("Roster", back_populates="team")

class Roster(Base):
    """
    Players on a team for a specific week.
    """
    __tablename__ = "rosters"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Relationships
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    nfl_player_id = Column(Integer, ForeignKey("nfl_players.id"), nullable=False)
    
    # Position and status
    roster_position = Column(String, nullable=False)  # QB, RB1, BENCH, etc.
    week_number = Column(Integer, nullable=False, index=True)
    is_starter = Column(Boolean, default=False, nullable=False)
    
    # External info
    provider_roster_slot_id = Column(String, nullable=True)
    last_updated = Column(DateTime, default=func.now(), nullable=False)
    
    # Relationships
    team = relationship("Team", back_populates="rosters")

class GameSchedule(Base):
    """
    NFL game scheduling information.
    """
    __tablename__ = "game_schedules"
    
    id = Column(Integer, primary_key=True, index=True)
    nfl_team_home = Column(String, nullable=False, index=True)
    nfl_team_away = Column(String, nullable=False, index=True)
    week_number = Column(Integer, nullable=False, index=True)
    season_year = Column(Integer, nullable=False, index=True)
    game_time = Column(DateTime, nullable=False)
    status = Column(String, nullable=False, default=StatusEnum.SCHEDULED)  # scheduled, active, completed

class PlayerStats(Base):
    """
    Actual player performance statistics.
    """
    __tablename__ = "player_stats"
    
    id = Column(Integer, primary_key=True, index=True)
    nfl_player_id = Column(Integer, ForeignKey("nfl_players.id"), nullable=False)
    week_number = Column(Integer, nullable=False, index=True)
    season_year = Column(Integer, nullable=False, index=True)
    
    # Normalized stat fields for fantasy scoring
    # Passing stats
    passing_yards = Column(Float, default=0.0)
    passing_tds = Column(Integer, default=0)
    interceptions = Column(Integer, default=0)
    passing_completions = Column(Integer, default=0)
    passing_attempts = Column(Integer, default=0)
    
    # Rushing stats
    rushing_yards = Column(Float, default=0.0)
    rushing_tds = Column(Integer, default=0)
    rushing_attempts = Column(Integer, default=0)
    
    # Receiving stats
    receiving_yards = Column(Float, default=0.0)
    receiving_tds = Column(Integer, default=0)
    receptions = Column(Integer, default=0)
    targets = Column(Integer, default=0)
    
    # Misc stats
    fumbles_lost = Column(Integer, default=0)
    
    # Kicking stats
    fg_made_1_29 = Column(Integer, default=0)
    fg_made_30_39 = Column(Integer, default=0)
    fg_made_40_49 = Column(Integer, default=0)
    fg_made_50_plus = Column(Integer, default=0)
    extra_points_made = Column(Integer, default=0)
    
    # Defense stats
    sacks = Column(Float, default=0.0)
    defensive_interceptions = Column(Integer, default=0)
    fumble_recoveries = Column(Integer, default=0)
    defensive_tds = Column(Integer, default=0)
    safeties = Column(Integer, default=0)
    
    # Raw data and metadata
    provider_id = Column(String, nullable=True)
    raw_stats = Column(JSON, nullable=True)  # Original provider-specific data
    last_updated = Column(DateTime, default=func.now())
    
    # Relationships
    player = relationship("NFLPlayer", back_populates="stats")

class PlayerProjection(Base):
    """
    Projected player performance.
    """
    __tablename__ = "player_projections"
    
    id = Column(Integer, primary_key=True, index=True)
    nfl_player_id = Column(Integer, ForeignKey("nfl_players.id"), nullable=False)
    week_number = Column(Integer, nullable=False, index=True)
    season_year = Column(Integer, nullable=False, index=True)
    
    # Same normalized stat fields as PlayerStats
    # Passing stats
    passing_yards = Column(Float, default=0.0)
    passing_tds = Column(Integer, default=0)
    interceptions = Column(Integer, default=0)
    passing_completions = Column(Integer, default=0)
    passing_attempts = Column(Integer, default=0)
    
    # Rushing stats
    rushing_yards = Column(Float, default=0.0)
    rushing_tds = Column(Integer, default=0)
    rushing_attempts = Column(Integer, default=0)
    
    # Receiving stats
    receiving_yards = Column(Float, default=0.0)
    receiving_tds = Column(Integer, default=0)
    receptions = Column(Integer, default=0)
    targets = Column(Integer, default=0)
    
    # Misc stats
    fumbles_lost = Column(Integer, default=0)
    
    # Metadata
    projection_source = Column(String, nullable=False)  # e.g., "espn", "our AI model"
    projection_data = Column(JSON, nullable=True)  # Additional projection details
    created_at = Column(DateTime, default=func.now())
    
    # Relationships
    player = relationship("NFLPlayer", back_populates="projections")

class PlayerPoints(Base):
    """
    Cached calculated fantasy points.
    """
    __tablename__ = "player_points"
    
    id = Column(Integer, primary_key=True, index=True)
    nfl_player_id = Column(Integer, ForeignKey("nfl_players.id"), nullable=False)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False)
    week_number = Column(Integer, nullable=False, index=True)
    season_year = Column(Integer, nullable=False, index=True)
    points = Column(Float, nullable=False)
    calculated_at = Column(DateTime, default=func.now())

class PlayerNews(Base):
    """
    Player news and updates for AI recommendations.
    """
    __tablename__ = "player_news"
    
    id = Column(Integer, primary_key=True, index=True)
    nfl_player_id = Column(Integer, ForeignKey("nfl_players.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String, nullable=True)
    source_url = Column(String, nullable=True)
    published_at = Column(DateTime, nullable=False)
    sentiment_score = Column(Float, nullable=True)  # Optional, for AI analysis
    
    # Relationships
    player = relationship("NFLPlayer", back_populates="news")