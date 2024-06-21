x = 0;y = 0; dx = 0.1; dy = 0.03;iwa_dy = 0.8;iwa_y=0;iwa_y2=0;hosi_y = 0;hosi_dy=0.8;hosi_y2 = 0;hosi_dy2 = 0.8;aman_y = 0;hosi1 = 0;hosi2 = 0;moya_j = 0;big_hosi = 0;big_hosi2 = 0#星や宇宙の進む速度を変更する関数を設定する。
moya_r = [0] * 500;moya_x = [0] * 500;moya_y = [0] * 500#宇宙にある靄のようなものの一つ一つの初期設定
elli_X = [0] * 500 ; elli_Y = [0] * 500                 #星の初期設定
elli_Y = [0] * 500 ; elli_Y = [0] * 500                 #上記に同じ
kuromoya_r = [0] * 50                                   #黒色の靄の位置の初期設定
moya_dx = [0] * 50
moya_dy = [0] * 50
ama_x = [0] * 80;ama_y = [0] * 80                       #天の川の位置の初期設定(真ん中右寄りにある星の群れ)
ama_x2 = [0] * 80;ama_y2 = [0] * 80                     #天の川の位置の初期設定(真ん中右寄りにある星の群れ)
aman_x = [0] * 20                                       #天の川の位置の初期設定(真ん中右寄りにある星の群れ)
aman_y = [0] * 20                                       #天の川の位置の初期設定(真ん中右寄りにある星の群れ)
hosi1 = [0] * 2500                                      #星の初期設定
hosi2 = [0] * 2500                                      #星の初期設定
bighosi = [0] * 200                                     #星の初期設定
bighosi2 = [0] * 200                                    #星の初期設定
iwa_c1 = [0] * 13                                       #名前表示の星座の色設定
iwa_c2 = [0] * 13                                       #名前表示の星座の色設定
iwa_c3 = [0] * 13                                       #名前表示の星座の色設定
line1=0; line2=0; line3=0                               #星と星を結ぶ線の初期設定
naga_x=700; naga_y=-50                                  #流れ星の初期位置設定
s = 70; ds =1                                           #流れ星の出る条件の初期設定
star_n = 0                                              #流れ星を設定するための関数
kusa_x = 0   
ura_kusa_x = 0                                           #草を動かすための、草の座標ｘ
kusa_dx = 5                                             #草の速さを決める関数dx
kusa_ran = 0                                            #草が自然にランダムに決まるように設定
startup = 1                                             #メニュー画面で使う関数 
load = 0                                                #press k to start を点滅させるために使う関数
loadx = 0                                               #上記と同じ
load_dx = 1                                             #上記と同じ
mc1 = 100;mc2 =50;mc3 = 200                             #色をカラフルにする関数
mcd1 = 20; mcd2 = 20; mcd3 = 20                         #色を常時変化させる関数

def setup():                                           #def setup関数での設定                                    
    size(800, 600)                                     #ウィンドウを作成
    for i in range(500):                               #0~499までのiを作成
        moya_r[i] = random(70, 220)                    
        moya_x[i] = random(0, 800)                     #靄のx座標を0から800まででランダムに設定
        moya_y[i] = random(0, 600)                     #靄のy座標を0から600まででランダムに設定
        elli_X[i] = random(0, 800)                     #円のx座標をランダムに設定
        elli_Y[i] = random(0, 600)                     #円のy座標をランダムに設定
    for i in range(50):
        kuromoya_r[i] = random(0, 40)                  #黒い靄に代入する値をランダムで設定
        moya_dx[i] = random(-10*i, 10*i)               #靄一つの中でランダムに設定
        moya_dy[i] = random(-10*i, 10*i)               #靄一つの中でランダムに設定
    for aman in range(0, 400, 20):                   
        for i in range(80):                           
            ama_x[i] = random(-2*i, 4*i)               #天の川のx座標
            ama_y[i] = random(-2*i, 4*i)               #天の川のy座標
            ama_x2[i] = random(-2*i, 4*i)              #天の川2個目のx座標
            ama_y2[i] = random(-2*i, 4*i)              #天の川2個目のy座標
    for i in range(2500):
        hosi1[i] = random(0, 800)                      #星の座標をランダムに設定
        hosi2[i] = random(0, 600)                      #星の座標をランダムに設定
    for i in range(200):                               
        bighosi[i] = random(0, 800)                    #大きめの星のｘ座標をランダムに設定
        bighosi2[i] = random(0, 600)                   #大きめの星のｙ座標をランダムに設定
    for i in range(13):
        iwa_c1[i] = random(140, 255)                   #イワタと表示する星座の明るさの赤をランダムに設定
        iwa_c2[i] = random(200, 255)                   #イワタと表示する星座の明るさの緑をランダムに設定
        iwa_c3[i] = 255                                #イワタと表示する星座の明るさの青を255に設定
    s = second
    frameRate(15)                                      #フレームレートを15に設定
  
