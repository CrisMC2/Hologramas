import pydicom as dicom
import numpy as np

#Procesado de la imagen dicom  
class DicomProccessing():
    """
    - El método procesa el archivo dicom en una escala según la visualización que se desea alcanzar.
    
    El método empieza limitando el arreglo por medio de numpy.clip.
    Seguidamente generamos una nueva matriz en base a numpy.uint8;
    
    
    Parámetros:
        - self (DicomProcessing_) : Una instancia de la clase DicomProccessing_.
        - file_dicom (pydicom o array)    : Instancia de la clase pydicom  
        - hounsmin (int)          : Valor mínimo en la escala de houns que se visualizará.
        - hounsmax (int)          : Valor máximo en la escala de houns que se visualizará.
    
    Defecto:
        - hounsmin (int)          : -200
        - hounsmax (int)          :  200 
        
    Retonar:
        dc (array)                : Array procesado a partir del pixel_array del archivo pydicom.
        
    """
    def processing_dicom(self, file_dicom, hounsmin=-200, hounsmax=200):
        if isinstance(file_dicom, dicom): #Si es instancia de pydicom
            array_dicom = file_dicom.pixel_array
        elif isinstance(file_dicom, np.ndarray): #Si es un arreglo de numpy
            array_dicom = file_dicom
            
        dc = np.clip(array_dicom, hounsmin, hounsmax)
        
        range_houns = dc.max() - dc.min()
        if (range_houns == 0): #Verificamos que el rango no sea 0
            return TypeError("El rango de houns no es correcto (Rango de valores min y max del array igual a 0)")
        
        dc = np.uint8((dc-dc.min())/(range_houns)*255) #Si range_houns es 0 habrá una excepción
        
        return dc
    
class AbsDicomOrder():
    def order_dicom_folder(self, list_dicoms: list, reverse=False):
        try:
                #De esta manera solo modifica la lista en el lugar y retorna null
            # return list_dicoms.sort(key=lambda x: x.InstanceNumber, reverse=reverse)
            
            #Para hacer que funcione o bien aplicamos sorted (lista, key=)
                #O bien aplicamos sort y luego retornamos
            
            list_dicoms.sort(key=lambda x: x.InstanceNumber, reverse=reverse)
            return list_dicoms
        except:
            print(f"No se pudo ordenar la lista que proporcionaste: \n{list_dicoms}.")
            return None   
    
    """
    El siguiente método permite ordenar una lista de archivos pydicom.
    
    - El método utiliza el elemento x.InstanceNumber para ordenar
    - El elemento utilizado es el número de instancia debido a que representa el orden en el que las imágenes fueron tomadas.
    - El método permite determinar si se desea ordenar de manera normal o en reversa.
    
    Parámetros: 
        - self (AbsDicomOrder_)         : Instancia de la clase AbsDicomOrder_
        - list_dicoms (List<pydicom>)   : Lista de archivos de la clase pydicom
        - reverse (bool)                : True  => para ordenar los elementos en el orden normal (ascendente)
                                          False => para ordenar los elementos en reversa (descendente)

    Defecto:
        - reverse (bool)                : False
        
    Retorno:
        - list_dicoms (List<pydicom>)   : La misma lista de elementos dicom, pero ya ordenados en base a su InstanceNumber.
        
    """