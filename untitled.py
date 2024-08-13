import pandas as pd

df1 = pd.read_csv('item_spend.csv')
df2 = pd.read_csv('player_activity.csv')
df3 = pd.read_csv('player_statistics.csv')

merged_df = df1.merge(df2, on=['account_id', 'platform_id', 'occur_date'], how='inner')\
               .merge(df3, on=['account_id', 'platform_id', 'occur_date'], how='inner')

merged_df.to_csv('merged_file.csv', index=False)
