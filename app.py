import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="IA - Cáncer de Mama",
    page_icon="🎗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
    }
    section[data-testid="stSidebar"] {
        background-color: #0F2D3C;
        color: white;
    }
    .highlight-pink {
        color: #E60067;
        font-size: 40px;
        font-weight: bold;
    }
    .badge-birads {
        color: #722ED1;
        font-size: 28px;
        font-weight: bold;
    }
    .badge-risk {
        color: #CF1322;
        font-size: 28px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# BARRA LATERAL - NAVEGACIÓN
with st.sidebar:
    st.markdown("### 🎗️ **IA - CÁNCER DE MAMA**")
    st.caption("Sistema de apoyo al diagnóstico")
    st.divider()
    
    st.radio(
        "Navegación", 
        ["Inicio", "Pacientes", "Estudios", "Resultados", "Historial", "Configuración", "Ayuda"],
        label_visibility="collapsed"
    )
    
    st.divider()
    st.info("🛡️ **Aviso:** Los resultados de IA son una herramienta de apoyo. La decisión final siempre es del médico.")

# ENCABEZADO
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("🎗️ IA – CÁNCER DE MAMA")
    st.caption("Sistema de apoyo al diagnóstico")
with col_head2:
    st.markdown("**Dr. Martínez**  \n*Oncología* 👨‍⚕️")
    st.button("📄 Reporte completo")

st.divider()

# COLUMNAS PRINCIPALES
col_left, col_right = st.columns([3, 2])

# ----- COLUMNA IZQUIERDA -----
with col_left:
    st.subheader("👤 Datos del paciente")
    p_col1, p_col2, p_col3 = st.columns([1, 2, 2])
    
    with p_col1:
        st.markdown("**ID:** P-0001256")
        st.markdown("**Edad:** 48 años")
        st.markdown("**Sexo:** Femenino")
    with p_col2:
        st.markdown("**Factores de riesgo:**")
        st.markdown("• Edad > 40 años\n• Menarquia temprana\n• Primer embarazo > 30 años\n• Uso de terapia hormonal")
    with p_col3:
        st.markdown("**Antecedentes familiares:**")
        st.markdown("• Madre con cáncer de mama\n• Tía materna con cáncer de mama")

    st.divider()

    st.subheader("📤 Carga de estudios")
    st.caption("Seleccione y cargue los estudios del paciente")
    
    img_col1, img_col2, img_col3, img_col4 = st.columns(4)
    with img_col1:
        st.markdown("**Mastografía**")
        st.caption("MG_2024_05_12.dcm")
        st.success("✔ Cargado")
    with img_col2:
        st.markdown("**Ultrasonido**")
        st.caption("US_2024_05_12.dcm")
        st.success("✔ Cargado")
    with img_col3:
        st.markdown("**Resonancia**")
        st.caption("RM_2024_05_12.dcm")
        st.success("✔ Cargado")
    with img_col4:
        st.markdown("**Biopsia**")
        st.caption("Bx_2024_05_14.dcm")
        st.success("✔ Cargado")

    st.file_uploader(
        "Arrastre aquí más estudios o haga clic para cargar (DICOM, JPG, PNG, PDF)",
        type=["dcm", "jpg", "png", "pdf"]
    )

    st.divider()

    st.subheader("📝 Notas del médico")
    st.text_area(
        "Observaciones:",
        placeholder="Escribe aquí tus observaciones...",
        max_chars=1000,
        height=100
    )

# ----- COLUMNA DERECHA -----
with col_right:
    st.subheader("🧠 Resultado de IA")
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.caption("Probabilidad de cáncer")
        st.markdown('<div class="highlight-pink">93%</div>', unsafe_allow_html=True)
    with res_col2:
        st.progress(0.93)
        st.caption("0% -------------------- 100%")

    st.divider()

    class_col1, class_col2 = st.columns(2)
    with class_col1:
        st.caption("Clasificación")
        st.markdown('<div class="badge-birads">BI-RADS 5</div>', unsafe_allow_html=True)
    with class_col2:
        st.caption("Nivel de riesgo")
        st.markdown('<div class="badge-risk">🔴 Alto</div>', unsafe_allow_html=True)

    st.divider()

    st.markdown("**Hallazgos detectados por IA**")
    st.markdown("🔬 **Masa irregular:** Lesión con bordes irregulares en cuadrante superoexterno.")
    st.markdown("🧫 **Microcalcificaciones:** Agrupaciones de microcalcificaciones pleomórficas.")
    st.markdown("🧬 **Ganglios sospechosos:** Ganglios axilares con engrosamiento cortical y pérdida de hilio graso.")

    st.divider()

    st.warning("⭐ **Recomendación:** Se recomienda realizar biopsia y valoración por oncología.")

    st.divider()

    st.subheader("Decisión del médico (obligatoria)")
    st.radio(
        "Seleccione una opción:",
        ["Confirmar diagnóstico", "Solicitar más estudios", "No confirmar"]
    )
    
    if st.button("💾 Guardar decisión", type="primary", use_container_width=True):
        st.success("Decisión guardada con éxito.")

# PIE DE PÁGINA
st.divider()
st.caption("ℹ️ Este sistema no reemplaza el juicio clínico del profesional de la salud. Los resultados deben interpretarse en el contexto clínico del paciente.")
