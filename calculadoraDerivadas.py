import streamlit as st
#Utilizamos un archivo de requerimientos para instalar sympy ya que streamlit descarga automaticamente esto
import sympy as sp

# Configuración inicial
st.title("Calculadora de Derivadas")
st.write("Esta app fue elaborada por **Juan Pablo Zuluaga Mesa**")
st.write("Esta aplicación te permite calcular la derivada de funciones matemáticas.")

# Entrada de la función
st.subheader("Ingrese la función")
funcion = st.text_input("Escribe tu función, usando 'x' como variable:", value="x**2 + 3*x + 5")

# Mostrar la función
if funcion:
    try:
        # Definir la variable y la función
        x = sp.symbols("x")
        expresion = sp.sympify(funcion)
        
        # Calcular la derivada
        derivada = sp.diff(expresion, x)
        
        # Mostrar resultados
        st.subheader("Resultado")
        st.latex(f"La\\derivada\\de\\la\\función\\{sp.latex(expresion)}\\es:\\{sp.latex(derivada)}")
    except (sp.SympifyError, ValueError):
        st.error("Por favor, ingresa una función válida.")

# Instrucciones adicionales
st.write("Ejemplo de entrada válida: `x**2 + 3*x + 5` o `sin(x) + log(x)`.")
st.write("Soporta funciones como `sin`, `cos`, `tan`, `exp`, `log`, entre otras.")
