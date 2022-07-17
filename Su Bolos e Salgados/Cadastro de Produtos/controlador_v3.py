#v3 - Campos de Texto, rótulos, imagens, botão e função para o botão.

from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PySide2.QtGui import QIcon, QPixmap
import mysql.connector
import sys

#Comunicação com o banco de dados.
banco = mysql.connector.connect(
    #Aqui é necessário inserir as informações de acesso do banco de dados.
    host='localhost',
    user='root',
    passwd="senha",
    database='confeitaria_suzana'
)


#Classe que recebe como parâmetro 'QWidget, que neste caso é uma classe mãe'
class Janela(QWidget):
    def __init__(self):            #"Construtor" da classe, ou seja, este método irá chamar todos os outros métodos
        super().__init__()         #da classe e também

        #Configurações básicas da janela, como título, tamanho, cor
        self.setWindowTitle("Suzana Doces e Salgados")
        self.setGeometry(420, 180, 1080, 720)                #esq, sup, larg e alt
        self.setMinimumWidth(360)
        self.setMinimumHeight(240)
        self.setAutoFillBackground(True)                     #Habilita a troca de cor do fundo da janela
        self.setStyleSheet('background-color: #ffc8c8;')     #Coloca a cor no plano de fundo
        icone = QIcon('cake.png')
        self.setWindowIcon(icone)

        #Coloquei porque não estava conseguindo acessar.
        '''Estava inicalmente em 'montar_formulário()', mas desta forma eu não consegui acessar
        na função 'cadastrar()' porque me retornava um problema com o escopo. Deixo aqui este 
        relato para não esquecer de ajustar posteriormente.
        '''


        #Chamada das demais funções da Classe
        self.inserir_imagem()
        self.montar_formulario()
        self.botao()

    #Informaçoes de Texto da Janela
    def montar_formulario(self):
        #Posições de Referência
        dir_x = 450
        dir_y = 300
        esp = 80

        #Rótulos
        lbl_codigo = QLabel('   Código: ', self)
        lbl_codigo.move(dir_x, dir_y)
        lbl_descricao = QLabel('Descrição: ', self)
        lbl_descricao.move(dir_x, dir_y + esp)
        lbl_preco = QLabel('Preço(R$): ', self)
        lbl_preco.move(dir_x, dir_y + 2*esp)

        #Caixas de Texto
        global caixa_codigo, caixa_descricao, caixa_preco
        caixa_codigo = QLineEdit(self)
        caixa_codigo.move(dir_x + 70, dir_y-2)
        caixa_codigo.setPlaceholderText('cógigo do produto')
        caixa_descricao = QLineEdit(self)
        caixa_descricao.move(dir_x + 70, dir_y + esp - 2)
        caixa_descricao.setPlaceholderText('descrição do produto')
        caixa_preco = QLineEdit(self)
        caixa_preco.move(dir_x + 70, dir_y + 2*esp - 2)
        caixa_preco.setPlaceholderText('preço do produto')

    #Insere as imagens da Janela
    def inserir_imagem(self):
        logo = QIcon('C:/Users/guigs/Documents/Suzana Soares/Logo/Conf_Suzana.png')
        lbl_logo = QLabel('Logo', self)
        pixmap1 = logo.pixmap(275, 275, QIcon.Active)
        lbl_logo.setPixmap(pixmap1)
        lbl_logo.move(430, 0)

    #Define os botões da Janela
    def botao(self):
        botao_cadastrar = QPushButton('Cadastrar', self)
        botao_cadastrar.move(540, 560)
        botao_cadastrar.clicked.connect(self.cadastrar)

    def cadastrar(self):
        codigo = caixa_codigo.text()
        descricao = caixa_descricao.text()
        preco = caixa_preco.text()

        print(f'''O produto foi cadastrado com sucesso!
        =-=-=-=- RESUMO -=-=-=-=
        Código: {codigo}
        Descrição: {descricao}
        Preço(R$): {preco}''')

        cursor = banco.cursor()
        comando_SQL = 'insert into produtos_cadastrados (codigo, descricao, preco) value (%s,%s,%s);'
        dados = (str(codigo), str(descricao), str(preco))
        cursor.execute(comando_SQL, dados)
        banco.commit()

        caixa_codigo.clear()
        caixa_descricao.clear()
        caixa_preco.clear()


def executar():
    interface_grafica = QApplication(sys.argv)

    inst1 = Janela()                         #Cria uma instancia da classe janela
    inst1.show()                             #Etiliza o '.show()' que herdado da classe QWidget(mãe) para abrir a janela
    interface_grafica.exec_()                #manteném a instancia interface gráfica rodando (loop)
    sys.exit(0)                              #possibilita usar o "X" dos Sistema Windowns para fechar a interface gráfica e  interromper o loop


executar()