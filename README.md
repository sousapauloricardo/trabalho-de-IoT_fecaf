# Pipeline de Dados IoT com Docker e MySQL

Este projeto automatiza a coleta, armazenamento e visualização de dados de dispositivos IoT utilizando uma arquitetura moderna e escalável. O sistema processa leituras de temperatura de sensores, armazena em um banco de dados MySQL via Docker e apresenta os resultados em um dashboard interativo.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Banco de Dados:** MySQL 8.0 (Containerizado)
* **Visualização:** Streamlit e Plotly
* **Integração:** SQLAlchemy e PyMySQL
* **Infraestrutura:** Docker & Docker Compose

## 📁 Estrutura do Projeto
Com base na organização atual:
```text
PROJETO - PIPELINE DE DADOS COM IOT/
├── data/
│   └── database.py          # Configurações de conexão e Engine
├── sql/
│   └── views.sql            # Definições das Views Analíticas
├── src/
│   ├── dashboard.py         # Interface visual (Streamlit)
│   └── ingestion.py         # Script de carga e ETL
├── .env                     # Variáveis de ambiente (Senhas)
├── .gitignore               # Arquivos ignorados pelo Git
├── docker-compose.yml       # Orquestração do MySQL
└── README.md                # Documentação do projeto
```

## 🚀 Como Executar

### 1. Configuração do Banco (Docker)
Com o Docker Desktop rodando, suba o serviço do banco de dados:
```bash
docker-compose up -d
```

### 2. Configuração do Ambiente
Instale as dependências necessárias:
```bash
pip install pandas sqlalchemy pymysql cryptography streamlit plotly python-dotenv
```

### 3. Ingestão de Dados
Execute o script para ler o arquivo CSV (que deve estar na raiz ou conforme apontado no script) e carregar no MySQL:
```bash
python src/ingestion.py
```

### 4. Criação das Views
Certifique-se de executar os comandos do arquivo `sql/views.sql` no seu terminal MySQL para habilitar os gráficos do dashboard.

### 5. Visualização (Dashboard)
Inicie a interface gráfica:
```bash
streamlit run src/dashboard.py
```

## 📊 Insights e Análises (Views SQL)
* **Média de Temperatura:** Identifica dispositivos operando fora da curva normal.
* **Leituras por Hora:** Mapeia os períodos de maior tráfego de dados.
* **Max/Min por Dia:** Monitora picos térmicos para prevenção de falhas.

## 💻 Comandos Git Utilizados
```bash
git init
git add .
git commit -m "Projeto final: Pipeline de Dados IoT"
git remote add origin [URL-DO-REPOSITORIO]
git push -u origin main
```