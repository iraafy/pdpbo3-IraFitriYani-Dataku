class GetData:

    def __init__(self, input1, input2, input3, drop, check, radio):
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3
        self.drop = drop
        self.check = check 
        self.radio = radio

    def setInput1(self, input1):
        self.input1 = input1

    def getInput1(self):
        return self.input1

    def setInput2(self, input2):
        self.input2 = input2

    def getInput2(self):
        return self.input2

    def setInput3(self, input3):
        self.input3 = input3

    def getinput3(self):
        return self.input3

    def setDrop(self, drop):
        self.drop = drop

    def getDrop(self):
        return self.drop

    def setFinalValue(self, check):
        self.check = check

    def getCheck(self):
        return self.check
    
    def setRadio(self, radio):
        self.radio = radio

    def getRadio(self):
        return self.radio