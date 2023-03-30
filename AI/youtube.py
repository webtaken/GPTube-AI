from typing import List
from models.comment import Comment
from . import tokenizer, model
import torch

def bert_prediction(comments: List[Comment]):
    for comment in comments:
        try:
            tokens = tokenizer.encode(comment.text_display, return_tensors="pt")
            result = model(tokens)
            score = int(torch.argmax(result.logits))+1
            comment.score = score
        except RuntimeError:
            print(f"failed for comment: {comment.comment_id}")
            pass