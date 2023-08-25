from ipaddress import collapse_addresses
from matplotlib.collections import LineCollection
from re import X
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

def visualization(center, point, start, end):
    ### ОКРУЖНОСТЬ ###
    radius = np.linalg.norm(center - point) # радиус = длина вектора
    # Генерируем набор углов для построения окружности
    angles = np.linspace(0, 2 * np.pi, 50)

    # Вычисляем координаты точек окружности
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    ###################

    ### КАСАТЕЛЬНАЯ ###
    m = -(point[0] - center[0]) / (point[1] - center[1]) # Угловой коэффициент для касательной

    xTang = np.linspace(point[0] - 0.00015, point[0] + 0.00015, 50) # набор координат х для уравнения касатльной
    yTang = m * (xTang - point[0]) + point[1] # Уравнение касательной y - y1 = m(x - x1) => y = m(x - x1) + y1
    ###################
    
    ### ГОТОВИМ КООРДИНАТЫ ДЛЯ РАСЧЕТОВ ###
    endTang = ([xTang[len(xTang)-1], yTang[len(yTang)-1]]) # координаты конца касательной


    a = - ((point[1] * (end[0] - point[0]) / (math.sqrt(point[0]**2 + point[1]**2)))) # первая часть числителя
    b = (point[0] * (end[1] - point[1])) / ( math.sqrt(point[0]**2 + point[1]**2)) # вторая часть числителя
    c = math.sqrt((end[0] - point[0])**2 + (end[1] - point[1])**2) # знаменатель
    cos = (a + b)/c # косинус дельта
    cos4a = (8 * cos**4) - (8 * cos**2) + 1 

    cosToEdge = math.acos(cos) # извлекаем угол
    radToDegree = math.degrees(cosToEdge) # из радиан в градусы
    #######################################

    return cos4a

    # Создаем график и отображаем точку и окружность
    # fig, ax = plt.subplots()
    # ax.plot(x, y,)
    # ax.plot(point[0], point[1], 'ro')
    # ax.plot(center[0], center[1], 'bo')
    # ax.plot(start[0], start[1], 'bo')
    # ax.plot(end[0], end[1], 'yo')
    # ax.plot(start[0], start[1], color='yellow')
    # ax.plot(xTang, yTang, 'red')
    # ax.plot([point[0], end[0]], [point[1], end[1]], 'b') # соединение центра и конца
    # ax.plot([start[0], point[0]], [start[1], point[1]], 'b') # соединение центра и конца
    # ax.set_aspect('equal')
    # ax.legend()

    # plt.axis([0.704, 0.710, -0.0015, 0.0020]) # для увеличение масштаба графика
    
    # plt.show()

def all(x_start, y_start, x_middle, y_middle, x_end, y_end):
    fig, ax = plt.subplots(figsize=(8, 6))

    # Создание палочек
    lines = [((x_s, y_s), (x_m, y_m), (x_e, y_e)) for x_s, y_s, x_m, y_m, x_e, y_e in zip(x_start, y_start, x_middle, y_middle, x_end, y_end)]
    line_collection = LineCollection(lines, linewidths=2, colors='green')
    ax.add_collection(line_collection)

    # Настройка графика
    ax.autoscale()
    ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Визуализация палочек')

    # Отображение графика
    plt.grid(True)
    plt.show()

# считываем файл с координатами
f = open('C:\\Users\\l.khusainova\\Desktop\\частицы_методы\\анизатропия\\Adv100\\Data\\130000.txt')
arr = []

x_start = []
y_start = []
x_middle = []
y_middle = []
x_end = []
y_end = []

S4 = 0 # параметр тетратического порядка
for line in f:
    l = line.split('\t')
    
    # формируем вектор конца палочки
    x1, y1 = float(l[0]), float(l[1]) # начало палочки
    x2, y2 = float(l[2]), float(l[3]) # середина палочки
    x3, y3 = float(l[4]), float(l[5]) # конец палочки

    center = ([x2, y2])
    start = ([x1, y1])
    end = ([x3, y3])

    arr.append(visualization(np.array([0, 0]), center, start, end))

    # формируем массивы для визуализации палочек
    x_start.append(l[0])
    y_start.append(l[1])
    x_middle.append(l[2])
    y_middle.append(l[3])
    x_end.append(l[4])
    y_end.append(l[5])


S4 = round(mean(arr), 4) # параметр тетратического порядка ()

print("Параметр тетратического порядка: ", S4)
# visualization(np.array([0, 0]), center, start, end)

all(x_start, y_start, x_middle, y_middle, x_end, y_end)


    

    