from django.contrib import admin #adminモジュールを呼び出す
from .models import post         #構築したモデルをインポートする

admin.site.register(post)        #管理サイトで編集できるモデルを呼び出す
