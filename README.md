Description:
These datafiles contain information about how Grand Theft Auto Online players interact with gameplay content, purchase items, and generally engage with the online world. 
Sample: 9,476 players with 3 months of gameplay data
The data is segmented into three datafiles: 
1. General player statistics: player_statistics.csv
2. Item Spend: item_spend.csv
3. Activities Played: player_activity.csv
The datafiles are all comma-delineated and the contents of each are described in more detail below. All three datasets can be joined together using the following columns: account_id, platform_id, and occur_date. 

Data Dictionary
General Player Statistics
This csv file is named player_statistics.csv and contains the following columns:
Column Name	Data Type	Description
account_id	bigint	Unique account ID tied to platform
platform_id	string	Platform indicator (PC, PS4, XBOX)
occur_date	date	Date field in the format YYYY-MM-DD (day of occurrence)
ltd_days_played	bigint	Lifetime days played as of the date
first_day_played	timestamp	First login date for the account
evc_balance	bigint	Earned (via in-game activities) GTA$ balance at the end of the day 
pvc_balance	bigint	Paid (with $USD) GTA$ balance at the end of the day
char_rank	bigint	Main character rank
daily_playtime	double	Playtime for the date (in hours)
days_since_first	bigint	Days since first day played as of the date

Item Spend
This csv file is named item_spend.csv and contains the following columns:
Column Name	Data Type	Description
account_id	bigint	Unique account ID tied to platform
platform_id	string	Platform indicator (PC, PS4, XBOX)
occur_date	date	Date field in the format YYYY-MM-DD (day of occurrence)
item	string	Item name (as seen in game)
item_type	string	Item type descriptor (vehicle, property, weapon)
item_sub_type	string	Secondary item type descriptor (car, helicopter, garage, etc.)
money_spent	bigint	GTA$ spent


Activity Played
This csv file is named player_activity.csv and contains the following columns:
Column Name	Data Type	Description
account_id	bigint	Unique account ID tied to platform
platform_id	string	Platform indicator (PC, PS4, XBOX)
occur_date	date	Date field in the format YYYY-MM-DD (day of occurrence)
activity_type	string	Broad activity category (Heist, Races, Biker Missions, etc.)
time_spent	double	Time spent in activity (in hours)
kills	bigint	Number of kills during activity
deaths	bigint	Number of deaths during activity
suicides	bigint	Number of suicides during activity
money_earned	bigint	GTA$ earned in activity
rp_earned	bigint	RP (experience) earned in activity
success	tinyint	Indicator of a successful activity conclusion (0: Failure, 1: Success)
money_vs_time_spent	double	(money_earned + 1) / time_spent
rp_vs_time_spent	double	(rp_earned + 1) / time_spent


