#v1 - Criando a janela

from PySide2.QtWidgets import QApplication, QWidget
import sys

class Janela(QWidget):             #Classe que recebe como parâmetro 'QWidget, que neste caso é uma classe mãe'
    def __init__(self):            #Construtor da classe
        super().__init__()         #Acessa o métido construtor da classe mãe

interface_grafica = QApplication(sys.argv)

inst1 = Janela()  #Instancia da classe
inst1.show()      #utiliza o '.show()' que vem junto com o pacote QWidget

interface_grafica.exec_() #manteném a instancia interface gráfica rodando (loop)
sys.exit(0)               #possibilita usar o "X" dos Sistema Windowns para fechar a interface gráfica e interromper o
                          #loop

''' Até agora, eu criei duas coisas, uma classe herda os a classe QWidget. Esta classe vai me permitir
escrever na janela e interagir com ela. A segunda, foi uma instancia da classe QApplication. Ela acessa
o sistema Windowns e permite abrir e fechar janelas.'''
