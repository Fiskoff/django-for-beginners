from django.db import models

class Post(models.Model):
    # Fields
    title = models.CharField(max_length=120, default="Без названия")
    text = models.TextField()

    # Metadata
    # Позволяет установить дополнительные параметры модели, такие как имя таблицы, порядок и подробное имя. Не является обязательным в модели.
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    # Methods
    # Действуют на экземпляры классов
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)