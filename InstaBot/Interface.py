from selenium import webdriver
from tkinter import *
from tkinter.ttk import *
from InstaBot.Module1_urls import module1
from InstaBot.Module2_sort import module2
from InstaBot.Module3_like import module3
from InstaBot.Module4_del import module4
from InstaBot.Module5_celeba import module5, module6
from InstaBot.path import path_sort, path_users, path_subscriptions, path_web_driver
from InstaBot.functions import open_file_to_list, text_to_list, login_inst
from threading import Thread


# Функция которая вызывается по нажатию кнопки
def button_1_module_1():
    label.configure(text="Модуль 1 начал работать")
    window.update()
    module1()
    mas_txt = open_file_to_list(path_users)
    txt = text_to_list(lst=mas_txt, count=10)
    text.insert(1.0, txt)
    label.configure(text="Модуль 1 завершен!\n(Колличество записей: {})".format(len(mas_txt)))
    window.update()


# Функция которая вызывается по нажатию кнопки
def button_2_module_1():
    mas_txt = open_file_to_list(path_users)
    txt = text_to_list(lst=mas_txt, count=10)
    text.delete(1.0, END)
    text.insert(1.0, txt)


def button_3_module_2():
    label.configure(text="Модуль 2 начал работать")
    window.update()
    module2()
    mas_txt = open_file_to_list(path_sort)
    txt = text_to_list(lst=mas_txt, count=10)
    text.insert(1.0, txt)
    label.configure(text="Модуль 2 завершен!\n(Колличество записей: {})".format(len(mas_txt)))
    window.update()


def button_4_module_2():
    mas_txt = open_file_to_list(path_sort)
    txt = text_to_list(lst=mas_txt, count=10)
    text.delete(1.0, END)
    text.insert(1.0, txt)


def button_5_module_3():
    label.configure(text="Модуль 3 начал работать")
    window.update()
    module3()
    mas_txt = open_file_to_list(path_subscriptions)
    txt = text_to_list(lst=mas_txt, count=10)
    text.insert(1.0, txt)
    label.configure(text="Модуль 3 завершен!\n(Колличество записей: {})".format(len(mas_txt)))
    window.update()


def button_6_module_4():
    label.configure(text="Модуль 4 начал работать")
    window.update()
    module4()
    label.configure(text="Модуль 4 завершен!")
    window.update()


def button_7_module_5():
    label.configure(text="Подписка запустилась (процессом)")
    window.update()
    # module5()
    Thread(target=module5).start()


def button_8_module_6():
    label.configure(text="Накрутка запустилась (процессом)")
    window.update()
    Thread(target=module6).start()


def button_login():
    browser = webdriver.Chrome(path_web_driver)
    login_inst(browser=browser)


window = Tk()  # Инициализация интерфейса
window.geometry('840x400')  # Создание окна по размерам в пикселях

# Создаем элементы (Надписи, Кнопки, Поля для ввода)
label = Label(window, text="", font=("Arial Bold", 30))
button1 = Button(window, text="Обновить модуль 1", command=button_1_module_1, width=15)
button2 = Button(window, text="Показать модуль 1", command=button_2_module_1, width=15)
button3 = Button(window, text="Обновить модуль 2", command=button_3_module_2, width=15)
button4 = Button(window, text="Показать модуль 2", command=button_4_module_2, width=15)
button5 = Button(window, text="Обновить модуль 3", command=button_5_module_3, width=15)
button6 = Button(window, text="Отписаться", command=button_6_module_4, width=15)
button7 = Button(window, text="Селеба", command=button_7_module_5, width=15)
button8 = Button(window, text="Накрутка", command=button_7_module_5, width=15)
button_login = Button(window, text="Вход в аккаунт", command=button_login, width=15)

entry = Entry(window, width=10)
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)  # установите вариант по умолчанию
text = Text(width=50, heigh=10, wrap=WORD)

# Размещаем в нашем окне элементы на основе сетки (grid, pack, place)
label.grid(column=0, row=0, columnspan=5, sticky=W + E)  # слева_на_право
button_login.grid(column=0, row=1)

button1.grid(column=0, row=2)
button2.grid(column=1, row=2)
button3.grid(column=2, row=2)
button4.grid(column=3, row=2)
button5.grid(column=4, row=2)
button6.grid(column=0, row=3)
button7.grid(column=0, row=4)
button8.grid(column=1, row=4)
text.grid(column=1, row=5, columnspan=5, sticky=W + E)

# entry.grid(column=1, row=0)
# combo.grid(column=3, row=0)
# Запуск то что создали в window
window.mainloop()
