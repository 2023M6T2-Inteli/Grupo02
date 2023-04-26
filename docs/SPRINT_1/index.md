<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

# Conteúdo
- [Manuais](#manuais)
  - [Manual de Implantação](#manual-de-implantação)
  - [Manual do Usuário](#manual-do-usuário)
- [Referências](#referências)

# 1. Entendimento de negócio
## Fatores Mercadológicos
<p align="center"> Relação entre o produto desenvolvido e sua precificação com o merdaco atual </p> 

O produto será desenvolvido com a principal função de simular virtualmente a movimentação de um robô que, por sua vez, irá estar em um espaço confinado com objetivo primordial de captar informações sobre o ambiente atmosférico especificado na planta disponibilizada pela Gerdau. Após a simulação consolidada, haverá uma demonstração com um robô de forma física, que irá avaliar o local ao seu entorno, tendo a possibilidade de selecionar pontos específicos com intervalos de distâncias reguláveis. Ademais, os dados atmosféricos coletados pelos sensores estão relacionados principalmente à taxa de oxigênio local, pressão atmosférica, velocidade da ventilação para a remoção de compostos contaminantes, entre outros itens gasosos.

Em um conceito macro do projeto, é possível perceber que seu processo de desenvolvimento será pautado na segurança e na confiabilidade dos sensores usados na sua implementação. Portanto, o robô em sua versão final será capaz de se mover de maneira autônoma, voltando para seu ponto de origem caso aconteça alguma falha, utilizando filmagens para acrescentar na inspeção que será feita. Diante desse cenário, a comercialização dentro desse setor na robótica acontece com custos elevados, dado a quantidade de requisitos e a possibilidade de customização do projeto.

## 1.1. Análise setorial
(Oceano azul)

## 1.2. Análise empresarial
(Matriz SWOT)

## 1.3. Análise do time de desenvolvimento
(Matriz de Riscos)

## 1.4. Análise da solução
(Proposta de valor)

# 2. Entendimento do metadesign

## 2.1. Fatores mercadológicos

## 2.2. Sistema produto/design

## 2.3. Sustentabilidade ambiental

## 2.4. Influências socioculturais

## 2.5. Tipológico-formais e ergonômicos
## 2.6. Tecnologia produtiva e materiais empregados

# 3. Descrição da arquitetura do sistema.

## 3.1  Engenharia de requisitos
### Requisitos funcionais e não funcionais 
1. Os usuários terão acesso aos dados e às funcionalidades do sistema por meio de uma interface de usuário, que contará com uma cimulação do robô e uma aba para o operador fazer sua guiagem.
    1. Utilizando electron e react para criar uma aplicação web capaz de rodar de forma local.
    2. Os dados necessários para o sistema serão fornecidos por uma API, utilizando MongoDB.
    3. A cimulação será feita com a biblioteca ROS2 e suas ferramentas.
    4. Com o auxílio de uma câmara nosso sistema será capaz de processar e fazer o stream para o controlador do que está acontecendo. 
    
2. Coleta e armazenagem de dados em área por sensores.
    1. Nosso robô contará com sensores atmosféricos e de procimidade.
    2. Nosso robô fará o envio dos dados coletados para nossa aplicação por meio do protocolo HTTP, utilizando WIFI. 
    3. Nosso sistema irá fazer a captura dos dados por meio de um sistema de metrôs.
   

# 4. Sistema de locomoção e otimização de rota.

# 5. Interface de usuário.

# 6. Sistema de visão computacional.

# 7. Sistemas de segurança.

# 8. Backend.

# 9. Integração de sistemas. 

# 10.  Validação da eficácia do sistema. 
