from django.shortcuts import render
from .forms import UserForm

# ユーザー登録func
# 課題: 画像のアップロード処理,formオブジェクトの使用について
# 出力: (post) 入力エラー: signup.html
# 出力: (post) 入力正常 : index_be.html
# 出力: (get) セッションにユーザ: index_af.html
# 出力: (get) セッションにユーザなし: index_be.html
def signupfunc(request):
    #requestがpostの場合
    if request.method == 'post':
        # エラー内容を格納していくリスト
        errorList = []
        # formオブジェクト生成 -> reqestの内容を持つobjectを引数に
        form = UserForm(req.POST, req.FILES)

        #input_username = request.post['username']
        #input_password = request.post['password']
        # 画像のアップロード -> 保存のやり方
        #input_image = request.post['image']
        #input_otherinfo = request.post['otherinfo']

        # userformオブジェクトから入力内容を取得する
        input_username = form.cleaned_data['username']
        input_password = form.cleaned_data['password']
        input_image = form.cleaned_data['image']
        input_otherinfo = form.cleaned_data['otherinfo']
        # フォームオブジェクトが有効でない場合
        #if not form.is_valid():
        #    # usernameのmax_length, min_length チェック
        #   if not form.username.max_length or not form.username.min_length:
        #        errorList.append('ユーザ名は3文字以上15文字以内で入力してください')

        # usernameが5文字以上、15文字以内
        username_count = len(input_username)
        if username_count < 5 or username_count > 15:
            errorList.append('ユーザ名は3文字以上15文字以内で入力してください')
        # usernameは英数字で構成
        if not input_username.isalnum():
            errorList.append('ユーザー名は英数字で入力してください')
        # passwordが5文字以上、15文字以内
        password_count = len(input_password)
        if password_count < 5 or password_count > 15:
            errorList.append('パスワードは5文字以上、15文字以内で入力してください')
        # passwordは英数字で構成
        if not input_password.isalnum():
            errorList.append('パスワードは英数字で入力してください')

        # errorListが空でない場合 -> ポリシー違反が発生 -> signup.htmlに戻る
        if len(errorList) >= 1:
            return render(request, 'signup.html', {'errorList':errorList})
        # errorListが空でない場合 -> userオブジェクト作成
        else:
            user = User()
            user.username = input_username
            user.password = input_password
            user.image = input_image
            user.otherinfo = input_otherinfo
            user.save()
            return render(request, 'index_be.html')

    #requestがgetの場合
    else
        # セッションにユーザがいる場合
        if 'user' in request.session:
            user = request.session['user']
            return render(request, 'index_af.html', {'user': user})
        # セッションにユーザーがいない場合
        else
            return render(request, 'index_be.html')

# ログインfunc
# 課題: user = user.objects.get(username=input_username)の問題の是非
# 出力: (post) 入力内容と合うユーザが存在: index_af.html
# 出力: (post) 入力内容と合うユーザが不在: login.html
# 出力: (get)  入力内容と合うユーザが存在: index_af.html
# 出力: (get)  入力内容と合うユーザが不在: index_be.html
def loginfunc(request):
    #requestがpostの場合
    if request.method == 'post':
        input_username = request.post['username']
        input_password = request.post['password']
        try:
               # userテーブルからusernameがinput_usernameのユーザーの取得を試みる
               user = user.objects.get(username=input_username) #=== 課題 ===#
               # セッションにユーザ追加
               request.session['user'] = user 
               # ユーザーが既に存在している場合、ログイン成功 -> index_af.htmlに遷移
               return render(request, 'index_af.html', {'user' : user}) 
        except:
               # input_usernameのユーザーがuserテーブルに存在していない場合 -> ログイン画面に戻る
               return render(request, 'login.html', {'error':'ログイン名またはパスワードが間違っています'})
    #requestがgetの場合
    else:
        # セッションにuserが存在する場合
        if 'user' in request.session:
            user = request.session['user']
            return render(request, 'index_af.html', {'user':user})
        # セッションにuserがいない場合
        else:
            return render(request, 'index_be.html')
)


