Predição de Chance de Admissão - Machine Learning com Keras

Este projeto é uma aplicação em Python que utiliza um modelo treinado em Keras/TensorFlow para prever a Chance of Admit de um candidato com base em suas características acadêmicas. O projeto inclui uma interface gráfica desenvolvida com Tkinter para facilitar a interação do usuário.

📌 Funcionalidades

Carrega um modelo pré-treinado em Keras (modelo_chance_admit.h5).

Solicita ao usuário os valores das características do candidato.

Valida automaticamente os valores inseridos.

Realiza a previsão usando o modelo.

Exibe a chance prevista de admissão em percentual, com uma barra de progresso visual.

🛠 Tecnologias Utilizadas

Python 3.11

TensorFlow / Keras

NumPy

Tkinter

📂 Estrutura do Projeto
predicao_chance_admit/
│
├── modelo_treinado.keras   # Modelo treinado em Keras
├── predict_admit.py        # Código principal
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências do projeto

⚙️ Instalação

Clone este repositório:

git clone https://github.com/LucasCerqueira1244/Machine-Learning-com-Keras.git
cd predicao_chance_admit


Crie um ambiente virtual:

python -m venv venv


Ative o ambiente virtual:

Windows

.\venv\Scripts\activate


Mac/Linux

source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Certifique-se de ter o arquivo modelo_treinado.keras na pasta do projeto.

🚀 Como Executar

No terminal, dentro da pasta do projeto:

python predict_admit.py


Isso abrirá a interface gráfica, onde você poderá inserir os dados do candidato e obter a previsão da chance de admissão.

🖥 Uso

Na interface, preencha os campos:

Nota GRE (0 a 340)

Nota TOEFL (0 a 120)

Avaliação da Universidade (1 a 5)

SOP (1 a 5)

LOR (1 a 5)

CGPA (0 a 10)

Pesquisa (0 = Não, 1 = Sim)

Clique em "Prever Chance" para gerar a previsão. O resultado aparecerá na tela e será exibido na barra de progresso.

📄 Licença

Este projeto está licenciado sob a Licença MIT — consulte o arquivo LICENSE
 para mais detalhes.