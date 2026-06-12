import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="CKD Prediction App",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# IMPORTS
# ==========================================

from about import show_about
from user_instructions import show_instructions
from model import show_model
from medicalinfo import show_medicalinfo
from history import show_prediction_history
from login import login_user
from register import register_user

# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Sidebar width */
section[data-testid="stSidebar"]{
    width:280px !important;
}

/* Main page spacing */
.main .block-container{
    padding-top:1.5rem;
}

/* Hide default radio label spacing */
div.row-widget.stRadio > div{
    flex-direction:column;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# AFTER LOGIN
# ==========================================

if st.session_state["logged_in"]:

    # --------------------------------------
    # SIDEBAR HEADER
    # --------------------------------------

    st.sidebar.markdown("""
    <h2 style='text-align:center;'>
    🩺 CKD System
    </h2>
    """, unsafe_allow_html=True)

    # --------------------------------------
    # WELCOME CARD
    # --------------------------------------

    st.sidebar.markdown(
        f"""
        <div style="
            background:linear-gradient(135deg,#2563EB,#1D4ED8);
            padding:15px;
            border-radius:12px;
            text-align:center;
            color:white;
            margin-bottom:20px;
            font-size:18px;
            font-weight:600;
        ">
            👋 Welcome<br>
            {st.session_state['user_name']}
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------
    # NAVIGATION
    # --------------------------------------

    st.sidebar.markdown("### 🧭 Navigation")

    page = st.sidebar.radio(
        "",
        [
            "📖 About The Project",
            "📋 User Instructions",
            "🏥 Medical Reference",
            "🧪 Model",
            "📜 Prediction History"
        ]
    )

    # --------------------------------------
    # PUSH LOGOUT LOWER
    # --------------------------------------

    st.sidebar.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

    if st.sidebar.button(
        "🚪 Logout",
        use_container_width=True
    ):
        st.session_state.clear()
        st.rerun()

    # --------------------------------------
    # PAGE ROUTING
    # --------------------------------------

    if page == "📖 About The Project":
        show_about()

    elif page == "📋 User Instructions":
        show_instructions()

    elif page == "🏥 Medical Reference":
        show_medicalinfo()

    elif page == "🧪 Model":
        show_model()
    elif page == "📜 Prediction History":
        show_prediction_history(
            st.session_state["user_id"]
        )

# ==========================================
# LOGIN / REGISTER SCREEN
# ==========================================

else:

    left_col, divider_col, right_col = st.columns([6.3, 0.15, 3.55])

    with left_col:

        hero_img, hero_text = st.columns([1.4, 3.6])
        with hero_img:

            st.image(
                "kidney.png",
                width=320
            )
        with hero_text:
            st.markdown("""
            <h1 style="
                font-size:48px;
                font-weight:800;
                line-height:1.2;
                margin-top:0px;
                margin-bottom:10px;
            ">
            Chronic&nbsp;Kidney&nbsp;Disease
            <br>
            Prediction System🩺
            </h1>
            """, unsafe_allow_html=True)

            st.markdown("""
            <p style="
                color:#94A3B8;
                font-size:24px;
                font-weight:500;
            ">
            AI-Powered Kidney Health Assessment
            </p>
            """, unsafe_allow_html=True)

        st.markdown("""
        <style>

        .feature-grid{
        display:grid;
        grid-template-columns:1fr 1fr;
        gap:10px;
        margin-top:30px;
        }

        .feature-card{
        background:#1E293B;
        padding:12px;
        border-radius:12px;
        text-align:center;
        border:1px solid #334155;
        }

        .feature-icon{
        font-size:26px;
        margin-bottom:5px;
        }

        .feature-title{
        font-size:15px;
        font-weight:600;
        color:white;
        }

        </style>

        <div class="feature-grid">

        <div class="feature-card">
        <div class="feature-icon">🩺</div>
        <div class="feature-title">Early Risk Detection</div>
        </div>

        <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">eGFR Calculator</div>
        </div>

        <div class="feature-card">
        <div class="feature-icon">🔬</div>
        <div class="feature-title">Explainable AI</div>
        </div>

        <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Clinical Insights</div>
        </div>

        </div>
        """, unsafe_allow_html=True)
    # -------------------------------------- # CENTER DIVIDER # --------------------------------------
    with divider_col: st.markdown("""
     <div style=" 
     border-left:2px solid #334155;
      height:700px; 
      margin:auto; "> 
    </div> 
    """, unsafe_allow_html=True)

    with right_col:

        option = st.radio(
            "",
            ["Login", "Register"],
            horizontal=True
        )

        if option == "Login":
            login_user()
        else:
            register_user()