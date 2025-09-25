# 🎓 Predição de Chance de Admissão com Keras e Tkinter

Este projeto utiliza um **modelo de Machine Learning treinado em Keras** para prever a **Chance of Admit** de um candidato com base em suas características acadêmicas.  
A interface gráfica foi construída em **Tkinter**, permitindo uma interação simples e intuitiva.

---

## 📸 Demonstração da Interface

<img width="502" height="683" alt="image" src="https://github.com/user-attachments/assets/b9e02c65-5d4c-45d9-9cef-efd7c3bdad53" />


Na interface, o usuário insere os seguintes dados:
- **Nota GRE**
- **Nota TOEFL**
- **Avaliação da Universidade**
- **SOP (Statement of Purpose)**
- **LOR (Letter of Recommendation)**
- **CGPA (Cumulative GPA)**

Após preencher os campos e clicar em **"Prever Chance"**, o sistema retorna a probabilidade de admissão em percentual.

---

## 🚀 Tecnologias Utilizadas
- Python 3.11+
- TensorFlow / Keras
- Tkinter (para GUI)

---

## ⚙️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/LucasCerqueira1244/Machine-Learning-com-Keras.git
   cd Machine-Learning-com-Keras

Crie um ambiente virtual e ative

python -m venv venv
# Windows (PowerShell)
.\venv\Scripts\activate

Instale as dependências

pip install -r requirements.txt

Execute o programa

python predict_admin.py

## 📂 Estrutura do Projeto
📦 Machine-Learning-com-Keras

 ┣ 📜 predict_admit.py                 # Código principal com Tkinter
 
 ┣ 📜 modelo_treinado.keras            # Modelo Keras treinado
 
 ┣ 📜 requirements.txt                 # Dependências do projeto
 
 ┣ 📜 README.md                        # Documentação do projeto


## 📖 Objetivo do Trabalho

Este projeto foi desenvolvido como parte da disciplina de Machine Learning, com o objetivo de aplicar um modelo treinado em Keras em um programa real que interaja com o usuário e forneça previsões personalizadas.
 
