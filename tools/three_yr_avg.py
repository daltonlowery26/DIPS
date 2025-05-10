import numpy as np
import pandas as pd

# three year avg of data

def three_year_avg(df):
    combined_rows = []
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols = [col for col in numeric_cols if col not in ['Season', 'Age', 'PA']]  # exclude Season, Age, PA

    for name, group in df.groupby('Name'):
        group_sorted = group.sort_values('Season')
        n = len(group_sorted)
        if n < 1:
            continue
        for i in range(n):
            window = group_sorted.iloc[i:i+3]
            if len(window) == 0:
                continue
            # Use the latest season and age in the window
            season_label = window.iloc[-1]['Season']
            age_label = window.iloc[-1]['Age']
            pa_label = window['PA'].mean()
            # Average numeric columns (except Season, Age, PA)
            averaged = window[numeric_cols].multiply(window['PA'], axis=0).sum() / window['PA'].sum()
            new_row = {'Name': name, 'Season': season_label, 'Age': age_label, 'PA': pa_label}
            for col in numeric_cols:
                new_row[col] = averaged[col]
            combined_rows.append(new_row)
            if i + 3 >= n:
                break

    avg_three = pd.DataFrame(combined_rows)
    return avg_three