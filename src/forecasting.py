# forecasting.py
import pandas as pd
from prophet import Prophet

def forecast_demand(item_title, forecast_period=4, input_csv='data/demand_data.csv'):
    df = pd.read_csv(input_csv)
    item_df = df[df['title'] == item_title][['week', 'demand']]
    item_df.columns = ['ds', 'y']
    item_df['ds'] = pd.to_datetime(item_df['ds'])

    model = Prophet()
    model.fit(item_df)

    future = model.make_future_dataframe(periods=forecast_period, freq='W')
    forecast = model.predict(future)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
