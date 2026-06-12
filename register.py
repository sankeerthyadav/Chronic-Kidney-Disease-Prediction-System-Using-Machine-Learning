import streamlit as st
import bcrypt

from db import get_connection


def register_user():

    st.subheader("Register")

    name = st.text_input(
        "Name",
        key="register_name"
    )

    email = st.text_input(
        "Email",
        key="register_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="register_password"
    )

    if st.button("Register"):

        if not name or not email or not password:
            st.warning("Please fill all fields")
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email=%s
            """,
            (email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:

            st.error("Email already registered ❌")

        else:

            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")

            cursor.execute(
                """
                INSERT INTO users(
                    name,
                    email,
                    password
                )
                VALUES(%s,%s,%s)
                """,
                (
                    name,
                    email,
                    hashed_password
                )
            )

            conn.commit()

            st.success(
                "Registration Successful ✅"
            )

        cursor.close()
        conn.close()