def draw():
    global x, y, dx, dy, iwa_dy, iwa_y, hosi_y, hosi_dy, hosi_y2, hosi_dy2, line1, line2, line3, s, ds, naga_x, naga_y, star_n, kusa_x, kusa_dx, kura_ran, ura_kusa_x, startup, loadx, load_dx, load, mc1, mc2, mc3, mcd1, mcd2, mcd3
    backhaikei(x, y)                                   #グローバル定数として使うものを設定、背景関数を表示
    
    #-------move star------
    iwa_y += iwa_dy                                    #イワタと表示する星座を下に動くように設定
    if iwa_y >= 500:                                   #イワタと表示する星座が下に行くと画面の上に行くように設定
        iwa_y = -400                                   #上に同じ
        
    hosi_y += hosi_dy                                  #星を下に動くように設定
    if hosi_y >= 600:                                  #星が下に行くと画面の上に行くように設定
        hosi_y = -600                                  #上に同じ
        
    hosi_y2 += hosi_dy2                                #もともと画面の上にある星が下に行くように設定
    if hosi_y2 >= 1200:                                #もともと画面の上の星が下に行くと画面の上に行くように設定
        hosi_y2 = 0                                    #上に同じ
    
    
    #------touch star--------
    if mousePressed:                               #星を見つけてクリックした際の設定
        if (70 <= mouseX <= 150) and (70+iwa_y <= mouseY <= 180+iwa_y):
            line1 = 1                                  #イの範囲を押したときにline1を1にする
        elif (205 <= mouseX <= 260) and (180+iwa_y <= mouseY <= 300+iwa_y):
            line2 = 1                                  #ワの範囲を押したときにline2を１にする
        elif (400 <= mouseX <= 460) and (325+iwa_y <= mouseY <= 430+iwa_y):
            line3 = 1                                  #タの範囲を押したときにline3を１にする
    
    
    #---------星----------
    moyan(0, 0)                                        #もやを０，０の場所に追加する
    moya(0, 0)                                         #もやを０，０の場所に追加する
    for aman in range(0, 450, 150):                    #天の川に０～３５０までの数字を入れる
        amanogawa(350+aman, 0+aman+hosi_y)             #  天の川に見せるための星の固まりを描画
        amanogawa2(370+aman, 30+aman+hosi_y)           #二つ目の天の川の描画
    for aman in range(0, 450, 150):                    #あまんに０～４５０まで入れる。
        amanogawa(-50+aman, -500+aman+hosi_y2)         #移動したときに出てくる天の川を表示するコマンド
        amanogawa2(-40+aman, -530+aman+hosi_y2)        #移動したときに出てくる天の川を表示するコマンド

    
    hosibosi(0, 0+hosi_y)                              #星々を表示するコマンド
    big_hosi(0, 0+hosi_y)                              #星々を表示するコマンド
    hosibosi(0, -600+hosi_y2)                          #上から流れてくる星々を表示するコマンド
    big_hosi(0, -600+hosi_y2)                          #上から流れてくる星々を表示するコマンド
    iwa_hosi(0, 0+iwa_y)                               #星座を表示するコマンド
    
        #---------line---------
    strokeWeight(1)
    if line1 == 1:                                     #いの星々を結ぶ線を描画
        stroke(255, 200)                               #線の色を白色に決める
        line(150, 70+iwa_y, 120, 100+iwa_y)            #いの一番上の線の描画
        line(70, 120+iwa_y, 120, 100+iwa_y)            #いの真ん中から左下の星の線の描画
        line(120, 100+iwa_y, 105, 180+iwa_y)           #いの真ん中から下への線の描画
        noStroke()                                     #輪郭をなくす
    if line2 == 1:                                     #わの星々を結ぶ線の描画
        stroke(255, 200)                               #線の色を白色に設定
        line(210, 180+iwa_y, 205, 200+iwa_y)           #ワの一番左の線を描画
        line(210, 180+iwa_y, 277, 195+iwa_y)           #ワの上の線の描画
        line(277, 195+iwa_y, 230, 280+iwa_y)           #ワの右の線の描画
        noStroke()                                     #輪郭をなくす
    if line3 == 1:                                     #タの星々を描画する線の描画
        stroke(255, 200)                               #線の色を白色に設定
        line(400, 320+iwa_y, 390, 355+iwa_y)           #タの左の線の描画
        line(400, 320+iwa_y, 460, 325+iwa_y)           #タの上の線の描画
        line(460, 325+iwa_y, 450, 370+iwa_y)           #タの右上の線の描画
        line(390, 355+iwa_y, 450, 370+iwa_y)           #タの真ん中の線の描画
        line(450, 370+iwa_y, 410, 440+iwa_y)           #タの下の線のンの描画
        noStroke()                                     #輪郭をなくす
        
    if keyPressed:                                     #もしキーを押したとき
        if key == " ":                                 #もしキーがスペースキーなら
            line1 = 0                                  #星座の線を消す
            line2 = 0                                  #星座の線を消す
            line3 = 0                                  #星座の線を消す
            
    s += ds                                            #流れ星が流れる時間を決めるｓを増やす
    if s >= 100:                                       #もしｓが１００を超えたなら
        star_n = 1                                     #流れ星を描画
        s = 0                                          #ｓを０にする　これのループ
        
    if star_n == 1:                                    #もし上でstar_nが１になっていたなら、、、
        nagarebosi(naga_x, naga_y)                     #ながれぼし　一号を設定
        nagarebosi(naga_x+180, naga_y-200)             #流れ星２号を１号より１８０ー２００ずらして描画
        nagarebosi(naga_x-40, naga_y-160)              #流れ星３号を１号よりー４０－４０ずらして描画
        nagarebosi(naga_x+80, naga_y-40)               #流れ星４号を８０ー４０ずらして描画
        naga_x -= 10                                   #ながれぼしを－１０ずつずらす
        naga_y += 10                                   #流れ星のｙ座標を１０ずつ増やす
        naga_x -= 10                                   #流れ星のｘ座標を－１０ずつ減らす
        naga_y += 10                                   #流れ星のｙ座標を１０ずつ増やす
        
        if naga_y >= 1000:                             #流れ星が下に行ったら
            naga_y = -50                               #流れ星を上に戻す
            naga_x = 700                               #流れ星を上に戻す
            star_n = 0                                 #star_nを０にする
        
        
    
    #-------temae---------
    mountain(0, 0)                                     #山を表示する関数を描画
    ura_kusa(0, 0)                                     #裏側の草を表示する関数を描画
    kusa(0, 0)                                         #草を表示する関数を描画
    
    
    
    kusa_x += kusa_dx                                  #草のｘ座標をｄｘ分増やす
    ura_kusa_x = kusa_x + random(-10, 10)              #裏の草はそれよりもランダムに与えられた分自由に動く
    if kusa_x >= 20:                                   #草が最初の座標より２０まで動いたら
        kusa_dx *= -1                                  #反対方向に動かせる
    elif kusa_x <= -10:                                #草が最初の座標より－１０までうごいたら
        kusa_dx *= -1                                  #反対方向に動かす
    kusa_ran = int(random(0,10))                       #kusa_ranの草をランダムに動かす関数をランダムに０から１０まで設定し続ける
    if kusa_ran <= 2:                                  #kusa_ranが２以下ならば
        kusa_dx *= -1                                  #反対方向に動かす
        
        
        
