import glob
import os
import sys
import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *




def makeShortcuts (inputPath,outputPath):
    try:
      currentPath = inputPath+"/**/*.exe"
      for f in glob.glob(currentPath, recursive=True):
          if("UnityCrashHandler" not in f):
              # Make a link on the desktop
              print(f) 
              os.symlink(f, os.path.expanduser(outputPath+"/"+os.path.basename(f)))
    except:
       print("Unexpected error occurred")

class window(QWidget):
    def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.resize(800,100)
      self.setWindowTitle("Game Lab Shortcut Creator")


      self.label = QLabel(self)
      self.label.setText("Input Path:")
      self.label.move(100,5)

      self.labelThree = QLabel(self)
      self.labelThree.move(100,65)

      self.labelTwo = QLabel(self)
      self.labelTwo.setText("Output Path:")
      self.labelTwo.move(100,35)

    #   Select input
      self.inputButton = QPushButton(self)
      self.inputButton.setText("Select")
      self.inputButton.clicked.connect(self.selectInput)

    #   Select output
      self.inputButton = QPushButton(self)
      self.inputButton.setText("Select")
      self.inputButton.move(0,30)
      self.inputButton.clicked.connect(self.selectOutput)

    #  Run button
      self.inputButton = QPushButton(self)
      self.inputButton.setText("Run")
      self.inputButton.move(0,60)
      self.inputButton.clicked.connect(self.runCommand)


    def selectInput(self):
        file = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.inputFilePath = file
        print(file)
        self.label.setText("Input Path:"+file)
        self.label.adjustSize()
        self.label.update()

    def selectOutput(self):
        file = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.outputPath = file
        print(file)
        self.labelTwo.setText("Output Path:"+file)
        self.labelTwo.adjustSize()
        self.labelTwo.update()
    
    def runCommand(self):
        makeShortcuts(self.inputFilePath, self.outputPath)
        self.labelThree.setText("Done!")
        self.labelThree.adjustSize()
        self.labelThree.update()
def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()




