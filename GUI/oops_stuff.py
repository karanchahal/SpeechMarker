import sys
from PyQt4 import QtGui,QtCore # QtCore for even Handling

class  Window(QtGui.QMainWindow):   # Inheriting

    def __init__(self):
        super(Window,self).__init__() # with super we return a parent object,overides the default constructor
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PyQT")
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        ''' Sets actionBar '''
        extractAction = QtGui.QAction("&Get to the chopper!!",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        ''' Sets menu bar and adds action to it '''
        mainMenu = self.menuBar();
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        '''Adding Buttons '''
        btn = QtGui.QPushButton("Quit",self) # Quits the application button
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint()) # or btn.minimumSizeHint()
        btn.move(100,100)


        '''Connects the Action to the yet to be done toolbar'''
        extractAction = QtGui.QAction(QtGui.QIcon('icons/icon.png'),'Flee the Scene',self)
        extractAction.triggered.connect(self.close_application)

        '''Adds toolbar and the action '''
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        self.show()

    def close_application(self):
        '''Adds the Pop Up message BOx Functionality'''
        choice = QtGui.QMessageBox.question(self,'Extract!',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if(choice == QtGui.QMessageBox.Yes):
            print "Extracting Now.."
            sys.exit()
        else:
            pass

        # End    

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    app.exec_()

run()
