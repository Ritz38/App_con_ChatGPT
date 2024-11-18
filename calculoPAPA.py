import streamlit as st
import pandas as pd

# Configuración inicial
st.title("Cálculo de PAPA")
st.write("Esta app fue elaborada por **Juan Pablo Zuluaga Mesa**")
st.write("Calcula tu Promedio Académico Ponderado Acumulado y porcentaje de avance en la carrera.")

# Crear o cargar datos
if "asignaturas" not in st.session_state:
    st.session_state["asignaturas"] = pd.DataFrame(
        columns=["Asignatura", "Tipología", "Nota", "Créditos"]
    )

# Entrada de datos
st.subheader("Agregar Asignatura")
asignatura = st.text_input("Nombre de la asignatura:")
tipologia = st.selectbox(
    "Tipología de la asignatura:",
    [
        "Fundamentación obligatoria",
        "Fundamentación optativa",
        "Disciplinar obligatoria",
        "Disciplinar optativa",
        "Libre elección",
        "Trabajo de grado",
    ],
)
nota = st.number_input("Nota definitiva (0.0 - 5.0):", min_value=0.0, max_value=5.0, step=0.1)
creditos = st.number_input("Número de créditos:", min_value=1, step=1)

# Agregar asignatura
if st.button("Agregar asignatura"):
    nueva_fila = pd.DataFrame(
        {
            "Asignatura": [asignatura],
            "Tipología": [tipologia],
            "Nota": [nota],
            "Créditos": [creditos],
        }
    )
    st.session_state["asignaturas"] = pd.concat(
        [st.session_state["asignaturas"], nueva_fila], ignore_index=True
    )
    st.success("Asignatura agregada exitosamente.")

# Mostrar asignaturas
st.subheader("Asignaturas registradas")
if st.session_state["asignaturas"].empty:
    st.write("No hay asignaturas registradas.")
else:
    st.dataframe(st.session_state["asignaturas"])

# Cálculo del PAPA global
st.subheader("Cálculo del PAPA Global")
if not st.session_state["asignaturas"].empty:
    df = st.session_state["asignaturas"]
    total_pesos = (df["Nota"] * df["Créditos"]).sum()
    total_creditos = df["Créditos"].sum()
    papa_global = total_pesos / total_creditos if total_creditos > 0 else 0

    st.write(f"**PAPA Global:** {papa_global:.2f}")

# Cálculo del PAPA por tipología
st.subheader("Cálculo del PAPA por Tipología")
if not st.session_state["asignaturas"].empty:
    tipologias = df["Tipología"].unique()
    for tip in tipologias:
        df_tip = df[df["Tipología"] == tip]
        total_pesos_tip = (df_tip["Nota"] * df_tip["Créditos"]).sum()
        total_creditos_tip = df_tip["Créditos"].sum()
        papa_tip = total_pesos_tip / total_creditos_tip if total_creditos_tip > 0 else 0

        st.write(f"**{tip}:** {papa_tip:.2f}")

# Cálculo del porcentaje de avance
st.subheader("Porcentaje de Avance en la Carrera")
if not st.session_state["asignaturas"].empty:
    creditos_acumulados = df["Créditos"].sum()
    porcentaje_avance = (creditos_acumulados / 160) * 100
    st.write(
        f"Has completado {creditos_acumulados} créditos de 160 necesarios para graduarte "
        f"(Ingeniería de Sistemas e Informática)."
    )
    st.write(f"**Porcentaje de avance:** {porcentaje_avance:.2f}%")

# Ejemplo de formato CSV
st.subheader("Ejemplo de formato CSV")
st.write("""
    Asignatura,Calificación,Créditos,Tipología
    Cálculo 1,4.5,5,Fundamentación obligatoria
    Programación,4.7,4,Disciplinar obligatoria
    Física,3.8,5,Fundamentación optativa
    Base de datos,4.2,3,Disciplinar optativa
""")
st.write("El archivo CSV debe estar separado por comas `,`.")

# Descarga de datos
st.download_button(
    label="Descargar datos",
    data=st.session_state["asignaturas"].to_csv(index=False),
    file_name="asignaturas.csv",
    mime="text/csv",
)

# Carga de datos
st.subheader("Carga tus datos")
archivo = st.file_uploader("Sube un archivo CSV con tus asignaturas:", type="csv")
if archivo:
    try:
        st.session_state["asignaturas"] = pd.read_csv(archivo)
        st.success("Datos cargados exitosamente.")
    except Exception as e:
        st.error(f"Hubo un error al cargar el archivo: {e}")
