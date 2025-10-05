import numpy as np
import tensorflow as tf
import cv2

from typing import List
from Gestures.config import ConstantDefineModel as consDefMo
from Gestures.core.HandsDetector import HandsCatch
from Gestures.methods.help_predict import HelpPredict

from Gestures.config import ConstantDefineModel as consDefMod

class DefineModel():
    def __init__(self):
        self.hands_catch = HandsCatch(consDefMo.DEFAULT_STATIC_IMAGE_MODE, 
                                      consDefMo.DEFAULT_MAX_NUM_HANDS)
        self.help_predict = HelpPredict(consDefMo.DEFAULT_STATIC_IMAGE_MODE, 
                                        consDefMo.DEFAULT_MAX_NUM_HANDS)    
        self.model: tf.keras.model = None
        self.labels: List = None
    
    def choose_model(self, path_model: str):
        self.model = tf.keras.models.load_model(path_model)
    
    def choose_output(self, list_output: List[str]):
        self.labels = list_output
        
    def proccess_model(self, frame: cv2.typing.MatLike):
        if not self.model or not self.labels:
            raise ValueError("DefineModel->proccess_model: Se intento procesar el modelo sin definir el modelo y el output del modelo.")
        
        # frame = self.hands_catch.drawHands(frame= frame, proccess=True)
        frame = self.hands_catch.drawHands(frame, True)
        list_landmark = self.hands_catch.guardar_frames(frame=frame, cant_frames=consDefMod.CANT_FRAMES_PREDICT)

        if list_landmark:
            array_landmark = np.array(list_landmark)
            print(array_landmark.shape)
            
            print(array_landmark.shape, array_landmark.size)
            tensor_landmark = tf.convert_to_tensor(array_landmark.reshape(-1, 60, 21, 3))

            predict = self.model.predict(tensor_landmark, verbose=0)
            decision = self.help_predict.predicts(list_predict=predict, 
                                                  label_predict=self.labels, img=frame, 
                                                  list_landmark=list_landmark)

            list_landmark.clear()
            if decision:
                print(f"Predicción: {decision[0]}")
                print(f"Valor: {decision[1]}")
                return frame, decision
            else:
                print("Gesto confuso o no definido")
        
        return frame, None