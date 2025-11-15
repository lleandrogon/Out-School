# 📊 ETL Out-of-School Pipeline  
Pipeline de ETL usando **Apache Airflow**, **Pandas** e **PostgreSQL** para processar dados públicos sobre pessoas fora da escola (Fundamental I, Fundamental II e Ensino Médio).

## 🚀 Visão Geral

Este projeto implementa um fluxo de ETL totalmente automatizado utilizando **Apache Airflow**.  
O pipeline:

1. **Extrai** dados brutos de três arquivos CSV:
   - primary.csv  
   - Lower Secondary.csv  
   - Upper Secondary.csv

2. **Transforma** os dados com **Pandas**, padronizando colunas, ajustando tipos, lidando com valores nulos e preparando tudo para armazenamento.

3. **Carrega** os dados transformados em um banco de dados **PostgreSQL**.

Todo o ambiente é executado através de **Docker Compose**, usando a imagem oficial do Airflow.

---

**Tecnologias utilizadas:**

- Apache Airflow  
- Python 3 + Pandas  
- Docker Compose  
- PostgreSQL

---

## 🐳 Como executar o projeto

### 1️⃣ Pré-requisitos

- Docker  
- Docker Compose  

### 2️⃣ Subir o ambiente Airflow

No diretório raiz do projeto, execute:

**docker compose up -d**

### 3️⃣ Configurar a conexão com o PostgreSQL no Airflow

Para que o Airflow consiga enviar os dados transformados para o PostgreSQL da sua máquina local, é necessário **criar uma conexão manualmente na interface web**.

#### 🛠️ Criando a conexão `education_docker`

1. Acesse o Airflow em:  
   **http://localhost:8080**

2. Vá até o menu:  
   **Admin → Connections**

3. Clique em **+ Add Connection**

4. Preencha os campos da seguinte forma:

| Campo | Valor |
|-------|-------|
| **Conn Id** | `education_docker` |
| **Conn Type** | `Postgres` |
| **Host** | `host.docker.internal` |
| **Schema** | *nome do seu banco local* |
| **Login** | *seu usuário do Postgres* |
| **Password** | *sua senha* |
| **Port** | `5432` |

Essa conexão será usada pelo **PostgresHook** dentro das tasks da DAG.

> **Importante:** `host.docker.internal` é necessário para que o container do Airflow consiga enxergar o PostgreSQL que está rodando na sua máquina.

---

Depois dessa etapa, seu pipeline já estará pronto para extrair, transformar e carregar os dados no banco.

Se quiser, posso revisar o README completo e reorganizar para ficar ainda mais profissional.