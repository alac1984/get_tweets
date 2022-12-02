import psycopg2
from config import config

def create_tables():
    with psycopg2.connect(config.conn_str) as conn:
        cur = conn.cursor()
        cur.execute("""
            create table if not exists tweets (
                id bigint primary key,
                username varchar not null,
                text varchar,
                detected timestamp
            )
        """)
        cur.execute("""
            create index idx_tweets_id on tweets(id);
        """)
        # TODO: create persistence for last user checked
        cur.execute("""
            create table if not exists users(
                id bigint primary key,
                IMPLEMENT OTHER TUPLES
            )
        """)
        conn.commit()

if __name__ == "__main__":
    create_tables()
