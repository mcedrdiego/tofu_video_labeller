import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen

from signals import SignalBus


class LabelSliderWidget(QWidget):

    def __init__(self):
        super(LabelSliderWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(170, 30)
        self.setMaximumHeight(30)
        self.value = 2
        self.num = [2, 4, 6, 8]

    def setValue(self, value):
        self.value = value

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        MAX_CAPACITY = 8
        OVER_CAPACITY = 10
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)
        size = self.size()
        w = size.width()
        h = size.height()
        step = int(round(w / 5))
        till = int(((w / OVER_CAPACITY) * self.value))
        full = int(((w / OVER_CAPACITY) * MAX_CAPACITY))

        if self.value >= MAX_CAPACITY:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till-full, h)
        else:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)
        j = 0

        for i in range(step, 5*step, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i-fw//2, h//2, str(self.num[j]))
            j = j + 1


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        OVER_CAPACITY = 10
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(0, OVER_CAPACITY)
        sld.setValue(2)

        self.c   = Communicate()
        self.wid = BurningWidget()

        self.c.updateBW[int].connect(self.wid.setValue)
        sld.valueChanged[int].connect(self.changeValue)

        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(sld)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(500, 300, 390, 210)
        self.setWindowTitle('Burning widget')

    def changeValue(self, value):
        self.c.updateBW.emit(value)
        self.wid.repaint()
