import sys
import os
import cv2
import numpy as np
import tensorflow as tf

#En este caso importaremos un archivo proveniente desde fuera de nuestra carpeta (la de ahora)
        #Para ello agregaremos al "path" de python, la ubicación del archivo
            #Lo que aquí está pasando es que se está referenciando mediante la ruta absoluta a la carpeta donde está todo
            #Pero para no hacerlo manualmente lo que hacemos es obtener la ubicación del archivo (dirname) después de haber vuelto una carpeta atrás (..)
            
# ---------------- RUTAS ----------------
def configurar_rutas():
    carpeta = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    sys.path.append(carpeta)  #Necesario para importar HandsDetector

    carpeta_2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    sys.path.append(carpeta_2) #Necesario para importar help_predict

# ---------------- INICIALIZACIÓN ----------------
def inicializar_componentes():
    import core.HandsDetector as hs
    from methods.help_predict import HelpPredict
    #Cargamos el modelo de IA
    #NOTA => Entrada esperada del modelo = (60,21,3)
    
    labels = ["Choose_Function", "Displace_Left", "Displace_Right", "Zoom_In", "Zoom_Out", "Scroll_Up", "Scroll_Down"]
    path_modelo = os.path.join("Reconocimiento_gestual", "resources", "Modelos", "Renovados", "Modelo_60_frames_Conv_lstm.keras") #Sino me equivoco esto pasa porque al inicio cambiamos el path del sistema
    
    modelo = tf.keras.models.load_model(path_modelo)
    landmark = hs.HandsDownload(0, False, 1)
    help_predictor = HelpPredict(False, 1)

    return modelo, landmark, help_predictor, labels

# ---------------- PROCESAMIENTO Y PREDICCIÓN ----------------
def ejecutar_reconocimiento_gestos(modelo, landmark, help_predictor, labels):
    video = cv2.VideoCapture(0)

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            print("Video no reconocido")
            break
        #La 
        # frame = cv2.flip(frame, 1)
        frame = landmark.drawHands(frame, True)
        list_landmark = landmark.guardar_frames(frame, 60)  #Definimos la lista de landmarks

        if list_landmark: #Convertimos la lista en un array (1, 60, 21, 3)
            array_landmark = np.array([np.array(value) for i in list_landmark for j in i for value in j])
            #Y luego en un tensor (por eficiencia), y luego reestructuramos el array para que sea de la forma que deseamos
            tensor_landmark = tf.convert_to_tensor(array_landmark.reshape(-1, 60, 21, 3))
            print("Forma del tensor:", tensor_landmark.shape)

            predict = modelo.predict(tensor_landmark, verbose=0)
            decision = help_predictor.predicts(predict, labels, frame, list_landmark)

            if decision:
                print(f"Predicción: {decision[0]}")
                print(f"Valor: {decision[1]}")
            else:
                print("Gesto confuso o no definido")

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) == 27:  # ESC para salir
            break

    video.release()
    cv2.destroyAllWindows()

# ---------------- EJECUCIÓN GENERAL ----------------
def main():
    configurar_rutas()
    modelo, landmark, help_predictor, labels = inicializar_componentes()
    ejecutar_reconocimiento_gestos(modelo, landmark, help_predictor, labels)

# Si ejecutas directamente este archivo:
if __name__ == "__main__":
    main()
