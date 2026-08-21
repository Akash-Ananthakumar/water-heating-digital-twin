import matplotlib.pyplot as plt

water_temperature = 25 #starting temperature in Celsius
heater_power = 2000 #heater power in watts
water_mass = 1  #mass of water in kilograms
specific_heat = 4186    #specific heat capacity of water in J/(kg·°C)
ambient_temperature = 25    #ambient temperature in Celsius

time_data = [] #time data for plotting
temperature_data = [] #temperature data for plotting

for second in range(60):

    heat_energy = heater_power * 1

    heat_loss = 0.1 * (water_temperature - ambient_temperature)

    net_heat = heat_energy - heat_loss

    temperature_change = net_heat / (water_mass * specific_heat)

    water_temperature = water_temperature + temperature_change

    time_data.append(second + 1)
    temperature_data.append(water_temperature)

plt.plot(time_data, temperature_data)

plt.xlabel("Time (seconds)")
plt.ylabel("Water Temperature (°C)")
plt.title("Water Temperature vs Time")

plt.show()