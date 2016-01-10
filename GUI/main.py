import sys
from PyQt4 import QtGui # contains the most import Gui assets

app = QtGui.QApplication(sys.argv) # sys.argv allows us to add command line arguments

"""Window"""
window = QtGui.QWidget()
window.show() # Important to always show

window.setGeometry(300,100,500,300)
window.setWindowTitle("PyQT!")

"""Exits the application"""
app.exec_()
