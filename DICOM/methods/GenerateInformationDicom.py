import pydicom as dicom
import numpy as np

from typing import List, Dict 
from PyQt5.QtGui import QPixmap

from services.DicomExtract import DicomExtract
from services.InformationDicom import InformationPatient, InformationStudySerie, InformationImage
from core.classes.DicomMatrix import DicomMatrix
from utils.Pixmap import Pixmap

class GenerateInformation():
	def __init__(self):
		self.create_objects()

	def create_objects(self) -> None:
        self.obj_dicom_extract = DicomExtract()
        self.obj_dicom_matrix = DicomMatrix()
        self.obj_pixmap = Pixmap()
        
        self.obj_info_patient = InformationPatient()
        self.obj_info_study_serie = InformationStudySerie()
        self.obj_info_image = InformationImage()
    
    """
    El método "create_objects" de la clase Ui_subviewDicomController
    tiene por finalidad generar instancias de otras clases que son necesarias para el funcionamiento de la subinterfaz
    
    - Instancias:
        - self.obj_dicom_extract (DicomExtract) : Instancia de la clase DicomExtract, encargada de encapsular la lógica del
                                                    procesamiento inicial de los dicom.
        
        - self.obj_dicom_matrix (DicomMatrix)   : Instancia de la clase DicomMatrix, encargada de encapsular la lógica para
                                                    la creación de la matriz tridimensional de los dicom
        
        - self.obj_pixmap (Pixmap)              : Instancia de la clase Pixmap, encargada de encapsular la lógica para
                                                    crear un elemento Pixmap utilizable.
    """    
	def generate_dicoms_matrix3D(self, path: Union[str, List]) -> tuple[List, np.array]:
        dicoms_utilities = self.obj_dicom_extract.extract_dicoms(path)
        matrix_dicom = self.obj_dicom_matrix.generate_matrix(self.dicoms_utilities)
        
        return dicoms_utilities, matrix_dicom

    def generate_matrix2D(self, ):
        pass
        
    def generate_pixmap(self, matrix_2d: np.array) -> QPixmap:
        pixmap = self.obj_pixmap.create_pixmap(matrix_2d)

        return pixmap

    def generate_information_dicom(self, dicom_item: dicom.FileDataset) -> tuple[Dict, Dict]:
        dict_info_patient = self.obj_info_patient.get_information(dicom_item,
                                                            PatientName=True, PatientID=True, 
                                                            PatientBirthDate=True, PatientSex=True)
        dict_info_study = self.obj_info_study_serie.get_information(dicom_item,
                                                                   BodyPartExamined=True, StudyInstanceID=True, 
                                                                   StudyDate=True, StudyTime=True, InstitutionName=True)
		# self.dict_info_image = self.obj_info_image.get_information(self.dicoms_utilities[0], InstanceNumber=True, Rows=True, Columns=True)
        #Comentamos esta variable debido a que no se utiliza

        return dict_info_patient, dict_info_study