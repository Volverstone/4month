from django.db import models

# Create your models here.


'''
Posts.objects.all() - достает все обьекты таблицы без исключения
Posts.objects.filter(title="Текстовая запись") - достает лишь нужные обьекты
Posts.objects.get(title="Текстовая запись") - достает один нужный обьект
Posts.objects.create(title="Текстовая запись", content="Текстовая запись", rate=0) - создает обьект
'''
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return f"{self.title}"