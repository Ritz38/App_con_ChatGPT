import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración inicial
st.title("Gestión de Finanzas Personales")
st.write("Esta app fue elaborada por **Juan Pablo Zuluaga Mesa**")
st.write("Lleva un registro de tus presupuestos, ingresos, gastos y metas de ahorro.")

# Crear o cargar datos
if "finanzas" not in st.session_state:
    st.session_state["finanzas"] = pd.DataFrame(
        columns=["Fecha", "Tipo", "Categoría", "Monto", "Nota"]
    )

# Opciones de ingreso
tipo_registro = st.selectbox(
    "Selecciona el tipo de registro:",
    ["Presupuesto", "Ingreso", "Gasto", "Meta de ahorro"]
)

categoria = st.text_input("Categoría (ejemplo: Alimentos, Transporte, etc.):")
monto = st.number_input("Monto:", min_value=0.0, step=0.01)
nota = st.text_area("Nota adicional:")

# Registrar transacción
if st.button("Registrar"):
    nueva_fila = pd.DataFrame(
        {
            "Fecha": [datetime.now().strftime("%Y-%m-%d")],
            "Tipo": [tipo_registro],
            "Categoría": [categoria],
            "Monto": [monto],
            "Nota": [nota],
        }
    )
    st.session_state["finanzas"] = pd.concat(
        [st.session_state["finanzas"], nueva_fila], ignore_index=True
    )
    st.success("Registro guardado exitosamente.")

# Mostrar datos registrados
st.subheader("Historial de registros")
if st.session_state["finanzas"].empty:
    st.write("No hay registros disponibles.")
else:
    st.dataframe(st.session_state["finanzas"])

# Generar reportes
st.subheader("Generar Reportes")
periodo = st.selectbox("Selecciona el periodo:", ["Semanal", "Mensual"])
categoria_reporte = st.text_input(
    "Filtrar por categoría (opcional, deja en blanco para todas):"
)

if st.button("Generar Reporte"):
    df = st.session_state["finanzas"]
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    if periodo == "Semanal":
        filtro_fecha = df["Fecha"] >= (datetime.now() - pd.Timedelta(days=7))
    elif periodo == "Mensual":
        filtro_fecha = df["Fecha"] >= (datetime.now() - pd.Timedelta(days=30))
    
    if categoria_reporte:
        df_reporte = df[filtro_fecha & (df["Categoría"] == categoria_reporte)]
    else:
        df_reporte = df[filtro_fecha]
    
    if df_reporte.empty:
        st.write("No hay datos disponibles para este periodo.")
    else:
        total_presupuesto = df_reporte[df_reporte["Tipo"] == "Presupuesto"]["Monto"].sum()
        total_ingresos = df_reporte[df_reporte["Tipo"] == "Ingreso"]["Monto"].sum()
        total_gastos = df_reporte[df_reporte["Tipo"] == "Gasto"]["Monto"].sum()
        total_ahorro = df_reporte[df_reporte["Tipo"] == "Meta de ahorro"]["Monto"].sum()
        diferencia = total_ingresos - total_gastos - total_presupuesto

        st.write(f"**Total presupuestado:** {total_presupuesto}")
        st.write(f"**Total ingresos:** {total_ingresos}")
        st.write(f"**Total gastos:** {total_gastos}")
        st.write(f"**Total metas de ahorro:** {total_ahorro}")
        st.write(f"**Diferencia (real vs presupuestado):** {diferencia}")

# Guardar y cargar datos
st.download_button(
    label="Descargar datos",
    data=st.session_state["finanzas"].to_csv(index=False),
    file_name="finanzas_personales.csv",
    mime="text/csv",
)

st.subheader("Carga tus datos")
archivo = st.file_uploader("Sube un archivo CSV con tus datos:", type="csv")
if archivo:
    st.session_state["finanzas"] = pd.read_csv(archivo)
    st.success("Datos cargados exitosamente.")
