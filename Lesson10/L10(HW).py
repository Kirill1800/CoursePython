from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def base():
    text = ""
    for i in range(5):
        text += str(i)
    text = "Мое резюме"

    body = '''<div class="_2r__xiKDurulGZmkq4_dl"><ul>
<li>
<p><a rel="nofollow noopener noreferrer" href="http://www.thefreedictionary.com/" target="_blank">The Free Dictionary</a> – словарь + идиомы, форум, игры, а если зарегистрироваться, то будут начисляться очки за прочтение статей и другие активности.</p>
</li>
<li>
<p class="adme-img-description"><a rel="nofollow noopener noreferrer" href="http://www.real-english.com/" target="_blank">Real English</a> – сайт, на котором можно услышать настоящий разговорный английский. Записаны диалоги&nbsp;с реальными людьми на улице на различные темы.</p>
</li>
<li>
<p class="adme-img-description"><a rel="nofollow noopener noreferrer" href="http://learnit90.ru/" target="_blank">Learn It</a> – учите английский самостоятельно в группе единомышленников. 3-месячный марафон, задания каждые 3 дня, уровень — любой.</p>
</li>
<li>
<p class="adme-img-description"><a rel="nofollow noopener noreferrer" href="http://www.esolcourses.com/topics/learn-english-with-songs.html" target="_blank">Esolcourses</a> - учим английский по песням -&nbsp;слушаем, читаем субтитры, делаем задания к музыкальным композициям.</p>
</li>
<li>
<p class="adme-img-description"><a rel="nofollow noopener noreferrer" href="http://readlang.com/" target="_blank">Readlang</a> - лучший сайт для чтения: загружаете текст или выбираете из библиотеки, нажимаете на непонятное слово или словосочетание и сразу видите&nbsp;перевод, переносите на карточки.</p>
</li>
<li>
<p class="adme-img-description"><a rel="nofollow noopener noreferrer" href="https://vk.com/stopthepress" target="_blank">Stop the Press</a> - группа Вконтакте, где какой-то прекрасный человек ежедневно выкладывает новые pdf свежих журналов.</p>
<h3 class="adme-img-description" style="text-align: center;">
<br>
Сайты Британского совета</h3>
</li>
<li>
<p><a rel="nofollow noopener noreferrer" href="http://learnenglishkids.britishcouncil.org/en/" target="_blank">Для детей</a></p>
</li>
<li>
<p class="adme-img-description"><a rel="nofollow noopener noreferrer" href="http://learnenglishteens.britishcouncil.org/" target="_blank">Для подростков</a></p>
</li>
<li>
<p class="adme-img-description"><a rel="nofollow noopener noreferrer" href="http://learnenglish.britishcouncil.org/en/" target="_blank">Для взрослых</a></p>
</li>
</ul>
</div>'''

    return render_template("base.html", TITLE=text, BODY=body)


# @app.route('/home')
# def index():
#     return render_template("index.html")
#
#
# @app.route('/about')
# def about():
#     return render_template("about.html")
#
#
# @app.route('/user<string:name>/<int:id>')
# def user(name, id):
#     return "User page: " + name + "-" + str(id)


# Запуск
if __name__ == '__main__':
    app.run()
