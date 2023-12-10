from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    author = models.ForeignKey(User ,on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    date = models.DateTimeField('Дата Заметки')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

