# Импортируем модули
import customtkinter as ctk
from Generator import generate_password
# Создаем нужные функции и переменные
number_of_symbs = 18
def display_password(number_of_symbs:int|str = 12) -> None:
    """
    Функция для выведения пароля на экран.
    """
    # Очищаем поле вывода
    text_output.delete(0, "end")
    # Создаем пароль
    password = generate_password(number_of_symbs)
    # Выводим пароль на экран
    text_output.insert(0, password)
# Создание итерфейса
# Темная тема
ctk.set_appearance_mode("dark")
# root - с англ. корень (здесь: корневое (главное) окно)
root = ctk.CTk()
# Имя окна
root.title("Password Generator")
# Запрет на изменение размеров окна
root.resizable(0, 0)
# Виджеты
# поле для вывода пароля
text_output = ctk.CTkEntry(root, placeholder_text = "PASSWORD", justify  = "center" , width = 140, height = 28, corner_radius = 9, border_color="cyan", text_color = "green", font = ("Gabriola", 15))
# Размещаем виджет на сетке
text_output.grid(row = 0, column = 0, padx = 40, pady = 3)
# Кнопка
button = ctk.CTkButton(root, corner_radius = 9, fg_color = "turquoise", hover_color = "lightblue", text = ("PRESS TO GENERATE PASSWORD"), font = ("Gabriola", 15), hover = True, command = lambda: display_password(number_of_symbs), text_color = "black")
button.grid(row = 1, column = 0, pady = 10)
# Запуск основного цикла
root.mainloop()