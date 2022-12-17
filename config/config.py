import os
from dotenv import dotenv_values


class Config:
    def __init__(self):
        # Get environment

        if os.environ.get("GET_TWEETS"):
            self.env = os.environ
        else:
            self.env = dotenv_values(".env")

        self.DB_USER = self.env["DB_USER"]
        self.DB_PASSWORD = self.env["DB_PASSWORD"]
        self.DB_HOST = self.env["DB_HOST"]
        self.DB_PORT = self.env["DB_PORT"]
        self.DB_DB = self.env["DB_DB"]
        self.TWITTER_TOKEN = self.env["TWITTER_TOKEN"]

    @property
    def conn_str(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DB}"
