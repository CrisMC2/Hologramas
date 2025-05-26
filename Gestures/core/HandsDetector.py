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
    
    def drawHands(self, frame: cv2.typing.MatLike, draw: bool =False):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # frame = cv2.flip(frame, 1) #Al no incluir esta línea de código, los videos de la mano derecha serán de la mano izquierda
        
        self.result = self.hands.process(frame)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if self.result.multi_hand_landmarks:
            for id, landmark in enumerate(self.result.multi_hand_landmarks):                
                if draw: 
                    # print(self.result.multi_handedness[id].classification[0].label)
                    self.mp_drawing.draw_landmarks(
                        frame, 
                        landmark,
                        self.mp_hands.HAND_CONNECTIONS
                    )
        
        return frame
    
    def findLandmark(self, draw=True, handNo=0):
        listLandmark = list()
        
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
        return listLandmark
    
    
    
    
    
    
#==============================================================================================
#esta clase actualmente no se utiliza    
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
        self.video_frame = 0 #Sirve para resetear
        # self.Hands_Detector = HandsDetector(static_image_mode=maxHands, detection_confidence, tracking_confidence)
    

    def guardar_frames(self, frame: cv2.typing.MatLike, cant_frames: int):
        if self.video_frame == 0:
            self.listLm.clear()
        
        if self.result.multi_hand_landmarks:
            # if self.video_frame <=15:
            #     cv2.putText(frame, "Cargando...", (10,50), cv2.FONT_HERSHEY_COMPLEX, 2, (231, 154,36), 2)
                
            # else:
            lm = self.findLandmark(draw=False) 
            self.listLm.append(lm) #No es necesario confirmar si existe o no, porque self.result ya se encarga de ello

            if len(self.listLm) == cant_frames:
                cv2.putText(frame, "Procesando", (10,50), cv2.FONT_HERSHEY_COMPLEX, 2, (67, 218,115), 2)
                self.video_frame=0
                
                return self.listLm

            # print(self.video_frame)
            self.video_frame+=1
        else:
            if self.listLm:
                self.video_frame=0