from django.db import models
from common.models import CommonModel

# - User: FK
    # => User : Comment => 1:N
    # -> User : Comment, Comment, Comment => o
    # -> Comment : User, User, User => x
# - Video: FK
    # => Video : Comment => 1:N
    # -> Video : Comment, Comment, Comment => o
    # -> Comment : Video, Video, Video => x
# - content
# - like
# - dislike

class Comment(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # 대댓글
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)