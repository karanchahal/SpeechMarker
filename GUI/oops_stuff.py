import sys
from PyQt4 import QtGui,QtCore # QtCore for even Handling

class  Window(QtGui.QMainWindow):   # Inheriting

     def __init__(self):
         super(Window,self).__init__() # with super we return a parent object,overides the default constructor
         self.setGeometry(50,50,500,300)
         self.setWindowTitle("PyQT")
         self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
         self.home()

     def home(self):
         btn = QtGui.QPushButton("Quit",self) # Quits the application button
         btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

         btn.resize(100,100)
         btn.move(100,100)

         self.show()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    app.exec_()

run()
