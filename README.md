<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="20%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

# Simulação de robôs para aplicações diversas

## Safe McQueen

## Integrantes: <a href="https://www.linkedin.com/in/alberto-da-rocha-miranda-angrysine/">Alberto Miranda</a>, <a href="https://www.linkedin.com/in/amanda-fontes/">Amanda Fontes</a>, <a href="https://www.linkedin.com/in/antonio-angelo-teixeira-a70b781a7/">Antonio Teixeira</a>, <a href="https://www.linkedin.com/in/jv-oliveira-rodrigues/">Joao Vitor Oliveira</a>, <a href="https://www.linkedin.com/in/lucas-henrique-sales-de-souza/">Lucas Sales</a>,<a href="https://www.linkedin.com/in/tainara-rodrigues-teixeira/">Tainara Teixeira</a>, <a href="https://www.linkedin.com/in/vitor-zeferino/"> Vitor Zeferino</a>

## Descrição

📜 O projeto foca no desenvolvimento de uma simulação de robôs que cumprem um papel de realizar a inspeção de espaços confinados visando a segurança do trabalho. Nosso projeto é um desenvolvimento, em simulação, de um robô capaz de se mover em ambientes de espaço confinado, coletar dados a partir de sensores (principalmente de oxigênio e outros gases) e que utiliza imagens para apoiar na inspeção prévia da estrutura e localizar rachaduras. 
<br><br>

## 🛠 Estrutura de pastas
```bash
.
├── LICENSE
├── README.md
├── docs
│   ├── README.md
│   ├── _config.yml
│   └── index.md
├── media
│   ├── arquitetura_sistema
│   ├── artefatos_negocios
│   ├── interface_usuario
│   ├── visao_computacional
│   └── README.md
└── src
│   ├── backend
│   ├── frontend
│   ├── gazebo
│   ├── visão_computacional
    └── README.md

3 directories, 15 files
```

A pasta raiz contem dois arquivos que devem ser alterados:

<b>README.MD</b>: Arquivo que serve como guia e explicação geral sobre seu projeto. O mesmo que você está lendo agora.

Há também 3 pastas que seguem da seguinte forma:

<b>docs</b>: Aqui está o arquivo index.md, que serve como o ponto principal da documentação do projeto.

<b>media</b>: Algumas imagens do sistema, logos e tabelas, prontos para serem utilizados e visualizados.

<b>src</b>: Nesta pasta está todo o código fonte do sistema, pronto para para ser baixado e modificado.


## 💻 Configuração para Desenvolvimento

<!-- Descreva como instalar todas as dependências para desenvolvimento e como rodar um test-suite automatizado de algum tipo. Se necessário, faça isso para múltiplas plataformas. -->

Para abrir este projeto você necessita das seguintes ferramentas:

### Ros Humble Turtlebot3
Para instalar esse pacote, abra o terminal do ubuntu e execute:

```sudo apt install ros-humble-turtlebot3*```

Isso instalará todos os pacotes necessários para executar o Gazebo, o ambiente de simulação que utilizamos.
Por fim, execute no terminal do ubuntu:

```gazebo```


## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/2023M6T2-Inteli/Safe-McQueen/">Safe-McQueen</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName">INTELI, Alberto Miranda, Amanda Fontes, Antonio Teixeira, Joao Vitor Oliveira, Lucas Sales, Tainara Teixeira, Vitor Zeferino</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## 🎓 Referências

Aqui estão as referências usadas no projeto.

1. <https://github.com/iuricode/readme-template>
2. <https://github.com/gabrieldejesus/readme-model>
3. <https://creativecommons.org/share-your-work/>
4. <https://www.robotis.us/turtlebot-3-burger-us/>
5. <https://www.arducore.com.br/modulo-sensor-de-gas-amonia-mq-135-mq-135-arduino-pic?utm_[…]emsUyRupLv3cH6KkyQNeWCK8ZT5kR232Obgy_JhbGMYNIBoCtvUQAvD_BwE>
6. <https://www.robocore.net/acessorios-raspberry-pi/camera-para-raspberry-pi-rev-1-3?gcl[…]ylU27O2mcY2VCdnCc8crxZjaG2UlU2uJwvVlelRYsTp56dxoCRKwQAvD_BwE>
