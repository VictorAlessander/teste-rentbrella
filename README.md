# Rentbrella Job Test

Projeto proposto pela empresa Rentbrella (https://github.com/rentbrella) como desafio técnico para a vaga de Engenheiro de Software Pleno.

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

> Frontend: 172.20.0.6:3000

> BD: 172.20.0.2:3306

> Redis: 172.20.0.3:6379

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

> React (Frontend)

Escolhido devido a uma maior familiaridade com o framework, mas poderia ter sido o Vue.JS também.
