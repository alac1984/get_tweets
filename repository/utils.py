import psycopg2
from config import config


def create_tables():
    with psycopg2.connect(config.conn_str) as conn:
        cur = conn.cursor()
        # tb_tweets
        cur.execute(
            """
            create table if not exists tb_tweets (
                tweet_id bigint primary key,
                username varchar not null,
                text varchar,
                detected timestamp
            )
        """
        )
        # tb_tweets indexes
        cur.execute(
            """
            create index idx_tweets_id on tweets(tweet_id);
        """
        )
        # tb_users
        cur.execute(
            """
            create table if not exists tb_users(
                user_id bigint primary key,
                name varchar(80) not null,
                description text,
                created_at timestamp,
                username varchar(20),
                location varchar(100)
            )
        """
        )
        # tb_users indexes
        cur.execute(
            """
            create index idx_tb_user_id on tb_users(user_id);
        """
        )
        conn.commit()


def get_users_list():
    return [
        "pythonjazz",
        "coproduto",
        "laislima_dev",
    ]


if __name__ == "__main__":
    create_tables()
