import mysql.connector  # Correção: "input" não é usado para importar módulos

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",   # Correção: Faltava vírgula
    user="root",        # Usuário do MySQL
    password="",        # Senha do MySQL (padrão do XAMPP é vazia)
    database="bd_forms.sql"  # Nome do banco (verifique se existe)
)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Capturar dados do usuário
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ")

# Criar a query SQL usando placeholders (%s) para evitar SQL Injection
sql = "INSERT INTO cadastro (nome, sobrenome, email, senha) VALUES (%s, %s, %s, %s)"
valores = (nome, sobrenome, email, senha)

# Executar a inserção
cursor.execute(sql, valores)

# Confirmar a inserção no banco de dados
conexao.commit()


