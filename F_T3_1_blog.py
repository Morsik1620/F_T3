from flask import Flask, render_template, request
app = Flask(__name__) # с помощью этой переменной фреймворк определяет пути к корневому каталогу
menu = ["Домашняя страница", "Дневник программиста"]
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        zz = request.form.get("zz")
        tz = request.form.get("tz")
        if zz and tz:
            data.append({"zz": zz, "tz": tz})
    return render_template('first_page.html', data=data, menu = menu)

data = []  # Список для хранения введенных данных

@app.route("/pd", methods=["GET", "POST"])
def pd():
    if request.method == "POST":
        zz = request.form.get("zz")
        tz = request.form.get("tz")
        if zz and tz:
            data.append({"zz": zz, "tz": tz})
    return render_template("notes.html", data=data, menu = menu)








#per = {'tz':'taz', 'zz': 'ZagZag'}
#tm = Template('{{p.tz()}} {{p.zz()}}')
#msg = tm.render(p = per)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__': #
    app.run(debug=True)