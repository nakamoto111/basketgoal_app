from django.db import models

# Create your models here.

# userの情報を構成する
class User(models.Model):
    # 名前   
    name = models.CharField(max_length=30)
    # パスワード
    password = models.CharField(max_length=30)
    # アイコン画像
    image = models.ImageField(upload_to='')
    # 備考 
    otherinfo = models.TextField(max_length=1000)


# ゴール情報
class Goal(models.Model):
    # 場所のpk (どこの都道府県に所属してるか)
    prefecture_pk = models.IntegerField()
    # 住所(県名以下)
    address = models.CharField(max_length=100)
    # ゴールの名前
    name = models.CharField(max_length=30)
    # ゴールの画像
    image = models.ImageField(upload_to='')
    # 利用可能時間（モデルで時刻の指定方法はある？）
    starttime = models.TimeField()
    # 利用終了時間
    endtime = models.TimeField()
    # URL -> ホームページへのURLなど
    url = models.URLField()
    # 説明
    explanation = models.TextField(max_length=1000)
    # 備考
    otherinfo = models.TextField(max_length=1000)


# 感想情報
# 課題: 外部キーの指定の仕方
class Impression(models.Model):
    # ゴールの主キー
    goalpk = models.IntegerField()
    # 感想を投稿したユーザーの主キー
    userpk = models.IntegerField()
    # 感想
    impression = models.TextField()
    # 感想へのいいね
    good = models.IntegerField()
    # いいねを押したユーザー
    good_users = models.ManyToManyField(User)


# 変更申請
class Changeapplication(models.Model):
    # ゴールの主キー
    goalpk = models.IntegerField()
    # 変更した変数
    changedvariable = models.CharField(max_length=30)
    # changedvariableで指定した変数の前の状態
    before = models.TextField()
    # changedvariableで指定した変数の後の状態
    after = models.TextField()
    # 変更に対してのいいね
    good = models.IntegerField()
    # いいねを押したユーザー
    good_users = models.ManyToManyField(User)

# 感想 
class Impression(models.Model):
    # ゴールの主キー(外部きー)
    goalpk = models.IntegerField()
    # 感想を記載したユーザーの主キー(外部キー)
    userpk = models.IntegerField()
    # 感想
    impression = models.TextField(max_length=1000)
    # 変更申請に対するいいね
    good = models.IntegerField()
