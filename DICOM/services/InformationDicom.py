import pydicom as dicom

from core.abstracts.AbsDicomInformation import AbsDicomInformation, AbsDicomAnonimize

class InformationPatient(AbsDicomInformation, AbsDicomAnonimize):
    
    
    """
    Cambiar la lista por un diccionario
    """
    def get_information(self, dc: dicom.FileDataset, PatientName=False, PatientID=False, 
                        PatientBirthDate=False, PatientSex=False) -> dict:
        dict_information = dict()
        if PatientName:
            dict_information["PatientName"] = dc.PatientName
            # list_information.append(dc.PatientName)
        if PatientID:
            dict_information["PatientID"] = dc.PatientID
            # list_information.append(dc.PatientID)
        if PatientBirthDate:
            dict_information["PatientBirthDate"] = dc.PatientBirthDate
            # list_information.append(dc.PatientBirthdate)
        if PatientSex:
            dict_information["PatientSex"] = dc.PatientSex
            # list_information.append(dc.PatientSex)

        
        return dict_information
    
    def set_information(self, dc: dicom.FileDataset, PatientName: str, PatientID: str, PatientBirthDate: str, PatientSex: str):
        if PatientName:
            dc.PatientName = PatientName
        if PatientID:
            dc.PatientID = PatientID
        if PatientBirthDate:
            dc.PatientBirthDate = PatientBirthDate
        if PatientSex:
            dc.PatientSex = PatientSex
        
        
    def anonymize_dicom(self, dc: dicom.FileDataset, PatientName="Desconocido", PatientID="NAn", PatientBirthDate="NAn", PatientSex="Nan", 
                        StudyDate="Nan", StudyTime="Nan", InstitutionName="Nan", InstitutionAdress="Nan"):
        
        dc.PatientName = PatientName
        dc.PatientID = PatientID
        dc.PatientBirthDate = PatientBirthDate
        dc.PatientSex = PatientSex
        dc.StudyDate = StudyDate
        dc.StudyTime = StudyTime
        dc.InstitutionName = InstitutionName
        dc.InstitutionAdress = InstitutionAdress
        
class InformationStudySerie(AbsDicomInformation):    
    def get_information(self, dc: dicom.FileDataset, BodyPartExamined=False, StudyInstanceUID=False, 
                        SeriesInstanceUID=False, StudyDate=False, StudyTime=False, 
                        InstitutionName=False, InstitutionAdress=False) -> dict:
        
        dict_information = dict()
        
        if BodyPartExamined:
            dict_information["BodyPartExamined"] = dc.BodyPartExamined
            # list_information.append(dc.BodyPartExamined)
        if StudyInstanceUID:
            dict_information["StudyInstanceUID"] = dc.StudyInstanceUID
            # list_information.append(dc.StudyInstanceID)
        if SeriesInstanceUID:
            dict_information["SeriesInstanceUID"] = dc.SeriesInstanceUID
            # list_information.append(dc.SeriesInstanceUID)
        if StudyDate:
            dict_information["StudyDate"] = dc.StudyDate
            # list_information.append(dc.StudyDate)
        if StudyTime:
            dict_information["StudyTime"] = dc.StudyTime
            # list_information.append(dc.StudyTime)
        if InstitutionName:
            dict_information["InstitutionName"] = dc.InstitutionName
            # list_information.append(dc.InstitutionName)
        if InstitutionAdress:
            dict_information["InstitutionAdress"] = dc.InstitutionAdress
            # list_information.append(dc.IntitutionAdress)
            
        return dict_information

    def set_information(self, dc: dicom.FileDataset, BodyPartExamined: str, StudyInstanceID: str, SeriesInstanceUID: str, StudyDate: str, StudyTime: str, 
                        InstitutionName: str, InstitutionAdress: str):
        
        
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

class InformationImage(AbsDicomInformation):
    def get_information(self, dc: dicom.FileDataset, Modality=False, ImagePositionPatient=False, ImageOrientationPatient=False, 
                        InstanceNumber=False, PixelSpacing=False, SliceThickness=False, Rows=False, Columns=False,  
                        WindowCenter=False, WindowWidth=False, RescaleIntercept=False, RescaleSlope=False) -> dict:  
        
        dict_information = dict()
        if Modality:
            dict_information["Modality"] = dc.Modality
            # list_information.append(dc.Modality)
        if ImagePositionPatient:
            dict_information["ImagePositionPatient"] = dc.ImagePositionPatient
            # list_information.append(dc.ImagePositionPatient)
        if ImageOrientationPatient:
            dict_information["ImageOrientationPatient"] = dc.ImageOrientationPatient
            # list_information.append(dc.ImageOrientationPatient)
        if InstanceNumber:
            dict_information["InstanceNumber"] = dc.InstanceNumber
            # list_information.append(dc.InstanceNumber)
        if PixelSpacing:
            dict_information["PixelSpacing"] = dc.PixelSpacing
            # list_information.append(dc.PixelSpacing)
        if SliceThickness:
            dict_information["SliceThickness"] = dc.SliceThickness
            # list_information.append(dc.SliceThickness)
        if Rows:    
            dict_information["Rows"] = dc.Rows
        if Columns:
            dict_information["Columns"] = dc.Columns
        if WindowCenter:
            dict_information["WindowCenter"] = dc.WindowCenter
            # list_information.append(dc.WindowCenter)
        if WindowWidth:
            dict_information["WindowWidth"] = dc.WindowWidth
            # list_information.append(dc.WindowWidth)
        if RescaleIntercept:
            dict_information["RescaleIntercept"] = dc.RescaleIntercept
            # list_information.append(dc.RescaleIntercept)
        if RescaleSlope:
            dict_information["RescaleSlope"] = dc.RescaleSlope
            # list_information.append(dc.RescaleSlope)
        
        return dict_information

    def set_information(self, dc: dicom.FileDataset, Modality: str, ImagePositionPatient: str, ImageOrientationPatient: str, 
                        PixelSpacing: str, SliceThickness: str, SpacingBetweenSlices: str, 
                        WindowCenter: str, WindowWidth: str, RescaleIntercept: str, RescaleSlope: str):
        
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
