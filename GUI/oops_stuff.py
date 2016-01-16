import sys
from PyQt4 import QtGui,QtCore # QtCore for even Handling

class  Window(QtGui.QMainWindow):   # Inheriting

    def __init__(self):
        super(Window,self).__init__() # with super we return a parent object,overides the default constructor
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PyQT")
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))

        extractAction = QtGui.QAction("&Get to the chopper!!",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar();
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit",self) # Quits the application button
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint()) # or btn.minimumSizeHint()
        btn.move(100,100)

        extractAction = QtGui.QAction(QtGui.QIcon('icons/icon.png'),'Flee the Scene',self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        self.show()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self,'Extract!',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if(choice == QtGui.QMessageBox.Yes):
            print "Extracting Now.."
            sys.exit()
        else:
            pass

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    app.exec_()

run()
