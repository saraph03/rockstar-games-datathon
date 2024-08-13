import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

player_data = pd.read_csv('merged_file.csv')

# Ensure the date columns are in datetime format
player_data['first_day_played'] = pd.to_datetime(player_data['first_day_played'])
player_data['last_play_date'] = player_data['first_day_played'] + pd.to_timedelta(player_data['ltd_days_played'], unit='D')
retention_periods = [1, 5, 10, 15, 20, 25, 30]

def calculate_retention(data, retention_days):
    retention_counts = {}
    for days in retention_days: 
        data[f'retention_{days}_date'] = data['first_day_played'] + pd.Timedelta(days=days)
        
        
        retention_counts[days] = data.apply(lambda row: (row['last_play_date'] >= row[f'retention_{days}_date']) and (row['daily_playtime'] > 0), axis=1).mean()
        
    return retention_counts

# Calculate retention rates
retention_rates = calculate_retention(player_data, retention_periods)
print(retention_rates)

# Convert retention rates to a DataFrame for visualization
retention_df = pd.DataFrame(list(retention_rates.items()), columns=['Days', 'Retention Rate'])

# Plot the retention rates
plt.figure(figsize=(10, 6))
sns.barplot(x='Days', y='Retention Rate', data=retention_df)
plt.title('Player Retention Rates')
plt.xlabel('Days')
plt.ylabel('Retention Rate')
plt.show()







