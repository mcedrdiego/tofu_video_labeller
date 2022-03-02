

class Label:
    def __init__(self, name, group, pred_incomp):
        self.name = name
        self.group = group
        self.pred_incompatibilies = pred_incomp


class LabelGroups:
    
    def __init__(self):
        self.labels = {}
    
    def clear(self):
        self.labels = {}

    def getGroupName(self, labelName):
        if labelName in self.labels:
            return self.labels[labelName].group
    
    def getPredIncomp(self, labelName):
        if labelName in self.labels:
            return self.labels[labelName].pred_incompatibilies
        
    def isIncompPred(self, label1, label2):
        return label2 in self.getPredIncomp(label1)
        
        
    def addLabel(self, labelName, group, pred_incomp):
        self.labels[labelName] = Label(labelName, group, pred_incomp)

    def removeLabel(self, labelName):
        self.labels.pop(labelName)