##startup-------------------------
    if startup == 1:                                   #メニュー画面の表示
        loadx += load_dx                               #読み込むときに使う関数を増やしていく
        if loadx >= 2:                                 #２になったら
            loadx = 0                                  #０に戻す
            if load == 1:                              #1なら
                load = 0                               #０にして
            else:
                load = 1                               #０なら１にする
        fill(255)                                      #色を白色にする
        rect(100, 100, 600, 400)                       #四角形を描く
        fill(250, 235, 190)                            #色を黄色にする
        stroke(220, 205, 160)                          #枠を黄色にする
        strokeWeight(5)                                #線の太さを５にする
        triangle(100, 100, 100, 250, 350, 100)         #デザインの三角形を描く
        stroke(mc1+100, mc2+100, mc3+100)              #色を虹色にする
        line(700, 450, 550, 500)                       #デザインの線を描画
        line(700, 450, 400, 500)                       #デザインの線を描画
        line(700, 350, 380, 500)                       #デザインの線を描画
        stroke(220, 205, 160)                          #線を黄色にする
        strokeWeight(5)                                #線の太さを５にする
        line(100, 100, 100, 500)                       #枠組みを作る
        line(100, 100, 700, 100)                       #枠組みを作る
        line(100, 500, 700, 500)                       #枠組みを作る
        line(700, 100, 700, 500)                       #枠組みを作る
        fill(mc1, mc2, mc3)                            #虹色にする
        mc1 += mcd1                                    #色を常時変化させる
        mc2 += mcd2                                    #色を常時変化させる
        mc3 += mcd3                                    #色を常時変化させる
        if mc1 >= 255 or mc1 <= 0:                     #色が限界値に達したら
            mcd1 *= -1                                 #反対向きに移動させる
        if mc3 >= 255 or mc3 <= 0:                     #色が限界値
            mcd3 *= -1                                 #反対向きに移動させる
        if mc2 >= 255 or mc2 <= 0:                     #色が限界値に達したら
            mcd2 *= -1                                 #反対向きに移動させる
        textSize(75)                                   #文字の大きさを７５に設定する
        text("Star hunt!", 150, 240)                   #星をかる！と英語で表示する
        fill(0)                                        #色を黒色にする
        textSize(35)                                   #大きさを３５にする
        text("searching for sign of my name", 140,300) #名前の星座を探せ！
        textSize(20)#大きさを２０にする
        text("This program is heavy, so press and hold until it reacts.", 140, 350)
         #このプログラムは重いです。なので反応するまで押してくださいとの英語のプログラムを表示する。
        
        #文字入力
        fill(0)                                        #色を黒色にする
        
        if load == 1:                                  #ロード関数が１ならば
            textSize(20)                               #文字を２０に設定して
            text("-press K to start-", 500, 470)       #この関数を表示させる
        
    if keyPressed:                                     #もしキーが押されたら
        if key == "k":                                 #Kキーならば
            startup = 0                                #メニューを消す

        
    
