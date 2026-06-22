# ============================================================
# FILE: self_reference.py
# TOPIC: Self-referencing model - model khud ko reference kare
# FOLDER: 14_pydantic/01_basics
# ============================================================
# Self-reference = model ke andar wahi model as field (recursive structure)
# 'Comment' string mein likho - class abhi define ho rahi hai
# Optional[List['Comment']] = replies mein aur Comments ho sakte hain
# model_rebuild() = forward references resolve karta hai - ZAROORI hai!
# Use case: comments with replies, tree structures, linked lists
# ============================================================

from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None  # 'Comment' = self-reference (string mein)

# model_rebuild() ZAROORI hai - 'Comment' string ko actual class se replace karega
Comment.model_rebuild()


# Nested comments with replies - tree structure!
comment = Comment(
    id= 1,
    content="First comment",
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(id=3, content="reply 2", replies=[
            Comment(id=4, content="nested reply")  # reply ke andar reply!
        ])
    ]
)
