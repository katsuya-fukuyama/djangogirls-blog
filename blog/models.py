from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): #models.Model = これはDBに保存してね
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #Foreighn = 他のモデルへのリンク
    title = models.CharField(max_length=100) #Char = 文字数制限あり
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #ブログ公開メソッド
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #titleを返す