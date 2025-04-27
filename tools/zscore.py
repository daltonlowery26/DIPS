import numpy as np
import pandas as pd 

def normalize(input_df):
    # Verify input_df has required columns
    required_cols = ['Season', 'Name', 'PA']
    if not all(col in input_df.columns for col in required_cols):
        raise ValueError(f"Input DataFrame must contain columns: {required_cols}")
    
    def mean_year(group):
        weights = group.index.map(lambda x: input_df.loc[x, 'PA'])
        if (weights <= 0).any():
            weights = None  # Fall back to unweighted if invalid PA values
        avg = np.average(group, weights=weights)
        return avg

    def calculate_weighted_std(group):
        weights = group.index.map(lambda x: input_df.loc[x, 'PA'])
        if (weights <= 0).any():
            weights = None  # Fall back to unweighted if invalid PA values
        avg = np.average(group, weights=weights)
        variance = np.average((group - avg)**2, weights=weights)
        return np.sqrt(variance)
    

    # Calculate means
    mean_values = pd.DataFrame(index=input_df['Season'].unique())
    for col in input_df.select_dtypes(include=[np.number]).columns:
        if col not in ['Season', 'MLBAMID']:
            yearly_mean = input_df.groupby('Season')[col].apply(mean_year)
            mean_values[col] = yearly_mean
    mean_values = mean_values.reset_index().rename(columns={'index': 'Season'})
    mean_values = mean_values.sort_values(by=['Season'])

    # Calculate standard deviations
    std_values = pd.DataFrame(index=input_df['Season'].unique())
    for col in input_df.select_dtypes(include=[np.number]).columns:
        if col not in ['Season', 'MLBAMID']:
            yearly_std = input_df.groupby('Season')[col].apply(calculate_weighted_std)
            std_values[col] = yearly_std
    std_values = std_values.reset_index().rename(columns={'index': 'Season'})
    std_values = std_values.sort_values(by=['Season'])

    def z_scores(player_df, mean_df, std_df):
        # Only select numeric columns excluding Season and MLBAMID
        numeric_cols = player_df.select_dtypes(include=[np.number]).columns
        numeric_cols = [col for col in numeric_cols if col not in ['Season', 'MLBAMID']]
        
        z_scores = pd.DataFrame(index=player_df.index)
        z_scores['Name'] = player_df['Name']  # Add Name first
        z_scores['Season'] = player_df['Season']  # Add Season

        # Calculate z-scores for each column
        for col in numeric_cols:
            for idx in player_df.index:
                season = player_df.loc[idx, 'Season']
                value = player_df.loc[idx, col]
                mean = mean_df.loc[mean_df['Season'] == season, col].iloc[0]
                std = std_df.loc[std_df['Season'] == season, col].iloc[0]
                if std == 0:  # Avoid division by zero
                    z_scores.loc[idx, col] = 100
                else:
                    z_scores.loc[idx, col] = 100 + ((value - mean) / std * 10)

        return z_scores

    # Calculate and return z-scores
    return z_scores(input_df, mean_df=mean_values, std_df=std_values)
