
import pymysql.cursors
def retornar_pedidos():
	# Abrimos uma conexão com o banco de dados:
	conexao = pymysql.connect(host='sql10.freemysqlhosting.net', db='sql10348793', user='sql10348793', passwd='NRqVZeAfi7')
	 
	# Cria um cursor:
	cursor = conexao.cursor()
	 
	sql = "SHOW COLUMNS FROM Camisas" 
	sql_padrao = "SELECT count(*) FROM Camisas"

	# Executa o comando:
	cursor.execute(sql_padrao)
	 
	# Recupera o resultado:
	resultado = cursor.fetchall()
	 
	# Mostra o resultado:
	print('Resultado ')
	 
	for linha in resultado :
	    print(linha[0])
	 
	# Finaliza a conexão
	conexao.close()

	return linha
