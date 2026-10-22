import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random

# 1. CONFIGURAÇÃO DA PÁGINA COM TEMA INTEGRADO
st.set_page_config(page_title="Bradesco - Intelligence", layout="wide", page_icon="🏦")

# Injeção de CSS para customizar cartões e fontes (Padrão corporativo moderno)
st.markdown("""
    <style>
    .metric-card {
        background-color: #1e1e24;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #cc092f; /* Vermelho Bradesco */
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .metric-title { color: #aeaeae; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
    .metric-value { color: #ffffff; font-size: 28px; font-weight: bold; margin-top: 5px; }
    </style>
""", unsafe_allow_html=True)

st.title("🏦 Bradesco — Banking Intelligence")
st.markdown("<p style='color:#aeaeae; font-size:18px;'>Plataforma Avançada de Monitoramento e Modelagem de Propensão de Crédito</p>", unsafe_allow_html=True)
st.write("---")

# 2. CARREGAMENTO DE DADOS OTIMIZADO
@st.cache_data
def carregar_dados():
    clients_data = []
    for i in range(1, 10001):
        clients_data.append({
            "client_id": i,
            "segmento": random.choice(['Varejo', 'Prime', 'Exclusive']),
            "idade": random.randint(18, 80),
            "regiao": random.choice(['SP', 'RJ', 'MG', 'PR', 'BA'])
        })
    df_c = pd.DataFrame(clients_data)

    tx_data = []
    for client_id in range(1, 10001):
        for _ in range(random.randint(5, 30)):
            tipo = random.choice(['PIX', 'CARTAO_CREDITO', 'TED', 'BOLETO', 'APP_LOGIN'])
            valor = 0.0 if tipo == 'APP_LOGIN' else round(random.uniform(5.0, 5000.0), 2)
            tx_data.append({"client_id": client_id, "tipo_transacao": tipo, "valor": valor, "dias_atras": random.randint(1, 90)})
    df_t = pd.DataFrame(tx_data)

    df_logins_30d = df_t[(df_t['tipo_transacao'] == 'APP_LOGIN') & (df_t['dias_atras'] <= 30)]
    features_logins = df_logins_30d.groupby('client_id').size().reset_index(name='qtd_logins_30d')
    features_valores = df_t.pivot_table(index='client_id', columns='tipo_transacao', values='valor', aggfunc='sum', fill_value=0).reset_index()
    
    features_valores = features_valores.rename(columns={
        'CARTAO_CREDITO': 'vlr_cartao_90d', 'PIX': 'vlr_pix_90d', 'TED': 'vlr_ted_90d', 'BOLETO': 'vlr_boleto_90d'
    }).drop(columns=['APP_LOGIN'], errors='ignore')

    features_valores['vlr_total_movimentado_90d'] = features_valores['vlr_cartao_90d'] + features_valores['vlr_pix_90d'] + features_valores['vlr_ted_90d'] + features_valores['vlr_boleto_90d']
    df_final = df_c.merge(features_logins, on='client_id', how='left').merge(features_valores, on='client_id', how='left').fillna(0)
    df_final['target_propensao_credito'] = np.where((df_final['qtd_logins_30d'] >= 2) & (df_final['vlr_total_movimentado_90d'] > 15000), 1, 0)
    return df_final

df = carregar_dados()

# 3. FILTROS NA SIDEBAR
st.sidebar.header("Painel de Filtros")
segmento_selecionado = st.sidebar.multiselect("Segmento do Cliente:", options=df['segmento'].unique(), default=df['segmento'].unique())
df_filtrado = df[df['segmento'].isin(segmento_selecionado)]

# 4. CARDS DE MÉTRICAS MODERNOS
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='metric-card'><div class='metric-title'>Total de Clientes Analisados</div><div class='metric-value'>{len(df_filtrado):,}</div></div>", unsafe_allow_html=True)
with col2:
    clientes_propensos = df_filtrado['target_propensao_credito'].sum()
    st.markdown(f"<div class='metric-card'><div class='metric-title'>Clientes Propensos (Target 1)</div><div class='metric-value'>{clientes_propensos:,}</div></div>", unsafe_allow_html=True)
with col3:
    taxa_conversao = (clientes_propensos / len(df_filtrado)) * 100 if len(df_filtrado) > 0 else 0
    st.markdown(f"<div class='metric-card'><div class='metric-title'>Taxa de Propensão Geral</div><div class='metric-value'>{taxa_conversao:.2f}%</div></div>", unsafe_allow_html=True)

st.write("---")

# Paleta de Cores Institucional (Vermelho Bradesco, Cinza, Grafite)
cores_bradesco = ['#cc092f', '#f4f4f6', '#333333', '#737373']

# 5. GRÁFICOS DESIGN ULTRA MODERN
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.markdown("#### 📊 Distribuição de Carteira por Segmento")
    fig1 = px.pie(df_filtrado, names='segmento', hole=0.5, color_discrete_sequence=cores_bradesco)
    fig1.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1, use_container_width=True)

with col_graf2:
    st.markdown("#### 📈 Volume Financeiro Médio por Faixa Etária")
    df_filtrado['faixa_etaria'] = pd.cut(df_filtrado['idade'], bins=[0, 25, 40, 60, 100], labels=['<25 anos', '25-40 anos', '40-60 anos', '60+ anos'])
    df_gasto = df_filtrado.groupby('faixa_etaria', observed=False)['vlr_total_movimentado_90d'].mean().reset_index()
    
    fig2 = px.bar(df_gasto, x='faixa_etaria', y='vlr_total_movimentado_90d', color_discrete_sequence=['#cc092f'])
    fig2.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', yaxis_title="Média (R$)")
    st.plotly_chart(fig2, use_container_width=True)

st.write("---")

# 6. DATAFRAME ANALÍTICO ESTILIZADO
st.markdown("#### 🔍 Exploração da ABT (Analytical Base Table)")
st.dataframe(df_filtrado[['client_id', 'segmento', 'idade', 'regiao', 'qtd_logins_30d', 'vlr_total_movimentado_90d', 'target_propensao_credito']].head(50), use_container_width=True)