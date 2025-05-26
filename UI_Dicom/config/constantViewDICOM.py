########################################################
#Búsqueda de archivos
DIRECTORY_SEARCH_DEFAULT = "E:\\UNCP\\SEMILLEROS\\PROYECTO\\PRUEBAS"
"""
DIRECTORY_SEARCH_DEFAULT indica el directorio desde el cual la App 
iniciará al momento de intentar abrir algún archivo DICOM
"""

EXTENTION_DICOM = "*.dcm"
"""
EXTENTION_DICOM indica la extensión del tipo de archivo que buscará la App.

Nota => Es muy importante dejar el asterisco del inicio, caso contrario no funcionará
"""

FILTER_SEARCH            = f"Dicom ({EXTENTION_DICOM})"
"""
FILTER_SEARCH indica el filtro que usará la aplicación para encontrar elementos, este lo combinamos
con EXTENTION_DICOM debido a que será la misma extensión.

Nota => Es importante que ambas constantes funcionen por separado.
"""


KEEP_DIRECTORY_DEFAULT   = False
"""
KEEP_DIRECTORY_DEFAULT configura si el directorio de inicio (DIRECTORY_SEARCH_DEFAULT) será el Path
que se usará durante toda la ejecución de la aplicación, o si caso contrario se utilizará otra variable
que capte la dirección que el usuario está escogiendo a lo largo de la App 
"""

########################################################
#ACCIONES Y MENÚS
VIEWS_DICOM = ["Axial View", "Saggital View", "Coronal View"]
"""
VIEWS_DICOM indica la cantidad de vistas que poseerá la App. 
Por defecto el código funciona para los 3, y la cantidad de acciones y demás está configurada para 3 vistas.

Lo que puedes cambiar aquí, no es la cantidad, sino el texto que se mostrará para cada una de las acciones sin perjudicar
a ninguna parte de la estructura del código.

"""