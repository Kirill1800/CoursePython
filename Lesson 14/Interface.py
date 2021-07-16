import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

x = 0


# Функция которая вызывается по нажатию кнопки
def first_button():
    global x
    x += 1
    label.configure(text=combo.get())


window = Tk()  # Инициализация интерфейса
window.geometry('600x250')  # Создание окна по размерам в пикселях

# Создаем элементы (Надписи, Кнопки, Поля для ввода)
label = Label(window, text="Привет", font=("Arial Bold", 30))
button = Button(window, text="Не нажимать!", command=first_button)
entry = Entry(window, width=10)
combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)  # установите вариант по умолчанию

# Размещаем в нашем окне элементы на основе сетки
label.grid(column=0, row=0)
button.grid(column=2, row=0)
entry.grid(column=1, row=0)
combo.grid(column=3, row=0)
# Запуск то что создали в window
window.mainloop()
