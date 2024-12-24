from django.db import models
from common.models import CommonModel

# - User: FK => subscriber (구독을 하는 사람)
# - User: FK => subscribed_to (구독을 받는 사람)

class Subscription(CommonModel):
    subscriber =  models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to =  models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscribers')

    # 역참조 시 헷갈리지 않도록 직관적으로 related_name을 지정한다.
    # user.subscribers.all() => 특정 사용자를 구독한 사람들의 목록보기 / 잇섭을 구독한 사람들 보기)
    # user.subscriptions.all() => 특정 사용자가 구독한 사람들의 목록보기 / 내가 구독한 유튜버들 보기)
