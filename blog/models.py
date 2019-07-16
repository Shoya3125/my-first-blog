from django.db import models
from django.utils import timezone

# Create your models here.
#Fieldを定義している
class post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    Create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publis(self):          #クラス内メソッド
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
