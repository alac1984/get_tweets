"""repository/models/user.py"""
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from repository.base import Base


class User(Base):
    __tablename__ = "tb_user"

    id = Column(Integer(), primary_key=True)
    twitter_id = Column(Integer(), nullable=False)
    username = Column(String(), nullable=False)
    created_at = Column(DateTime(), nullable=False)
    description = Column(String())
    location = Column(String())
    last_scraped = Column(Boolean(), default=False)
