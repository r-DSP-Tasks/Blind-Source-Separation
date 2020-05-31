import mainUI as ui
from PyQt5 import QtWidgets, QtGui
import logging
import helpers as fns
import simpleaudio as sa
import numpy as np
from time import sleep
from functools import partial


class decomposer(ui.Ui_MainWindow):
    """
    Main Application for decomposer.
    This app uses FastICA Algorithms to separate music file into
    their components (Vocals ad Musicals).

    =======================================================

    Note: Works with WAV files only !!

    =======================================================

    **Basic Usage**

    - Load A wav file.
    - Play each result.
    - Save results in file.
    """
    def __init__(self, starter_window):
        super(decomposer, self).setupUi(starter_window)
        self.loaded_file = None
        self.loaded_file_format = None
        self.data = None
        self.rate = None
        self.channels = [None, None]
        self.logger = logging.getLogger()  # Logger maintainer
        self.logger.setLevel(logging.DEBUG)
        self.play_btns = [self.result1, self.result2]

        # Connections
        self.load.clicked.connect(self.load_file)
        for indx, btn in enumerate(self.play_btns):
            self.play_btns[indx].clicked.connect(partial(self.play, indx))
        self.save.clicked.connect(self.save_results)

    def load_file(self):
        """
        Responsible for the following :

        - Loading desired file
        - Passing the file path to main extraction function
        - Decompose file to it`s components
        """
        self.statusbar.showMessage("Loading Audio File")
        self.loaded_file, self.loaded_file_format = QtWidgets.QFileDialog.getOpenFileName(None, "Load Audio File",
                                                                                          filter="*.wav")
        self.logger.debug("File %s Loaded" % self.loaded_file)

        # CHECK CONDITIONS
        if self.loaded_file == "":
            self.logger.debug("loading cancelled")
            self.statusbar.showMessage("Loading cancelled")
            pass
        else:
            self.logger.debug("starting extraction of data")
            self.rate, self.data = fns.load_wav(self.loaded_file)
            # Start Decomposition
            if len(self.data.shape) == 1:
                self.logger.debug("loaded a mono file")
                self.show_message("Warning", "Load a stereo file", QtWidgets.QMessageBox.Ok,
                                  QtWidgets.QMessageBox.Warning)
            else:

                self.decompose()

            self.statusbar.showMessage("Loading Done")
            self.logger.debug("Loading Done")

    def decompose(self):
        """
        Main Decomposition Function.
        Uses sklearn.FastICA algorithm to extract the music file
        components.

        :return: two numpy array vocals and musicals
        """
        self.logger.debug("Starting Decomposition")
        self.channels = fns.decompose(self.data)
        self.logger.debug("Success")

    def play(self, data):
        """
        plays the result in app player
        """
        self.logger.debug("Playing .. ")

        if self.channels[data] is not None:
            sa.stop_all()
            sa.play_buffer(self.channels[data], 1, 2, self.rate)
            sleep(1)

        else:
            self.logger.debug("Fail to play")
            self.show_message("Warning", "Load A file First", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Warning)
            pass

    def save_results(self):
        """
        Saves extracted results into results/
        """

        self.statusbar.showMessage("Saving .. ")
        fns.save_wav("results/"+self.loaded_file.split("/")[-1]+"1.wav", data=self.channels[0], sr=self.rate)
        fns.save_wav("results/"+self.loaded_file.split("/")[-1]+"2.wav", data=self.channels[1], sr=self.rate)
        self.statusbar.showMessage("Files saved at `results/`")
        self.logger.debug("Saving done")

    def show_message(self, header, message, button, icon):
        """
        Responsible for showing message boxes

        ============= ===================================================================================
        **Arguments**
        header:       Box header title.
        message       the informative message to be shown.
        button:       button type.
        icon:         icon type.
        ============= ===================================================================================
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(header)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(button)
        self.logger.debug("messege shown with %s %s " % (header, message))
        msg.exec_()


if __name__ == '__main__':
    import sys
    logging.basicConfig(filename="logs/logfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = decomposer(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
