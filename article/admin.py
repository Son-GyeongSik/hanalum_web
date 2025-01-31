from django.contrib import admin

from .models import Article, ArticleAttachment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """게시글 어드민 설정 클래스입니다."""

    list_display = [
        'board',
        'author',
        'anonymous_author',
        'title',
        'top_fixed',
        'status',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'board',
        'top_fixed',
        'anonymous_author',
        'status',
        'author',
        'title',
    ]