def backhaikei(x, y):                                  #背景を表示する関数
    global moya_j                                      #靄で使う関数をglobal定数として設定
    yz_c1 = (1, 30, 50)                                #夜空の色を設定
    yz_c2 = (40, 100, 180)                             #夜空の色の二色目を設定
    noStroke()#枠をなくす
    for i in range(80):                                #１から８０までiに設定
        for j in range(60):                            #1～６０までjに設定
            yozo_color = (yz_c1[0] + ((yz_c2[0]-yz_c1[0])/60)*j,#解像度の８００＊６００まで１０ピクセル筒
                          yz_c1[1] + ((yz_c2[1]-yz_c1[1])/60)*j,#色を少しづつ変えて青色～紫色の
                          yz_c1[2] + ((yz_c2[2]-yz_c1[2])/60)*j)#グラデーションを作るように設定
            fill(yozo_color[0], yozo_color[1], yozo_color[2])#色を決めて
            rect(i*10, j*10, 10, 10)                   #グラデーションになるように少しづつ色の違う四角形を表示
    for moya_j in range(500):                          #宇宙のガスを表示するように設定
        if 300 <= moya_x[moya_j] <= 500 or 200 <= moya_y[moya_j]:#真ん中を除いて
            fill(255, 2)                               #色を設定
            ellipse(moya_x[moya_j], moya_y[moya_j], moya_r[moya_j], moya_r[moya_j])#大量の薄い円を描画
            fill(0, 30, 50, 3)                          #円を利用して靄を描画
            ellipse(elli_X[moya_j], elli_Y[moya_j], moya_r[i], moya_r[i])
        else:
            fill(255, 1)                                #色を設定
            ellipse(moya_x[moya_j], moya_y[moya_j], moya_r[moya_j], moya_r[moya_j])
            fill(0, 30, 50, 3)                           #円を描画（とても薄い）
            ellipse(elli_X[moya_j], elli_Y[moya_j], moya_r[moya_j], moya_r[moya_j])

