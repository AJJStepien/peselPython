from PyQt5.QtWidgets import *    
from PyQt5.QtGui import *
from pesel_ui import *      #import gui z pliku pesel_ui

class Pesel(QWidget, Ui_Dialog):    #   główna klasa programu. Dziedziczy po klasie QWidget oraz Ui_Dialog z pesel_ui.py
    def __init__(self, parent=None):    #   konstruktor
        super(Pesel).__init__(parent)   #   odwołanie do konstruktora klasy nadrzędnej
        self.setupUi(self)              #   stworzenie okienka
                        

if __name__ == '__main__':          #   Główna pętla programu. Powoduje, że okienko się wyświetla
    import sys                      #   Import biblioteki sys, która pozwala "rozmawiać" z wejściem od użytkownika
    app = QtWidgets.QApplication(sys.argv) #    Informacja, że program będzie reagował na argumenty przekazane od użytkownika z linii poleceń 
    window = QtWidgets.QDialog()    #   informacja, że okienko będzie klasy QDialog()
    ui = Ui_Dialog()                #   przypiszemy do zmiennej ui informacje zawarte w klasie Ui_Dialog z pesel_ui.py
    ui.setupUi(window)              #   przekazanie, że nasza metoda setupUi z python_ui.py będzie wywoływała okienko "window"
    window.show()                   #   trzeba też powiedzieć, żeby okienko było widoczne
    sys.exit(app.exec_())           #   a tutaj określamy jak zamknąć nasz program


