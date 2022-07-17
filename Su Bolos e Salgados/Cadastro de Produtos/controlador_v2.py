#v2 - Configurando a janela

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon, QPixmap
import sys

class Janela(QWidget):             #Classe que recebe como parâmetro 'QWidget, que neste caso é uma classe mãe'
    def __init__(self):            #Construtor da classe
        super().__init__()         #Acessa o métido construtor da classe mãe

        self.setWindowTitle("Suzana Doces e Salgados")
        self.setGeometry(420, 180, 1080, 720) #esq, sup, larg e alt
        self.setMinimumWidth(360)
        self.setMinimumHeight(240)

        self.setAutoFillBackground(True)                     #Habilita a troca de cor do fundo da janela
        self.setStyleSheet('background-color: #00ffff;')     #Coloca a cor no plano de fundo

        icone = QIcon('cake.png')
        self.setWindowIcon(icone)

interface_grafica = QApplication(sys.argv)

inst1 = Janela()  #Instancia da classe
inst1.show()      #utiliza o '.show()' que vem junto com o pacote QWidget

interface_grafica.exec_() #manteném a instancia interface gráfica rodando (loop)
sys.exit(0)               #possibilita usar o "X" dos Sistema Windowns para fechar a interface gráfica e interromper o
                          #loop
