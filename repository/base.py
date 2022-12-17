import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import settings

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


Base = declarative_base()
engine = create_engine(settings.conn_str)
logging.debug(f"engine creation: {engine}")
