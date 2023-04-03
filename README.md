# Build GW_ENTRADA:
	docker build .

# Build GW_TRATAMENTO:
	docker build .

# Compose
    docker-compose build
    docker-compose up // verbose
    docker-compose up -d // detached

# Para testes utilizar o client.py:
	python client.py

# Descrição

Todas as imagens foram escritas em cima do Linux Alpine, por ser uma distro leve.

O Gateway de Entrada possui um socket que fica disponível para o client, não necessitando
assim que se configure um schedule a cada 20 segundos evitando erros de sincronismo.
O client disconecta do server passando a seguinte mensagem: !DISCONNECT

O Gateway de Tratamento possui um schedule que é executado a cada 20 segundos, ou seja,
a cada 20 segundos ele faz um select, busca os dados pendentes, trata a String e remove o dado pendente.

Cada serviço possui uma classe de wait_for_db, ou seja, enquanto o banco não fica disponível os outros
containers não sobem.

# Caso obtenham um erro de binding de uso da porta 5050 basta executar o seguinte comando:
	sudo netstat -tulpn | grep 5050
	kill -9 num_processo

Em relação às migrações não utilizei nenhum framework... fiz manualmente.
É normal o sistema lançar uma exception caso a base de dados já exista.
Caso não queira ver a exception basta remover o comando de migration do docker-compose

      python db/wait_for_db.py &&
      python db/migration.py && // remover esta linha
      python server.py

# Overview do psycopg2
O driver do banco é compilado em tempo real, resultando assim em mais desempenho, pois o binário
é gerado especificamente para a distro em execução.