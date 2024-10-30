import numpy
import matplotlib.pyplot as plt


# расчет зависимости s(x)
def x_s_calculate(x_r, x_l, t, mu_1, mu_2, m, u):
    x = numpy.array([x_l + i * (x_r - x_l) / 99 for i in range(99)])    # разбиение отрезка [x_l;x_r) на 99
                                                                        # равноудаленных точек
    mu_0 = mu_2 / mu_1                                                  # отношение вязкости жидкости 2 к жидкости 1
    s = ((mu_0 * u * t / ((x_r - x) * m)) ** 0.5 - mu_0) / (1 - mu_0)   # вычисление насыщенности жидкости 2

    # вычисление насыщенности жидкости 2 на заданном отрезке, если вязкость жидкости 2 больше
    if mu_0 > 1:
        s = -s

    # исправление не физичных значений насыщенности жидкостью 2
    for i in range(99):
        if s[i] > 1:
            s[i] = 1
        if s[i] < 0:
            s[i] = 0

    # добавление правой точки интервала с насыщенностью 1
    x = numpy.append(x, x_r)
    s = numpy.append(s, 1)

    # отрисовка графика
    draw_graph(x, s)

    # сохранение s(x) в dependence_s_x.txt
    save_txt(x, s)


# отрисовка графика
def draw_graph(x, s):
    fig, ax1 = plt.subplots(1, 1)                   # создание осей
    ax1.plot(x, s)                                  # ввод зависимости s(x)
    ax1.grid()                                      # создание сетки на графике
    ax1.set_ylabel('$Водонасыщенность, д.ед.$')     # подпись оси y
    ax1.set_xlabel('Координата, м')                 # подпись оси x
    ax1.set_xlim(int(min(x) - 1), int(max(x) + 1))  # задание интервала отрисовки оси x
    ax1.set_ylim(0, 1.1)                            # задание интервала отрисовки оси y
    plt.savefig('graph.png')                        # сохранение графика как файла graph.png


# вывод пар значений x, s в txt файл
def save_txt(x, s):
    x_s = numpy.column_stack([x, s])                   # попарное объединение x, s
    numpy.savetxt('dependence_s_x', x_s, fmt='%.10f')  # сохранение s(x) в dependence_s_x.txt (числа формата десятичной дроби с плавающей запятой)
