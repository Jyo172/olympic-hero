# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
#Code starts here
data = pd.read_csv(path)
data = data.rename(columns={'Total':'Total_Medals'})
print(data.head(10))


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'], 'Both', np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', 'Winter'))
better_event = data['Better_Event'].value_counts().index[0]
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries.drop(len(top_countries)-1)
def top_ten(df,col):
    country_list = []
    country_list = list(df.nlargest(10,col)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
test_list = [top_10_summer,top_10_winter,top_10]
common = list(set.intersection(*map(set, test_list)))
print(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1)
ax_1 = summer_df.plot.bar(x='Country_Name', y='Total_Summer')
ax_1.set_title('Summer')
ax_2 = winter_df.plot.bar(x='Country_Name', y='Total_Winter')
ax_2.set_title('Winter')
ax_3 = top_df.plot.bar(x='Country_Name', y='Total_Medals')
ax_3.set_title('Total_Medals')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)
print(winter_country_gold)
print(top_country_gold)



# --------------
#Code starts here
data_1 = data.drop(len(data)-1)
data_1['Total_Points'] = 3*data_1['Gold_Total']+2*data_1['Silver_Total']+1*data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points,best_country)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar',stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


