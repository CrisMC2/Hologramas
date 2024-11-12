from abc import ABC, abstractmethod
import pydicom as dicom
import numpy as np
from glob import glob
import os

#Generamos un caso TEMPLATE (la clase es abstracta, pero algunos métodos no)
    #Esto hace que las clases puedan usar por defecto el método proporcionado, o sobreescribirlo si así lo desean
class DicomRead_(ABC):
    def read_dicom(self, path_file):
        try:
            return dicom.dcmread(path_file)
        except:
            print("El archivo no pudo leerse")
            return None
    
#Procesado de la imgen dicom  
class DicomProccessing_(ABC):
    def processing_dicom(self, file_dicom, hounsmin=-200, hounsmax=200):
        dc = np.clip(file_dicom.pixel_array, hounsmin, hounsmax)
        dc = np.uint8((dc-dc.min())/(dc.max()-dc.min())*255)
        
        return dc
        
#TEMPLATE
class DicomExtract_(ABC):
    def extract_dicoms_folder(self, path_folder):
        try:
            list_ = glob(path_folder+"\*.dcm")
            if list_:
                return list_
            else:
                print("La dirección especificada no contiene ningún archivo DICOM")
                return None
        except:
            print("No se pudo extraer los archivos desde la dirección especificada.")
            return None
class DicomConvertdcm_(ABC):
    def __init__(self):
        self.read = DicomRead_()
    def extract_dicoms_paths(self, list_paths):
        list_dicoms = list()
        try:
            for file in list_paths:
                list_dicoms.append(self.read.read_dicom(file))

            return list_dicoms
        except:
            print("No se pudieron leer todos los archivos")
            return None
            
class DicomOrder_(ABC):
    def order_dicom(self, list_dicoms, reverse=False):
        try:
                #De esta manera solo modifica la lista en el lugar y retorna null
            # return list_dicoms.sort(key=lambda x: x.InstanceNumber, reverse=reverse)
            
            #Para hacer que funcione o bien aplicamos sorted (lista, key=)
                #O bien aplicamos sort y luego retornamos
            
            list_dicoms.sort(key=lambda x: x.InstanceNumber, reverse=reverse)
            return list_dicoms
        except:
            print("No se pudo ordenar la lista que proporcionaste")
            return None
        
    
#Toda la información de DICOM
class DicomInformation_ (ABC):
    def __init__(self):
        self.read= DicomRead_()
    
    @abstractmethod
    def get_information(self):
        pass
    
    @abstractmethod
    def set_information(self):
        pass

class DicomAnonimize_(ABC):
    @abstractmethod
    def anonymize_dicom(self):
        pass   
    
###########################################################
#Convertir DICOM a otro formato
class DicomPaths_(ABC):
    def exists_save(self, path_save):
        try:
            if not os.path.exists(path_save):
                os.makedirs(path_save)
                print("Carpeta creada")
                
        except:
            print("La ubicación proporcionada es incorrecta")
    
    def exists_folder(self, path_folder):
        if os.path.exists(path_folder):
            return True
        
        else:
            return False

class DicomConvert_(ABC):
    @abstractmethod
    def convert_dicom(self):
        pass    
    
    @abstractmethod
    def save_convert(self):
        pass
    
    @abstractmethod
    def extract_features(self):
        pass
 
class FeaturesVideo_(ABC):
    @abstractmethod
    def define_shape(self):
        pass
    
    @abstractmethod
    def define_mode(self):
        pass
    
    @abstractmethod
    def define_codec(self):
        pass
    
###########################################################
class DicomViews_(DicomExtract_, DicomProccessing_, DicomOrder_, DicomPaths_, DicomConvertdcm_):
    @abstractmethod
    def create_view(self):
        pass

    @abstractmethod
    def define_aspect(self):
        pass
    
    #Generamos una función de instancia de DicomPaths_
    def exists_folder(self, path_folder):
        try:
            return all(lambda file: os.path.splitext(file)[1]==".dcm" for file in path_folder)
                
        except:
            print("No se puede acceder a los archivos especificados")
            return False
        
    def extract_dicoms_paths_(self, path_files):
        try:
            lista_paths = list(map(lambda file: file if os.path.splitext(file)[1] == ".dcm" else None, path_files))
            lista_paths = [file for file in lista_paths if file is not None]
            
        except:
            print("No se pudo acceder a la dirección especificada")
            return None
        
        #Debemos retornar la función (o una variable a la cual se le haya dado su valor)
            #En caso de no hacerlo Python tomará a esa función y terminará todo el proceso secuencial 
                #(No se ejecutará la función: self.matriz_some_dicoms)
                
        return DicomConvertdcm_.extract_dicoms_paths(self, lista_paths)
        
    def extract_multi_dicoms(self, path_folder):
        #Accedemos a la función de clase de DicomPaths 
        if DicomPaths_.exists_folder(DicomPaths_, path_folder):
            lista_dicoms = self.extract_dicoms_folder(path_folder)
         
            if lista_dicoms:
                lista_dicoms = self.extract_dicoms_paths(lista_dicoms)   
                lista_dicoms = self.order_dicom(lista_dicoms)
                 # print(len(lista_dicoms))
                # shape_array = list(lista_dicoms[0].shape)
                # shape_array.append(len(lista_dicoms))
                # print(shape_array)
                # array_3D = np.zeros(shape_array)

                # for i in range(shape_array[2]):
                #     array_3D[:,:,i] = lista_dicoms[i]
                    
                return lista_dicoms
    
    def extract_some_dicoms(self, path_files):
        if self.exists_folder(path_files):
            lista_dicoms = self.extract_dicoms_paths_(path_files)
            
            if lista_dicoms:
                lista_dicoms = self.order_dicom(lista_dicoms)
            return lista_dicoms
    
    def generate_matriz_dicoms(self, lista_dicoms, hounsmin=-200, hounsmax=200):
        lista_dicoms = list(map(lambda dc: self.processing_dicom(dc, hounsmin, hounsmax), lista_dicoms))
        
        #Shape => (profundidad, filas, columnas)
        lista_dicoms = np.array(lista_dicoms)
        return lista_dicoms             
        
# print(DicomViews_.mro())