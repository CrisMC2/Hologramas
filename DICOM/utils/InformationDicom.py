import pydicom as dicom

from DICOM.core.abstracts.AbsDicomInformation import AbsDicomInformation, AbsDicomAnonimize

class InformationPatient(AbsDicomInformation, AbsDicomAnonimize):
    def get_information(self, dc: dicom, PatientName=False, PatientID=False, PatientBirthDate=False, PatientSex=False):
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
    
    def set_information(self, dc: dicom, PatientName: str, PatientID: str, PatientBirthDate: str, PatientSex: str):
        if PatientName:
            dc.PatientName = PatientName
        if PatientID:
            dc.PatientID = PatientID
        if PatientBirthDate:
            dc.PatientBirthDate = PatientBirthDate
        if PatientSex:
            dc.PatientSex = PatientSex
        
        
    def anonymize_dicom(self, dc: dicom, PatientName="Desconocido", PatientID="NAn", PatientBirthDate="NAn", PatientSex="Nan", 
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
    def get_information(self, dc: dicom, BodyPartExamined=False, StudyInstanceID=False, SeriesInstanceUID=False, StudyDate=False, StudyTime=False, 
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

    def set_information(self, dc: dicom, BodyPartExamined: str, StudyInstanceID: str, SeriesInstanceUID: str, StudyDate: str, StudyTime: str, 
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
    def get_information(self, dc: dicom, Modality=False, ImagePositionPatient=False, ImageOrientationPatient=False, InstanceNumber=False,
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

    def set_information(self, dc: dicom, Modality: str, ImagePositionPatient: str, ImageOrientationPatient: str, 
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
