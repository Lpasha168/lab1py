import os
data = []
with open('csv_20260206_08a514.txt', 'r') as x:
    for line in x:
        data.append(line)
info = []
datawt = []
datawt = data

for x in range(len(datawt)):
    print(x+1)
    prover = []
    fs = datawt[x].split(',')
    for x in fs:
        if x.isdigit() or (x.startswith('-') and x[1:].isdigit()):
            prover.append('0')
            print('digit')
        elif '.' in x:
            prover.append('1')
            print('float')
        else:
            prover.append('2')
            print('string')
    info.append(prover)
for x in range(len(info)):
    print(info[x])
itog = [int(x) for x in info[0]]
if sum(itog) == 10:
    print('head')





try:
    cy = int(input("Введите текущий год: "))
    by = int(input("Введите год рождения: "))

    assert by <= cy, "Год рождения не может быть больше текущего года!"

    age = cy - by

    assert age >= 0, "Возраст не может быть отрицательным!"
    assert age <= 120, "Возраст не может быть больше 120 лет!"

    print(f"Ваш возраст: {age} лет")

except ValueError:
    print("Ошибка: Введите числовое значение!")

except AssertionError as e:
    print(f"Ошибка: {e}")

except Exception:
    print("Произошла непредвиденная ошибка.")


try:
    user_input = input("Введите сумму: ")
    amount = int(user_input)
    
    assert amount > 0, "Сумма должна быть положительной!"
    assert amount % 100 == 0, "Сумма должна быть кратна 100!"
    
    print(f"Выдано {amount} руб.")

except ValueError:
    print("Ошибка: Введите числовое значение!")

except AssertionError as e:
    print(f"Ошибка: {e}")












