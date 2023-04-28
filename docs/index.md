<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="30%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="40%"></a>
</td>
</tr>
</table>

# Sumário

- [Sumário](#sumário)
- [1. Entendimento de negócio](#1-entendimento-de-negócio)
  - [1.1. Análise setorial](#11-análise-setorial)
  - [1.2. Análise empresarial](#12-análise-empresarial)
  - [1.3. Análise do time de desenvolvimento](#13-análise-do-time-de-desenvolvimento)
  - [1.4. Análise da solução](#14-análise-da-solução)
- [2. Entendimento do metadesign](#2-entendimento-do-metadesign)
  - [2.1. Fatores mercadológicos](#21-fatores-mercadológicos)
    - [Relação entre o produto desenvolvido e sua precificação com o merdaco atual](#relação-entre-o-produto-desenvolvido-e-sua-precificação-com-o-merdaco-atual)
    - [Precificação](#precificação)
  - [2.2. Sistema produto/design](#22-sistema-produtodesign)
    - [Missão do projeto proposto](#missão-do-projeto-proposto)
    - [Unidade formal entre design, divulgação e venda](#unidade-formal-entre-design-divulgação-e-venda)
  - [2.3. Sustentabilidade ambiental](#23-sustentabilidade-ambiental)
  - [2.4. Influências socioculturais](#24-influências-socioculturais)
  - [2.5. Tipológico-formais e ergonômicos](#25-tipológico-formais-e-ergonômicos)
  - [2.6. Tecnologia produtiva e materiais empregados](#26-tecnologia-produtiva-e-materiais-empregados)
- [3. Arquitetura do sistema](#3-arquitetura-do-sistema)
  - [3.1 Engenharia de requisitos](#31-engenharia-de-requisitos)
    - [Requisitos Funcionais](#requisitos-funcionais)
    - [Requisitos Não Funcionais](#requisitos-não-funcionais)
- [4. Sistema de locomoção e otimização de rota](#4-sistema-de-locomoção-e-otimização-de-rota)
- [5. Interface de usuário](#5-interface-de-usuário)
- [6. Sistema de visão computacional](#6-sistema-de-visão-computacional)
- [7. Sistemas de segurança](#7-sistemas-de-segurança)
- [8. Backend](#8-backend)
- [9. Integração de sistemas](#9-integração-de-sistemas)
- [10. Validação da eficácia do sistema](#10-validação-da-eficácia-do-sistema)
- [11. Referências](#11-referências)
- [12. Material de apoio](#12-material-de-apoio)
- [13. Anexos](#13-anexos)

# 1. Entendimento de negócio

## 1.1. Análise setorial

(Oceano azul)

## 1.2. Análise empresarial

(Matriz SWOT)

## 1.3. Análise do time de desenvolvimento

(Matriz de riscos)

## 1.4. Análise da solução

<p align="center"><img src="media\proposta_de_valor.png" width="60%"></p>
Nossa proposta de valor consiste em uma solução que contempla os seguintes serviços: 
<ul>
  <li> Simulação do trajeto de um robô seguidor e seus dados de sensores para medição atmosférica</li>
  <li> Interface gráfica com um dashboard interativo para os dados captados </li>
  <li> Protótipo de robô seguidor focado no funcionamento dos sensores </li>
</ul>
Essa solução consegue mitigar as principais dores do cliente: a segurança do operador que realiza a manutenção e a dificuldade em avaliar se há riscos ao colaborador sem entrar no ambiente confinado. Essas dores são sanadas graças aos sensores que identificam a presença e a quantidade de componentes gasosos tóxicos, inflamáveis e seu nível de perigo no local; além do fato de que o protótipo verificará o ambiente primeiro, perdendo a necessidade de um colaborador se arriscar dentro dos ambientes confinados.

Outrossim, há uma interface gráfica que tem como objetivo ajudar no planejamento para as inspeções e manutenções desses ambientes confinados. Essa interface gráfica possuirá dashboards que se atualizam em tempo real e, também, fotos do interior do ambiente confinado que serão captadas pela câmera que o protótipo está equipado.

# 2. Entendimento do metadesign

## 2.1. Fatores mercadológicos

#### Relação entre o produto desenvolvido e sua precificação com o merdaco atual

O produto será desenvolvido com a principal função de simular virtualmente a movimentação de um robô que, por sua vez, irá estar em um espaço confinado com objetivo primordial de captar informações sobre o ambiente atmosférico especificado na planta disponibilizada pela Gerdau. Após a simulação consolidada, haverá uma demonstração com um robô de forma física, que irá avaliar o local ao seu entorno, tendo a possibilidade de selecionar pontos específicos com intervalos de distâncias reguláveis. Ademais, os dados atmosféricos coletados pelos sensores estão relacionados principalmente à taxa de oxigênio local, pressão atmosférica, velocidade da ventilação para a remoção de compostos contaminantes, entre outros itens gasosos.

Em um conceito macro do projeto, é possível perceber que seu processo de desenvolvimento será pautado na segurança e na confiabilidade dos sensores usados na sua implementação. Portanto, o robô em sua versão final será capaz de se mover de maneira autônoma, voltando para seu ponto de origem caso aconteça alguma falha, utilizando filmagens para acrescentar na inspeção que será feita. Diante desse cenário, a comercialização dentro desse setor na robótica acontece com custos elevados, dado a quantidade de requisitos e a possibilidade de customização do projeto.

#### Precificação

O processo de precificação acontece com o objetivo primordial de levantar os dados sobre os serviços necessários para a implementação da solução, de modo que, seja visível os materiais utilizados, uma estimativa mais realista possível do tempo que será preciso para o protótipo ser consolidado. Doravante e além desses parâmetros, é imprescindível nesta etapa a contribuição da equipe de desenvolvimento para explicar ao parceiro os principais benefícios dos componentes e como eles se relacionam com os requisitos, para assim, ser alcançado um excelente padrão de qualidade dentro do alinhamento de expectativas realizado na conversa com o colaborador empresarial em questão, especialmente os representantes do setor industrial e automotivo da Gerdau.

No total iram ser 10 semanas, mudando gradativamente o processo de simulação feita ROS2 para o ambiente de demonstração física utilizando o robô TurtleBot 3 Burger que está custando atualmente 3.279 reais, para as medições vamos implementar na solução os seguintes sensores: o MQ-135, usado para mensurar a taxa de gases tóxicos e está custando em média 20 reais, o Bme-280, que tem como principal função a medição de temperatura, umidade e pressão atmosférica, hoje está sendo comercializado por 40 reais, e para a inspeção do ambiente vamos usar no robô a câmera para Raspberry, estimado no valor de 70 reais. Com isso, o custo total dos nossos principais componentes para o desenvolvimento do projeto, será de 3.409 reais.

## 2.2. Sistema produto/design

#### Missão do projeto proposto

O propósito do projeto elaborado para a Gerdau relaciona-se à crescente atenção da empresa aos aspectos de segurança que envolvem seus funcionários e colaboradores. Sabendo-se que um desejo da instituição é evitar a exposição ao risco nos espaços confinados com os quais a Gerdau trabalha, evidencia-se o desafio de projetar uma solução capaz de informar, de maneira precisa, as condições atmosféricas do espaço a ser inspecionado. A missão do projeto está diretamente relacionada à visão institucional da Gerdau, que tem como princípios a valorização da segurança e inovação.

#### Unidade formal entre design, divulgação e venda

A princípio, será concebida uma simulação virtual do veículo autônomo guiado atuando sobre um espaço confinado genérico. Desse modo, será possível estudar a viabilidade da construção de um protótipo físico que atenda aos requisitos da empresa. É ideal que o protótipo seja capaz de reproduzir os resultados obtidos por meio da simulação. Além disso, é de fundamental importância que o protótipo seja escalável — requisito imperativo para a implementação do produto por parte do cliente. O produto desenvolvido, portanto, será apresentado ao mercado como ferramenta de apoio à manutenção da segurança do trabalho, cumprindo o papel de inspecionar de forma eficaz os ambientes confinados que ofereçam potenciais riscos em casos de intervenção humana. Espera-se tornar evidente a qualidade do produto por meio de demonstrações de seu funcionamento, desde sua configuração no ambiente industrial em que será utilizado até a geração do relatório referente à inspeção feita. Os diferenciais da solução, como a possibilidade de análise de imagens computacionais e controle do veículo via interface, também serão destacados. Será imprescindível, por fim, tratar de maneira transparente o processo de produção do veículo, evidenciando os aspectos que funcionam e os pontos de melhoria para implementação futura.

## 2.3. Sustentabilidade ambiental

## 2.4. Influências socioculturais

## 2.5. Tipológico-formais e ergonômicos

## 2.6. Tecnologia produtiva e materiais empregados

# 3. Arquitetura do sistema

<p align="center"><img src="diagrama_solução.drawio" width="60%"></p>

Atualmente nossa arquitetura pode ser dividia em 2 partes:
A primeira envolve todo o sistema que controla o robo e seus periféricos, esse parte lida com a comunicação entre os componentes e a simulação do robo, essa parte é feita utilizando o ROS2, que é um framework de robótica que permite a comunicação entre os componentes do sistema, além disso ele também permite a simulação do robo, o que facilita o desenvolvimento do sistema, pois não é necessário ter um robo fisico para testar o sistema. A segunda parte é uma solução web que permite a visualização dos dados coletados pelo robo, essa parte é feita utilizando o React, que é um framework de desenvolvimento web, flask que é um framework de desenvolvimento web para python e sqlite.

## 3.1 Engenharia de requisitos

### Requisitos Funcionais

1. Os usuários terão acesso aos dados e às funcionalidades do sistema por meio de uma interface de usuário, que contará com uma simulação do robô e uma aba para o operador fazer sua guiagem.

2. Coleta e armazenagem de dados em área por sensores.

### Requisitos Não Funcionais

    1. Utilizando electron para criar uma aplicação web capaz fornecer dados em tempo real.
    2. Os dados necessários para o sistema serão fornecidos por uma API, utilizando Sqlite.
    3. A simulação será feita com a biblioteca ROS2 e suas ferramentas.
    4. Com o auxílio de uma câmara nosso sistema será capaz de processar e fazer o stream para o controlador do que está acontecendo.
    5. Nosso robô contará com sensores atmosféricos.
    6. Nosso robô fará o envio dos dados coletados para nossa aplicação por meio do ROS2, utilizando o metodo publisher-subscriber.

# 4. Sistema de locomoção e otimização de rota

# 5. Interface de usuário

# 6. Sistema de visão computacional

# 7. Sistemas de segurança

# 8. Backend

# 9. Integração de sistemas

# 10. Validação da eficácia do sistema

# 11. Referências

BRASIL. Ministério do Trabalho e Emprego. Portaria nº 202, de 22 de dezembro de 2006 - **NR33**. Diário Oficial da União, 27 de dezembro de 2006.<br>
MELLO, Pedro. Estratégia do Oceano Azul - 22. DÊGRAU10, 01 ago. 2020. Disponível em: https://degrau10.com.br/estrategia-do-oceano-azul/. Acesso em: 19 abr. 2023.<br>

NR 33. Serviço Nacional de Aprendizagem Rural. Brasília: **Senar**, 2018. Disponível em: https://www.cnabrasil.org.br/assets/arquivos/220-NR33.pdf. Acesso em: 25 abr. 2023.<br>

SAFE. Qual a relação entre segurança do trabalho e a sustentabilidade?. **SAFE**, 15 jun. 2020. Disponível em: https://blog.safesst.com.br/seguranca-do-trabalho-e-sustentabilidade/. Acesso em: 26 abr. 2023.<br>

RIBEIRO, Fran. Morre funcionário da Usiminas hospitalizado após vazamento de gás dentro da empresa. **G1**, 12 dez. 2022. Disponível em: https://g1.globo.com/mg/vales-mg/noticia/2022/12/12/morre-funcionario-da-usiminas-hospitalizado-apos-vazamento-de-gas-dentro-da-empresa.ghtml. Acesso em: 26 abr. 2023.<br>

G1 Sul do Rio e Costa Verde. Funcionário morre em acidente de trabalho na CSN, em Volta Redonda. **G1**, 27 mar. 2023. Disponível em: https://g1.globo.com/rj/sul-do-rio-costa-verde/noticia/2023/03/27/funcionario-morre-em-acidente-de-trabalho-na-csn-em-volta-redonda.ghtml. Acesso em: 26 abr. 2023.<br>

RODRIGUES, Fania. Operários denunciam aumento de acidentes de trabalho na CSN. **Brasil de Fato**, 09 nov. 2016. Disponível em: https://www.brasildefato.com.br/2016/11/09/operarios-denunciam-aumento-de-acidentes-de-trabalho-na-csn-em-volta-redonda/. Acesso em: 26 abr. 2023.

# 12. Material de apoio

https://www.robotis.us/turtlebot-3-burger-us/
https://www.arducore.com.br/modulo-sensor-de-gas-amonia-mq-135-mq-135-arduino-pic?utm_[…]emsUyRupLv3cH6KkyQNeWCK8ZT5kR232Obgy_JhbGMYNIBoCtvUQAvD_BwE
https://produto.mercadolivre.com.br/MLB-3389876702-bme280-modulo-sensor-de-presso-umidade-[…]Rlb8L5vxx2GtEwmO16FrFjN6fAUqAICrxO5YPVuPjRoCTDMQAvD_BwE
https://www.robocore.net/acessorios-raspberry-pi/camera-para-raspberry-pi-rev-1-3?gcl[…]ylU27O2mcY2VCdnCc8crxZjaG2UlU2uJwvVlelRYsTp56dxoCRKwQAvD_BwE
https://www.glassdoor.com.br/Sal%C3%A1rios/engenheiro-de-controle-e-automa%C3%A7%C3%A3o-sal%C3%A1rio-SRCH_KO0,34.htm

# 13. Anexos
