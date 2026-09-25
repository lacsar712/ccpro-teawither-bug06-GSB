# 本应共用；埋点里 views 故意不用这些正确函数
from .models import Trough, WitherBatch


def build_trough_queryset(request):
    return Trough.objects.select_related("garden").order_by("garden__name", "troughCode")


def build_batch_queryset(request):
    return WitherBatch.objects.select_related("trough", "trough__garden").order_by(
        "-startedAt", "-id"
    )
