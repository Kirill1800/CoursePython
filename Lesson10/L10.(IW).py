from flask import Flask, render_template
from time import sleep

app = Flask(__name__)


# 0 страница сайта (доступ по /)
@app.route('/')
def root():
    return "Текс для коряня сайта"


# 1 страница сайта (доступ по /)
@app.route('/main')
def main():

    lst = []
    for i in range(5):
        lst.append("Строка №" + str(i))

    return render_template("main.html", MAS=lst)


# 2 страница сайта (доступ по /hello)
@app.route('/login')
def login():
    # От (наш бэкэнд код)
    x = 15 + 3
    # До
    return render_template("login.html", NAME="Игорь", NUM=x)


# Запуск
if __name__ == '__main__':
    app.run()
