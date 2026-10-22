# consultoria-bradesco# 🏦 Projeto: Consultoria Inteligência Analítica — Bradesco
**Repositório de Soluções de Advanced Analytics & Data Science**

Este repositório contém os entregáveis técnicos desenvolvidos para simular um cenário real de consultoria e modelagem preditiva avançada voltada à área de Inteligência e Analytics do **Bradesco** (Osasco-SP). O objetivo principal é mapear oportunidades de negócio e implementar modelos de inteligência artificial para otimizar a rentabilidade e o engajamento digital dos correntistas.

---

## 🏗️ Escopo da Solução Desenvolvida
O projeto resolve três pilares cruciais para a operação analítica de um ecossistema bancário moderno:
1. **Otimização de Infraestrutura e Engenharia de Features:** Consolidação do histórico transacional e cadastral de correntistas em uma ABT (*Analytical Base Table*) de alta performance, gerando métricas agregadas temporais.
2. **Modelagem Preditiva Avançada (Machine Learning):** Desenvolvimento de um modelo preditivo de **Propensão de Compra** utilizando o algoritmo *Random Forest Classifier* para identificar clientes propensos à contratação de crédito baseado em comportamento digital.
3. **Plataforma Visual de Business Intelligence:** Criação de um Dashboard interativo e premium utilizando **Streamlit** e **Plotly** para monitoramento executivo em tempo real e tomadas de decisão ágeis pelas áreas de negócio.

---

## 🛠️ Stack Tecnológica Aplicada
* **Manipulação e Engenharia de Dados:** Pandas / NumPy
* **Machine Learning e Estatística:** Scikit-Learn (Random Forest)
* **Visualização e Data Apps:** Streamlit / Plotly Express / Injeção de CSS Customizado
* **Arquitetura Industrializada Alvo:** Databricks / Apache Spark / PySpark / Delta Lake

---

## 📊 Estrutura dos Arquivos do Portfólio
* **`app_dashboard.py`**: Código-fonte da aplicação interativa do Dashboard Corporativo com visual moderno e identidade visual do banco.
* **`02_model_training.py`**: Pipeline integrado de Machine Learning focado em geração de dados, treino do classificador, separação de bases e validação estatística de métricas (*Acurácia* e *AUC-ROC*).
* **`model_metadata.json`**: Artefato automatizado para auditoria de modelos, garantindo processos rígidos de governança de dados exigidos no setor bancário.

---

## 📈 Resultados e Impacto de Negócio Obtidos
* **Segmentação Estratégica:** Mapeamento visual das fatias de carteira dos correntistas divididas entre os perfis *Varejo*, *Prime* e *Exclusive*.
* **Identificação de Alavancas de Valor:** O classificador identificou que a *frequência de logins na conta digital nos últimos 30 dias* é a variável mais importante para a conversão de novas ofertas.
* **Otimização de CAC:** Alocação inteligente de recursos de marketing ao focar as campanhas de crédito apenas na parcela de clientes identificada como proponente (Target 1).