def moyan(x, y):       
    for kuromoya_j in range(7):                     #黒い靄を描画するためにkuromoya_jに０～７まで代入
        moya(elli_X[kuromoya_j], elli_Y[kuromoya_j])#靄関数を８回描画（ランダムな位置に）
        
        
def moya(x, y):
    for i in range(50):                              #５０回繰り返す
        for j in range(50):                          #５０回繰り返す
            fill(0, 0.3)#薄く設定
            ellipse(x + moya_dx[i], y + moya_dy[i], kuromoya_r[i], kuromoya_r[i])#円を一か所に大量に描画
            

def amanogawa(x, y):
    for i in range(20):                              #２０回繰り返す
        for k in range(80):                          #８０回繰り返す　20*80回
            amamoya_r = random(0, 15)                #アマモヤ関数を０から１５で作る
            fill(255, 1)                             #色を薄い白色を作る
            ellipse(ama_x[k]+ x, ama_y[k] + y, amamoya_r, amamoya_r)#靄を作る
            fill (220, 220, 255, 255)                #色をあかるく決める
            ellipse(ama_x[k] + x, ama_y[k] + y, 0.7, 0.7)#大量の天の川の星を描画
def amanogawa2(x, y):
    for i in range(20):                              #２０回繰り返す
        for k in range(80):                          #８０回繰り返す　20*80回
            amamoya_r = random(0, 15)                #アマモヤ関数を０から１５で作る
            fill(100, 100, 255, 1)                   #色を薄く作る（青メイン）
            ellipse(ama_x2[k]+ x, ama_y2[k] + y, amamoya_r, amamoya_r)#靄を作る
            fill (200,200, 255, 255)                 #青中心の色を作る
            ellipse(ama_x2[k] + x, ama_y2[k] + y, 0.5, 0.5)#天の川の青っぽい星を描画
            
            
def hosibosi(x, y):
    for hosi in range(2500):                         #星を２５００個描画する
        fill(random(50, 255),random(100, 255), random(180, 255))#色を明るく変わるように設定
        ellipse(hosi1[hosi], hosi2[hosi]+y, 1, 1)    #星を描画
def big_hosi(x, y):
    for big_h in range(200):                         #でかめの星を２００個描画
        fill(random(80, 150),random(150, 230), random(180, 255))#色を明るく変わるように設定
        ellipse(bighosi[big_h], bighosi2[big_h]+y, random(2,3), random(2,3))#星を描画
