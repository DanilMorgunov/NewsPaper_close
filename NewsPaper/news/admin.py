from django.contrib import admin
from .models import Post, Category, Author, PostCategory, Comment
from modeltranslation.admin import TranslationAdmin

def nullify_rating(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(rating=0)
nullify_rating.short_description = 'Обнулить ратинг' # описание для более понятного представления в админ панеле задаётся, как будто это объект


class AuthorAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Author._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_display = ('id', 'ratingAuthor')
    list_filter = ('id', 'ratingAuthor')
admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Author._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_display = ('author', 'categoryType', 'dateCreation', 'title', 'text', 'rating')
    list_filter = ('author', 'categoryType', 'dateCreation', 'rating')
    search_fields = ('author', 'title', 'text') # тут всё очень похоже на фильтры из запросов в базу


class PostAdminTranslate(TranslationAdmin):
    model = Post

admin.site.register(Post, PostAdmin)


class PostCategoryAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Author._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_display = ('postThrough', 'categoryThrough')
    list_filter = ('postThrough', 'categoryThrough')
    search_fields = ('postThrough', 'categoryThrough') # тут всё очень похоже на фильтры из запросов в базу
admin.site.register(PostCategory, PostCategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Author._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_display = ('commentPost', 'commentUser', 'text', 'dateCreation', 'rating',)
    list_filter = ('commentUser', 'dateCreation', 'rating')
    search_fields = ('commentPost', 'text') # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullify_rating] # добавляем действия в список
admin.site.register(Comment, CommentAdmin)