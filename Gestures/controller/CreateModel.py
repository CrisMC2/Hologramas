from Gestures.core.DefineModel import DefineModel
from Gestures.config import ConstantDefineModel as consDefMod

def create_model():
    define_model = DefineModel()
    define_model.choose_model(consDefMod.PATH_MODEL)
    define_model.choose_output(consDefMod.LIST_LABELS_OUTPUT)
    
    return define_model