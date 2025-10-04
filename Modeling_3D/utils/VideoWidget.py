import cv2

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap


from Shared.classes.SignalData import Emit_Data
from Gestures.controller.CreateModel import create_model
from Modeling_3D.config import constantGestureMove as consGesMo

class VideoWidget(QWidget):    
    def __init__(self):
        super().__init__()
        
        
        self.timer = QTimer()
        

        self.signal = Emit_Data()
        self.model = create_model()
        
        self.timer.timeout.connect(self.__update_frame)
        
    def define_components(self, cap_insert: cv2.VideoCapture, video_label: QLabel, size_cap: list[int, int]=None):
        self.cap = cap_insert
        self.label = video_label
        
        if size_cap:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, size_cap[0])
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, size_cap[1])
        
    def start_timer(self):    
        #Aquí se dispara el __update_frame
        self.timer.start(consGesMo.START_TIMER)
    
    def stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()
        
    def __update_frame(self):
        ret, frame = self.cap.read()
        
        if ret == None:
            print("No se pudo capturar el Frame")
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        frame, list_predict = self.model.proccess_model(frame)
        
        if list_predict:
            self.predict = list_predict[0]
            self.value_predict = list_predict[1]
        
            print("VideoWidget->__update_frame: Emitiendo señal.")
            self.signal.emit_signal(self.predict)
        
        pixmap = self.__convert_frame_pixmap(frame)
        
        self.label.setPixmap(pixmap)
        
    def __convert_frame_pixmap(self, frame: cv2.typing.MatLike):
        height, width, channel = frame.shape
        bytes_per_line = width*channel
        
        #QImage(frame, width, height, bytes_per_line, format)
        image = QImage(frame, width, height, 
                       bytes_per_line, 
                       QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        
        return pixmap
    
    def closeEvent(self, event):
        if self.cap:
            self.cap.release()
            self.stop_timer()
            
        super().closeEvent(event)