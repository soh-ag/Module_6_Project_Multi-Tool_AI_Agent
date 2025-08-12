
import sqlite3
import csv

def create_database_and_import_data(db_name, csv_file, table_name, columns):
    """
    Creates a SQLite database, a table, and imports data from a CSV file.
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create table
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})")

        # Import data from CSV
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            for row in reader:
                cursor.execute(f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(columns))})", row)

        conn.commit()
        print(f"Database '{db_name}' and table '{table_name}' created successfully.")

    except sqlite3.Error as e:
        print(f"Error creating database or importing data: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # Heart Disease Dataset
    heart_disease_columns = [
        "age INTEGER", "sex INTEGER", "cp INTEGER", "trestbps INTEGER", "chol INTEGER",
        "fbs INTEGER", "restecg INTEGER", "thalach INTEGER", "exang INTEGER",
        "oldpeak REAL", "slope INTEGER", "ca INTEGER", "thal INTEGER", "target INTEGER"
    ]
    create_database_and_import_data(
        "heart_disease.db",
        "heart.csv",
        "heart_disease",
        heart_disease_columns
    )

    # Cancer Prediction Dataset
    cancer_columns = [
        "Age INTEGER", "Gender TEXT", "BMI REAL", "Smoking INTEGER", "GeneticRisk INTEGER",
        "PhysicalActivity REAL", "AlcoholIntake REAL", "CancerHistory INTEGER", "Diagnosis INTEGER"
    ]
    create_database_and_import_data(
        "cancer.db",
        "The_Cancer_data_1500_V2.csv",
        "cancer",
        cancer_columns
    )

    # Diabetes Dataset
    diabetes_columns = [
        "Pregnancies INTEGER", "Glucose INTEGER", "BloodPressure INTEGER",
        "SkinThickness INTEGER", "Insulin INTEGER", "BMI REAL",
        "DiabetesPedigreeFunction REAL", "Age INTEGER", "Outcome INTEGER"
    ]
    create_database_and_import_data(
        "diabetes.db",
        "diabetes.csv",
        "diabetes",
        diabetes_columns
    )
