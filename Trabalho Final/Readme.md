# Projeto de Inteligência de Negócios e Visualização de Dados

Este projeto foca na integração e análise de dados financeiros e macroeconômicos para fornecer insights aprofundados do mercado e auxiliar na tomada de decisões de investimento.

---

## 📅 Detalhes do Projeto

* **Disciplina:** Inteligência de Negócios e Visualização de Dados
* **Período:** 2025.1
* **Professor:** Bruno Riccelli dos Santos Silva

---

## 👥 Equipe

* Luis Fernando Passos
* Wildney Kesney Rodrigues de Sousa 

---

## 💡 Introdução

Este documento descreve uma proposta de projeto focada na integração e análise de dados financeiros e macroeconômicos. O objetivo principal é fornecer uma visão aprofundada do mercado, ligando o desempenho de ativos com eventos externos e indicadores econômicos, para auxiliar na tomada de decisões de investimento e na identificação de tendências. A arquitetura proposta envolve um pipeline de **ETL (Extração, Transformação e Carga)** utilizando tecnologias de **Big Data** para processamento em tempo real e armazenamento eficiente, conforme solicitado no documento norteador.

---

## 🎯 Objetivo

O objetivo central deste projeto é analisar o comportamento do mercado financeiro em tempo real, estabelecendo correlações entre o desempenho de ativos e eventos externos, como notícias relevantes e indicadores econômicos. Ao fazer isso, busca-se auxiliar investidores e analistas na tomada de boas decisões quanto a investimentos e na identificação de tendências de mercado.

---

## 🌐 APIs Escolhidas

Para a coleta de dados, o projeto utilizará três fontes de API REST distintas, cada uma fornecendo informações para a análise do mercado financeiro e o contexto macroeconômico:

* **brapi.dev:** Esta API será a principal fonte de dados para cotações de ações (preços, volume, etc.) e outras informações de mercado, como índices e moedas. É fundamental para obter dados em tempo real sobre o desempenho dos ativos.
* **BrasilAPI:** Utilizada para buscar informações contextuais importantes, como feriados bancários, taxas de juros (SELIC, CDI), e até mesmo informações de CEPs, que podem ser relevantes para contextualizar regionalmente empresas ou eventos.
* **Serviço Dados IBGE (API):** Essencial para a coleta de dados macroeconômicos. Através desta API, serão obtidos índices de inflação (IPCA), Produto Interno Bruto (PIB) e taxas de desemprego, fornecendo o panorama econômico que influencia diretamente o mercado financeiro.

---

## ✨ Relevância para o Projeto

A integração e análise dessas fontes de dados são de extrema relevância para o projeto, pois permitem:

* **Análise Abrangente:** Combinar dados de cotações de ativos com indicadores macroeconômicos e eventos externos (como notícias) oferece uma visão holística do mercado, permitindo identificar padrões e correlações que não seriam evidentes sem nosso pipeline.
* **Tomada de Decisão Informada:** Ao correlacionar o desempenho dos ativos com fatores externos, o projeto capacita os usuários a tomar decisões de investimento mais informadas e estratégicas.
* **Identificação de Tendências:** A capacidade de processar e analisar dados em tempo real facilita a identificação precoce de tendências de mercado, permitindo reações rápidas a mudanças e oportunidades.

---

## ⚙️ Adequação da Arquitetura

A arquitetura proposta para este projeto é adequada para resolver o problema de monitoramento e análise de desempenho do mercado financeiro em tempo real, devido aos seguintes pontos:

* **Escalabilidade e Tempo Real:** A utilização de **Apache Kafka** para ingestão de dados em tempo real e **Apache Spark** para processamento distribuído garante que o sistema possa lidar com grandes volumes de dados de mercado e processá-los com baixa latência.
* **Armazenamento Flexível e Otimizado:** O **Data Lake** permite o armazenamento de dados brutos em diversos formatos, enquanto o **Data Warehouse** com tabelas dimensionais e de fatos otimiza as consultas analíticas. O uso de formatos como **Parquet** para dados processados melhora ainda mais o desempenho das consultas.
* **Orquestração:** **Apache Airflow** é uma ferramenta eficiente para orquestrar todo o pipeline ETL, garantindo que os dados sejam ingeridos, processados e carregados de forma consistente e agendada.
