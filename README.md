Warehouse AI – Demand Forecasting and Inventory Optimization System
Overview

Warehouse AI is an end-to-end demand forecasting and inventory optimization system built using Python. The project simulates product demand, forecasts future sales using time-series modeling, and calculates optimal inventory levels through an interactive dashboard.

The goal of this project is to demonstrate how machine learning and statistical modeling can be applied to real-world supply chain and inventory management problems.

Problem Statement

Inventory mismanagement leads to stockouts, overstocking, and financial losses. Businesses need accurate demand forecasting to:

Predict future product demand

Maintain optimal stock levels

Reduce holding costs

Avoid stock shortages

This project provides a complete pipeline to address these challenges.

Project Architecture

The system follows this workflow:

Data Scraping
Product data is scraped from an e-commerce demo website and stored as raw data.

Demand Simulation
Weekly demand data is generated from raw product data to simulate historical sales.

Forecasting
Facebook Prophet is used to forecast future demand based on historical trends.

Inventory Optimization
Reorder point and safety stock are calculated using statistical methods.

Dashboard
Streamlit provides an interactive interface for selecting products and visualizing forecasts.

Project Structure
warehouse-ai-demand-forecasting/
│
├── data/
│   ├── raw_data.csv
│   ├── demand_data.csv
│
├── src/
│   ├── scraper.py
│   ├── preprocessing.py
│   ├── forecasting.py
│   ├── inventory_optimizer.py
│   ├── dashboard.py
│
├── requirements.txt
├── README.md
└── .gitignore
Technologies Used

Python

Pandas

NumPy

Prophet (Time-Series Forecasting)

Streamlit

BeautifulSoup

Requests

Forecasting Method

The project uses Prophet for time-series forecasting. The model:

Learns trend and weekly seasonality

Generates future demand predictions

Provides upper and lower confidence intervals

This allows businesses to estimate expected demand and uncertainty.

Inventory Optimization Logic

The system calculates:

Reorder Point
Reorder Point = Average Demand × Lead Time

Safety Stock
Safety Stock = Service Factor × Standard Deviation × √Lead Time

These metrics help maintain optimal inventory levels while accounting for demand variability.

How to Run the Project

Clone the repository

git clone https://github.com/YOUR_USERNAME/warehouse-ai-demand-forecasting.git
cd warehouse-ai-demand-forecasting

Create virtual environment

python -m venv venv
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Generate data (first time only)

python src/scraper.py
python src/preprocessing.py

Run the dashboard

python -m streamlit run src/dashboard.py

The application will open in your browser.

Key Features

Automated product data scraping

Weekly demand simulation

Time-series demand forecasting

Reorder point and safety stock calculation

Interactive dashboard for visualization