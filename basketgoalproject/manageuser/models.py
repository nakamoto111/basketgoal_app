from django.db import models

# Create your models here.

# userの情報を構成する
class User(models.Model):
    # 名前(policy-> 3文字以上30文字以下) (min_lengthは指定可能??)
    name = models.CharField(max_length=30)
    # パスワード(policy-> 10文字以上30文字以下) 
    password = models.CharField(max_length=30)
    # アイコン画像
    image = models.ImageField(upload_to='')
    # 備考(1000文字以内) 
    otherinfo = models.TextField()

class Prefecture(models.Model):
    # 県名
    name = CharField(max_length=20)

class changedhistory(models.Model):
    # ゴールの主キー
    goalpk = models.IntegerField()
    # 変更した変数
    changedvariable = models.TextField()
    # changedvariableで指定した変数の前の状態
    before = models.TextField()
    # changedvariableで指定した変数の後の状態
    after = models.TextField()





