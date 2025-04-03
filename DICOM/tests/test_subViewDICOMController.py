import sys
import os

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from controllers import subViewDicomController as Ui_SubView

if __name__ == "__main__":
    app = Ui_SubView.QApplication([])
    window = Ui_SubView.Ui_subViewDicomController()
    window.show()
    
    app.exec()