import pandas as pd
import numpy as np

def calculate_reorder_and_safety_stock(forecasted_df, lead_time=2, service_factor=1.65):
    avg_demand = forecasted_df['yhat'].mean()
    std_dev = forecasted_df['yhat'].std()

    reorder_point = avg_demand * lead_time
    safety_stock = service_factor * std_dev * (lead_time ** 0.5)

    return {
        'Reorder Point': round(reorder_point),
        'Safety Stock': round(safety_stock)
    }
