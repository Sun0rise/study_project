from Main_window_design2 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QEvent, QObject, QCoreApplication
from Calculations import x_s_calculate


class Ui_MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi(self)
        self.pushButton_calc.clicked.connect(self.calculate)  # Событие нажатия на кнопку "Расчитать"
        self.show()

# функция для расчета и вывода графика S(x)
    def calculate(self):
        x_l = float(self.lineEdit_x_left.text())           # левая граница пласта (вытеснение жидкости)
        x_r = float(self.lineEdit_x_right.text())          # правая граница пласта (закачка жидкости)
        t = float(self.lineEdit_time.text()) * 60          # время фильтрации второй жидкости, с
        mu_1 = float(self.lineEdit_viscosity_1.text())     # вязкость жидкости 1, мПа*с
        mu_2 = float(self.lineEdit_viscosity_2.text())     # вязкость жидкости 2, мПа*с
        m = float(self.lineEdit_poro.text())               # пористость, д.ед.
        u = float(self.lineEdit_filt_rate.text()) * 0.001  # суммарная скорость фильтрации двух жидкостей, м/с
        x_s_calculate(x_r, x_l, t, mu_1, mu_2, m, u)       # вызов функции для расчета и вывода графика
        # вывод графика в отдельном окне
        self.label_gr = QLabel(self)
        self.pixmap = QPixmap('graph.png')
        self.label_gr.setPixmap(self.pixmap)
        self.setCentralWidget(self.label_gr)
        self.resize(self.pixmap.width(), self.pixmap.height())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.__init__(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

