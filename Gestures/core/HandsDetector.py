import mediapipe as mp
import cv2 


class HandsDetector():
    def __init__(self, static_image_mode: bool, maxHands: int, detection_confidence: float =0.5, tracking_confidence: float=0.5):
        self.mode = static_image_mode
        self.maxHands = maxHands
        self.detection_confidence=detection_confidence
        self.tracking_confidence = tracking_confidence
        
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(static_image_mode = self.mode, 
                                         max_num_hands = self.maxHands,
                                         min_detection_confidence = self.detection_confidence,
                                         min_tracking_confidence = self.tracking_confidence)
    
    def proccess_frame(self, frame: cv2.typing.MatLike):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    def drawHands(self, frame: cv2.typing.MatLike, proccess: bool =False, landmark=None):
        if proccess:
            self.proccess_frame(frame)
            
            if self.result.multi_hand_landmarks:
                for id, landmark in enumerate(self.result.multi_hand_landmarks):                
                    # print(self.result.multi_handedness[id].classification[0].label)
                    self.mp_drawing.draw_landmarks(
                        frame, 
                        landmark,
                        self.mp_hands.HAND_CONNECTIONS
                    )
        else:
            if landmark:
                self.mp_drawing.draw_landmarks(
                    frame, 
                    landmark,
                    self.mp_hands.HAND_CONNECTIONS
                )
            
        return frame
    
    def findLandmark(self, frame: cv2.typing.MatLike, handNo=0, proccess=True):
        listLandmark = list()
        if proccess:
            self.proccess_frame(frame)
                
        if self.result.multi_hand_landmarks:
            #HandNo hace referencia a la mano que quieres usar 
                #En caso de especificar 0, significa que usarás la primera mano en ser detectada
                    #Mientras que si usas 1, usarás la segunda en ser detectada
            landmark = self.result.multi_hand_landmarks[handNo]
            
            for id, lm in enumerate (landmark.landmark):
                x = lm.x
                y = lm.y
                z = lm.z
                listLandmark.append([x, y, z])  
            
        else:
            print("HandsDetector->findLandmark: Self.result no está inicializado o no encuentra landmarks en la imagen.")

        return listLandmark

    def rescale_landmark(self, img, list_lm):
        height, width, _ = img.shape
        list_tempo_1 = list()
        
        #Recorremos cada frame
        for i in list_lm:
            #Recogemos los 21 listas de 2 datos cada una de cada frame
            list_tempo = [[int(values[0]*width), int(values[1]*height)] for values in i]
            list_tempo_1.append(list_tempo)
        return list_tempo_1
    
    
#==============================================================================================  
class HandsCatch(HandsDetector):
    """
    La clase HandsCatch
    """
    def __init__(self, static_image_mode: bool, maxHands: int, 
                 detection_confidence: int=0.5, tracking_confidence: int=0.5):
        super().__init__(static_image_mode=static_image_mode, 
                         maxHands=maxHands, detection_confidence=detection_confidence, 
                         tracking_confidence=tracking_confidence)
        
        self.listLm = list()
        self.frame_overall = 0
        # self.Hands_Detector = HandsDetector(static_image_mode=maxHands, detection_confidence, tracking_confidence)
    

    def guardar_frames(self, frame: cv2.typing.MatLike, cant_frames: int):
        # self.proccess_frame(frame) #Esto generará al self.result
        
        if self.frame_overall == 0:
            self.listLm.clear()
        
        if self.result.multi_hand_landmarks:
            lm = self.findLandmark(frame=frame, proccess=False) 
            
            
            self.listLm.append(lm) #No es necesario confirmar si existe o no, porque self.result ya se encarga de ello

            if len(self.listLm) == cant_frames:
                cv2.putText(frame, "Procesando", (10,50), cv2.FONT_HERSHEY_COMPLEX, 2, (67, 218,115), 2)
                self.frame_overall = 0
                return self.listLm
            
            self.frame_overall+=1 
            
        else:
            if self.listLm:
                self.frame_overall =0