import streamlit as st
import requests

st.set_page_config(page_title="🔮 Previsão de Cancelamento", layout="centered")
st.title("🔍 Previsão de Cancelamento de Clientes")
st.markdown("Preencha os dados abaixo para prever se o cliente irá cancelar:")

# Campos do formulário
with st.form("formulario_cliente"):
    idade = st.number_input("Idade", min_value=18, max_value=100)
    tempo_como_cliente_meses = st.number_input("Tempo como cliente (meses)", min_value=0)
    renda_mensal = st.number_input("Renda mensal (R$)", min_value=0.0, format="%.2f")
    engajamento_mensal = st.number_input("Engajamento mensal")
    ultima_atividade_dias = st.number_input("Dias desde última atividade")
    interacoes_com_pushs = st.number_input("Interações com pushs")
    numero_contatos_suporte = st.number_input("Contatos com suporte")
    ticket_medio = st.number_input("Ticket médio (R$)")
    nps = st.number_input("NPS")
    uso_cashback = st.selectbox("Usa cashback?", [0, 1])
    bonus_recebido = st.selectbox("Recebeu bônus?", [0, 1])
    score_interno = st.number_input("Score interno")

    plano_atual = st.selectbox("Plano atual", ["Básico", "Padrão", "Premium"])
    canal_aquisicao = st.selectbox("Canal de aquisição", ["Orgânico", "Google Ads", "Facebook", "Indicação"])
    categoria_profissional = st.selectbox("Categoria profissional", ["Estudante", "Profissional", "Empreendedor"])
    cidade = st.text_input("Cidade")
    dispositivo_preferido = st.selectbox("Dispositivo preferido", ["Mobile", "Desktop", "Tablet"])
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])

    submitted = st.form_submit_button("🔍 Prever cancelamento")

# Quando o botão for clicado
if submitted:
    payload = {
        "idade": idade,
        "tempo_como_cliente_meses": tempo_como_cliente_meses,
        "renda_mensal": renda_mensal,
        "engajamento_mensal": engajamento_mensal,
        "ultima_atividade_dias": ultima_atividade_dias,
        "interacoes_com_pushs": interacoes_com_pushs,
        "numero_contatos_suporte": numero_contatos_suporte,
        "ticket_medio": ticket_medio,
        "nps": nps,
        "uso_cashback": uso_cashback,
        "bonus_recebido": bonus_recebido,
        "score_interno": score_interno,
        "plano_atual": plano_atual,
        "canal_aquisicao": canal_aquisicao,
        "categoria_profissional": categoria_profissional,
        "cidade": cidade,
        "dispositivo_preferido": dispositivo_preferido,
        "sexo": sexo
    }

    try:
        url = "https://fastapi-churn-app.onrender.com/predict"
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            resultado = response.json()
            st.success(f"✅ Probabilidade de cancelamento: **{resultado['probabilidade_cancelamento'] * 100:.2f}%**")
            st.info(f"Vai cancelar? {'✅ Sim' if resultado['vai_cancelar'] else '❌ Não'}")
        else:
            st.error("Erro na API: " + response.text)

    except Exception as e:
        st.error(f"Erro ao fazer requisição: {e}")
