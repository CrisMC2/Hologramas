from core.abstracts.AbsDicomConverFormat import AbsDicomConvert, AbsFeaturesVideo
from services.DicomExtract import DicomExtract
from core.classes.DicomProcessing import DicomOrder

class DicomConvertVideo(AbsDicomConvert, AbsFeaturesVideo, DicomOrder, DicomExtract):     
    def extract_features(self, path_file):
        name = self.read_dicom(path_file)
        name = name.PatientName
        return name
    
    def define_mode(self, format: str):
        if format == 'mp4':
            return 'mp4v'
        elif format == 'avi':
            return 'XVID'
        elif format == 'mov':
            return 'avc1'
        elif format == 'mkv':
            return 'H264'
        else:
            return None
    
    def define_shape(self, path_file):
        dc = self.read_dicom(path_file)
        columns, rows = dc.Columns, dc.Rows
        return columns, rows
    
    def define_codec(self, path_save, path_file, format, fps):
        shape = self.define_shape(path_file)
        name = self.extract_features(path_file)
        fourcc = self.define_mode(format)
        self.exists_save(path_save)
        
        out = cv2.VideoWritter(os.path.join(path_save, name+"."+format), cv2.VideoWritter_fourcc(*+fourcc), fps, shape)
        return out
    
    def convert_dicom(self, path_folder, path_save, format='mp4v', fps=15, houns_min=-200, houns_max=200):
        if self.exists_folder(path_folder):
            self.exists_save(path_save)
            folder = self.extract_dicoms_folder(path_folder)
            
            if len(folder)>2:
                lista_dicoms = self.order_dicom(path_folder)
                lista_dicoms = list(map(lambda dc : self.processing_dicom(dc, houns_min, houns_max), lista_dicoms))
                out = self.define_codec(path_save, lista_dicoms[0], format, fps)
                
                for id, file in enumerate(lista_dicoms):
                    img = cv2.cvtColor(file, cv2.COLOR_RGB2GRAY)
                    out.write(img)
                    
                    print(f"Convert {id}° file")
                
                out.release()
            else:
                print("Cantidad de elementos dicom insuficiente")
        else:
            print("No se encontró la ubicación del archivo")
