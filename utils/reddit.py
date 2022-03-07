import os
from typing import List

import praw

reddit_user = os.environ.get("REDDIT_USERNAME")
reddit_secret = os.environ.get("REDDIT_SECRET")
reddit_id = os.environ.get("REDDIT_ID")

reddit = praw.Reddit(
    user_agent=f"Comment Extraction (by u/{reddit_user})",
    client_id=reddit_id,
    client_secret=reddit_secret,
)


def get_reddit_comments(thread_url: str) -> dict:
    submission = reddit.submission(url=thread_url)
    # only get top level comments
    submission.comments.replace_more(limit=0)

    comments = [
        (comment.created_utc, comment.body) for comment in submission.comments
    ]
    return comments


class CommentsBucket:
    def __init__(
        self,
        comments: List[str],
        start_time: int,
        end_time: int,
        bucket_size: int,
    ) -> None:
        self.bucket_size = bucket_size
        self.buckets = self.make_buckets(start_time, end_time, comments)

    def make_buckets():
        pass

    def analyse_buckets():
        pass
