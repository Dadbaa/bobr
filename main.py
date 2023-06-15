from flask import Flask, render_template, request, make_response, flash, redirect

app = Flask(__name__)


@app.route("/")
def index():
    strng = request.cookies.get('strng')
    if strng is None:
        user = "Бобёр"
    else:
        user = strng
    resp = make_response(render_template('index.html', name=user))

    return resp


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/contact")
def contact():
  return '''
        <nav>
    <a href="/">ГЛАВНАЯ</a>
    <a href="/about">Хатка бобра</a>
    <a href="/contact">О бобрах</a>
    </nav>
    <body>
      <h1>БОБРЫ!</h1>
      <img src="/static/1.jpg">
      
      <img src="/static/6.jpg">
      <h3>Бобры предпочитают селиться по берегам медленно текущих речек, стариц, прудов и озёр, водохранилищ, ирригационных каналов и карьеров. Избегают широких и быстрых рек, а также водоёмов, промерзающих зимой до дна. Для бобров важно наличие по берегам водоёма древесно-кустарниковой растительности из мягких лиственных пород, а также обилие водной и прибрежной травянистой растительности, составляющей их рацион. Бобры превосходно плавают и ныряют. Большие лёгкие и печень обеспечивают им такие запасы воздуха и артериальной крови, что обыкновенный бобр может нырять на 4,9 минуты на глубину 4,2 метра[15]. За ночь обыкновенный бобр может проплыть до 20 километров[16]. На суше бобры довольно неуклюжи.
Живут бобры поодиночке или семьями. Полная семья состоит из 5—8 особей: семейной пары и молодых бобров — приплода прошлого и текущего годов. Семейный участок иногда занимается семьёй в течение многих поколений. Небольшой водоём занимает одна семья или холостой бобр. На более крупных водоёмах длина семейного участка вдоль берега составляет от 0,3 до 2,9 км. От воды бобры редко удаляются более чем на 200 м. Протяжённость участка зависит от количества кормов. В богатых растительностью местах участки могут соприкасаться и даже пересекаться, в других бобры одной семьи жестоко преследуют «чужака»[17]. Границы своей территории бобры метят секретом мускусных желёз — бобровой струёй. Метки наносятся на особые холмики из грязи, ила и веток высотой 30 см и шириной до 1 м. Между собой бобры общаются с помощью пахучих меток, поз, ударов хвостом по воде и криков, напоминающих свист. При опасности плывущий бобр громко хлопает хвостом по воде и ныряет. Хлопок служит для всех бобров в пределах слышимости сигналом тревоги. Всю зиму семья бобров живёт в одной норе. Весной, с появлением зелени, бобровая семья расходится в пределах участка обитания поодиночке или группами по 2 — 3 бобра. Осенью семьи снова собираются в одном месте. 
    </body>'''


@app.route('/forma', methods=["POST", "GET"])
def forma():
    if request.method == 'POST' or request.args.get('strng'):
        strng = request.form[
            'strng'] if request.method == 'POST' else request.args.get('strng')
        user = strng
        if request.cookies.get('strng') is None:
            resp = make_response(render_template('forma.html', name=user))
            resp.set_cookie('strng', strng)
            #flash('Я тебя запомнил')
            return resp
        else:
            resp = make_response(render_template('forma.html', name=user))
            resp.set_cookie('strng', strng)
            return resp
    else:
        strng = request.cookies.get('strng')
        if strng is None:
            user = "Бобёр"
        else:
            user = strng
        resp = make_response(render_template('forma.html', name=user))
        resp.set_cookie('strng', strng)
        return resp


@app.errorhandler(404)
def page_not(error):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
