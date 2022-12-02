import os

class Config:
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ['DB_PORT']
    DB_DB = os.environ['DB_DB']
    TWITTER_TOKEN = os.environ['TWITTER_TOKEN']

    @property
    def conn_str(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DB}"

config = Config()
