import streamlit as st

# Título de la app
st.title("Mi primera app")

# Autor de la app
st.write("Esta app fue elaborada por **Juan Pablo Zuluaga Mesa**")

# Solicitar el nombre del usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre:")

# Imprimir un mensaje de bienvenida si el usuario ingresó su nombre
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
