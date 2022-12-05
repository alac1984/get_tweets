import os
from dotenv import dotenv_values


class Config:
    def __init__(self, type: str):
        if type == "prod":
            self.DB_USER = os.environ['DB_USER']
            self.DB_PASSWORD = os.environ['DB_PASSWORD']
            self.DB_HOST = os.environ['DB_HOST']
            self.DB_PORT = os.environ['DB_PORT']
            self.DB_DB = os.environ['DB_DB']
            self.TWITTER_TOKEN = os.environ['TWITTER_TOKEN']

        if type == "devel":
            env = dotenv_values(".env")
            self.DB_USER = env['DB_USER']
            self.DB_PASSWORD = env['DB_PASSWORD']
            self.DB_HOST = env['DB_HOST']
            self.DB_PORT = env['DB_PORT']
            self.DB_DB = env['DB_DB']
            self.TWITTER_TOKEN = env['TWITTER_TOKEN']

    @property
    def conn_str(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DB}"
