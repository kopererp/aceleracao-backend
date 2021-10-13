## Aceleração Koper back-end

- [Projeto](#computer-projeto)
- [Tecnologias](#toolbox-tecnologias)
- [Iniciando o projeto](#gear-iniciando-o-projeto)
  - [Subindo a aplicação](#flight_departure-subindo-a-aplicação)
  - [Monitorando a aplicação](#tv-monitorando-a-aplicacao)
  - [Parando a aplicação](#flight_arrival-parando-a-aplicação)
  - [Executando os testes](#technologist-executando-os-testes)

### :computer: Projeto

Bem vindo ao repositório do projeto, apresentamos abaixo as instruções para que você possa dar andamento as atividades propostas!

_Antes de seguir aqui leia todas as informações disponiveis no quadro do trello._

1. A primeira coisa que você deverá criar é o seu quadro no Trello a partir do nosso [quadro modelo.](https://trello.com/b/Yg0WsaGC/acelera%C3%A7%C3%A3o-dio-backend)
   - As instruções para criar o seu quadro então disponíveis no cartão intitulado **Instruções de uso do Quadro**.
2. Após criar seu quadro, você deve fazer um fork deste repositório.
   - Caso fique com dúvida, siga o [tutorial.](https://www.youtube.com/watch?v=q-QTbNu8Ybc&ab_channel=WillianJustenCursos)
3. Com seu repositório e quadro criados, você deverá fazer sua primeira alteração no projeto.
   - No seu repositório, abra o arquivo README.md e adicione seu nome e link do seu quadro, e depois faça um commit das alterações;
   - No seu quadro, adicione seu nome e o link do seu repositório no cartão intitulado **Informações do candidato**

Agora basta seguir as instruções disponíveis no seu quadro do Trello e executar as tarefas propostas.

Boa sorte!

## :toolbox: Tecnologias

Este projeto utiliza as seguintes tecnologias:

- [Python 3.8](https://www.python.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [mongoengine](http://mongoengine.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Graphene](https://graphene-python.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

Bibliotecas auxiliares:

- [graphene-mongo](https://graphene-mongo.readthedocs.io/en/latest/)
- [graphene-sqlalchemy](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/)

Bibliotecas para os testes:

- [pytest](https://docs.pytest.org/)
- [factoryboy](https://factoryboy.readthedocs.io/)

Bancos de dados:

- [PostgreSQL](https://www.postgresql.org/)
- [MongoDB](https://www.mongodb.com/)

# :building_construction: Estrutura do projeto

```
app/
├── __init__.py
├── main.py (Instância a aplicação)
├── documents.py (Define os documentos do MongoDB)
├── models.py (Define os modelos do PostgreSQL)
├── events.py (Define as ações que são executados na inicialização do sistema)
├── routers (Rotas do projeto e seus endpoints, normalmente implementado em REST)
│   ├── __init__.py
│   └── example.py (Uma rota de exemplo)
├── templates (Define os templates utilizados pelas rotas)
│   └── example.html (Um template utilizando Jinja)
├── schema.py (Define o schema do GraphQL, a Query e Mutation raíz do grafo)
├── settings.py (Define as configurações do projeto e as variáveis de ambiente)
├── types.py (Define os types compartilhados entre os módulos GraphQL)
├── module_example (Um módulo GraphQL)
│   ├── __init__.py
│   ├── mutations.py (Define as mutations relacionadas ao módulo)
│   ├── queries.py (Define as queries relacionadas ao módulo)
│   ├── types.py (Define os types relacionados ao módulo)
│   └── validators.py (Define as validações utilizadas pelas queries e mutations)
```

## :gear: Iniciando o projeto

O ambiente de desenvolvimento é gerenciado através do Docker Compose, para iniciar o projeto você vai precisar realizar os seguinte passos:

- Instalar o [Docker](https://docs.docker.com/get-docker/)
- Realizar o [pós-instalação](https://docs.docker.com/engine/install/linux-postinstall/) caso esteja usando Linux
- Instalar o [Docker Compose](https://docs.docker.com/compose/install/)

### :flight_departure: Subindo a aplicação

```bash
$ docker-compose up -d
```

Após você subir a aplicação você vai ter disponível no seu ambiente um PostgreSQL, um MongoDB e uma aplicação base para você entender a estrutura do projeto. Você pode acessar a aplicação através do [Playground](http://localhost:5000/playground).

### :tv: Monitorando a aplicação

```bash
$ docker-compose logs --tail 100 -f
```

### :flight_arrival: Parando a aplicação

```bash
$ docker-compose stop
```

### :technologist: Executando os testes:

Caso o ambiente esteja up

```bash
$ docker-compose exec api pytest -vv -x -s
```

Caso o ambiente esteja down

```bash
$ docker-compose run api pytest -vv -x -s
```

# :memo: Variáveis de ambiente

Configurações relativas a acesso a recursos e credenciais são armazenadas no projeto utilizando variáveis de ambiente. As variávels de ambiente definem configurações para os diferentes ambientes do projeto (development, staging, production).

| Variável     | Descrição                    | Valor padrão                         |
| ------------ | ---------------------------- | ------------------------------------ |
| MONGO_URI    | URI de conexão ao MongoDB    | "mongodb://mongo/dio"                |
| POSTGRES_URI | URI de conexão ao PostgreSQL | "postgresql://dio:dio@postgres:5432" |
