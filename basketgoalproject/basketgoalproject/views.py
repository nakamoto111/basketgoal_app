from django.shortcuts import render
#sessionのimportっているっけ

def indexfunc(request):
    # セッションにユーザー->ログイン後画面
    if 'user' in request.session:
        user = request.session['user']
        return render(request, 'index_af.html', {'user':user})
    # セッションにユーザーがいない場合
    else
        return render(request, 'index_be.html')
