# desafio_coopersystem
Para executar o projeto com Docker:
Basta rodar o comando docker-compose up no arquivo docker-compose.yml


Uso da API:
localhost:8000/api/products Para ver a lista completa de produtos ou cadastrar um novo
localhost:8000/api/products/<nome_produto  Para filtar um produto especifico pelo nome
localhost:8000/api/v1/orders Para ver a lista completa de pedidos ou cadastrar um novo
localhost:8000/api/v1/orders/<status> Para filtrar os pedidos por status
  
Para testar api via insomnia ou postman é necessário criar um user e criar um token 
comandos para serem executados:
python manage.py createsuperuser
e depois
python manage.py drf_create_token <username> 
para obter o token a ser usado
  
Swagger:
  localhost:8000/docs tem um bug ainda não corrigido e não funciona se a autenticação do rest framework estar ativada
  
  
Test:
Para ver a cobertura dos testes para abrir o arquivo index dentro da pasta htmlcov
