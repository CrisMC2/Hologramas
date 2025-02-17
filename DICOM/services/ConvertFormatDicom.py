import pydicom as dicom
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
import dicom2nifti

from PIL import Image
from glob import glob
    
from abstract.AbsDicomConverFormat import AbsDicomConvert, AbsFeaturesVideo
from abstract.AbsDicomExtract import AbsDicomExtract
from abstract.AbsDicomProcessing import AbsDicomOrder

class DicomConvertNifti(AbsDicomConvert, AbsDicomExtract):
    pass

class DicomConvertImage(AbsDicomConvert, AbsDicomExtract):    
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

class DicomConvertVideo(AbsDicomConvert, AbsFeaturesVideo, AbsDicomOrder, AbsDicomExtract):     
    def extract_features(self, path_file):
        name = self.read_dicom(path_file)
        name = name.PatientName
        return name
    
    def define_mode(self, format):
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

class DicomConvert3D(AbsDicomConvert):
    def convert_dicom_3d(self):
        pass