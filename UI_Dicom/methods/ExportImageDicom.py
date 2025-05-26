import os
from PIL import Image

from core.abstracts.AbsDicomConverFormat import AbsDicomConvert
from services.DicomExtract import DicomExtract

class DicomConvertImage(AbsDicomConvert, DicomExtract):    
    def convert_dicom(self, path_file, houns_min=-200, houns_max=200):
        dc = self.processing_dicom(path_file, houns_min, houns_max)
        dc_image = Image.fromarray(dc)
        return dc_image
    
    def extract_features(self, path_file):
        dc = self.read_dicom(path_file)
        name, instance = str(dc.Name), dc.IstanceNumber
        return name, instance
            
    def save_convert(self, path_folder, path_save, format, houns_min=-200, houns_max=200):
        if self.exists_folder(path_folder):
            folder = self.extract_dicoms_folder(path_folder)
            
            if len(folder)!=0:            
                name, _ = self.extract_features(folder[0])
                path_save = os.path.join(path_save, name)
                self.exists_save(path_save)
                
                for path_file in folder:
                    img = self.convert_dicom(path_file, houns_min, houns_max)
                    _, instance = self.extract_features(path_file)
                                       
                    img.save(os.path.join(path_save,(instance+"."+format)))
            else:
                print("No se encontraron archivos dicom en la carpeta especificada")