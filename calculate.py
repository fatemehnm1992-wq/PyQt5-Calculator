# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("calc")
        MainWindow.resize(373, 497)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Display
        self.outputlabel = QtWidgets.QLabel(self.centralwidget)
        self.outputlabel.setGeometry(QtCore.QRect(10, 10, 351, 81))

        font = QtGui.QFont()
        font.setPointSize(19)

        self.outputlabel.setFont(font)
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputlabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.outputlabel.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter
        )
        self.outputlabel.setObjectName("outputlabel")


        # Buttons
        buttons = [
            ("percentbutton", "%", 10, 100, lambda: self.press_it("%")),
            ("cbutton", "C", 100, 100, lambda: self.press_it("C")),
            ("errorbutton", "<<", 190, 100, lambda: self.remove_it()),
            ("devidbutton", "/", 280, 100, lambda: self.press_it("/")),

            ("sevenbutton", "7", 10, 170, lambda: self.press_it("7")),
            ("eightbutton", "8", 100, 170, lambda: self.press_it("8")),
            ("ninebutton", "9", 190, 170, lambda: self.press_it("9")),
            ("multiplybutton", "x", 280, 170, lambda: self.press_it("*")),

            ("fourbutton", "4", 10, 240, lambda: self.press_it("4")),
            ("fivebutton", "5", 100, 240, lambda: self.press_it("5")),
            ("sixbutton", "6", 190, 240, lambda: self.press_it("6")),
            ("minusbutton", "-", 280, 240, lambda: self.press_it("-")),

            ("onebutton", "1", 10, 310, lambda: self.press_it("1")),
            ("twobutton", "2", 100, 310, lambda: self.press_it("2")),
            ("threebutton", "3", 190, 310, lambda: self.press_it("3")),
            ("addbutton", "+", 280, 310, lambda: self.press_it("+")),

            ("plusminusbutton", "+/-", 10, 380, lambda: self.plus_minus_it()),
            ("zeroButton", "0", 100, 380, lambda: self.press_it("0")),
            ("decimalbutton", ".", 190, 380, lambda: self.dot_it()),
            ("equalbutton", "=", 280, 380, lambda: self.math_it()),
        ]


        for name, text, x, y, action in buttons:

            button = QtWidgets.QPushButton(
                self.centralwidget,
                clicked=action
            )

            button.setGeometry(
                QtCore.QRect(x, y, 81, 61)
            )

            button_font = QtGui.QFont()
            button_font.setPointSize(19)
            button.setFont(button_font)

            button.setObjectName(name)
            button.setText(text)

            setattr(self, name, button)


        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 29))
        MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            # Add decimal point
    def dot_it(self):

        screen = self.outputlabel.text()

        if "." not in screen:
            self.outputlabel.setText(f"{screen}.")


    # Button press handler
    def press_it(self, pressed):

        screen = self.outputlabel.text()

        if pressed == "C":
            self.outputlabel.setText("0")

        elif pressed == "%":

            try:
                value = float(screen)
                self.outputlabel.setText(str(value / 100))

            except:
                self.outputlabel.setText("ERROR")


        elif screen == "0":

            self.outputlabel.setText(pressed)


        else:

            self.outputlabel.setText(
                f"{screen}{pressed}"
            )


    # Remove last character
    def remove_it(self):

        screen = self.outputlabel.text()

        if len(screen) > 1:

            self.outputlabel.setText(
                screen[:-1]
            )

        else:

            self.outputlabel.setText("0")


    # Calculate result
    def math_it(self):

        screen = self.outputlabel.text()

        try:

            allowed_chars = "0123456789+-*/."

            if all(char in allowed_chars for char in screen):

                answer = eval(screen)

                self.outputlabel.setText(
                    str(answer)
                )

            else:

                self.outputlabel.setText("ERROR")


        except ZeroDivisionError:

            self.outputlabel.setText(
                "Cannot divide by zero"
            )


        except:

            self.outputlabel.setText(
                "ERROR"
            )


    # Change positive / negative
    def plus_minus_it(self):

        screen = self.outputlabel.text()

        if screen.startswith("-"):

            self.outputlabel.setText(
                screen.replace("-", "", 1)
            )

        else:

            self.outputlabel.setText(
                f"-{screen}"
            )



    # Window title
    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(
            _translate(
                "MainWindow",
                "PyQt5 Calculator"
            )
        )

        self.outputlabel.setText(
            _translate(
                "MainWindow",
                "0"
            )
        )



if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())