from django.urls import path
from .views import registergoalfunc, updategoalfunc, impressionfunc, impressiongoodfunc, changegoodfunc
from .views import decideregisterfunc, decideupdatefunc, detailgoalscreenfunc, selectgoalinmapfunc, selectgoalscreenfunc

urlpatterns = [
    # ゴール新規登録
    path('register/', registergoalfunc, name='register'),
    # ゴール情報更新
    path('update/', updategoalfunc, name='update'),
    # 感想投稿
    path('impression/', impressionfunc, name='impression'),
    # 感想にいいね
    path('impressiongood/', impressiongoodfunc, name='impressiongood'),
    # 変更申請にいいね 
    path('changegood/', changegoodfunc, name='changegood'),
    # ゴール登録申請確定
    path('decideregister/', decideregisterfunc, name='decideregister'),
    # ゴール変更申請確定 
    path('decideupdate/<int:pk>',decideupdatefunc,name='decideupdate'),
    # ゴール詳細画面表示 (リストからゴール選択)  
    path('detailgoalscreen/', detailgoalscreenfunc, name='detailgoalscreen'),
    # 地図からゴール選択
    path('selectgoalinmap/', selectgoalinmapfunc, name='selectgoalinmap'),
    # ゴール選択画面表示 (都道府県検索)
    path('selectgoalscreen/', selectgoalscreenfunc, name='selectgoalscreen'),
]
