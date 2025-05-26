#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2025 Javier Gómez - lalax-systems
MIT License

Script de extracción de datos Forex para sistemas de IA:
- Descarga históricos de Yahoo Finance
- Guarda en formato CSV
- Manejo de errores integrado
"""
import yfinance as yf
import pandas as pd
from datetime import datetime

def download_forex_data(ticker, start_date, end_date):
    """
    Descarga datos históricos de Forex desde Yahoo Finance
    
    Args:
        ticker (str): Par de divisas (ej: 'EURUSD=X')
        start_date (str): Fecha inicio formato 'YYYY-MM-DD'
        end_date (str): Fecha fin formato 'YYYY-MM-DD'
    
    Returns:
        pd.DataFrame: Datos OHLCV o None si hay error
    
    Example:
        >>> download_forex_data('EURUSD=X', '2020-01-01', '2023-12-31')
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        filename = f"../data/{ticker.replace('=X', '').lower()}_daily.csv"
        data.to_csv(filename)
        print(f"Datos guardados en {filename}")
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    download_forex_data('EURUSD=X', '2022-01-01', datetime.now().strftime('%Y-%m-%d'))