# ユーザー更新func
# 課題: 削除時にポップアップで確認をする方法
# 課題: DBからデータ削除
# 課題; DBの更新処理 (正しいかチェック)
# 出力: セッションタムアウト
# 出力: (post) ポリシー違反、内容変更されていない: user_update.html
# 出力: (post)  
def updatefunc(request):
    # requestがpostの場合
    if request.method == 'post':
        
        # sessionに格納されているuser情報を取得する -> セッションになければsessiontimeout
        # セッションからユーザー情報取得
        if 'user' in request.session:
            session_user = request.session['user']
            session_username = session_user.username
            session_password = session_user.password
            session_image = session_user.image
            session_otherinfo = session_user.otherinfo
        else:
            # error -> セッションタイムアウト画面
            return render(request, 'sessiontimeout.html')

        # 押されたボタンがdelete or update
        # === 更新処理 === #
        # もし押されたボタンが更新なら
        if request.post['act'] == 'update':
            # formオブジェクト生成 -> reqestの内容を持つobjectを引数に
            form = UserForm(req.POST, req.FILES)
            # userformオブジェクトから入力内容を取得する
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password']
            input_image = form.cleaned_data['image']
            input_otherinfo = form.cleaned_data['otherinfo']
                        ## ポリシー違反チェック
            # エラー内容を格納していくリスト
            errorList = []
            # usernameが5文字以上、15文字以内
            username_count = len(input_username)
            if username_count < 5 or username_count > 15:
                errorList.append('ユーザ名は3文字以上15文字以内で入力してください')
            # usernameは英数字で構成
            if not input_username.isalnum():
                errorList.append('ユーザー名は英数字で入力してください')
            # passwordが5文字以上、15文字以内
            password_count = len(input_password)
            if password_count < 5 or password_count > 15:
                errorList.append('パスワードは5文字以上、15文字以内で入力してください')
            # passwordは英数字で構成
            if not input_password.isalnum():
                errorList.append('パスワードは英数字で入力してください')

            # errorListが空でない場合 -> ポリシー違反が発生 -> signup.htmlに戻る
            if len(errorList) >= 1:
                return render(request, 'user_update.html', {'errorList':errorList})

            ## 全く内容が変更されていないかチェック
            # 初期値初期化
            param = 0
            errorList = []
            # username
            if input_username != session_username:
                param = 1
            # password
            elif input_password != session_password:
                param = 1
            # image
            elif input_image != session_image:
                param = 1
            # otherinfo
            elif input_otherinfo != session_otherinfo:
                param = 1
            
            if param == 0:
                errorList.append('内容の変更がありません')
                return render(request, 'user_update.html', {'errorList':errorList})
            else:
                session_user.username = input_username
                session_user.password = input_password
                session_user.image = input_image
                session_user.otherinfo = input_otherinfo
                # DB変更
                session_user.save()
        # もし押されたボタンが削除なら
        else:
            #=== 削除処理===#
            # 確認処理 -> ポップアップを出す -> 課題
            # DBからデータ削除 -> 課題
            user = user.objects.filter(username=session_username).delete()  #削除処理
            
    # requestがgetの場合-> ユーザー情報更新画面表示
    else:
       # セッションからユーザー情報取得
       if 'user' in request.session:
           user = request.session['user']
           return render(requst, 'user_update.html', {'user', user}) 
       else:
           # error -> セッションタイムアウト画面
           return render(request, 'sessiontimeout.html')

# ログアウト処理
# 出力: セッションにユーザ存在: login_be.html
# 出力: セッションいユーザ不在: sessiontimeout.html
def logoutfunc(request):
    # requestがpostの場合
    if request.method == 'post':
        # セッションにユーザーが存在している場合
        if 'user' in request.session:
            del request.session['user']
            return render(request, 'index_be.html')
        else:
            return render(request, 'sessiontimeout.html')
