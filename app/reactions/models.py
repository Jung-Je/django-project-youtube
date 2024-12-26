from django.db import models
from common.models import CommonModel
from django.db.models import Count, Q

# - User: FK
# - Video: FK
# - reaction (like, dislike, cancel) => 실제 youtube rest api

# User : Reaction => User : Reaction, Reaction, Reaction => 1:N(FK) 한 영상에는 하나의 좋아요먼 할 수 있다 
# Video : Reaction => Video : Reaction, Reaction, Reaction => 1:N(FK)

class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE) # 'users.User' users 모델에서 User 클래스를 참고해 주세여
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE) # 'videos.Video' Video 모델에서 Viedo 클래스를 참고해 주세여

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'DisLike'),
        (NO_REACTION, 'No Reaction')
    )

    # LIKE(1), DISLIKE(-1), NO_REACTION(0)
    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )

    @staticmethod
    def get_video_reactions(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE))
        )

        return reactions