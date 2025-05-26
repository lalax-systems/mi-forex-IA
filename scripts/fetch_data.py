import yfinance as yf
import pandas as pd
from datetime import datetime

# Configuración
def download_forex_data(ticker, start_date, end_date):
    """
    Descarga datos históricos de Forex desde Yahoo Finance
    Ejemplo: download_forex_data('EURUSD=X', '2020-01-01', '2023-12-31')
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        filename = f"../data/{ticker.replace('=X', '').lower()}_daily.csv"
        data.to_csv(filename)
        print(f"Datos guardados en {filename}")
        return data
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_forex_data('EURUSD=X', '2022-01-01', datetime.now().strftime('%Y-%m-%d'))