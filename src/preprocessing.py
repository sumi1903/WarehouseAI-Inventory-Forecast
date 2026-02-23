    import pandas as pd
    import numpy as np

    def generate_weekly_demand(input_csv='data/raw_data.csv', output_csv='data/demand_data.csv'):
        raw_df = pd.read_csv(input_csv)
        weeks = pd.date_range('2024-01-01', periods=20, freq='W')

        simulated = []
        for _, row in raw_df.iterrows():
            for week in weeks:
                demand = np.random.poisson(lam=10) + np.random.randint(0, 5)
                simulated.append({
                    'title': row['title'],
                    'week': week,
                    'demand': demand
                })

        df = pd.DataFrame(simulated)
        df.to_csv(output_csv, index=False)
        print("Saved:", output_csv)

    if __name__ == '__main__':
        generate_weekly_demand()