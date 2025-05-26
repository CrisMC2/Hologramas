from PyQt5.QtWidgets import QWidget

def load(path: str):
    with open(path, "r") as file:
        style = file.read()
    
    return style

def apply_style(path: str, element: QWidget):
    style = load(path)
    element.setStyleSheet(style)
    
def apply_style_to_list(path: str, list_elements: list[QWidget]):
    style = load(path)
    
    for ele in list_elements:
        ele.setStyleSheet(style)