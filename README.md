<h1 align="center">Programação em Sockets - Redes de Computadores</h1>
<p align="center">Essa atividade tem como objetivo introduzir os princípios da programação com sockets para explanar a arquitetura cliente-servidor</p>
</br>
<h4>Guilherme Frutuoso de Almeida</h4>
<h4>Thiago Martins Nogueira</h4>
</br>

<h2>instalação</h2>
<h5>git clone https://github.com/GuilhermeFA00/sockets </h5>

<h2>pré-requisitos</h2>
<h5>Ferramenta/Linguagem utilizada: Python (version >= 3.9)</h5>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white"/>
<h2>local-files</h2>
<h5>server.py(Código do servidor)</h5>
<h5>client.py(Código do cliente)</h5>
<h2>como-rodar</h2>
<h5>Abra seu terminal e execute o arquivo server.py . Ele ficará em espera. Execute o arquivo client.py. Veja os prints no terminal</h5>
</br>

<h2>Funcionamento</h2>
<h3>Parte servidor</h3>
<p>Quando criamos uma instância do objeto socket, passamos dois parâmetros: O primeiro parâmetro é AF_INET e o segundo é SOCK_STREAM. AF_INET refere-se à família de endereços ipv4. O SOCK_STREAM significa protocolo TCP orientado a conexão.
Agora podemos nos conectar a um servidor usando este socket.</p>

<p>Um objeto server tem o método "bind" que o liga a um IP e porta específicos para que ele possa ouvir as solicitações recebidas nesse IP e na porta estabelecida. O obejto server também tem um método chamado "listen" que coloca o server no modo de "escuta". Isso permite que o servidor escute as conexões de entrada. E por último, um "server object" também tem os métodos "accept" e "close". O método accept inicia uma conexão com o cliente e o método close fecha a conexão com o cliente.</p>

<p>Além da estrutura comum para criação de um lado servidor com sockets, criamos sub-rotinas especifícas para fazer transformações necessárias, como "int->bytes/bytes->int", saber a quantidade de casas de um número e diferenciar se um número é primo ou par.</p>

<h3>Parte cliente</h3>
<p>O código que estabelece a parte do cliente é menor e mais simples: Ele cria um objeto socket, usa .connect() para se conectar ao servidor e chama s.sendall() para enviar sua mensagem. Por fim, ele chama s.recv() para ler a resposta do servidor e a imprime.</p>
<p>Também utilizamos de conversões e encodes no arquivo do cliente, além, é claro, de utilizar a biblioteca "random" para gerar o número aleatório</p>
</br>
<img src="https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg"/>
