from flask import Flask, render_template, url_for
import pymongo

string = "mongodb+srv://root:root@cluster0.sygbz.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = pymongo.MongoClient(string)
collection = client["MyDataBase"]["Test2"]
finish = collection.find()[0]

app = Flask(__name__)


@app.route('/')
def index():
    title = "Мое резюме"
    return render_template("index.html", TITLE=title, SKILL=skill_development(),
                           SKILL_TITLE=skill_development(mode="Title"), SOFT=new_skills(),
                           SOFTWARE=new_skills(mode="Title"), EXPERIENCE=experience(),
                           WORK_EXPERIENCE=experience(mode="Title"), INFORM=information(),
                           INFORMATION=information(mode="Title"))


def skill_development(mode=None):
    if not mode:
        result = ["HTML5/CSS", "JavaScript &amp; jQuery", "PHP Backend", "SQL Databases", "Wordpress", "Pligg CMS",
                  "Some Objective-C"]
    elif mode == "Title":
        result = "Развитие"
    else:
        result = "Ошибка"
    return result


def new_skills(mode=None):
    if not mode:
        result = ["Adobe Photoshop", "Adobe Dreamweaver", "MS Office 2007-2010", "cPanel &amp;phpMyAdmin", "Xcode 4"]
    elif mode == "Title":
        result = "Программное обеспечение"
    else:
        result = "Ошибка"
    return result


def experience(mode=None):
    if not mode:
        result = ["Freelance Web Designer/Developer ~ 2007-2009", "Best Buy - Geek Squad In-Store Agent ~ 2008-2009",
                  "Freelance Writer for Hongkiat.com ~ 2011-Present"]
    elif mode == "Title":
        result = "Опыт работы"
    else:
        result = "Ошибка"
    return result


def information(mode=None):
    if not mode:
        result = collection
    elif mode == "Title":
        result = "Немного обо мне"
    else:
        result = "Ошибка"
    return result


# Запуск
if __name__ == '__main__':
    app.run()
