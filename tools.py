import sqlite3
from googlesearch import search

def HeartDiseaseDBTool(query: str) -> str:
    """Connects to the heart disease database, executes a query, and returns the result."""
    try:
        conn = sqlite3.connect("heart_disease.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return str(result)
    except sqlite3.Error as e:
        return f"Error executing query: {e}"
    finally:
        if conn:
            conn.close()

def CancerDBTool(query: str) -> str:
    """Connects to the cancer database, executes a query, and returns the result."""
    try:
        conn = sqlite3.connect("cancer.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return str(result)
    except sqlite3.Error as e:
        return f"Error executing query: {e}"
    finally:
        if conn:
            conn.close()

def DiabetesDBTool(query: str) -> str:
    """Connects to the diabetes database, executes a query, and returns the result."""
    try:
        conn = sqlite3.connect("diabetes.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return str(result)
    except sqlite3.Error as e:
        return f"Error executing query: {e}"
    finally:
        if conn:
            conn.close()

def MedicalWebSearchTool(query: str) -> str:
    """Performs a web search for a given query and returns the top 5 results."""
    try:
        search_results = []
        for result in search(query, num_results=5):
            search_results.append(result)
        return "\n".join(search_results)
    except Exception as e:
        return f"Error performing web search: {e}"
