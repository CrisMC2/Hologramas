import os
import sys

_append = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(_append)

from views import subViewDICOM
if __name__ == "__main__":
    app = subViewDICOM.QApplication(sys.argv)
    window = subViewDICOM.Ui_subViewDicom()
    window.show()
    
    sys.exit(app.exec_())