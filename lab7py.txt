import matplotlib.pyplot as plt
import numpy as np


#данные из файла
raw_data = """x;y
1;107
2;23
3;62
4;24
5;53
6;115
7;101
8;65
9;NaN
10;99
11;62
12;68
13;135
14;65
15;104
16;61
17;83
18;99
19;157
20;140
21;99
22;99
23;151
24;130
25;115
26;131
27;99
28;150
29;163
30;165
31;161
32;168
33;130
34;194
35;177
36;208
37;201
38;154
39;NaN
40;120"""


x_all = []
y_all = []

for line in raw_data.strip().split("\n")[1:]:
    x_str, y_str = line.split(";")
    x_all.append(int(x_str))
    if y_str == "NaN":
        y_all.append(None)
    else:
        y_all.append(float(y_str))

x_all = np.array(x_all)




def get_linear_value(x_target, p1, p2):
   
    #матрица системы
    A = np.array([[p1[0], 1], [p2[0], 1]])
    B = np.array([p1[1], p2[1]])
    # Решаем Ax = B, получаем [a, b]
    a, b = np.linalg.solve(A, B)
    return a * x_target + b


def get_quadratic_value(x_target, p1, p2, p3):
    
    #матрица системы
    A = np.array(
        [[p1[0] ** 2, p1[0], 1], [p2[0] ** 2, p2[0], 1], [p3[0] ** 2, p3[0], 1]]
    )
    B = np.array([p1[1], p2[1], p3[1]])
    a, b, c = np.linalg.solve(A, B)
    return a * (x_target**2) + b * x_target + c



# вычисление пропущенных 
p_x7 = (7, y_all[6])
p_x8 = (8, y_all[7])
p_x10 = (10, y_all[9])

y9_linear = get_linear_value(9, p_x8, p_x10)
y9_quad = get_quadratic_value(9, p_x7, p_x8, p_x10)

p_x37 = (37, y_all[36])
p_x38 = (38, y_all[37])
p_x40 = (40, y_all[39])

y39_linear = get_linear_value(39, p_x38, p_x40)
y39_quad = get_quadratic_value(39, p_x37, p_x38, p_x40)

print(
    f"x = 9: Линейная = {y9_linear:.2f}, Квадратичная = {y9_quad:.2f}"
)
print(
    f"x = 39: Линейная = {y39_linear:.2f}, Квадратичная = {y39_quad:.2f}"
)

y_linear_filled = [
    y if y is not None else (y9_linear if x == 9 else y39_linear)
    for x, y in zip(x_all, y_all)
]
y_quad_filled = [
    y if y is not None else (y9_quad if x == 9 else y39_quad)
    for x, y in zip(x_all, y_all)
]


#построение графиков

plt.figure(figsize=(12, 6))

#исходные известные точки
x_known = [x for x, y in zip(x_all, y_all) if y is not None]
y_known = [y for y in y_all if y is not None]
plt.scatter(
    x_known, y_known, color="black", zorder=5, label="Исходные точки"
)

#график линейной интерполяции
plt.plot(
    x_all,
    y_linear_filled,
    color="tab:blue",
    linestyle="-",
    alpha=0.7,
    label="Линейная интерполяция",
)
plt.scatter(
    [9, 39],
    [y9_linear, y39_linear],
    color="tab:blue",
    s=100,
    edgecolors="black",
    zorder=6,
    label="NaN (Линейная)",
)

#график квадратичной интерполяции
plt.plot(
    x_all,
    y_quad_filled,
    color="tab:red",
    linestyle="--",
    alpha=0.7,
    label="Квадратичная интерполяция",
)
plt.scatter(
    [9, 39],
    [y9_quad, y39_quad],
    color="tab:red",
    s=100,
    edgecolors="black",
    zorder=6,
    label="NaN (Квадратичная)",
)


plt.title("Интерполяция пропущенных значений (NaN) матричным методом")
plt.xlabel("X")
plt.ylabel("Y")
plt.xticks(x_all)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
