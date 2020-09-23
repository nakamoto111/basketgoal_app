from django import forms
from .models import place 

# ゴール登録Form
# 課題: ChoiseField -> choisesの書き方

class GoalForm(forms.Form):
    # place DBからpkと県名を取得する
    object_list = place.objects.all()
    # -> for文で回すか、そのまま入れれるものなのか -> 格納表記
    prefecture = forms.ChoiseField(
        # 今のchoicesは例
        choices = (
                (1, '愛知県'),
                (2, '青森県'),
                (3, '石川県'),
                (4, '富山県'),
                (5, '東京都')
        )
    )
    address = forms.CharField(max_length=100)
    name = forms.CharField(max_length=30)
    image = forms.ImageField(required=False, upload_to='')
    starttime = forms.TimeField(required=False)
    endtime = forms.TimeField(required=False)
    url = forms.URLField(required=False)
    explanation = forms.TextField(required=False, max_length=1000)
    otherinfo = forms.TextField(required=False, max_length=1000)

# ゴール情報更新画面でのフォームオブジェクト
class UpdateApplication(forms.Form):

    # コンストラクタ -> goal(呼び出し元でsessionからとってくる)を引数
    def __init__(self, goal):
        self.fields['prefecture'] = goal.prefecture_pk #initial={'placepk':fields['prefecture']
        self.fields['address'] = goal.address
        self.fields['name'] = goal.name
        self.fields['image'] = goal.image
        self.fields['starttime'] = goal.startime
        self.fields['endtime'] = goal.endtime
        self.fields['url'] = goal.url
        self.fields['explanation'] = goal.explanation
        self.fields['otherinfo'] = goal.otherinfo

    # place DBからpkと県名を取得する
    object_list = goal.objects.all()
    # object_listの型を確認
    # -> for文で回すか、そのまま入れれるものなのか
    prefecture = forms.ChoiseField(
        # 今のchoicesは例
        choices = (
                ('ja', '日本'),
                ('us', 'アメリカ'),
                ('uk', 'イギリス'),
                ('ch', '中国'),
                ('kr', '韓国')
        ),
        initial = self.fields['prefecture']
    )
    address = forms.CharField(max_length=100, initial=fields['address'])
    # 住所が存在するか否か -> 無理 
    name = forms.CharField(max_length=30, initial=fields['name'])
    image = forms.ImageField(required=False, initial=fields['image'])
    starttime = forms.TimeField(required=False, initial=fields['starttime'])
    endtime = forms.TimeField(required=False, initial=fields['endtime'])
    url = forms.URLField(required=False, initial=fields['url'])
    explanation = forms.TextField(required=False, max_length=1000, initial=fields['explanation'])
    otherinfo = form.TextField(required=False, max_length=1000, initial=fields['otherinfo'])


class ImpressionForm(forms.Form):
    impression = forms.TextField(max_length=1000)


