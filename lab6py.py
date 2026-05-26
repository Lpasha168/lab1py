import numpy as np
import matplotlib.pyplot as plt


#исходные данные
months = np.arange(1, 13)

data = {
    "month_number": months,
    "facecream": [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    "facewash": [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    "toothpaste": [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    "bathingsoap": [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    "shampoo": [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
    "moisturizer": [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    "total_units": [21100, 18330, 22470, 22270, 20960, 20140, 29550, 36140, 23400, 26670, 41280, 30020],
    "total_profit": [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200]
}


#1: простой линейный график общей прибыли
plt.figure(figsize=(8, 5))
plt.plot(data["month_number"], data["total_profit"])

plt.title("Company profit per month")
plt.xlabel("Month number")
plt.ylabel("Total profit")
plt.xticks(data["month_number"])
plt.grid(True, alpha=0.3)
plt.show()


#2: стилизованный линейный график количества проданных единиц
plt.figure(figsize=(8, 5))
plt.plot(
    data["month_number"], 
    data["total_units"], 
    label="Profit data of last year", 
    color="red", 
    linestyle="--", 
    marker="o", 
    markerfacecolor="red", 
    linewidth=3
)

plt.title("Company Sales data of last year")
plt.xlabel("Month number")
plt.ylabel("Total units")
plt.xticks(data["month_number"])
plt.legend(loc="lower right")
plt.grid(True, alpha=0.3)
plt.show()


#задание 3.1: все продукты на одном графике

plt.figure(figsize=(10, 6))
plt.plot(data["month_number"], data["facecream"], label="Face cream Sales Data", marker="o", linewidth=2)
plt.plot(data["month_number"], data["facewash"], label="Face Wash Sales Data", marker="o", linewidth=2)
plt.plot(data["month_number"], data["toothpaste"], label="ToothPaste Sales Data", marker="o", linewidth=2)
plt.plot(data["month_number"], data["bathingsoap"], label="BathingSoap Sales Data", marker="o", linewidth=2)
plt.plot(data["month_number"], data["shampoo"], label="Shampoo Sales Data", marker="o", linewidth=2)
plt.plot(data["month_number"], data["moisturizer"], label="Moisturizer Sales Data", marker="o", linewidth=2)

plt.title("Sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.xticks(data["month_number"])
plt.legend(loc="upper left")
plt.grid(True, alpha=0.3)
plt.show()


#задание 3.2: каждый продукт на отдельном графике 
products = {
    "Face cream": data["facecream"],
    "Face wash": data["facewash"],
    "Toothpaste": data["toothpaste"],
    "Bathingsoap": data["bathingsoap"],
    "Shampoo": data["shampoo"],
    "Moisturizer": data["moisturizer"]
}

for name, values in products.items():
    plt.figure(figsize=(8, 3))
    color = "black" if name == "Bathingsoap" else "red"
    plt.plot(data["month_number"], values, marker="o", color=color)
    plt.title(f"Sales data of a {name.lower()}")
    plt.xlabel("Month Number")
    plt.ylabel("Sales units in number")
    plt.xticks(data["month_number"])
    plt.grid(True, alpha=0.3)
    plt.show()


#задание 4: точечный график для зубной пасты со штриховой сеткой

plt.figure(figsize=(8, 5))
plt.scatter(data["month_number"], data["toothpaste"], label="Tooth paste Sales data", color="tab:blue")

plt.title("Tooth paste Sales data")
plt.xlabel("Month Number")
plt.ylabel("Number of units Sold")
plt.xticks(data["month_number"])
plt.grid(True, linestyle="--")
plt.legend(loc="upper left")
plt.show()

# ==============================================================================
# ЗАДАНИЕ 5: Столбчатая диаграмма (bar chart) для Face Cream и Face Wash
# ==============================================================================
plt.figure(figsize=(8, 5))
width = 0.35  # Ширина каждого столбца

# Смещаем столбцы влево и вправо от центра деления оси X
plt.bar(data["month_number"] - width/2, data["facecream"], width, label="Face Cream sales data")
plt.bar(data["month_number"] + width/2, data["facewash"], width, label="Face Wash sales data")

plt.title("Facewash and facecream sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.xticks(data["month_number"])
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper left")
plt.show()


#задание 6: Круговая диаграмма  годовых продаж всех продуктов
plt.figure(figsize=(8, 8))

#сумма продаж за год для каждого продукта
total_sales = [
    sum(data["facecream"]),
    sum(data["facewash"]),
    sum(data["toothpaste"]),
    sum(data["bathingsoap"]),
    sum(data["shampoo"]),
    sum(data["moisturizer"])
]

labels = ["FaceCream", "FaceWash", "ToothPaste", "Bathing soap", "Shampoo", "Moisturizer"]

plt.pie(total_sales, labels=labels, autopct="%1.1f%%", startangle=15)

plt.title("Sales data")
plt.legend(loc="lower right")
plt.show()
