import cv2

from Shared.classes.SignalData import Emit_Data

class EmitGest():
    def __init__(self):
        self.obj_emit = Emit_Data()
        
    def execute(self):
        from Gestures.controller.CreateModel import create_model
        define_model = create_model()
        
        video = cv2.VideoCapture(0)
        video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while video.isOpened():
            ret, frame = video.read()
            
            if not ret:
                print("execute_main: Video no encontrado")
                break
            
            frame, predict = define_model.proccess_model(frame)

            if predict:
                self.obj_emit.emit_signal(frame, predict)
        
        video.release()
        cv2.destroyAllWindows()    