

class Label:
    def __init__(self, name, pred_incomp):
        self.name = name
        self.pred_incompatibilies = pred_incomp


class Group:
    def __init__(self, name):
        self.name = name
        self.labels = {}
    
    def addLabel(self, label):
        self.labels[label.name] = label
        
    def removeLabel(self, labelName):
        self.labels.pop(labelName)
        
    def empty(self):
        return len(self.labels) == 0
    
class LabelGroups:
    
    def __init__(self):
        self.groups = {}
        self.labelGroup = {}
    
    def clear(self):
        self.groups = {}
        self.labelGroup = {}

    def getGroupName(self, labelName):
        return self.labelGroup[labelName]
    
    def getPredIncomp(self, labelName):
        group = self.labelGroup[labelName]
        if group == "":
            return []
        else:
            return self.groups[group].labels[labelName].pred_incompatibilies
        
    def isIncompPred(self, label1, label2):
        return label2 in self.getPredIncomp(label1)
        
    def addGroup(self, group, label):
        if not group in self.groups:
            self.groups[group] = Group(group)
        self.groups[group].addLabel(label)
        
    def addLabel(self, labelName, group, pred_incomp):
        self.labelGroup[labelName] = group
        if group != "":
            self.addGroup(group, Label(labelName, pred_incomp.split(";")))

    def removeLabel(self, labelName):
        group = self.labelGroup[labelName]
        if group != "":
            self.groups[group].removeLabel(labelName)
            if self.groups[group].empty():
                self.groups.pop(group)
        self.labelGroup.pop(labelName)
