import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("крестики-нолики")
        self.setGeometry(100, 100, 300, 360)
        self.setStyleSheet("background:#000000")
        self.create_widgets()
        self.show()

    def create_widgets(self):

        self.turn = 0
        self.times = 0
        self.push_list = []
        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append(QPushButton(self))
            self.push_list.append(temp)

        x = 90
        y = 90

        for i in range(3):
            for j in range(3):
                self.push_list[i][j].setGeometry(x * i + 20, y * j + 20, 80, 80)
                self.push_list[i][j].setStyleSheet("background-color:#FFFFFF;color: black;")
                self.push_list[i][j].setFont(QFont('Arial', 30, QFont.Bold))
                self.push_list[i][j].clicked.connect(self.action)

        reset_game = QPushButton("again", self)
        reset_game.setGeometry(35, 300, 110, 50)
        reset_game.setFont(QFont('Arial', 30))
        reset_game.setStyleSheet(
            "QPushButton{background-color:#000000; font-size:30px; color:white;}""QPushButton:pressed { background-color: white ;}")

        exit_game = QPushButton("exit", self)
        exit_game.setFont(QFont('Arial', 30))
        exit_game.setGeometry(165, 300, 100, 50)
        exit_game.setStyleSheet(
            "QPushButton{background-color:#000000; font-size:30px; color:white; }""QPushButton:pressed { background-color: white ;}")
        exit_game.clicked.connect(self.exit_)
        reset_game.clicked.connect(self.replay)

    def replay(self):

        self.turn = 0
        self.times = 0

        for buttons in self.push_list:
            for button in buttons:
                button.setEnabled(True)
                button.setText("")
                button.setStyleSheet("background-color:#FFFFFF;color: black;;")

    def exit_(self):
        self.close()

    def action(self):
        self.times += 1
        button = self.sender()
        button.setEnabled(False)

        if self.turn == 0:
            button.setText("X")
            self.turn = 1
        else:
            button.setText("O")
            self.turn = 0

        win = self.wins()
        i = 0
        if win == True:
            i = 0
        elif self.times == 9:
            for i in range(3):
                for j in range(3):
                    self.push_list[i][j].setStyleSheet("background-color:black;color:white")

    def wins(self):

        for i in range(3):
            if self.push_list[0][i].text() == self.push_list[1][i].text() \
                    and self.push_list[0][i].text() == self.push_list[2][i].text() \
                    and self.push_list[0][i].text() != '':

                for j in range(3):
                    self.push_list[j][i].setStyleSheet("color:white; background-color:black")
                return True

        for i in range(3):
            if self.push_list[i][0].text() == self.push_list[i][1].text() \
                    and self.push_list[i][0].text() == self.push_list[i][2].text() \
                    and self.push_list[i][0].text() != '':

                for j in range(3):
                    self.push_list[i][j].setStyleSheet("color:white; background-color:black")
                return True

        if self.push_list[0][0].text() == self.push_list[1][1].text() \
                and self.push_list[0][0].text() == self.push_list[2][2].text() \
                and self.push_list[0][0].text() != "":
            for i in range(3):
                for j in range(3):
                    if i == j:
                        self.push_list[i][j].setStyleSheet("color:white; background-color:black")
            return True

        if self.push_list[0][2].text() == self.push_list[1][1].text() \
                and self.push_list[1][1].text() == self.push_list[2][0].text() \
                and self.push_list[0][2].text() != "":
            for i in range(3):
                for j in range(3):
                    if ((i + j) == (3 - 1)):
                        self.push_list[i][j].setStyleSheet("color:white; background-color:black")
            return True

        return False


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exit(app.exec())


if __name__ == '__main__':
    main()
