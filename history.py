import streamlit as st
import pandas as pd
from database import get_prediction_history
def show_prediction_history(user_id):

    st.title("📜 Prediction History")

    history_df = get_prediction_history(user_id)

    if history_df.empty:

        st.info("No prediction history available.")

        return

    for _, row in history_df.iterrows():

        with st.expander(

            f"📅 {row['prediction_date']} | "
            f"{row['prediction_result']} | "
            f"{row['confidence_score']}%"

        ):

            st.write(
                f"**Prediction:** {row['prediction_result']}"
            )

            st.write(
                f"**Confidence:** {row['confidence_score']}%"
            )

            st.write(
                f"**eGFR:** {row['egfr']}"
            )

            input_df = pd.DataFrame({

                "Parameter":[

                    "Age",
                    "Blood Pressure",
                    "Specific Gravity",
                    "Albumin",
                    "Sugar",
                    "Blood Glucose Random",
                    "Blood Urea",
                    "Serum Creatinine",
                    "Sodium",
                    "Potassium",
                    "Hemoglobin",
                    "Packed Cell Volume",
                    "WBC Count",
                    "RBC Count",
                    "Hypertension",
                    "Diabetes",
                    "CAD",
                    "Appetite",
                    "Pedal Edema",
                    "Anemia"

                ],

                "Value":[

                    row["age"],
                    row["blood_pressure"],
                    row["specific_gravity"],
                    row["albumin"],
                    row["sugar"],
                    row["blood_glucose_random"],
                    row["blood_urea"],
                    row["serum_creatinine"],
                    row["sodium"],
                    row["potassium"],
                    row["hemoglobin"],
                    row["packed_cell_volume"],
                    row["white_blood_cell_count"],
                    row["red_blood_cell_count"],
                    row["hypertension"],
                    row["diabetes_mellitus"],
                    row["cad"],
                    row["appetite"],
                    row["pedal_edema"],
                    row["anemia"]

                ]

            })

            st.dataframe(
                input_df,
                use_container_width=True,
                hide_index=True
            )