import os
from PyQt5 import uic
try:
    from qgis.PyQt.QtGui import QDockWidget, QWidget
except:
    from qgis.PyQt.QtWidgets import QDockWidget, QWidget

uiFileDir = os.path.abspath(os.path.dirname(__file__))
selector_path = os.path.join(uiFileDir, "Selector.ui")
encoder_path = os.path.join(uiFileDir, "Encoder.ui")

UI_Selector = uic.loadUi(selector_path)
UI_Encoder = uic.loadUi(encoder_path)