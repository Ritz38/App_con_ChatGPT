import streamlit as st
import sympy as sp

# Configuración inicial
st.title("Calculadora de Derivadas")
st.write("Esta aplicación te permite calcular la derivada de funciones matemáticas de manera interactiva.")

# Crear una caja de texto para mostrar la expresión
if 'expresion' not in st.session_state:
    st.session_state['expresion'] = ''

# Función para agregar elementos a la expresión
def agregar_a_expresion(valor):
    st.session_state['expresion'] += valor

# Mostrar la expresión actual
st.subheader("Función actual:")
st.text(st.session_state['expresion'])

# Botones numéricos y de funciones
col1, col2, col3 = st.columns(3)

with col1:
    st.button('1', on_click=agregar_a_expresion, args=('1',))
    st.button('2', on_click=agregar_a_expresion, args=('2',))
    st.button('3', on_click=agregar_a_expresion, args=('3',))
    st.button('4', on_click=agregar_a_expresion, args=('4',))
    st.button('5', on_click=agregar_a_expresion, args=('5',))

with col2:
    st.button('6', on_click=agregar_a_expresion, args=('6',))
    st.button('7', on_click=agregar_a_expresion, args=('7',))
    st.button('8', on_click=agregar_a_expresion, args=('8',))
    st.button('9', on_click=agregar_a_expresion, args=('9',))
    st.button('0', on_click=agregar_a_expresion, args=('0',))

with col3:
    st.button('+', on_click=agregar_a_expresion, args=('+',))
    st.button('-', on_click=agregar_a_expresion, args=('-'))
    st.button('*', on_click=agregar_a_expresion, args=('*'))
    st.button('/', on_click=agregar_a_expresion, args=('/'))
    st.button('(', on_click=agregar_a_expresion, args=('(',))
    st.button(')', on_click=agregar_a_expresion, args=(')',))

# Botones para agregar funciones matemáticas
st.subheader("Funciones matemáticas:")
col1, col2 = st.columns(2)

with col1:
    st.button('sin', on_click=agregar_a_expresion, args=('sin(',))
    st.button('cos', on_click=agregar_a_expresion, args=('cos(',))
    st.button('tan', on_click=agregar_a_expresion, args=('tan(',))
    st.button('log', on_click=agregar_a_expresion, args=('log(',))
    st.button('exp', on_click=agregar_a_expresion, args=('exp(',))

with col2:
    st.button('x', on_click=agregar_a_expresion, args=('x',))
    st.button('sqrt', on_click=agregar_a_expresion, args=('sqrt(',))
    st.button('pi', on_click=agregar_a_expresion, args=('pi',))
    st.button('e', on_click=agregar_a_expresion, args=('e',))

# Opción para borrar la expresión
if st.button('Borrar'):
    st.session_state['expresion'] = ''

# Botón para calcular la derivada
if st.button('Calcular derivada'):
    if st.session_state['expresion']:
        try:
            x = sp.symbols('x')
            expresion = sp.sympify(st.session_state['expresion'])
            derivada = sp.diff(expresion, x)
            st.subheader("Resultado de la derivada:")
            st.latex(f"La derivada de la función es: \\ {sp.latex(derivada)}")
        except Exception as e:
            st.error(f"Hubo un error en la función: {e}")
    else:
        st.error("Por favor ingresa una función válida.")
