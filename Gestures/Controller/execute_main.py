import cv2

from core.DefineModel import DefineModel
from config import ConstantDefineModel as consDefMod

if __name__ == "__main__":
    
    define_model = DefineModel()
    define_model.choose_model(consDefMod.PATH_MODEL)
    define_model.choose_output(consDefMod.LIST_LABELS_OUTPUT)
    
    video = cv2.VideoCapture(0)

    while video.isOpened():
        ret, frame = video.read()
        
        if not ret:
            print("execute_main: Video no encontrado")
            break
        
        predict = define_model.proccess_model(frame)
        
        cv2.imshow("Video", frame)
        
        if cv2.waitKey(1) == 27:
            break
    
    video.release()
    cv2.destroyAllWindows()
    