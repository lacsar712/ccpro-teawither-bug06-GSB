# 整页视图与 HTMX 局部片段共用的查询/排序入口，保证刷新前后行集合一致
from .models import Trough, WitherBatch


def build_trough_queryset(request):
    return Trough.objects.select_related("garden").order_by("garden__name", "troughCode")


def build_batch_queryset(request):
    return WitherBatch.objects.select_related("trough", "trough__garden").order_by(
        "-startedAt", "-id"
    )
