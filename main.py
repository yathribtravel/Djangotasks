import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets  import QWebEngineView
from django.core.wsgi import get_wsgi_application
import os,django
# sys.path.append("/path/to/your/django/project")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path=os.path.join(BASE_DIR,"Djangotasks" )
# print(path)
sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Main.settings")
django.setup()




# from django.core.management import execute_from_command_line
# args = ['name', 'runserver', '0.0.0.0:8000']
# execute_from_command_line(args)

application = get_wsgi_application()

app = QApplication(sys.argv)
window = QMainWindow()
view = QWebEngineView()
view.load(QUrl('http://localhost:8000/')) #Load the Django URL
window.setCentralWidget(view)
window.show()
sys.exit(app.exec_())



# python main.py;python manage.py runserver ;  
# python manage.py runserver 0.0.0.0:8000  && python  main.py