df = pd.read_csv("rerun.csv")

df.head()

"""
Overall_power	GPS_power	Wifi_power	Cellular_power	GPS_accuracy	Wifi_accuracy	Cellular_accuracy	GPS_strength	Wifi_strength	Cellular_strength	Battery_percentage	Frequency	Target
0	809.0	55.0	33.7	21.3	28.3	27.5	36.0	-48.2	-51.7	-67.1	13.600	3	3
1	809.0	55.0	33.7	21.3	28.3	27.5	36.0	-48.2	-51.7	-67.1	13.600	3	3
2	512.0	65.1	39.9	25.1	19.9	29.4	49.5	-42.8	-53.4	-71.8	23.600	4	3
3	512.0	65.1	39.9	25.1	19.9	29.4	49.5	-42.8	-53.4	-71.8	23.600	4	3
4	721.0	73.1	34.9	20.3	19.9	20.8	37.1	-50.9	-80.0	-63.6	0.262	1	3
"""

df.tail()

df.columns.tolist()

df.describe()

df['Overall_power'].value_counts()

