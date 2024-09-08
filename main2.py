import os
import webbrowser
import asyncio
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets  import QWebEngineView
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application
import os,django
import pyautogui

# RUNSERVER
async def runserver():
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(BASE_DIR)
    path = r"C:\Users\yathrib travel\Desktop\GitHub\Djangotasks"
    os.chdir(path)
    os.system("py manage.py runserver")

# OPEN BROWSER
def openproject():
    # webbrowser.open_new_tab("http://127.0.0.1:8000/")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path=os.path.join(BASE_DIR,"Djangotasks" )
    # print(path)
    sys.path.append(path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Main.settings")
    django.setup()


    app = QApplication(sys.argv)
    window = QMainWindow()
    view = QWebEngineView()

    application = get_wsgi_application()


    # call_command('runserver',  '127.0.0.1:8000')

    view.load(QUrl('http://localhost:8000/')) #Load the Django URL
    window.setCentralWidget(view)
    window.show()

    sys.exit(app.exec_())
    os.system("py manage.py runserver")


# EXECUTE PROGRAM
async def main():
    # task1 = asyncio.create_task(runserver())
    openproject()
    # await task1



asyncio.run(main())