#!/usr/bin/env python3
"""
Cold Email Generator - Streamlit App Launcher
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the app
from app.main import create_streamlit_app
from app.chains import Chain
from app.portfolio import Portfolio
from app.utils import clean_text

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
