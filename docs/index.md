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
  - [1.3 Análise financeira](#13-análise-financeira)
  - [1.4. Análise do time de desenvolvimento](#14-análise-do-time-de-desenvolvimento)
    - [Matriz de riscos](#matriz-de-riscos)
  - [1.5. Análise da solução](#15-análise-da-solução)
- [2. Entendimento do metadesign](#2-entendimento-do-metadesign)
  - [2.1. Fatores mercadológicos](#21-fatores-mercadológicos)
    - [Relação entre o produto desenvolvido e sua precificação com o merdaco atual](#relação-entre-o-produto-desenvolvido-e-sua-precificação-com-o-merdaco-atual)
    - [Precificação](#precificação)
    - [Cenário do mercado.](#cenário-do-mercado)
  - [2.2. Sistema produto/design](#22-sistema-produtodesign)
    - [Missão do projeto proposto](#missão-do-projeto-proposto)
    - [Unidade formal entre design, divulgação e venda](#unidade-formal-entre-design-divulgação-e-venda)
  - [2.3. Sustentabilidade ambiental](#23-sustentabilidade-ambiental)
    - [Ecoeficiência ambiental proposta pelo projeto](#ecoeficiência-ambiental-proposta-pelo-projeto)
  - [2.4. Influências socioculturais](#24-influências-socioculturais)
  - [2.5. Tipológico-formais e ergonômicos](#25-tipológico-formais-e-ergonômicos)
  - [2.6. Tecnologia produtiva e materiais empregados](#26-tecnologia-produtiva-e-materiais-empregados)
  - [2.7. Entendimento da experiência do usuário](#27-entendimento-da-experiência-do-usuário)
    - [Persona](#persona)
    - [User Story](#user-story)
- [3. Arquitetura do sistema](#3-arquitetura-do-sistema)
  - [V1](#v1)
  - [V2](#v2)
  - [3.1 Engenharia de requisitos](#31-engenharia-de-requisitos)
    - [Requisitos Funcionais](#requisitos-funcionais)
    - [Requisitos Não Funcionais](#requisitos-não-funcionais)
  - [3.2 Viabilidade](#32-viabilidade)
- [4. Sistema de locomoção e otimização de rota](#4-sistema-de-locomoção-e-otimização-de-rota)
- [5. Interface de usuário](#5-interface-de-usuário)
  - [5.1. Visão geral do design](#51-visão-geral-do-design)
    - [Palheta de cores](#palheta-de-cores)
    - [Tipografia](#tipografia)
    - [Ícones](#ícones)
  - [5.2. Telas](#52-telas)
    - [Tela inicial](#tela-inicial)
    - [Tela principal](#tela-principal)
    - [Setup](#setup)
    - [Criar](#criar)
    - [Editar](#editar)
    - [Rodando](#rodando)
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

<p>Inicialmente, a empresa enfrentava desafios em relação à segurança, com riscos para a saúde e segurança de seus colaboradores. Sem a nossa solução, a Gerdau teria que continuar a lidar com os riscos e consequências negativas, como afastamentos, lesões, doenças, entre outros fatores que infelizmente estão sujeitos.</p>
<p>Nossa solução é uma forma de reduzir os riscos e garantir a segurança dos funcionários em espaços confinados. Isso envolve a implementação de novas tecnologias. Com a proposta da Safe McQueen, a Gerdau pode agora evitar riscos potenciais à saúde e ao bem-estar de seus funcionários. Por isso, nossa Matriz Oceano Azul é uma relação de fatores da empresa Gerdau atual, e a perspectiva após a solução implementada.</P>

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Grupo02/blob/main/media/artefatos_negocios/matriz_oceano_azul-1.png" width="60%"></p>
<ul>
  <li><b>Reduzir</b></li>
  Inovação: Reduzir a necessidade de equipamentos ou processos obsoletos no processo.<br>
  Segurança: Reduzir riscos e situações de perigo que os colaboradores enfrentam 
  
  <li><b>Eliminar</b></li>
  Sustentabilidade: Eliminar o uso de materiais prejudiciais ao meio ambiente na solução, utilizando materiais sustentáveis e com baixo impacto ambiental.
  
  <li><b>Aumentar</b></li>
  Tecnologia: Oferecer uma solução com tecnologia de ponta que facilite o trabalho dos funcionários.<br>
  Segurança: Aumentar a eficiência da solução no que se refere à segurança dos funcionários em espaços confinados.<br>
  Custos: Pode haver um aumento no custo inicial de implementação, porém, a longo prazo, a empresa terá redução de riscos e pode trazer benefícios para a imagem da empresa e, consequentemente, suas receitas.<br>
  Qualidade: A qualidade do serviço pode não aumentar. Todavia, a qualidade da experiência do funcionário pode ser aumentada, já que eles terão mais confiança e segurança em seu trabalho.
  
  
  <li><b>Criar</b></li>
  Perenidade: Criar uma solução que seja durável e de fácil manutenção.<br>
  Conforto: Criar um ambiente de trabalho mais confortável para os funcionários que precisam trabalhar em espaços confinados. Já que a segurança em ambientes confinados pode ser uma fonte de estresse e desconforto. Além de demonstrar a preocupação da empresa quanto a saúde deles.<br>
  Tecnologia: Com esse protótipo inicial é possível criar tecnologias mais avançadas; sistemas de monitoramento, sensores, até realidade virtual, o que pode ser visto como um diferencial tecnológico em relação à concorrência
</ul>

## 1.2. Análise empresarial

(Matriz SWOT)

## 1.3 Análise financeira

A análise financeira de um projeto visa mostrar a um parceiro de negócios que sua implementação é viável do ponto de vista financeiro, complementando a precificação. Nesse contexto, a mitigação do risco de acidentes no ambiente de trabalho foi considerada a forma de viabilizar o projeto. Com isso, os funcionários estariam mais protegidos em relação à entrada em ambientes confinados, o que reduziria o risco de acidentes e, consequentemente, os custos associados, como despesas médicas, indenizações, reparação de danos e perda de produtividade. Além disso, os custos indiretos, como danos à reputação e perda de negócios, também seriam minimizados.
Os acidentes no ambiente de trabalho não geram apenas custos financeiros diretos e indiretos, mas também podem ter um impacto negativo na moral e produtividade dos funcionários. Somado ao fato de que os funcionários podem precisar lidar com a interrupção do trabalho enquanto o acidente é investigado e resolvido, o que pode levar à perda de produtividade.
Em contrapartida, a implementação de políticas de segurança eficazes pode ter um impacto positivo na moral e produtividade dos funcionários. Ademais, uma cultura de segurança positiva pode levar a uma maior colaboração e comunicação entre os funcionários, o que pode melhorar a eficiência e a qualidade do trabalho. Portanto, investir em medidas preventivas e políticas de segurança eficazes é uma forma de proteger os funcionários, reduzir os custos associados a acidentes no ambiente de trabalho e melhorar a moral e produtividade da equipe. Dessa forma, é possível garantir a saúde e segurança dos funcionários e evitar custos desnecessários para a empresa, tornando a implementação do projeto financeiramente viável e positiva para todos os envolvidos.
Foi realizada uma pesquisa com o objetivo de coletar informações quantitativas sobre os custos dos acidentes de trabalho, a fim de embasar a abordagem proposta na análise financeira. O grupo teve como prioridade os dados relacionados aos acidentes sofridos pelos funcionários da empresa, incluindo desde casos leves até os mais graves. Além disso, foram levantadas informações sobre as multas decorrentes da emissão de gases durante o processo de fundição do aço, que é a principal atividade realizada pela Gerdau. Com base nas pesquisas realizadas na internet, foi elaborada uma planilha de preços que mostra o custo de alguns acidentes que poderiam ser evitados pela empresa ao adotar soluções preventivas.

<img src="https://github.com/2023M6T2-Inteli/Grupo02/blob/main/media/artefatos_negocios/numeros_analise.jpeg"></img>
fontes: Indenização por acidente de trabalho: valor, requisitos e como receber (2023):
https://mdn.adv.br/indenizacao-por-acidente-de-trabalho/#:~:text=Para%20a%20CLT%2C%20o%20valor,com%20a%20gravidade%20da%20situa%C3%A7%C3%A3o.

Tabelas de Preços de Referência para Cálculo de Multas Ambientais divulgadas pela Companhia Ambiental do Estado de São Paulo (Cetesb) em 2021:
(https://cetesb.sp.gov.br/legislacao-e-normas/).

## 1.4. Análise do time de desenvolvimento

#### Matriz de riscos

Uma matriz de riscos é uma ferramenta utilizada para avaliar e gerenciar os riscos e oportunidades envolvidos em um projeto, atividade ou processo. Ela ajuda a identificar e avaliar os potenciais riscos e a probabilidade de sua ocorrência, bem como o impacto que eles podem exercer sobre o projeto ou atividade. A matriz também pode ajudar a definir a prioridade das ações correspondentes ao gerenciamento do projeto, indicando quais riscos devem ser tratados com maior urgência, por exemplo. Além disso, no projeto em questão, a criação da matriz visa apresentar ao parceiro o que a equipe imagina enfrentar e pensar em conjunto em maneiras de mitigar os riscos, bem como aproveitar as oportunidades existentes.
<img src="https://github.com/2023M6T2-Inteli/Grupo02/blob/main/media/artefatos_negocios/matriz_riscos.png"></img>

## 1.5. Análise da solução

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Grupo02/blob/main/media/artefatos_negocios/proposta_de_valor.png" width="60%"></p>
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

O produto será desenvolvido com a principal função de simular virtualmente a movimentação de um robô que, por sua vez, irá estar em um espaço confinado com objetivo primordial de captar informações sobre o ambiente atmosférico. Atualmente, a Confederação Nacional da Indústria (CNI) realizou um estudo para mapear os principais níveis de automação industrial do Brasil, aproximadamente 19% das indústrias já possuem sistemas integrados de engenharia, aumentando, portanto, sua produtividade e garantindo a segurança humana em trabalhos com altos riscos. Em 2022, foram contabilizados três milhões de robôs operando em indústrias em todo o mundo, ao total foram mais de US$ 13,2 bilhões investidos nos últimos anos para a instalação desses projetos robóticos. Especificamente, com o robô a ser utilizado para a solução descrita acima, não irá ultrapassar US$ 1000, é notório, portanto, que o valor investido não é exageradamente elevado, visto que, hoje tem robôs no mercado que custam mais milhões de dólares.

#### Precificação

O processo de precificação acontece com o objetivo primordial de levantar os dados financeiros sobre os serviços necessários para a implementação da solução, de modo que, seja visível o preço dos materiais utilizados, por exemplo: o modelo do robô, taxa de importação, os sensores atmosféricos a serem utilizados, a câmera, etc , as ferramentas digitais usadas no desenvolvimento do projeto que podem incluir algum gasto, por exemplo: o uso do figma e canva pro , o valor que será necessário para o treinamento dos funcionários para terem uma adaptação melhor com o sistema, e se tiver, acrescentar à soma outros fatores que necessitem investimentos para a implementação da solução ocorrer de maneira qualitativamente satisfatória.

### Cenário do mercado.

A indústria mundial da produção de aço, por séculos, tem se valorizado pela produção de um material resistente e durável, ganhando um importante espaço no avanço da sociedade, permitindo-nos construir pontes, ferrovias, navios e arranha-céus. Com a demanda crescente de aço, o setor consolidou um histórico de aumentos em sua capacidade, volume e valor.
O aço é importante pelas indústrias que fazem seu uso. Ele está presente na construção civil, na industria automobilística, nas forças armadas e em demais setores. O produto processado é usado na criação de diversos produtos do cotiano, como geladeiras, máquinas de lavar, trens e bisturis cirúrgicos.
Há uma preocupação relativa ao aspecto ecológico por parte da indústria, que tem explorado significativamente o conceito de aço verde – alternativa inovadora constituída pela fabricação de aço sem a necessidade do uso de combustíveis fósseis e pelo uso efetivo da sucata de metal. Dentre outras inovações dessa área, destaca-se o aumento da automatização de processos, com o uso de AGVs em tarefas de risco, diminuindo o erro humano em acidentes ecológicos.
O mercado nacional contou com um forte crescimento durante a pandemia de Covid-19, fazendo contra ponto ao setor nesse mesmo período. “Apesar da montanha-russa que foi 2022, foi um bom ano para o setor. Tanto que, em termos de vendas internas, este foi o quarto melhor da década”, resumiu o presidente-executivo do Aço Brasil, Marco Polo de Mello Lopes. Atualmente a área já não está mais em constante crescimento, apresentando um recuo em sua produção, que em fevereiro fechou em 2,5 milhões de toneladas, representando uma queda de 4,9%.

## 2.2. Sistema produto/design

#### Missão do projeto proposto

O propósito do projeto elaborado para a Gerdau relaciona-se à crescente atenção da empresa aos aspectos de segurança que envolvem seus funcionários e colaboradores. Sabendo-se que um desejo da instituição é evitar a exposição ao risco nos espaços confinados com os quais a Gerdau trabalha, evidencia-se o desafio de projetar uma solução capaz de informar, de maneira precisa, as condições atmosféricas do espaço a ser inspecionado. A missão do projeto está diretamente relacionada à visão institucional da Gerdau, que tem como princípios a valorização da segurança e inovação.

#### Unidade formal entre design, divulgação e venda

A princípio, será concebida uma simulação virtual do veículo autônomo guiado atuando sobre um espaço confinado genérico. Desse modo, será possível estudar a viabilidade da construção de um protótipo físico que atenda aos requisitos da empresa. É ideal que o protótipo seja capaz de reproduzir os resultados obtidos por meio da simulação. Além disso, é de fundamental importância que o protótipo seja escalável — requisito imperativo para a implementação do produto por parte do cliente. O produto desenvolvido, portanto, será apresentado ao mercado como ferramenta de apoio à manutenção da segurança do trabalho, cumprindo o papel de inspecionar de forma eficaz os ambientes confinados que ofereçam potenciais riscos em casos de intervenção humana. Espera-se tornar evidente a qualidade do produto por meio de demonstrações de seu funcionamento, desde sua configuração no ambiente industrial em que será utilizado até a geração do relatório referente à inspeção feita. Os diferenciais da solução, como a possibilidade de análise de imagens computacionais e controle do veículo via interface, também serão destacados. Será imprescindível, por fim, tratar de maneira transparente o processo de produção do veículo, evidenciando os aspectos que funcionam e os pontos de melhoria para implementação futura.

## 2.3. Sustentabilidade ambiental

#### Ecoeficiência ambiental proposta pelo projeto

O projeto em parceria com a Gerdau tem como objetivo alcançar a ecoeficiência de forma indireta, evitando impactos ambientais prejudiciais ao entorno da instalação da Gerdau. Uma das soluções propostas é o uso de Veículos Autônomos Guiados (AGVs) para monitorar regularmente as tubulações de gás e prevenir possíveis acidentes que possam contaminar o meio ambiente e afetar a saúde humana. Além disso, o uso de energia elétrica em vez de combustíveis fósseis torna essa solução ainda mais vantajosa para o meio ambiente.

O grupo também propôs uma solução visando ser mais ecoeficiente, que poderia ser aplicada em um projeto com fins lucrativos em parceria com a Gerdau. Em vez de vender diretamente um robô fabricado para o parceiro de negócio, a solução seria oferecer o robô como serviço de assinatura. Dessa forma, o parceiro ainda veria vantagens econômicas em contratar o serviço, já que o manteria sempre atualizado e contaria com o suporte mais assertivo, enquanto o grupo reduziria o uso de recursos naturais ao evitar a compra de mais um robô. Em resumo, o uso de veículos autônomos não apenas contribui para a ecoeficiência e a redução de danos ambientais, mas também torna os procedimentos de inspeção mais eficientes e seguros.

## 2.4. Influências socioculturais

## 2.5. Tipológico-formais e ergonômicos

## 2.6. Tecnologia produtiva e materiais empregados

## 2.7. Entendimento da experiência do usuário

### Persona

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Grupo02/blob/main/media/artefatos_negocios/persona.png" width="60%"></img></p>
A persona foi criada para ajudar a entender as necessidades e os desejos do público alvo para a solução de automação industrial que foi apresentada, ela é um personagem fictício, doravante, com informações reais fornecidas pelos representantes da Gerdau. Nesse caso, especificamente,  Joana é técnica em segurança do trabalho, realiza atividades de alto risco, e, portanto, está sempre com equipamentos de proteção individual, sobretudo, por serem ainda atividades arriscadas, compreende que é um trabalho bastante delicado. Com a implementação da solução em desenvolvimento , Joana teria que aprender a supervisionar o trabalho do robô, deixando para ele concluir a etapa mais perigosa e garantindo que seu desempenho nas demais responsabilidades do processo de inspeção do ambiente confinado estivessem ocorrendo de forma correta.

### User Story

# 3. Arquitetura do sistema

### V1

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Grupo02/blob/main/media/arquitetura_sistema/diagrama_solu%C3%A7%C3%A3ov1.drawio.png?raw=true" width="60%"></img></p>

Atualmente nossa arquitetura pode ser dividia em 2 partes:
A primeira envolve todo o sistema que controla o robo e seus periféricos, esse parte lida com a comunicação entre os componentes e a simulação do robo, essa parte é feita utilizando o ROS2, que é um framework de robótica que permite a comunicação entre os componentes do sistema, além disso ele também permite a simulação do robo, o que facilita o desenvolvimento do sistema, pois não é necessário ter um robo fisico para testar o sistema. A segunda parte é uma solução web que permite a visualização dos dados coletados pelo robo, essa parte é feita utilizando o React, que é um framework de desenvolvimento web, flask que é um framework de desenvolvimento web para python e sqlite.

### V2

<p align="center"><img src="https://github.com/2023M6T2-Inteli/Grupo02/blob/main/media/arquitetura_sistema/diagrama_solu%C3%A7%C3%A3ov2.drawio.png?raw=true" width="60%"></img></p>

Atualizamos nossa arquitetura para levar em conta que o robô não terá acesso a internet de forma constante por isso precisamos de um banco de dados embarcado para armazenar os dados coletados pelo robô, além disso agora o robo só manda dara os dados para o bancos de dados ao final da rota. Além disso estamos considerando usar uma bridge entre o ros2 e a websocket para que o robo possa mandar os dados para a aplicação web.

## 3.1 Engenharia de requisitos

A engenharia de requisitos tem como objetivo promover em frases curtas e objetivas funcionalidades e características específicas do sistema, assim, atendendo as necessidades e expectativas do usuário, cumprir as especificações técnicas, a conformidades com as regulamentações e o padrão de qualidade aplicável em cada etapa do projeto.

### Requisitos Funcionais

Tem como objetivo primordial descrever as principais funcionalidades e características específicas da interação do sistema robótico. Como: a configuração do intervalo de distância entre os pontos de medição, a transmissão das informações para o relatório e o armazenamento dos dados atmosféricos por meio de sensores.

1. Anteriormente ao processo de entrada aos espaços confinados, o robô será configurado para a definição do intervalo de distância entre os pontos da medição.

2. Após a concretização das medições, o robô enviar as informações para o relatório que poderá ser acessado via interface gráfica.

3. O armazenamento de dados atmosféricos referentes aos espaços confinados serão conletados por meio de sensores.

### Requisitos Não Funcionais

Tem como objetivo primordial descrever aspectos mais generalizados, como desempenho na usabilidade e segurança do sistema, não são diretamente relacionados às funcionalidades mas sim à eficiência e eficácia em relação ao usuário final da aplicação. Incluindo: a comunicação entre o robô e o Backend usando a arquitetura publisher/subscriber, a coordenação da simulação e protótipo por meio do sistema ROS2, a capacidade de armazenar arquivos de imagem e vídeo por meio da câmera, o uso de sensores de medição atmosférica e a escolha de tecnologias específicas para o armazenamento de dados não relacionais e a construção do Frontend.

1. Os dados necessários para o sistema serão enviados para o Backend pelo ROS2 usando a arquitetura publisher/subscriber.

2. Tanto a simulação quanto o protótipo serão coordenados por meio do sistema ROS2.

3. Com o auxílio de uma câmera, o sistema será capaz armazenar arquivos de imagens e/ou vídeos.

4. O robô contará com sensores de medição atmosférica, tais como de pressão, de temperatura e de umidade.

5. Será utilizado MongoDB para o armazenamento de dados não relacionais.

6. Será utilizado React para a construção do Frontend.

## 3.2 Viabilidade

Viabilidade Técnica

A viabilidade técnica, refere-se a possibilidade de implementar na prática a solução arquitetada, levando em consideração os recursos técnicos a serem utilizados ao decorrer do tempo necessário para a construção do protótipo final. Nesse sentido, é necessário que o projeto passe por pelas seguintes etapas para garantir sua viabilidade técnica:

1. Identificar as ferramentas digitais necessárias: especificamente no desenvolvimento dessa solução, é primordial o uso das seguintes tecnologias digitais: ROS2 (um conjunto de ferramentas e bibliotecas e nos permitirá integrar todo o sistema operacional para termos um ambiente robótico integrado e fundamentalmente composto pelo o Ubuntu e o TurtleSim) , Ubuntu (utilização da ferramenta que ele oferece para a simulação em 2D de robôs, o TurtleSim), mongoDB (programa de banco de dados orientado a documentos) , React JS (framework para desenvolvimento de front-end) e Gazebo (ferramenta de simulação do 3D para o sistema robótico).

2. Identificar os principais componentes físicos necessários: especificamente no desenvolvimento dessa solução, é primordial o uso dos seguintes componentes eletrônicos: robô TurtleBot 3 Burger, o sensor MQ-135 para mensurar a taxa de gases tóxicos, o sensor Bme-280 que tem como principal função a medição de temperatura, e para ser acoplado no robô a câmera para Raspberry Pi.

3. Alinhamento de conhecimento da equipe desenvolvedora da solução: para um melhor compartilhamento de conteúdo a ser colocado em prática, é necessário a garantia de que o projeto em todas as vertentes esteja em conformidade com o padrão de verificação e regulamentação técnicas viáveis, dado a boa documentação de tudo que for feito, a construção de um manual do usuário bem interativo, a integração do backend ocorrendo de forma correta, o controle da plataforma robótica e o sistema de segurança com a visão computacional sendo executado sem erros no sistema. Para a realização de todos os tópicos anteriores, é primordial um cruzamento de ideias e um bom desenvolvimento profissional da equipe.

4. Mapear possíveis desafios técnicos e proporcionar soluções, por exemplo, caso ocorra falha em algum sensor físico, é necessário um planejamento de um plano B, ter um segundo sensor para usar em casos de substituições.

# 4. Sistema de locomoção e otimização de rota

## 4.1 Sistema de locomoção 

<p> Nosso sistema de locomoção está operando com o sistema de nós do ROS. Esse sistema permite a comunicação entre nosso script em python e o ambiente de simulação Gazebo. </p>

### 4.1.1 Instalação do ambiente de simulação
Para abrir este projeto você necessita das seguintes ferramentas:

#### 4.1.1.1 Ros Humble Turtlebot3
Para instalar esse pacote, abra o terminal do ubuntu e execute:

```sudo apt install ros-humble-turtlebot3*```

Isso instalará todos os pacotes necessários para executar o Gazebo, o ambiente de simulação que utilizamos.
Por fim, execute no terminal do ubuntu para verificar se foi instalado corretamente:

```gazebo```

Em caso de erros, consulte a documentação de instalação do ros2 humble: [Documentação](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).


### 4.1.3 Comunicação 
A comunicação entre a plataforma robótica móvel e o sistema de simulação integrada ao sistema operacional robótico é feita por meio do protocolo TCP/IP, onde os nós definidos em nosso script se comunicam entre os nós do sistema como *subcribers* (que se inscrevem nos tópicos dos nós do sistema para receberem as mensagens que eles enviam) ou *publishers* (que publicam mensagens nos tópicos do sistema para executar comandos no robô, por exemplo).

Por enquanto, usamos os tópicos ```/odom```, para receber a posição atual do robô dentro do ambiente de simulação, e ```/cmd_vel```, para alterar a velocidade linear e angular do robô dentro do ambiente de simulação. Mas faremos uso de outros tópicos para receber as informações dos sensores que estão acoplados ao robô.

Essa interação entre os tópicos está descrita no diagrama de blocos abaixo, onde as setas pontilhadas indicam a direção das mensagens

<img src="../media/arquitetura_sistema/interacao_topicos.png">

# 5. Interface de usuário

## 5.1. Visão geral do design

<p>O sistema de design é uma coleção de elementos e padrões visuais que definem a aparência e a experiência do usuário em todo o projeto. Ele garante consistência e coesão em todas as telas e componentes, promovendo uma experiência de usuário unificada. A seguir, apresentamos os principais elementos do sistema de design:</p>

#### Palheta de cores

<p>A paleta de cores foi selecionada para transmitir a identidade visual da Gerdau. As cores utilizadas são:</p>

<li><b>Cor primária:</b> #004A8F</li>
<li><b>Cor secundária:</b> #F5F5F5</li>
<li><b>Cor de fundo:</b> #DAE2EA</li>
<li><b>Cor do texto (se fundo azul):</b> #FFFFFF</li>
<li><b>Cor do texto (se fundo branco):</b> #004A8F</li>

<p>O objetivo do grupo é utilizar essas cores em todo o projeto para manter a harmonia visual.</p>

#### Tipografia

<p>Acreditamos que seja importante compartilhar a tipografia, afinal ela tem um papel importante na legibilidade. As fontes selecionadas são:</p>

<li><b>Titulo:</b> Inter (Semi Bold, 36) </li>
<li><b>Subtítulo:</b> Inter (Semi Bold, 32) </li>
<li><b>Texto destaque:</b> Inter (Semi Bold, 18)</li>
<li><b>Texto padrão:</b> Inter (Regular, 20) </li>
<li><b>Texto descrição:</b> Inter (Regular, 14)</li>

<p>O objetivo do grupo é utilizar essas fontes em todas as telas para manter a consistência tipográfica.</p>

#### Ícones

<p>Os ícones fornecem representações visuais de elementos ou ações específicas. Utilizamos o plugin "Material Design Icons" para a maioria desse projeto. Alguns ícones relevantes incluem:</p>

<li><b>Ícone de mais:</b> Para adicionar</li>
<li><b>Ícone de lupa:</b> Para pesquisar</li>
<li><b>Ícone de pergaminho:</b> Para setup</li>
<li><b>Ícone de casa:</b> Para página inicial</li>
<li><b>Ícone de lápis:</b> Para editar</li>
<li><b>Ícone de play:</b> Para iniciar</li>
<li><b>Ícone de seta:</b> Para selecionar</li>
<li><b>Ícone de play:</b> Para iniciar</li>
<li><b>Ícone de x:</b> Para sair</li>

<p>Assim como nos tópicos anteriores, o objetivo do grupo é utilizar esses ícones no projeto para manter um padrão e facilitar a experiência do usuário de modo que fique mais intuitivo.</p>

## 5.2. Telas

<p>A seguir, apresentamos uma lista das telas principais do projeto, juntamente com uma breve descrição de suas funcionalidades:</p>

#### Tela inicial

<img src="https://github.com/2023M6T2-Inteli/Safe-McQueen/blob/main/media/interface_usuario/tela_inicial.png"></img>

<p>A tela inicial é a primeira informação que o usuário receberá. Essa é nossa página de boas vindas e após selecionar "iniciar", eles são redirecionados para a tela principal do aplicativo.</p>

#### Tela principal

<img src="https://github.com/2023M6T2-Inteli/Safe-McQueen/blob/main/media/interface_usuario/registros_inspeções_vazio.png">
<p>Essa é nossa tela principal do aplicativo, o histórico de inspeções. No príncipio ela está vazia, mas a intenção é que após o usuário cadastrar e realizar inspeções, aqui será demonstrado as informações, como na imagem abaixo.</p>
<img src="https://github.com/2023M6T2-Inteli/Safe-McQueen/blob/main/media/interface_usuario/registros_inspeções_preenchido.png">
<p>Aqui, os usuários podem checar as informações das inspeções realizadas com sua data e qual rota foi realizada.</p>

#### Setup

<img src="https://github.com/2023M6T2-Inteli/Safe-McQueen/blob/main/media/interface_usuario/setup_vazio.png">
<p>A tela de setup permite que os usuários visualizem e editem suas informações de rota, criem novas rotas ou inicie a inspeção de uma rota. A ideia é que o botão de "Iniciar inspeção" esteja inativo, e somente após selecionar uma rota clicando no ícone de seta ">>" a rota selecionada seja carregada como no exemplo da imagem abaixo</p>
<img src="https://github.com/2023M6T2-Inteli/Safe-McQueen/blob/main/media/interface_usuario/setup_selecionado.png">

#### Criar

<img src="https://github.com/2023M6T2-Inteli/Safe-McQueen/blob/main/media/interface_usuario/modal_crie.png">
<p>Ao clicar no "Adicionar nova rota" uma modal surge para que o usuário envie a planta e crie sua rota.</p>

#### Editar

<img src="https://github.com/2023M6T2-Inteli/Safe-McQueen/blob/main/media/interface_usuario/modal_edite.png">
<p>Ao clicar no lápis para editar uma rota, será aberta essa modal, semelhante a de criar, em que o usuário pode reorganizar a rota, alterar o nome, descrição e a imagem.</p>

#### Rodando

<img src="https://github.com/2023M6T2-Inteli/Safe-McQueen/blob/main/media/interface_usuario/rodando.png">
<p>Essa página é carregada quando a simulação é iniciada. Com informações relevantes para o projeto</p>

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

Mercado de automação e robótica industrial no Brasil
https://www.vdibrasil.com/aumento-no-mercado-de-robotica-e-automacao-em-2022/#:~:text=A%20ind%C3%BAstria%20de%20rob%C3%B3tica%20e,em%2013%25%20no%20%C3%BAltimo%20ano. Acesso em: 30/04/2023

# 12. Material de apoio

https://www.robotis.us/turtlebot-3-burger-us/
https://www.arducore.com.br/modulo-sensor-de-gas-amonia-mq-135-mq-135-arduino-pic?utm_[…]emsUyRupLv3cH6KkyQNeWCK8ZT5kR232Obgy_JhbGMYNIBoCtvUQAvD_BwE
https://produto.mercadolivre.com.br/MLB-3389876702-bme280-modulo-sensor-de-presso-umidade-[…]Rlb8L5vxx2GtEwmO16FrFjN6fAUqAICrxO5YPVuPjRoCTDMQAvD_BwE
https://www.robocore.net/acessorios-raspberry-pi/camera-para-raspberry-pi-rev-1-3?gcl[…]ylU27O2mcY2VCdnCc8crxZjaG2UlU2uJwvVlelRYsTp56dxoCRKwQAvD_BwE
https://www.glassdoor.com.br/Sal%C3%A1rios/engenheiro-de-controle-e-automa%C3%A7%C3%A3o-sal%C3%A1rio-SRCH_KO0,34.htm

# 13. Anexos
