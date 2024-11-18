import streamlit as st

# Funciones de conversión
def convertir(valor, conversion):
    if conversion == "Celsius a Fahrenheit":
        return (valor * 9 / 5) + 32
    elif conversion == "Fahrenheit a Celsius":
        return (valor - 32) * 5 / 9
    elif conversion == "Celsius a Kelvin":
        return valor + 273.15
    elif conversion == "Kelvin a Celsius":
        return valor - 273.15
    elif conversion == "Pies a metros":
        return valor * 0.3048
    elif conversion == "Metros a pies":
        return valor / 0.3048
    elif conversion == "Pulgadas a centímetros":
        return valor * 2.54
    elif conversion == "Centímetros a pulgadas":
        return valor / 2.54
    elif conversion == "Libras a kilogramos":
        return valor * 0.453592
    elif conversion == "Kilogramos a libras":
        return valor / 0.453592
    elif conversion == "Onzas a gramos":
        return valor * 28.3495
    elif conversion == "Gramos a onzas":
        return valor / 28.3495
    elif conversion == "Galones a litros":
        return valor * 3.78541
    elif conversion == "Litros a galones":
        return valor / 3.78541
    elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
        return valor * 16.3871
    elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
        return valor / 16.3871
    elif conversion == "Horas a minutos":
        return valor * 60
    elif conversion == "Minutos a segundos":
        return valor * 60
    elif conversion == "Días a horas":
        return valor * 24
    elif conversion == "Semanas a días":
        return valor * 7
    elif conversion == "Millas por hora a kilómetros por hora":
        return valor * 1.60934
    elif conversion == "Kilómetros por hora a metros por segundo":
        return valor / 3.6
    elif conversion == "Nudos a millas por hora":
        return valor * 1.15078
    elif conversion == "Metros por segundo a pies por segundo":
        return valor * 3.28084
    elif conversion == "Metros cuadrados a pies cuadrados":
        return valor * 10.7639
    elif conversion == "Pies cuadrados a metros cuadrados":
        return valor / 10.7639
    elif conversion == "Kilómetros cuadrados a millas cuadradas":
        return valor * 0.386102
    elif conversion == "Millas cuadradas a kilómetros cuadrados":
        return valor / 0.386102
    elif conversion == "Julios a calorías":
        return valor * 0.239006
    elif conversion == "Calorías a kilojulios":
        return valor / 239.006
    elif conversion == "Kilovatios-hora a megajulios":
        return valor * 3.6
    elif conversion == "Megajulios a kilovatios-hora":
        return valor / 3.6
    elif conversion == "Pascales a atmósferas":
        return valor / 101325
    elif conversion == "Atmósferas a pascales":
        return valor * 101325
    elif conversion == "Barras a libras por pulgada cuadrada":
        return valor * 14.5038
    elif conversion == "Libras por pulgada cuadrada a bares":
        return valor / 14.5038
    elif conversion == "Megabytes a gigabytes":
        return valor / 1024
    elif conversion == "Gigabytes a Terabytes":
        return valor / 1024
    elif conversion == "Kilobytes a megabytes":
        return valor / 1024
    elif conversion == "Terabytes a petabytes":
        return valor / 1024
    else:
        return "Conversión no válida"

# Configuración de la app
st.title("App de conversiones")
st.write("Selecciona una categoría y el tipo de conversión que deseas realizar.")

# Selección de categoría
categoria = st.selectbox(
    "Selecciona una categoría:",
    [
        "Conversiones de temperatura",
        "Conversiones de longitud",
        "Conversiones de peso/masa",
        "Conversiones de volumen",
        "Conversiones de tiempo",
        "Conversiones de velocidad",
        "Conversiones de área",
        "Conversiones de energía",
        "Conversiones de presión",
        "Conversiones de tamaño de datos",
    ],
)

# Opciones de conversión según la categoría
opciones_conversion = {
    "Conversiones de temperatura": [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius",
    ],
    "Conversiones de longitud": [
        "Pies a metros",
        "Metros a pies",
        "Pulgadas a centímetros",
        "Centímetros a pulgadas",
    ],
    "Conversiones de peso/masa": [
        "Libras a kilogramos",
        "Kilogramos a libras",
        "Onzas a gramos",
        "Gramos a onzas",
    ],
    "Conversiones de volumen": [
        "Galones a litros",
        "Litros a galones",
        "Pulgadas cúbicas a centímetros cúbicos",
        "Centímetros cúbicos a pulgadas cúbicas",
    ],
    "Conversiones de tiempo": [
        "Horas a minutos",
        "Minutos a segundos",
        "Días a horas",
        "Semanas a días",
    ],
    "Conversiones de velocidad": [
        "Millas por hora a kilómetros por hora",
        "Kilómetros por hora a metros por segundo",
        "Nudos a millas por hora",
        "Metros por segundo a pies por segundo",
    ],
    "Conversiones de área": [
        "Metros cuadrados a pies cuadrados",
        "Pies cuadrados a metros cuadrados",
        "Kilómetros cuadrados a millas cuadradas",
        "Millas cuadradas a kilómetros cuadrados",
    ],
    "Conversiones de energía": [
        "Julios a calorías",
        "Calorías a kilojulios",
        "Kilovatios-hora a megajulios",
        "Megajulios a kilovatios-hora",
    ],
    "Conversiones de presión": [
        "Pascales a atmósferas",
        "Atmósferas a pascales",
        "Barras a libras por pulgada cuadrada",
        "Libras por pulgada cuadrada a bares",
    ],
    "Conversiones de tamaño de datos": [
        "Megabytes a gigabytes",
        "Gigabytes a Terabytes",
        "Kilobytes a megabytes",
        "Terabytes a petabytes",
    ],
}

# Selección del tipo de conversión
tipo_conversion = st.selectbox(
    "Selecciona el tipo de conversión:",
    opciones_conversion[categoria],
)

# Entrada de valor a convertir
valor = st.number_input("Ingresa el valor que deseas convertir:", min_value=0.0)

# Mostrar el resultado
if st.button("Convertir"):
    resultado = convertir(valor, tipo_conversion)
    st.write(f"Resultado: {resultado}")
