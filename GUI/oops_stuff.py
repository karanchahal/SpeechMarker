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

        '''File Picker'''
        filePicker = QtGui.QAction("&Pick a File",self)
        filePicker.setShortcut("Ctrl+F")
        filePicker.setStatusTip("What do you think?")
        filePicker.triggered.connect(self.pickFile)


        ''' Sets menu bar and adds action to it '''
        mainMenu = self.menuBar();
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        filez = mainMenu.addMenu('&FilePicker')
        filez.addAction(filePicker)

        self.home()

    def home(self):
        ''' Adding Buttons '''
        btn = QtGui.QPushButton("Quit",self) # Quits the application button
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint()) # or btn.minimumSizeHint()
        btn.move(100,100)

        '''TOOLBAR'''

        ''' Connects the Action to the yet to be done toolbar '''
        extractAction = QtGui.QAction(QtGui.QIcon('icons/icon.png'),'Flee the Scene',self)
        extractAction.triggered.connect(self.close_application)

        ''' Adds toolbar and the action '''
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        '''FONTS'''

        fontChoice = QtGui.QAction(QtGui.QIcon('icons/icon.png'),'Flee the Scene',self)
        fontChoice.triggered.connect(self.fontChoices)
        self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        ''' Adding check box Functionality '''

        checkBox = QtGui.QCheckBox('Enlarge Window',self)
        checkBox.toggle()
        checkBox.stateChanged.connect(self.enlargeWindow)
        checkBox.move(100,25)

        '''Add Progress Bar '''
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QtGui.QPushButton("Download",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download);

        '''Drop Down button'''
        print self.style().objectName()
        self.styleChoice = QtGui.QLabel("Windows Vista",self);

        comboBox = QtGui.QComboBox(self)

        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.styleChoices)


        self.show()

    def pickFile(self):
        name = QtGui.QFileDialog.getOpenFileName(self,"Open File")
        file = open(name,'r')


    def fontChoices(self):
        font,valid = QtGui.QFontDialog.getFont()
        if valid :
            self.styleChoice.setFont(font)



    def styleChoices(self,text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download(self):
        self.completed = 0;
        while self.completed < 100:
            self.completed += 0.001
            self.progress.setValue(self.completed)

    def enlargeWindow(self,state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)

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
