import streamlit as st
import bcrypt
from db import get_connection


def login_user():

    st.markdown("""
    <style>

    .login-title{
        text-align:center;
        font-size:42px;
        font-weight:700;
        margin-bottom:5px;
    }

    .login-subtitle{
        text-align:center;
        color:#94A3B8;
        font-size:16px;
        margin-bottom:25px;
    }

    .login-card{
        margin-top:10px;
        max-width:350px;
        margin-left:auto;
        margin-right:auto;
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(12px);
        padding:30px;
        border-radius:20px;
        border:1px solid rgba(255,255,255,0.1);
        box-shadow:0 8px 32px rgba(0,0,0,0.3);
    }

    div[data-testid="stButton"] button{
        width:100%;
        border-radius:10px;
        height:50px;
        font-size:18px;
        font-weight:600;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="login-card">
        <div class="login-title">
        Welcome Back
        </div>

        <div class="login-subtitle">
        Login to access your CKD Prediction Dashboard
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        "<div style='height:15px'></div>",
        unsafe_allow_html=True
    )
    name = st.text_input(
        "👤 Name",
        key="login_name"
    )

    email = st.text_input(
        "📧 Email",
        key="login_email"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        key="login_password"
    )

    if st.button("Login"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE name=%s
            AND email=%s
            """,
            (name, email)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:

            stored_hash = user[3]

            if bcrypt.checkpw(
                password.encode("utf-8"),
                stored_hash.encode("utf-8")
            ):

                st.success("Login Successful ✅")

                st.session_state["logged_in"] = True
                st.session_state["user_id"] = user[0]
                st.session_state["user_name"] = user[1]
                st.session_state["user_email"] = user[2]

                st.rerun()

            else:
                st.error("Invalid Password ❌")

        else:
            st.error("User Not Found ❌")

    st.markdown("</div>", unsafe_allow_html=True)