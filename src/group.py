
from PyQt5.QtCore import pyqtSignal, QObject

class Label:
    def __init__(self, name, group, pred_incomp):
        self.name = name
        self.group = group
        self.pred_incompatibilies = pred_incomp


class LabelGroups(QObject):
    
    changed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        self.labels = {}
    
    def clear(self):
        self.labels = {}

    def getGroupName(self, labelName):
        if labelName in self.labels:
            return self.labels[labelName].group
        else:
            return ""
    
    def getPredIncomp(self, labelName):
        if labelName in self.labels:
            return self.labels[labelName].pred_incompatibilies
        else:
            return []
        
    def isIncompPred(self, label1, label2):
        return label2 in self.getPredIncomp(label1)
        
        
    def addLabel(self, labelName, group, pred_incomp):
        self.labels[labelName] = Label(labelName, group, pred_incomp)
        self.changed.emit()

    def removeLabel(self, labelName):
        self.labels.pop(labelName)
        self.changed.emit()
