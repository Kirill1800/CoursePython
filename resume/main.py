from flask import Flask, render_template
import pymongo
import ssl

# collection = client["MyDataBase"]["Test2"]
# finish = collection.find()[0]

app = Flask(__name__)

# Подключение к нашей БД
string = "mongodb+srv://root:root@cluster0.sygbz.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = pymongo.MongoClient(string, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)


# Основной код
@app.route('/')
def index():
    # Формирование главной HTML нашего резюме
    title = "Мое резюме"
    return render_template("index.html", TITLE=title, SKILL=skill_development(),
                           SKILL_TITLE=skill_development(mode="Title"), SOFT=new_skills(),
                           SOFTWARE=new_skills(mode="Title"), EXPERIENCE=experience(),
                           WORK_EXPERIENCE=experience(mode="Title"), INFORM=information(),
                           INFORMATION=information(mode="Title"))


def skill_development(mode=None):
    if not mode:
        result = client["MyDataBase"]["Information"].find({"Name": "Развитие-тело"})[0]["result"]
    elif mode == "Title":
        result = client["MyDataBase"]["Information"].find({"Name": "Развитие-заголовок"})[0]["result"]
    else:
        result = "Ошибка"
    return result


def new_skills(mode=None):
    if not mode:
        result = client["MyDataBase"]["Information"].find({"Name": "Скиллы-тело"})[0]["result"]
    elif mode == "Title":
        result = client["MyDataBase"]["Information"].find({"Name": "Скиллы-заголовок"})[0]["result"]
    else:
        result = "Ошибка"
    return result


def experience(mode=None):
    if not mode:
        result = client["MyDataBase"]["Information"].find({"Name": "Опыт-Тело"})[0]["result"]
    elif mode == "Title":
        result = client["MyDataBase"]["Information"].find({"Name": "Опыт-Заголовок"})[0]["result"]
    else:
        result = "Ошибка"
    return result


def information(mode=None):
    if not mode:
        result = client["MyDataBase"]["Information"].find({"Name": "Информация-Тело"})[0]["result"]
    elif mode == "Title":
        result = client["MyDataBase"]["Information"].find({"Name": "Информация-Заголовок"})[0]["result"]
    else:
        result = "Ошибка"
    return result


# Запуск
if __name__ == '__main__':
    app.run()

# База данных (включает в себя КОЛЛЕКЦИИ)
# Коллекции (включают в себя СТРОКИ)
