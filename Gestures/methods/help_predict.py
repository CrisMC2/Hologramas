import numpy as np
from Gestures.core.HandsDetector import HandsDetector
from Gestures.methods.position_hands import PositionFingers, PositionHands

class HelpPredict():
    def __init__(self, static_image_mode, max_num_hands):
        self.positionFingers = PositionFingers()
        self.hands = HandsDetector(static_image_mode=static_image_mode, 
                                   maxHands=max_num_hands)
        self.positionsHands = PositionHands()
        
    def predicts(self, list_predict: np.array, label_predict: list, img, list_landmark):
        if np.max(list_predict) > 0.6:
            #Ordenamos la predicción
            list_predictions = [(label_predict[index], list_predict[0][index]) for index in range(len(label_predict))]
            list_predictions = sorted(list_predictions, key= lambda x: x[1], reverse=True)
            
            #Utilizamos los últimos 10 frames
            list_landmark = list_landmark[-10:]
            
            #Reescalamos (necesitamos los valores respecto a su posición en la imagen)
            list_landmark = self.hands.rescale_landmark(img, list_landmark)
            
            
            if list_predictions[0][0] == "Choose_Function": #Choose Function
                value = self.choose_function(list_landmark)
                
                if value:
                    return [list_predictions[0][0], list_predictions[0][1]]
                
                elif list_predictions[1][0] == "Zoom_Out":
                    return [list_predictions[1][0], list_predictions[1][1]]
                else:
                    return None 
            
            elif list_predictions[0][0] == "Scroll_Down":
                value = self.scroll_down(list_landmark)
                   
                if value:
                    return [list_predictions[0][0], list_predictions[0][1]]
                
                elif list_predictions[1][0] == "Choose_Function":
                    print("Primer Scroll Down, luego Choose Function")
                    return [list_predictions[1][0], list_predictions[1][0]]
                else:
                    return None 
                       
            else:
                return [list_predictions[0][0], list_predictions[0][1]]
                
        else:
            return None
        
    def choose_function(self, list_landmark):
        #Generamos un array vacío
        valid = np.array([])
        
        #Iteramos respecto a cada frame
        for list_lm in list_landmark:
            valid = np.append(valid, self.positionFingers.extend_fingers(list_lm))
        
        #Verificamos que haya como mínimo más del 70% de True
        if np.mean(valid) >= 0.7:
            return True
        else:
            return False
            
    def scroll_down(self, list_landmark):    
        valid = np.array([])
        
        for lm in list_landmark:
            if self.positionsHands.define_position_hand(lm) == "Horizontal":
                valid = np.append(valid, not self.positionsHands.position_inicial_h(lm))
                
            else:
                valid = np.append(valid, np.array([False]))
        
        if np.mean(valid) >=0.7:
            return True
        else:
            return False