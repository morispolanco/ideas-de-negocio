import streamlit as st
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API

st.title('Generador de ideas de negocio')

capital_inicial = st.number_input('Capital inicial (en dólares)', min_value=0, value=10000)
tiempo_retorno = st.number_input('Tiempo esperado de retorno (en meses)', min_value=0, value=12)

prompt = f'Sugiéreme 3 ideas de negocio rentables con un capital inicial de {capital_inicial} dólares y un tiempo de retorno de la inversión de {tiempo_retorno} meses.'

response = openai.Completion.create(engine='text-davinci-003', prompt=prompt, max_tokens=1024)
ideas = response['choices'][0]['text'].split('\n')

st.write('## Ideas sugeridas:')
for idea in ideas:
  st.write('- ' + idea)
