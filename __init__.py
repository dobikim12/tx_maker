from PyQt5 import QtCore, QtGui, QtWidgets
import sys
path = 'D:\\Company\\_01.Pratice\\_python\\JS_PIPE'
if not path in sys.path:
    sys.path.append(path)
from tools.tx_maker import main



def show_window():
    global TX_Maker
    TX_Maker = QtWidgets.QMainWindow()
    ui = main.Ui_TX_Maker()
    ui.setupUi(TX_Maker)
    TX_Maker.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TX_Maker = QtWidgets.QMainWindow()
    ui = main.Ui_TX_Maker()
    ui.setupUi(TX_Maker)
    TX_Maker.show()
    sys.exit(app.exec_())




'''
import sys
path = 'D:\\Company\\_01.Pratice\\_python\\JS_PIPE'
if not path in sys.path:
    sys.path.append(path)
from tools import tx_maker
reload(tx_maker)

tx_maker.show_window()
'''