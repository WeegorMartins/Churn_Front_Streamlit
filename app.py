import streamlit as st
import requests

st.set_page_config(page_title="🔮 Previsão de Cancelamento", layout="centered")
st.title("🔍 Previsão de Cancelamento de Clientes")
st.markdown("Preencha os dados abaixo para prever a chance de um cliente cancelar:")

with st.form("formulario_cliente"):
    id_cliente = st.text_input("ID do Cliente", placeholder="CLT0000001_0")
    idade = st.number_input("Idade", min_value=18, max_value=100, step=1)
    sexo = st.selectbox("Sexo", ["M", "F"])
    cidade = st.selectbox("Cidade", ["SP", "RJ", "BH", "SSA", "POA", "REC"])
    plano_atual = st.selectbox("Plano Atual", ["Grátis", "Básico", "Empresarial", "Premium"])
    tempo_como_cliente_meses = st.number_input("Tempo como cliente (meses)", min_value=0)
    engajamento_mensal = st.number_input("Engajamento mensal")
    nps = st.slider("NPS", -100, 100, 0)
    numero_contatos_suporte = st.number_input("Contatos com suporte", min_value=0, step=1)
    ultima_atividade_dias = st.number_input("Dias desde última atividade", min_value=0, step=1)
    qtde_produtos_ativos = st.selectbox("Quantidade de produtos ativos", [1, 2, 3, 4, 5])
    renda_mensal = st.number_input("Renda mensal (R$)", min_value=0.0, format="%.2f")
    canal_aquisicao = st.selectbox("Canal de aquisição", ["Orgânico", "Pago", "Eventos", "Social Media"])
    dispositivo_preferido = st.selectbox("Dispositivo preferido", ["Web", "Android", "iOS"])
    categoria_profissional = st.selectbox("Categoria profissional", ["CLT", "Autônomo", "Servidor Público"])
    score_interno = st.number_input("Score interno", min_value=0.0)
    uso_cashback = st.slider("Uso de cashback (%)", 0, 100, 0)
    bonus_recebido = st.selectbox("Recebeu bônus?", [0, 1])
    interacoes_com_pushs = st.number_input("Interações com pushs", min_value=0, step=1)
    ticket_medio = st.number_input("Ticket médio (R$)", min_value=0.0)

    submitted = st.form_submit_button("🔍 Prever cancelamento")

if submitted:
    payload = {
        "id_cliente": id_cliente,
        "idade": idade,
        "sexo": sexo,
        "cidade": cidade,
        "plano_atual": plano_atual,
        "tempo_como_cliente_meses": tempo_como_cliente_meses,
        "engajamento_mensal": engajamento_mensal,
        "nps": nps,
        "numero_contatos_suporte": numero_contatos_suporte,
        "ultima_atividade_dias": ultima_atividade_dias,
        "qtde_produtos_ativos": qtde_produtos_ativos,
        "renda_mensal": renda_mensal,
        "canal_aquisicao": canal_aquisicao,
        "dispositivo_preferido": dispositivo_preferido,
        "categoria_profissional": categoria_profissional,
        "score_interno": score_interno,
        "uso_cashback": uso_cashback,
        "bonus_recebido": bonus_recebido,
        "interacoes_com_pushs": interacoes_com_pushs,
        "ticket_medio": ticket_medio
    }

    try:
        url = "https://fastapi-churn-app.onrender.com/predict"
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            resultado = response.json()
            st.success(f"✅ Probabilidade de cancelamento: **{resultado['probabilidade_cancelamento']*100:.2f}%**")
            st.info(f"Vai cancelar? {'✅ Sim' if resultado['vai_cancelar'] else '❌ Não'}")
        else:
            st.error("Erro na API: " + response.text)
    except Exception as e:
        st.error(f"Erro ao fazer requisição: {e}")
