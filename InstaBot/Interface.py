from selenium import webdriver
from tkinter import *
from tkinter.ttk import *
from InstaBot.Module1_urls import module1
from InstaBot.Module2_sort import module2
from InstaBot.Module3_like import module3
from InstaBot.Module4_del import module4
from InstaBot.Module5_celeba import module5
from InstaBot.path import path_sort, path_users, path_subscriptions, path_web_driver
from InstaBot.functions import open_file_to_list, text_to_list, login_inst


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
    label.configure(text="Модуль 5 начал работать")
    window.update()
    module5()
    label.configure(text="Модуль 5 завершен!")
    window.update()


def button_login():
    browser = webdriver.Chrome(path_web_driver)
    login_inst(browser=browser)


window = Tk()  # Инициализация интерфейса
window.geometry('780x400')  # Создание окна по размерам в пикселях

# Создаем элементы (Надписи, Кнопки, Поля для ввода)
label = Label(window, text="", font=("Arial Bold", 30))
button1 = Button(window, text="Обновить модуль 1", command=button_1_module_1)
button2 = Button(window, text="Показать модуль 1", command=button_2_module_1)
button3 = Button(window, text="Обновить модуль 2", command=button_3_module_2)
button4 = Button(window, text="Показать модуль 2", command=button_4_module_2)
button5 = Button(window, text="Обновить модуль 3", command=button_5_module_3)
button6 = Button(window, text="Отписаться", command=button_6_module_4)
button7 = Button(window, text="Запустить модуль 5", command=button_7_module_5)
button_login = Button(window, text="Вход в аккаунт", command=button_login)

entry = Entry(window, width=10)
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)  # установите вариант по умолчанию
text = Text(width=50, heigh=10, wrap=WORD)

# Размещаем в нашем окне элементы на основе сетки (grid, pack, place)
label.grid(column=0, row=0, columnspan=5, sticky=W + E)  # слева_на_право
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)
button4.grid(column=3, row=1)
button5.grid(column=4, row=1)
button6.grid(column=0, row=2)
button7.grid(column=1, row=2)
button_login.grid(column=2, row=2)
text.grid(column=1, row=3, columnspan=5, sticky=W + E)

# entry.grid(column=1, row=0)
# combo.grid(column=3, row=0)
# Запуск то что создали в window
window.mainloop()
