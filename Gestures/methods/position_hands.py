import mediapipe as mp
import cv2
import numpy as np
from math import acos, degrees

class Hands():
    def __init__(self, static_image_mode: bool, max_num_hands: int, detection_confidence=0.5, tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.drawing_hands = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(static_image_mode = static_image_mode, 
                                         max_num_hands = max_num_hands,
                                         min_detection_confidence= detection_confidence, 
                                         min_tracking_confidence= tracking_confidence)
    
    def find_landmark(self, img, rescale=False, handNo=0, draw=False):
        list_landmark=list()
        self.result = self.hands.process(img)
        
        height, width, _ = img.shape
        if self.result.multi_hand_landmarks:
            landmark = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(landmark.landmark):
                x = lm.x
                y = lm.y
                z = lm.z
                
                if rescale:
                    x = int(x*width)
                    y = int(y*height)
                    
                if draw:
                    self.drawing_hands.draw_landmarks(
                        img, 
                        landmark,
                        self.mp_hands.HAND_CONNECTIONS
                    )
                list_landmark.append([x, y, z])
                
        return list_landmark
        
    def rescale_landmark(self, img, list_lm):
        height, width, _ = img.shape
        list_tempo_1 = list()
        
        #Recorremos cada frame
        for i in list_lm:
            #Recogemos los 21 listas de 2 datos cada una de cada frame
            list_tempo = [[int(values[0]*width), int(values[1]*height)] for values in i]
            list_tempo_1.append(list_tempo)
        return list_tempo_1

class PositionFingers():
    def __init__ (self):
        self.points_palma = [0, 1, 2, 5, 9, 13, 17]
        self.points_pulgar = [2,3,4]
        self.points_indice = [6, 8]
        self.points_medio = [10,12]
        self.points_anular = [14,16]
        self.points_meñique = [18,20]
        self.dedos_arriba = np.array(False)
    
    def centroide_palma(self, list_landmark):
        centroide = np.empty((0,2))
        
        for value in self.points_palma:
            #Exoneramos el valor de "z" en el list_landmark
            centroide = np.concatenate((centroide, np.array([list_landmark[value]])), axis=0)
            
        centroide = np.mean(centroide, axis=0)
        return centroide
    
    def pulgar_extendido(self, list_landmark):
        list_tempo = np.empty((0,2))
        
        for value in self.points_pulgar:
            list_tempo = np.concatenate((list_tempo, np.array([list_landmark[value]])), axis=0)

        #Calculamos la distancia entre los puntos
        d1 = np.linalg.norm(list_tempo[0] - list_tempo[1])
        d2 = np.linalg.norm(list_tempo[1] - list_tempo[2])
        d3 = np.linalg.norm(list_tempo[0] - list_tempo[2])
        
        #Teorema del coseno (ángulo)
        angle = degrees(acos((d1**2 + d2**2 - d3**2)/(2*d1*d3)))
        return angle

    def resto_fingers(self, list_landmark):
        value_fingers = list()
        
        #Generamos un arreglo general con todos los valores de los dedos 
            #El arreglo tendrá la forma: [[4 elementos], [4 elementos]]
        for i, m, a, me in zip(self.points_indice, self.points_medio, self.points_anular, self.points_meñique):
            value_fingers.append([list_landmark[i], list_landmark[m], list_landmark[a], list_landmark[me]])
        
        return np.array(value_fingers)
    
    def extend_fingers(self, list_lm):
        # list_lm = self.Hands.find_landmark(img, rescale= self.rescale, draw=False)
        
        if list_lm:
            centroide = self.centroide_palma(list_lm)
            angle_pulgar = self.pulgar_extendido(list_lm)
            fingers = self.resto_fingers(list_lm)
            
            if angle_pulgar > 105:
                self.dedos_arriba = np.array(True)
            else:                
                self.dedos_arriba = np.array(False)
            
            #Si quieres agregar info a una lista, no lo hagas con paréntesis (), eso generará un generator
                #Hazlo siempre con corchetes
                #Calculamos la distancia de todos los puntos de los nudillos con el centroide
            distancias_down = np.array([np.linalg.norm(centroide - i, axis=0) for i in fingers[0]])
            
                #Calculamos la distancia de las yemas de los dedos al centroide
            distancias_up = np.array([np.linalg.norm(centroide - i, axis=0) for i in fingers[1]])
            
            #Generamos una matriz con los resultados de si la distancia a los puntos alejados (yemas)
                #Es mayor a la de los puntos más cercanos (nudillos)
            result = distancias_up - distancias_down
                #Esto nos dará un arreglo booleano
            result = result > 0
            
            #Se concatenan los 2 arrays en un vector 
                #Quedará un vector de la forma [5 elementos]
            self.dedos_arriba = np.append(self.dedos_arriba, result)
            # print(self.dedos_arriba)
            # cv2.putText(img,str(self.dedos_arriba.count(True)), (10,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,255), 2)
            
            #Verifica si todos los elementos son True
            if np.all(self.dedos_arriba):
                return True
            else:
                return False
    
class PositionHands():
    def __init__(self):
        self.position_fingers = PositionFingers()
        self.position_hand = list()
        self.defect_value_horizontal = 50
        self.value_position_h = self.defect_value_horizontal
        self.value_position_v = (self.defect_value_horizontal/2)+15
        
    
    #Devuelve True en caso de que la mano esté en la posición inicial horizontal 
        #Posición Inicial => Mano sin inclinación (superior e inferior)
    def position_inicial_h(self, list_landmark):
        wrist = np.array([])
        palm_hand = np.array([])
        centroide = self.position_fingers.centroide_palma(list_landmark)
        
        for id, lm in enumerate(list_landmark):
            if id == 0:
                palm_hand = lm
                break
        
        #Ponemos -30 porque queremos simular que el punto de la muñeca esté algo más abajo que la palma
        wrist = np.append(wrist, [palm_hand[0], palm_hand[1]-30])

        angle = self.angulo_points([wrist, palm_hand, centroide])
        
        #Estos valores se sacaron en base a experimentación
        if angle > 130 and angle <138:
            return True
        else:
            return False
        
    #Definimos si la mano está en posición vertical u horizontal
    def define_position_hand(self, list_landmark: list, points: list = [5,17]):
        distancia, p1, p2 = self.distancia_2_points(list_landmark, points)
        self.position_hand.append(distancia)
        
        #Como mínimo usamos 5 distancias (o sea, analizamos la distancia durante 5 frames)
        if len(self.position_hand) >=5:
            tempo = np.array(self.position_hand)
            
            
            if np.all(tempo > self.defect_value_horizontal):
                self.value_position_h = np.mean(tempo)
                self.value_position_v = (self.value_position_h/2)+15
            
            self.position_hand.clear()
                
        if distancia <= self.value_position_v:
            # return ["Vertical", distancia, p1, p2]
            return "Vertical"
        else:
            # return ["Horizontal", distancia, p1, p2]
            return "Horizontal"
    
    def angulo_points(self, list_points):
        d1 = np.linalg.norm(list_points[0] - list_points[1])
        d2 = np.linalg.norm(list_points[1] - list_points[2])
        d3 = np.linalg.norm(list_points[0] - list_points[2])
        angle = degrees(acos((d1**2 + d2**2 - d3**2)/(2*d1*d3)))
        # print(angle)
        return angle
        
    def distancia_2_points(self, list_landmark, points: list):
        points_interest = list()
        
        for value in points:
            points_interest.append(list_landmark[value][:-1])
        
        points_interest = np.array(points_interest)
        d1 = np.linalg.norm(points_interest[0] - points_interest[1])
        
        return [d1, points_interest[0], points_interest[1]]
           
if __name__ == "__main__":
    video = cv2.VideoCapture(1)        
    hands = Hands(False, 1)
    positionHands = PositionHands()
    p1 = (0,0)
    p2 = (0,0)
    color = (0,255,0)
    text = ""
    while video.isOpened:
        ret, frame = video.read()
        
        if ret == False:
            break
        
        # positionHands.extend_fingers(frame)
        list_lm = hands.find_landmark(frame, True, 0, True)
        if list_lm:
        #     list_lm = np.array(list_lm)
        #     print(np.mean(list_lm, axis=0))
            
        #     if np.mean(list_lm, axis=0)[2] > -0.008:
        #         color = (0, 0, 255)
        #         text="Muy abajo"
        #     else:
        #         color = (0,255,0)
        #         text="Bien"
                
                
        #     if np.mean(list_lm, axis=0)[2] > -0.001:
        #         color = (0, 0, 255)
        #         text="Muy arriba"
                
        #     else:
        #         color = (0,255,0)
                # text="Bien"
            print(f"HORIZONTAL: {positionHands.value_position_h}")
            print(f"VERTICAL: {positionHands.value_position_v}")
            
            
            orientacion, distancia, p1, p2 = positionHands.define_position_hand(list_lm)
            # print(distancia)
            
            if orientacion == "Horizontal":
                color = (0,0,255)
                text = orientacion
            else:
                color = (0,255,0)
                text = orientacion
        
        cv2.line(frame, p1, p2, color, 2)
        # cv2.rectangle(frame, (10, 50), (30, 70), color, 3)
        cv2.putText(frame, text, (10,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, color, 1)
        cv2.imshow("frame", frame)
        
        if cv2.waitKey(1) == 27:
            break

    video.release()
    cv2.destroyAllWindows()