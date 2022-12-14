def check_if_tweet_was_saved_before(tweet_id: int, id_list: list[int]) -> bool:
    return tweet_id in id_list
