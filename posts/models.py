from django.db import models
from django.contrib.auth.models import User

# Create your models here.


'''
Posts.objects.all() - достает все обьекты таблицы без исключения
Posts.objects.filter(title="Текстовая запись") - достает лишь нужные обьекты
Posts.objects.get(title="Текстовая запись") - достает один нужный обьект
Posts.objects.create(title="Текстовая запись", content="Текстовая запись", rate=0) - создает обьект
'''
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="posts")
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True, blank=True, related_name="posts")
    tags = models.ManyToManyField(Tag, null=True, blank=True)


    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    text = models.CharField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
