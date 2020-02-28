# Rentbrella Job Test

Projeto proposto pela empresa Rentbrella (https://github.com/rentbrella) como desafio técnico para a vaga de Engenheiro de Software Pleno.

O projeto consiste em um emprestimo que pode conter um ou mais cobranças. O valor do emprestimo e da cobrança são apenas demonstrativos.

# Contexto do desafio (https://github.com/rentbrella/vagas/blob/c9a27c860f1e67ded047cd167f83108a621ee965/challenges/backend-pleno.md)

# Instruções

* Implemente o escopo abaixo, conforme os requisitos;
* Se não conseguir atender todo escopo mas quiser participar do processo mesmo assim, siga os próximos passos;
* Crie um repositório privado aqui no GitHub com seu teste;
* Dê acesso ao usuário `thiagohdeplima`;
* No repositório, crie um arquivo nomeado README.md contendo:
  * Uma breve descrição do projeto e como executá-lo;
  * Uma explicação do porque escolheu as ferramentas utilizadas;
  * Seu nome, e-mail e telefone para contato.

# Escopo

Crie o projeto e implementação sistemas que serão responsáveis por gerenciar:

* Empréstimos feitos através das nossas estações;
* As cobranças geradas em razão destes empréstimos.

As cobranças são realizadas de forma assíncrona, independente da resposta da API para o usuário. Um empréstimo pode possuir diversas cobranças.

_Uma vez que este teste não implementa uma aplicação de verdade, podemos considerar como cobrança a mera inserção de um registro de cobrança no banco de dados, relacionando-a com o empréstimo_.

# Requisitos

* Escolha livremente a `stack` desta implementação;
* Justifique suas escolhas no arquivo `README.md`;
* Implemente o sistema com os requisitos acima;
* Crie testes automatizados para sua aplicação.

# Diferenciais

Iremos considerar como diferenciadas aplicações que implementem, além do escopo especificado acima, os seguintes recursos:

* Criação de um container de Docker para a aplicação;
* Criação de um aquivo `docker-compose.yml` para toda stack da aplicação;
* Implemente o escopo usando a arquitetura de microsserviços;
* Comuniquem os microsserviços por meio de brokers como [RabbitMQ](https://www.rabbitmq.com/) ou mesmo [Redis](https://redis.io/topics/pubsub).

# Contato

Nome: Victor Alessander Gomes Rocha

Telefone: (83) 99328-6604

Email: alessander@protonmail.com

# Uso

Como primeira execução: `docker-compose up --build -d` para iniciar construir e inicializar os containers.

A partir da segunda execução: `docker-compose up`

Para derrubar os containers: `docker-compose down`

IPs dos serviços:

> Cobrança: 172.20.0.5:5001

> Emprestimo: 172.20.0.4:5002

> BD: 172.20.0.2:3306

> Redis: 172.20.0.3:6379

> Worker: 172.20.0.7:8080

Espera-se que você tenha o Docker e o docker-compose instalados em sua máquina.

Caso desejar usar o portainer para gerenciar os containers, espera-se que você tenha criado em sua máquina um volume docker chamado `portainer_data`.

Considerando que você já tenha o volume criado, basta dar permissão ao script `startportainer.sh` usando o comando `chmod +x` (caso esteja no MacOS ou Linux) e em seguida executá-lo.


# Sobre as escolhas das tecnologias

Foi usado neste projeto a seguinte stack:

> Flask (Api)

Pela simplicidade, praticidade e necessidade, contendo apenas o necessário para o projeto. Se não fosse por isso, possívelmente seria usado o Django.

> Redis (Broker)

Maior viabilidade no que se trata de documentação contra o RabbitMQ e facilidade no uso com a linguagem Python usando o package `redis`.

> MySQL (Banco de dados)

Semelhança de sintaxe com o SQL Server onde eu tenho dominância (T-SQL), facilitando a interação direta com o banco via terminal, e também por se tratar de uma aplicação de pequeno porte.

