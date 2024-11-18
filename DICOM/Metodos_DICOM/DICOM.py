import pydicom as dicom
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
import dicom2nifti

from PIL import Image
from glob import glob

from Abstract_DICOM import DicomOrder_, DicomInformation_, DicomAnonimize_, DicomConvert_, FeaturesVideo_, DicomViews_, DicomExtract_

########################################################################################
#INFORMACIÓN

class InformationPatient(DicomInformation_, DicomAnonimize_):
    def get_information(self, dc, PatientName=False, PatientID=False, PatientBirthDate=False, PatientSex=False):
        list_information = list()
        if PatientName:
            list_information.append(dc.PatientName)
        if PatientID:
            list_information.append(dc.PatientID)
        if PatientBirthDate:
            list_information.append(dc.PatientBirthdate)
        if PatientSex:
            list_information.append(dc.PatientSex)

        return list_information
    
    def set_information(self, dc, PatientName=None, PatientID=None, PatientBirthDate=None, PatientSex=None):
        
        if PatientName:
            dc.PatientName = PatientName
        if PatientID:
            dc.PatientID = PatientID
        if PatientBirthDate:
            dc.PatientBirthDate = PatientBirthDate
        if PatientSex:
            dc.PatientSex = PatientSex
        
        
    def anonymize_dicom(self, dc, PatientName="Desconocido", PatientID="NAn", PatientBirthDate="NAn", PatientSex="Nan", 
                        StudyDate="Nan", StudyTime="Nan", InstitutionName="Nan", InstitutionAdress="Nan"):
        
        dc.PatientName = PatientName
        dc.PatientID = PatientID
        dc.PatientBirthDate = PatientBirthDate
        dc.PatientSex = PatientSex
        dc.StudyDate = StudyDate
        dc.StudyTime = StudyTime
        dc.InstitutionName = InstitutionName
        dc.InstitutionAdress = InstitutionAdress
        
class InformationStudySerie(DicomInformation_):    
    def get_information(self, dc, BodyPartExamined=False, StudyInstanceID=False, SeriesInstanceUID=False, StudyDate=False, StudyTime=False, 
                        InstitutionName=False, InstitutionAdress=False):
        
        
        list_information = list()
        
        if BodyPartExamined:
            list_information.append(dc.BodyPartExamined)
        if StudyInstanceID:
            list_information.append(dc.StudyInstanceID)
        if SeriesInstanceUID:
            list_information.append(dc.SeriesInstanceUID)
        if StudyDate:
            list_information.append(dc.StudyDate)
        if StudyTime:
            list_information.append(dc.StudyTime)
        if InstitutionName:
            list_information.append(dc.InstitutionName)
        if InstitutionAdress:
            list_information.append(dc.IntitutionAdress)
            
        return list_information

    def set_information(self, dc, BodyPartExamined=None, StudyInstanceID=None, SeriesInstanceUID=None, StudyDate=None, StudyTime=None, 
                        InstitutionName=None, InstitutionAdress=None):
        
        
        if BodyPartExamined:
            dc.BodyPartExamined = BodyPartExamined
        if StudyInstanceID:
            dc.StudyInstanceID = StudyInstanceID
        if SeriesInstanceUID:
            dc.SeriesInstanceUID = SeriesInstanceUID
        if StudyDate:
            dc.StudyDate = StudyDate
        if StudyTime:
            dc.StudyTime = StudyTime
        if InstitutionName:
            dc.InstitutionName = InstitutionName
        if InstitutionAdress:
            dc.InstitutionAdress = InstitutionAdress

class InformationImage(DicomInformation_):
    def get_information(self, dc, Modality=False, ImagePositionPatient=False, ImageOrientationPatient=False, InstanceNumber=False,
                        PixelSpacing=False, SliceThickness=False, SpacingBetweenSlices=False, 
                        WindowCenter=False, WindowWidth=False, RescaleIntercept=False, RescaleSlope=False):
        
        
        list_information = list()
        if Modality:
            list_information.append(dc.Modality)
        if ImagePositionPatient:
            list_information.append(dc.ImagePositionPatient)
        if ImageOrientationPatient:
            list_information.append(dc.ImageOrientationPatient)
        if InstanceNumber:
            list_information.append(dc.InstanceNumber)
        if PixelSpacing:
            list_information.append(dc.PixelSpacing)
        if SliceThickness:
            list_information.append(dc.SliceThickness)
        if SpacingBetweenSlices:
            list_information.append(dc.SpacingBetweenSlices)
        if WindowCenter:
            list_information.append(dc.WindowCenter)
        if WindowWidth:
            list_information.append(dc.WindowWidth)
        if RescaleIntercept:
            list_information.append(dc.RescaleIntercept)
        if RescaleSlope:
            list_information.append(dc.RescaleSlope)
        
        return list_information

    def set_information(self, dc, Modality=None, ImagePositionPatient=None, ImageOrientationPatient=None, 
                        PixelSpacing=None, SliceThickness=None, SpacingBetweenSlices=None, 
                        WindowCenter=None, WindowWidth=None, RescaleIntercept=None, RescaleSlope=None):
        
        if Modality:
            dc.Modality = Modality
        if ImagePositionPatient:
            dc.ImagePositionPatient = ImagePositionPatient
        if ImageOrientationPatient:
            dc.ImagePositionPatient = ImageOrientationPatient
        if PixelSpacing:
            dc.PixelSpacing = PixelSpacing
        if SliceThickness:
            dc.SliceThickness = SliceThickness
        if SpacingBetweenSlices:
            dc.SpacingBetweenSlices = SpacingBetweenSlices
        if WindowCenter:
            dc.WindowCenter = WindowCenter
        if WindowWidth:
            dc.WindowWidth = WindowWidth 
        if RescaleIntercept:
            dc.RescaleIntercept = RescaleIntercept
        if RescaleSlope:
            dc.RescaleSlope = RescaleSlope

########################################################################################
#CONVERSIONES       
class DicomConvertNifti(DicomConvert_, DicomExtract_):
    pass

class DicomConvertImage(DicomConvert_, DicomExtract_):    
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

class DicomConvertVideo(DicomConvert_, FeaturesVideo_, DicomOrder_, DicomExtract_):     
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

class DicomConvert3D(DicomConvert_):
    def convert_dicom_3d(self):
        pass
    
class ViewAxial(DicomViews_):
    def define_aspect(self, label):
        pass
    
    def create_view(self, array_dicoms, i):
        return array_dicoms[i,:,:]
    
class ViewSagittal(DicomViews_):
    def define_aspect(self, label):
        pass
    
    def create_view(self, array_dicoms, i):
        return array_dicoms[:,:,i]

class ViewCoronal(DicomViews_):
    def define_aspect(self, label):
        pass
    
    def create_view(self, array_dicoms, i):
        return array_dicoms[:,i,:]

                