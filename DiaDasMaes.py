import streamlit as st

st.set_page_config(page_title="Cartão Dia Das Mães", page_icon="💗")

st.title("💗💓💖Feliz Dia das Mães!")
nome = st.text_input("DIgite o nome da sua mãe: ")

if st.button("Mostrar Mensagem!"):
    if nome:
        st.success(f"{nome}, Você é incrivel, te amo!")
    else:
        st.warning("Digite o nome da sua mãe para ver a homenagem")

st.image("https://pmsaposse.sp.gov.br/wp-content/uploads/2019/05/Dia-das-maes-2.jpg", use_container_width=False)
import time

with st.spinner("carregando..."):
    time.sleep(2)

st.success("pronto!")

progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)