from django.shortcuts import render

# ゴール登録func
# 出力: (post) 入力エラー: goalregister.html
# 出力: (post) 入力正常 : goalregister_confirm.html
# 出力: (get) : goalregister.html

def registergoalfunc(request):
    #requestがpostの場合
    if request.method == 'post':
        # エラー内容を格納していくリスト
        errorList = []
        # formオブジェクト生成 -> reqestの内容を持つobjectを引数に
        form = GoalForm(req.POST, req.FILES)

        # goalformオブジェクトから入力内容を取得する -> user情報を格納する必要あり
        input_address = form.cleaned_data['address']
        input_name = form.cleaned_data['name']
        input_image = form.cleaned_data['image']
        input_starttime = form.cleaned_data['starttime']
        input_endtime = form.cleaned_data['endtime']
        input_url = form.cleaned_data['url']
        input_explanation = form.cleaned_data['explanation']
        input_otherinfo = form.cleaned_data['otherinfo']
    
        ## ポリシー違反チェック
        # addressが5文字以上、100文字以内
        address_count = len(input_address)
        if address_count < 5 or address_count > 100:
            errorList.append('住所は5文字以上100文字以内で入力してください')
        # addressは英数字で構成
        if not input_address.isalnum():
            errorList.append('住所は英数字で入力してください')
        # nameが5文字以上、30文字以内
        name_count = len(input_name)
        if name_count < 5 or name_count > 30:
            errorList.append('名前は5文字以上、30文字以内で入力してください')
        # nameは英数字で構成
        if not input_name.isalnum():
            errorList.append('名前は英数字で入力してください')

        # errorListが空でない場合 -> ポリシー違反が発生 -> goal_register.htmlに戻る
        if len(errorList) >= 1:
            return render(request, 'goalregister.html', {'errorList':errorList})
        # errorListが空でない場合 -> goalオブジェクト作成
        # セッションからユーザ情報を取得 -> goalオブジェクトに格納する
        else:
            goal = Goal()
            # formからinputされた内容を記述
            goal.address = input_address
            goal.name = input_name
            goal.image = input_image
            goal.starttime = input_starttime
            goal.endtime = input_endtime
            goal.url = input_url
            goal.explanation = input_explanation
            goal.otherinfo = input_otherinfo

            # セッションから取得したuser情報を取得 
            # セッションにuserが存在する場合
            if 'user' in request.session:
                user = request.session['user']
                goal.writeuser_pk = user.pk
                goal.save()
                # ゴール登録確認画面に遷移 (作成したゴールオブジェクトを渡す)
                # return render(request, 'goalregister_comfirm.html', {'goal', goal})
                # 今は一応登録を完了させる
                return render(request, 'index_af.html', {'user', user})

            # セッションにuserがいない場合
            else:
                return render(request, 'session.html')
    # requestがgetの場合
    else:
        if 'user' in request.session:
            return render(request, 'goalregister.html') 
        # セッションにログインしたユーザがいない -> セッションタイムアウト
        else:
            return render(request, 'sessiontimeout.html') 

# ゴール情報更新func
# 出力: セッションタムアウト
# 出力: (post) ポリシー違反、内容変更されていない: goalupdate.html
# 出力: (post) 正常: goalupdate_conform.html
# 出力: (get) goalupdate.html

def updategoalfunc(request):
    # requestがpostの場合
    if request.method == 'post':
        
        # sessionに格納されているgoal情報を取得する -> セッションになければsessiontimeout
        # セッションからゴール情報取得
        if 'goal' in request.session:
            session_goal = request.session['goal']
            session_address = session_goal.address
            session_name = session_goal.name
            session_image = session_goal.image
            session_starttime = session_goal.starttijme 
            session_endtime = session_goal.endtime
            session_url = session_goal.url
            session_explanation = session_goal.explanation
            session_otherinfo = session_goal.otherinfo
        else:
            # error -> セッションタイムアウト画面
            return render(request, 'sessiontimeout.html')

        # 押されたボタンがdelete or update
        # === 更新処理 === #
        # もし押されたボタンが更新なら
        if request.post['act'] == 'update':
            # formオブジェクト生成 -> reqestの内容を持つobjectを引数に
            form = GoalForm(req.POST, req.FILES)
            # goalformオブジェクトから入力内容を取得する
            input_address = form.cleaned_data['address']
            input_name = form.cleaned_data['name']
            input_image = form.cleaned_data['image']
            input_starttime = form.cleaned_data['starttime']
            input_endtime = form.cleaned_data['endtime']
            input_url = form.cleaned_data['url']
            input_explanation = form.cleaned_data['explanation']
            input_otherinfo = form.cleaned_data['otherinfo']

            #ポリシー違反チェック
            # addressが5文字以上、100文字以内
            address_count = len(input_address)
            if address_count < 5 or address_count > 100:
                errorList.append('住所は5文字以上100文字以内で入力してください')
            # addressは英数字で構成
            if not input_address.isalnum():
                errorList.append('住所は英数字で入力してください')
            # nameが5文字以上、30文字以内
            name_count = len(input_name)
            if name_count < 5 or name_count > 30:
                errorList.append('名前は5文字以上、30文字以内で入力してください')
            # nameは英数字で構成
            if not input_name.isalnum():
                errorList.append('名前は英数字で入力してください')

            # errorListが空でない場合 -> ポリシー違反が発生 -> goalupdate.htmlに戻る
            if len(errorList) >= 1:
                return render(request, 'goalupdate.html', {'errorList':errorList})

            ## 全く内容が変更されていないかチェック
            # 初期値初期化
            param = 0
            errorList = []
            # address
            if input_address != session_address:
                param = 1
            # name 
            elif input_name != session_name:
                param = 1
            # image
            elif input_image != session_image:
                param = 1
            # starttime 
            elif input_starttime != session_starttime:
                param = 1
            # endtime 
            elif input_endtime != session_endtime:
                param = 1
            # url 
            elif input_url != session_url:
                param = 1
            # explanation 
            elif input_explanation != session_explanation:
                param = 1
            # otherinfo 
            elif input_otherinfo != session_otherinfo:
                param = 1

            if param == 0:
                errorList.append('内容の変更がありません')
                return render(request, 'goalupdate.html', {'errorList':errorList})
            else:
                # ポリシー違反がなく更新内容がある場合は全ての情報を更新
                session_goal.address = input_address
                session_goal.name = input_name
                session_goal.image = input_image
                session_goal.starttime = input_starttime
                session_goal.endtime = input_endtime
                session_goal.url = input_url
                session_goal.explanation = input_explanation
                session_goal.otherinfo = input_otherinfo

                # DB変更
                session_goal.save()

        # 押されたボタンが削除の場合
        else:
            #=== 削除処理===#
            # 確認処理 -> ポップアップを出す -> 課題
            # DBからデータ削除 -> 課題
            goal = goal.objects.filter(name=input_name).delete()  #削除処理
            
    # requestがgetの場合
    else:
       # セッションからユーザー情報取得
       if 'goal' in request.session:
           goal = request.session['goal']
           return render(requst, 'goalupdate.html', {'goal', goal}) 
       else:
           # error -> セッションタイムアウト画面
           return render(request, 'sessiontimeout.html')

