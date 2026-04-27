import streamlit as st
import random
import streamlit.components.v1 as components

st.title("--- Calculadora Python --- 🧮")

# Criamos uma caixa para escolher a operação
operacao = st.selectbox(
    "Escolha a operação:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

# Criamos os campos para os números
num1 = st.number_input("Digite o primeiro número:", value=0.0)
num2 = st.number_input("Digite o segundo número:", value=0.0)

# O botão para calcular
if st.button("Calcular"):
    if operacao == "Soma (+)":
        st.success(f"Resultado: {num1} + {num2} = {num1 + num2}")
    
    elif operacao == "Subtração (-)":
        st.success(f"Resultado: {num1} - {num2} = {num1 - num2}")
    
    elif operacao == "Multiplicação (*)":
        st.success(f"Resultado: {num1} * {num2} = {num1 * num2}")
    
    elif operacao == "Divisão (/)":
        if num2 == 0:
            st.error("Erro: Divisão por zero não é permitida!")
        else:
            st.success(f"Resultado: {num1} / {num2} = {num1 / num2}")

# ... (todo o seu código da calculadora que já está lá)

# No final de tudo, cole o código do AdSense assim:
components.html(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4581971001324805"
     crossorigin="anonymous"></script>
    """,
    height=0
)
