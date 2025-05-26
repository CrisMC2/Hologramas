import core.HandsDetector as hs
from methods.help_predict import HelpPredict

class DefineModel():
    def __init__(self):
        self.hands_catch = hs.HandsCatch()
        self.help_predict = HelpPredict()    
        self.model = None
    
    