# 感想の投稿
def impressionfunc(request):
    #requestがpostの場合
    if request.method == 'post':
       # formオブジェクト生成 
        form = ImpressionForm(req.POST, req.FILES)

        # impressionformオブジェクトから入力内容を取得する
        input_impression = form.cleaned_data['impression']
    
        # セッションからユーザ情報、ゴール情報を取得   
        impression = Impression()
        # formからinputされた内容を記述
        goal.impression = input_impression

        # セッションから取得したuser情報、goal情報を取得 
        # セッションにuser, goalが存在する場合
        if 'user' in request.session:
            if 'goal' in request.session:
                user = request.session['user']
                goal = request.session['goal']
                impression.userpk = user.pk
                impression.goalpk = user.pk
                impression.save()
                return render(request, 'detailgoalscreen.html')
        # セッションにuser, goalがいない場合
        else:
            return render(request, 'sessiontimeout.html')



# 感想にいいねが押された場合に呼び出される
# 課題: 1ユーザが1いいねしか押せないようにする -> ManytoManyField
def impressiongoodfunc(request, pk):
    impression = Impression.objects.get(pk=pk)
    # セッションにあるユーザー情報を取得する
    if 'user' in request.session:
        user = request.session['user']
    else:
        return render(request, 'sessiontimeout.html')

    # 今いいねを押された感想にいいねを押したユーザーを取得する
    good_users = Impression.objects.get(pk=pk).good_users.all()
    # ログインしているユーザーがいいねを押したユーザーに含まれていない場合
    if user not in good_users:
        # いいね +1
        impression.good = impression.good + 1
        # いいねを押したユーザーのを追加する
        impression.good_users.add(user)
        # データベースの中で保存される
        impression.save()
    return redirect('detailgoalscreen')


# 変更申請にいいねが押された場合に呼び出される
def changegoodfunc(request, pk):
    changeapplication = Changeapplication.objects.get(pk=pk)
    # セッションにあるユーザー情報を取得する
    if 'user' in request.session:
        user = request.session['user']
    else:
        return render(request, 'sessiontimeout.html')

    # 今いいねを押された変更申請にいいねを押したユーザーを取得する
    good_users = changeapplication.objects.get(pk=pk).good_users.all()
    # ログインしているユーザーがいいねを押したユーザーに含まれていない場合
    if user not in good_users:
        # いいね +1
        changeapplication.good = changeapplication.good + 1
        # いいねを押したユーザーのを追加する
        changeapplication.good_users.add(user)
        # データベースの中で保存される
        changeapplication.save()
    return redirect('detailgoalscreen')


# ゴール詳細画面表示(リストからゴール選択) detailgoalscreenfunc
def detailgoalscreenfunc(request, pk):
    # 指定されたpkのゴールのオブジェクトをDBから取得
    goal = Goal.objects.get(pk=pk)
    # セッションに保存する
    request.session['goal'] = goal
    # ゴール詳細画面に遷移
    return redirect('detailgoalscreen')


# 地図からゴール選択 -> リストを目立たせる
def selectgoalinmapfunc(request, pk):
    # 指定されたpkのゴールのオブジェクトをDBから取得
    goal = Goal.objects.get(pk=pk)
    # ゴール詳細画面に遷移する
    return render(request, 'detailgoalscreen', {'selectedgoal', goal})


# ゴール選択画面表示(都道府県検索 -> ゴール一覧表示) selectgoalscreenfunc
def selectgoalscreenfunc(request, pk):
    # 指定されたprefectureのゴール一覧のオブジェクトをDBから取得
    goals = Goal.objects.get(prefecture_pk=pk)
    # セッションに保存する
    request.session['goals'] = goals
    # ゴール詳細画面に遷移
    return redirect('selectgoalscreen')




# decideregisterfunc
# decideupdatefunc


