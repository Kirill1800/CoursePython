import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from InstaBot.Module1_urls import main


# Функция которая вызывается по нажатию кнопки
def start_module_1():
    label.configure(text="Модуля 1 начал работать")
    window.update()
    main()
    label.configure(text="Модуль 1 завершен!")
    window.update()


window = Tk()  # Инициализация интерфейса
window.geometry('600x250')  # Создание окна по размерам в пикселях

# Создаем элементы (Надписи, Кнопки, Поля для ввода)
label = Label(window, text="", font=("Arial Bold", 30))
button = Button(window, text="MODULE 1", command=start_module_1)
entry = Entry(window, width=10)
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)  # установите вариант по умолчанию

# Размещаем в нашем окне элементы на основе сетки
label.grid(column=0, row=0)
button.grid(column=0, row=1)
# entry.grid(column=1, row=0)
# combo.grid(column=3, row=0)
# Запуск то что создали в window
window.mainloop()
