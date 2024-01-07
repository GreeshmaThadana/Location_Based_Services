# Power consumption by different position technologies"

plt.figure(figsize=(10, 5))
Overall_power = df['Overall_power']
GPS_power = df['GPS_power']
Wifi_power = df['Wifi_power']
Cellular_power = df['Cellular_power']
plt.plot(GPS_power )
plt.plot(Wifi_power )
plt.plot(Cellular_power)

plt.xlabel('Number of Data points')
plt.ylabel('Power Consumption')

plt.title("Power consumption by different position technologies")
plt.legend(['GPS', 'Wifi', 'Cellular']);


# Accuracy in metres precision of different position technologies

plt.figure(figsize=(10, 5))

GPS_accuracy = df['GPS_accuracy']
Wifi_accuracy = df['Wifi_accuracy']
Cellular_accuracy = df['Cellular_accuracy']
plt.plot(GPS_accuracy )
plt.plot(Wifi_accuracy )
plt.plot(Cellular_accuracy)

plt.xlabel('Number of Data points')
plt.ylabel('Accuracy')

plt.title("Accuracy in metres precision of different position technologies")
plt.legend(['GPS', 'Wifi', 'Cellular']);


# Signal strength of position technologies 

plt.figure(figsize=(10, 5))

GPS_strength = df['GPS_strength']
Wifi_strength = df['Wifi_strength']
Cellular_strength = df['Cellular_strength']
plt.plot(GPS_strength )
plt.plot(Wifi_strength )
plt.plot(Cellular_strength)

plt.xlabel('Number of Data points')
plt.ylabel('Strength')


plt.title("Signal strength of position technologies ")
plt.legend(['GPS', 'Wifi', 'Cellular']);


# Frequency of Position fixes VS Accuracy

plt.figure(figsize=(10, 5))

Frequency = df['Frequency']
plt.plot(Frequency, GPS_accuracy,'ob'  )
plt.plot(Frequency, Wifi_accuracy, 'or' )
plt.plot(Frequency, Cellular_accuracy, 'og')

plt.xlabel('Frequency of Position fixes')
plt.ylabel('Accuracy')

plt.legend(['GPS', 'Wifi', 'Cellular']);


# Frequency of position fixes VS Power consumption

plt.figure(figsize=(10, 5))
Overall_power = df['Overall_power']
plt.plot(Frequency, GPS_power, 'or' )
plt.plot(Frequency, Wifi_power, 'ob')
plt.plot(Frequency, Cellular_power, 'og')

plt.xlabel('Frequency of position fixes')
plt.ylabel('Power Consumption')

plt.legend(['GPS', 'Wifi', 'Cellular']);


# Change in Power consumption by GPS and Wifi for a range of frequency

plt.figure(figsize=(10, 5))
Frequency = df['Frequency']
frequency_1 = []
frequency_2 = []
diff_frequency = []
gps_1 = []
gps_2 = []
diff_gps = []
wifi_1 = []
wifi_2 = []
diff_wifi = []
for i in range(len(Frequency)):
  if(Frequency[i] == 1):
    gps_1.append(GPS_power[i])
    wifi_1.append(Wifi_power[i])
  if(Frequency[i] == 2):
     gps_2.append(GPS_power[i])
     wifi_2.append(Wifi_power[i])
a = min(len(gps_1),len(gps_2))
for i in range(a):
   diff_gps.append(gps_2[i] - gps_1[i])

b = min(len(wifi_1),len(wifi_2))
for i in range(b):
   diff_wifi.append(wifi_2[i] - wifi_1[i])

plt.plot(diff_gps)
plt.plot(diff_wifi)

plt.xlabel('number of the row')
plt.ylabel('Power Consumption difference')

plt.title("Change in Power consumption by GPS and Wifi for a range of frequency")
plt.legend(['GPS', 'Wifi']);


# Change in power consumption due to switching and frequency changing

plt.figure(figsize=(10, 5))
diff_gps_wifi = []

b = min(len(wifi_1),len(gps_1))
for i in range(b):
   diff_gps_wifi.append(gps_1[i] - wifi_1[i])

plt.plot(diff_gps)
plt.plot(diff_gps_wifi)

plt.xlabel('number of the row')
plt.ylabel('Power Consumption difference')

plt.title("Change in power consumption due to switching and frequency changing ")
plt.legend(['Frequency_change', 'Switching']);



