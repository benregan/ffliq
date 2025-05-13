"""
Pydantic schemas for API request and response validation.
"""
from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime

# Base schemas with common fields
class TimestampSchema(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# User schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase, TimestampSchema):
    id: int
    
    class Config:
        orm_mode = True

# Team schemas
class TeamBase(BaseModel):
    name: str
    league_id: int

class TeamCreate(TeamBase):
    logo_url: Optional[str] = None

class TeamResponse(TeamBase, TimestampSchema):
    id: int
    user_id: int
    provider_team_id: Optional[str] = None
    logo_url: Optional[str] = None
    
    class Config:
        orm_mode = True

# League schemas
class LeagueBase(BaseModel):
    name: str
    description: Optional[str] = None
    season_year: int
    
class LeagueCreate(LeagueBase):
    settings: Optional[Dict[str, Any]] = None
    settings_source: Optional[str] = None

class LeagueResponse(LeagueBase, TimestampSchema):
    id: int
    created_by_id: int
    status: str
    provider_league_id: Optional[str] = None
    last_sync_time: Optional[datetime] = None
    
    class Config:
        orm_mode = True

# NFLPlayer schemas
class NFLPlayerBase(BaseModel):
    name: str
    position: str
    nfl_team: str

class NFLPlayerCreate(NFLPlayerBase):
    jersey_number: Optional[int] = None
    headshot_url: Optional[str] = None
    global_player_id: str
    provider_player_ids: Optional[Dict[str, str]] = None
    active_flag: bool = True
    season_year: int
    status: Optional[str] = None

class NFLPlayerResponse(NFLPlayerBase):
    id: int
    jersey_number: Optional[int] = None
    headshot_url: Optional[str] = None
    global_player_id: str
    provider_player_ids: Optional[Dict[str, str]] = None
    active_flag: bool
    season_year: int
    status: Optional[str] = None
    
    class Config:
        orm_mode = True

# Roster schemas
class RosterBase(BaseModel):
    team_id: int
    nfl_player_id: int
    roster_position: str
    week_number: int
    is_starter: bool = False

class RosterCreate(RosterBase):
    pass

class RosterResponse(RosterBase):
    id: int
    last_updated: datetime
    provider_roster_slot_id: Optional[str] = None
    
    class Config:
        orm_mode = True

# PlayerStats schemas
class PlayerStatsCreate(BaseModel):
    nfl_player_id: int
    week_number: int
    season_year: int
    # Stats fields
    passing_yards: float = 0.0
    passing_tds: int = 0
    interceptions: int = 0
    passing_completions: int = 0
    passing_attempts: int = 0
    rushing_yards: float = 0.0
    rushing_tds: int = 0
    rushing_attempts: int = 0
    receiving_yards: float = 0.0
    receiving_tds: int = 0
    receptions: int = 0
    targets: int = 0
    fumbles_lost: int = 0
    # Optional fields
    provider_id: Optional[str] = None
    raw_stats: Optional[Dict[str, Any]] = None

class PlayerStatsResponse(PlayerStatsCreate):
    id: int
    last_updated: datetime
    
    class Config:
        orm_mode = True

# Additional schemas can be added as needed for other models