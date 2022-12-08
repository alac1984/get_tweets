from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from repository.base import Base


class User(Base):
    __tablename__ = "tb_user"

    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)
    created_at = Column(DateTime(), nullable=False)
    description = Column(String())
    location = Column(String())


class ScrapedUser(Base):
    __tablename__ = "tb_scraped_user"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("tb_user.id"))
    scraped_on = Column(DateTime(), default=datetime.now)
