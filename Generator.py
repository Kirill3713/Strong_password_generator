# Импортируем модули
import string
import random
# Создаем переменные алфавитов
a = string.digits
b = string.ascii_lowercase
c = string.ascii_uppercase
d = string.punctuation
special_symbs = "!@'£$%^&*()_+-+/*:~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ#/?.>,<\\`¬№;><=|™§×÷}[]‰✓✕¡¿⁈⁇µ⁒€$₽₴ß↔↘↗↖⇅⇊⇈⇵▬◌▲△■■⁰³⁹ⁱ⁻⁼⁺⅓⅞⅜⅚⅔½⅘⅐₃₉₋₍₄₂₅₎₌Ⅹ∆∉∊∑√∞∘≈≤≥⑦βαθγΞλΣπρνΨΩφ·ʹιͺ!£$%^_=-}&*()_+-+/*{[]:@~#?/>.<,|\\¬`№;°^^§$ß``´´ÖÜÄ'…" + '"'
symbs = [a, b, c, d, special_symbs]
# Создаем функцию
def generate_password(len:int|str = 12) -> str:
    """
    Функция для получения пароля.
    """
    # Обрабатываем введенную длину
    try:
        len = int(len)
    except ValueError:
        print("Можно вводить только числа.")
        try:
            len = int(input("Введите длину кода еще раз, пожалуйста."))
        except ValueError:
            print("Вы опять ввели некорректное значение! Перезапустите программу!")
            return
    # Создаем пароль
    password = ""
    for _ in range(len):
        group_to_add = random.choice(symbs)
        symb_to_add = random.choice(group_to_add)

        password += symb_to_add
    # Возвращаем результат
    return password
# Проверка на то, что мы запустили файл, а не импортировали
if __name__ == "__main__":
    print(generate_password(input("Введите кол - во символов в пароле: ")))