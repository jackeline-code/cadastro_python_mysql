from PyQt5 import  uic,QtWidgets
import mysql.connector

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_bd"
)

def editar_dados():
    global numero_id
    linha = segunda_tela.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro_pessoa")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM cadastro_pessoa WHERE id="+ str(valor_id))
    pessoa = cursor.fetchall()
    tela_editar.show() #tela editar aparece

    tela_editar.lineEdit.setText(str(pessoa[0][0]))
    tela_editar.lineEdit_2.setText(str(pessoa[0][1]))
    tela_editar.lineEdit_3.setText(str(pessoa[0][2]))
    tela_editar.lineEdit_4.setText(str(pessoa[0][3]))
    tela_editar.lineEdit_5.setText(str(pessoa[0][4]))
    tela_editar.lineEdit_6.setText(str(pessoa[0][5]))
    tela_editar.lineEdit_7.setText(str(pessoa[0][6]))
    tela_editar.lineEdit_8.setText(str(pessoa[0][7]))
    tela_editar.lineEdit_9.setText(str(pessoa[0][8]))
    tela_editar.lineEdit_10.setText(str(pessoa[0][9]))
    tela_editar.lineEdit_11.setText(str(pessoa[0][10]))
    numero_id = valor_id


def salvar_valor_editado():
    global numero_id

    # ler dados do lineEdit
    nome = tela_editar.lineEdit_2.text()
    sobrenome = tela_editar.lineEdit_3.text()
    cpf = tela_editar.lineEdit_4.text()
    nacionalidade = tela_editar.lineEdit_5.text()
    cep = tela_editar.lineEdit_6.text()
    estado = tela_editar.lineEdit_7.text()
    cidade = tela_editar.lineEdit_8.text()
    logradouro = tela_editar.lineEdit_9.text()
    email = tela_editar.lineEdit_10.text()
    telefone = tela_editar.lineEdit_11.text()



    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cadastro_pessoa SET nome = '{}', sobrenome = '{}', cpf = '{}', nacionalidade ='{}', cep ={}, estado ='{}', cidade ='{}', logradouro ='{}', email='{}', telefone ={} WHERE id = {}".format(nome,sobrenome,cpf,nacionalidade,cep,estado,cidade,logradouro,email,telefone,numero_id))
    banco.commit()
    #atualizar as janelas
    tela_editar.close()
    segunda_tela.close()
    lista_pessoa()

def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro_pessoa")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cadastro_pessoa WHERE id="+ str(valor_id))


def funcao_principal():
    nome = formulario.lineEdit.text()
    sobrenome = formulario.lineEdit_2.text()
    cpf = formulario.lineEdit_3.text()
    nacionalidade = formulario.lineEdit_4.text()
    cep = formulario.lineEdit_5.text()
    estado = formulario.lineEdit_6.text()
    cidade = formulario.lineEdit_7.text()
    logradouro = formulario.lineEdit_8.text()
    email = formulario.lineEdit_9.text()
    telefone = formulario.lineEdit_10.text()
    
   
    print("Nome:",nome)
    print("Sobrenome:",sobrenome)
    print("CPF:",cpf)
    print("Nacionalidade:",nacionalidade)
    print("CEP:",cep)
    print("Estado:",estado)
    print("Cidade:",cidade)
    print("Logradouro:",logradouro)
    print("Email:",email)
    print("Telefone:",telefone)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO cadastro_pessoa (nome,sobrenome,cpf,nacionalidade,cep,estado,cidade,logradouro,email,telefone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(nome),str(sobrenome),str(cpf),str(nacionalidade),str(cep),str(estado),str(cidade),str(logradouro),str(email),str(telefone))
    cursor.execute(comando_SQL,dados)
    banco.commit()

    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")
    formulario.lineEdit_7.setText("")
    formulario.lineEdit_8.setText("")
    formulario.lineEdit_9.setText("")
    formulario.lineEdit_10.setText("")

def lista_pessoa():
    segunda_tela.show()
    

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cadastro_pessoa"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(11)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 11):
           segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 



    
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar.ui")
tela_editar=uic.loadUi("editar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(lista_pessoa)
segunda_tela.pushButton.clicked.connect(excluir_dados)
tela_editar.pushButton.clicked.connect(salvar_valor_editado)
segunda_tela.pushButton_2.clicked.connect(editar_dados)

formulario.show()
app.exec()