def iwa_hosi(x, y):
    for i in range(13):                              #星座を描画
        fill(iwa_c1[i], iwa_c2[i], iwa_c3[i])        #最初に決めた色に設定
        if i == 0:
            ellipse( 150, 70+y, random(3, 4),random(3, 4))#少し大きめに描画
            fill(iwa_c1[i], iwa_c2[i], iwa_c3[i], random(4, 3))#薄く色を設定
            ellipse( 150, 70+y, random(25, 30), random(25, 30))#光を描画
            fill(iwa_c1[i], iwa_c2[i], iwa_c3[i], random(5, 3))#薄く色を設定
            ellipse( 150, 70+y, random(25, 30), random(15, 20))#光を描画
            fill(iwa_c1[i], iwa_c2[i], iwa_c3[i], random(5, 3))#色を薄く設定
            ellipse( 150, 70+y, random(25, 30), random(5, 10))#光を描画
        elif i == 1:#
            ellipse( 70, 120+y, random(2, 3),random(2, 3))#星座の星を描画
        elif i == 2:#
            ellipse( 120, 100+y, random(3, 4),random(3, 4))#星座の星を描画
        elif i == 3:#
            ellipse( 105, 180+y, random(3, 4),random(3, 4))#星座の星を描画
        elif i == 4:#
            ellipse( 210, 180+y, random(3, 4),random(3, 4))#星座の星を描画
            fill(iwa_c1[i], iwa_c2[i], iwa_c3[i], random(5, 3))#光を描画
            ellipse( 210, 180+y, random(25, 30), random(25, 30))#光を描画
            fill(iwa_c1[i], iwa_c2[i], iwa_c3[i], random(5, 3))#光を描画
            ellipse( 210, 180+y, random(25, 30), random(15, 20))#光を描画
            fill(iwa_c1[i], iwa_c2[i], iwa_c3[i], random(5, 3))#光を描画
            ellipse( 210, 180+y, random(25, 30), random(5, 10))#光を描画
        elif i == 5:                                       #星座の星を描画
            ellipse( 205, 200+y, random(2, 3),random(2, 4))#星座の星を描画
        elif i == 6:                                       #星座の星を描画
            ellipse( 277, 195+y, random(3, 4),random(3, 4))#星座の星を描画
        elif i == 7:                                       #星座の星を描画
            ellipse( 230, 280+y, random(3, 5),random(3, 5))#星座の星を描画
        elif i == 8:                                       #星座の星を描画
            ellipse( 400, 320+y, random(3, 4),random(3, 4))#星座の星を描画
        elif i == 9:                                       #星座の星を描画
            ellipse( 390, 355+y, random(3, 4),random(3, 4))#星座の星を描画
        elif i == 10:                                      #星座の星を描画
            ellipse( 460, 325+y, random(3, 4),random(3, 4))#星座の星を描画
        elif i == 11:                                      #星座の星を描画
            ellipse( 450, 370+y, random(3, 4),random(3, 4))#星座の星を描画
        elif i == 12:                                      #星座の星を描画
            ellipse( 410, 440+y, random(3, 4),random(3, 4))#光を描画
            fill(iwa_c1[i], iwa_c2[i], iwa_c3[i], random(5, 3))#光を描画
            ellipse( 410, 440+y, random(25, 30), random(25, 30))#光を描画
            fill(iwa_c1[i], iwa_c2[i], iwa_c3[i], random(5, 3))#光を描画
            ellipse( 410, 440+y, random(25, 30), random(15, 20))#光を描画
            fill(iwa_c1[i], iwa_c2[i], iwa_c3[i], random(5, 3))#光を描画
            ellipse( 410, 440+y, random(25, 30), random(5, 10))#光を描画


