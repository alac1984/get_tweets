import psycopg2
from config import config

USERS = (
    "pythonjazz",
    "ike_sigma",
    "coproduto",
    "sseraphini",
    "zanfranceschi",
    "shanselman",
    "cdibona",
    "rasmus",
    "addyosmani",
    "SaraJChipps",
)

def get_last_user() -> str:
    with psycopg2.connect(config.conn_str) as conn:
        cur = conn.cursor()
        cur.execute("select username, detected from tweets order by detected desc limit 1")
        result = cur.fetchone()
        return result[0] if result is not None else USERS[0]

def get_next_user() -> str:
    last_user = get_last_user()
    last_user_idx = USERS.index(last_user)
    if last_user_idx + 1 >= len(USERS):
        return USERS[0]

    return USERS[last_user_idx + 1]
