from db import get_connection
def create_prediction_history_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_history (

        id INT AUTO_INCREMENT PRIMARY KEY,

        user_id INTEGER,

        prediction_date VARCHAR(50),

        prediction_result VARCHAR(50),

        confidence_score FLOAT,

        egfr FLOAT,

        age INT,
    blood_pressure FLOAT,
    specific_gravity FLOAT,
    albumin INT,
    sugar INT,

    blood_glucose_random FLOAT,
    blood_urea FLOAT,
    serum_creatinine FLOAT,
    sodium FLOAT,
    potassium FLOAT,

    hemoglobin FLOAT,
    packed_cell_volume FLOAT,
    white_blood_cell_count FLOAT,
    red_blood_cell_count FLOAT,

    hypertension VARCHAR(20),
    diabetes_mellitus VARCHAR(20),
    cad VARCHAR(20),
    appetite VARCHAR(20),
    pedal_edema VARCHAR(20),
    anemia VARCHAR(20),

    FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()

from datetime import datetime
def save_prediction_history(
    user_id,
    prediction_result,
    confidence_score,
    egfr,

    age,
    blood_pressure,
    specific_gravity,
    albumin,
    sugar,

    blood_glucose_random,
    blood_urea,
    serum_creatinine,
    sodium,
    potassium,

    hemoglobin,
    packed_cell_volume,
    white_blood_cell_count,
    red_blood_cell_count,

    hypertension,
    diabetes_mellitus,
    cad,
    appetite,
    pedal_edema,
    anemia
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO prediction_history(

        user_id,
        prediction_date,

        prediction_result,
        confidence_score,
        egfr,

        age,
        blood_pressure,
        specific_gravity,
        albumin,
        sugar,

        blood_glucose_random,
        blood_urea,
        serum_creatinine,
        sodium,
        potassium,

        hemoglobin,
        packed_cell_volume,
        white_blood_cell_count,
        red_blood_cell_count,

        hypertension,
        diabetes_mellitus,
        cad,
        appetite,
        pedal_edema,
        anemia

    )

    VALUES (
%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s,
%s,%s,%s,%s,%s,
%s,%s,%s,%s,
%s,%s,%s,%s,%s,%s
)
    """,

    (

        user_id,
        datetime.now().strftime("%d-%b-%Y %I:%M %p"),

        prediction_result,
        confidence_score,
        egfr,

        age,
        blood_pressure,
        specific_gravity,
        albumin,
        sugar,

        blood_glucose_random,
        blood_urea,
        serum_creatinine,
        sodium,
        potassium,

        hemoglobin,
        packed_cell_volume,
        white_blood_cell_count,
        red_blood_cell_count,

        hypertension,
        diabetes_mellitus,
        cad,
        appetite,
        pedal_edema,
        anemia

    ))

    conn.commit()
    cursor.close()
    conn.close()
import pandas as pd

def get_prediction_history(user_id):

    conn = get_connection()

    query = """
    SELECT *
    FROM prediction_history
    WHERE user_id = %s
    ORDER BY id DESC
    """

    history_df = pd.read_sql(
        query,
        conn,
        params=(user_id,)
    )

    conn.close()

    return history_df