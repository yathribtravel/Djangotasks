import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from django.core.wsgi import get_wsgi_application
from PyQt5.QtCore import QUrl
# sys.path.append('/path/to/your/django/project')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path=os.path.join(BASE_DIR,"Djangotasks" )
# print(path)
sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Main.settings')
application = get_wsgi_application()

app = QApplication(sys.argv)


window = QMainWindow()
view = QWebEngineView()
view.load(QUrl('http://localhost:8000/')) 
window.setCentralWidget(view)
window.show()

sys.exit(app.exec_())




# pip install pyqt5 django