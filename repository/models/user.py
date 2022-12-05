from sqlalchemy import Column, Integer, String, DateTime
from repository.base import Base


class User(Base):
    __tablename__ = "tb_user"

    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)
    created_at = Column(DateTime(), nullable=False)
    description = Column(String())
    location = Column(String())
