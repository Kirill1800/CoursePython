from flask import Flask, render_template

app = Flask(__name__)


#  1 страница сайта (доступ по /)
@app.route('/')
def root():
    return 'Текст корня для сайта'


@app.route('/main')
def main():
    return render_template('main.html')


#  2 страница ()
@app.route('/login')
def login():
    #  От
    x = 15 + 3
    #  До
    return render_template("login.html", NAME="Кирилл", NUM=x)


#  Запуск
if __name__ == '__main__':
    app.run()