def mountain(x, y):                                            #山を表示する関数
    smooth(100)
    t1_u = (130, 530, 720)                                     #山の座標
    t2_u = (490, 460, 510)                                     #山の座標
    t3_u = (-100, 350, 550)                                    #山の座標
    t4_u = (600, 600, 600)                                     #山の座標
    t5_u = (400, 700, 880)                                     #山の座標
    t6_u = (600, 600, 600)                                     #山の座標
    t1_m = (60, 370, 610, 780)                                 #山の座標
    t2_m = (465, 525, 500, 450)                                #山の座標
    t3_m = (-100, 225, 500, 670)                               #山の座標
    t4_m = (600, 600, 600, 600)                                #山の座標
    t5_m = (225, 580, 800, 1200)                               #山の座標
    t6_m = (600, 600, 600, 600)                                #山の座標
    
    
    for i in range(3):                                         #山の位置によって色が変わるようにする
        fill(15, 25, 50)                                       #山の位置によって色が変わるようにする
        triangle(t1_u[i], t2_u[i], t3_u[i], t4_u[i], t5_u[i], t6_u[i])#山の位置によって色が変わるようにする
    for j in range(4):                                         #山の位置によって色が変わるようにする
        if j == 0 or j == 3:                                   #山の位置によって色が変わるようにする
            fill(15, 15, 30)                                   #山の位置によって色が変わるようにする
        else:
            fill(5, 23, 33)                                    #山の位置によって色が変わるようにする
        triangle(t1_m[j], t2_m[j], t3_m[j], t4_m[j], t5_m[j], t6_m[j])#山の位置によって色が変わるようにする
    
    for k in range(200):
        fill(random(0, 10), random(0, 7))                      #山の位置によって色が変わるようにする
        ellipse(random(0, 800), random(580, 600), random(50, 70), random(50, 70))#山の位置によって色が変わるようにする
        
def kusa(x, y):
    global kusa_x                                                    #草を表示するうえで使う関数をグローバル定数とする。
    k1 = (10+kusa_x, 40+kusa_x, 75+kusa_x, 90+kusa_x, 125+kusa_x, 140+kusa_x, 200+kusa_x, 150+kusa_x, 210+kusa_x, 260+kusa_x, 280+kusa_x, 350+kusa_x)#草の先端が動くようにする
    k2 = (500, 515, 500, 480, 550, 500, 540, 550, 560, 520, 540, 545)#草を描画する
    k3 = (0, 40, 25, 60, 80, 135, 150, 180, 200, 250, 300, 330)      #草を描画する
    k4 = (600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600)#草を描画する
    k5 = (25, 65, 50, 80, 115, 145, 170, 200, 220, 235, 315, 350)    #草を描画する
    k6 = (600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600)#草を描画する
    

    
    for i in range(12):
        fill(random(1,4),random(30, 35), random(1, 4))          #色を少し動く緑色に設定
        triangle(k1[i], k2[i], k3[i], k4[i], k5[i], k6[i])      #草を描画する
        
def ura_kusa(x, y):
    global ura_kusa_x#
    k1 = (-3+ura_kusa_x, 15+ura_kusa_x, 80+ura_kusa_x, 72+ura_kusa_x, 110+ura_kusa_x, 139+ura_kusa_x, 185+ura_kusa_x, 167+ura_kusa_x, 218+ura_kusa_x, 274+ura_kusa_x, 277+ura_kusa_x, 340+ura_kusa_x)#動くようにｘを関数に与えておいて設定
    k2 = (495, 500, 489, 500, 530, 490, 530, 540, 549, 519, 535, 540)#草を描画する
    k3 = (5, 37, 29, 69, 100, 139, 159, 183, 210, 290, 310, 342)     #草を描画する
    k4 = (600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600)#草を描画する
    k5 = (18, 58, 47, 83, 121, 143, 179, 203, 219, 280, 321, 331)    #草を描画する
    k6 = (600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600, 600)#草を描画する
    

    
    for i in range(12):
        fill(random(3, 5), random(23, 26), random(3, 5))             #少しくらい緑色を設定
        triangle(k1[i], k2[i], k3[i], k4[i], k5[i], k6[i])           #草を描画する
        
def nagarebosi(x, y):                                                #流れ星を表示する関数を設定
    noStroke()                                                       #枠を消す
    fill(255)                                                        #色を城に設定
    for i in range(20):                                              #２０回繰り返す
        ellipse(x+i*2, y-i*2,2-i*0.07,2-i*0.07)                      #少しづつ小さくなる円を描画
