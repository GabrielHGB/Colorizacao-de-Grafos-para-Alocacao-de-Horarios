<h1 align="center">🎨 Colorização de Grafos para Alocação de Horários</h1>

<p align="center">
Este projeto implementa a <strong>coloração de grafos</strong> como solução para o 
problema de <strong>alocação de horários</strong>, utilizando a biblioteca 
<strong>NetworkX</strong> para manipulação e visualização dos grafos.
</p>

<hr>

<h2>📌 Descrição</h2>

<p>
O sistema constrói um grafo a partir de um arquivo CSV contendo conflitos entre disciplinas
e aplica automaticamente o algoritmo <strong>DSATUR</strong> para realizar a coloração.
</p>

<p>
Cada cor representa um <strong>horário distinto</strong>, garantindo que disciplinas conflitantes
não sejam alocadas no mesmo período.
</p>

<hr>

<h2>⚙️ Instalação</h2>

<p>
Antes de executar o projeto, recomenda-se criar um <strong>ambiente virtual</strong> e instalar as dependências.
</p>

<h3>🐧 Linux / macOS</h3>

<pre>
python3 -m venv venv
source venv/bin/activate
pip install pandas matplotlib networkx colorama termcolor
</pre>

<h3>🪟 Windows</h3>

<pre>
python -m venv venv
venv\Scripts\activate
pip install pandas matplotlib networkx colorama termcolor
</pre>

<hr>

<h2>🧩 Dependências</h2>

<ul>
  <li><strong>pandas</strong> → leitura e manipulação dos arquivos CSV</li>
  <li><strong>matplotlib</strong> → geração e salvamento do grafo colorido</li>
  <li><strong>networkx</strong> → construção e coloração de grafos</li>
  <li><strong>colorama</strong> e <strong>termcolor</strong> → cores e formatação do terminal</li>
  <li><strong>time</strong> e <strong>os</strong> → controle de tempo e manipulação de arquivos</li>
</ul>

<hr>

<h2>▶️ Como Executar</h2>

<p>
Após ativar o ambiente virtual e instalar as dependências, execute o programa principal:
</p>

<pre>
python src/main.py
</pre>

ou

<pre>
python3 src/main.py
</pre>

<hr>

<h2>🚀 Execução</h2>

<ol>
  <li>O sistema solicita o nome do arquivo CSV localizado na pasta <strong>datasets_coloring/</strong>.</li>
  <li>O grafo é construído automaticamente.</li>
  <li>O algoritmo <strong>DSATUR</strong> é aplicado para realizar a coloração.</li>
  <li>As disciplinas são agrupadas por cor (horário) e exibidas no terminal.</li>
  <li>Opcionalmente, o usuário pode gerar a visualização gráfica do grafo.</li>
</ol>

<p>
Caso a visualização seja gerada, o arquivo será salvo como:
</p>

<pre>
grafo_colorido.png
</pre>

<hr>

<h2>📊 Estrutura do Projeto</h2>

<pre>
├── main.py
├── VisualizacaoGrafo.py
├── Documentação_Grafos_Tp2.pdf
├── datasets_coloring
│    ├── grande.csv
│    ├── medio.csv
│    ├── pequeno.csv
└── README.md
</pre>

<hr>

<p align="center">
📚 Projeto desenvolvido para aplicação prática de Teoria dos Grafos na organização de horários acadêmicos.
</p>