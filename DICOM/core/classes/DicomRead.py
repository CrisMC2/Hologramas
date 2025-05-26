import pydicom as dicom

#Generamos un caso TEMPLATE (la clase es abstracta, pero algunos métodos no)
    #Esto hace que las clases puedan usar por defecto el método proporcionado, o sobreescribirlo si así lo desean

class DicomRead():
    def read_dicom(self, path_file:str) -> dicom.FileDataset | None:
        try:
            return dicom.dcmread(path_file)
        except:
            print("El archivo no pudo leerse")
            return None
                
# print(DicomViews_.mro())