import matplotlib.pyplot as plt

water_temperature = 25
water_mass = 1
specific_heat = 4186
ambient_temperature = 25

heater_power = float(input("Enter heater power (W): "))
target_temperature = float(input("Enter target temperature (°C): "))

time_data = []
temperature_data = []

for second in range(300):

    if water_temperature < target_temperature:

        heat_energy = heater_power * 1

        heat_loss = 0.1 * (water_temperature - ambient_temperature)

        net_heat = heat_energy - heat_loss

        temperature_change = net_heat / (water_mass * specific_heat)

        water_temperature += temperature_change

    else:
        print("Target temperature reached!")
        break

    time_data.append(second + 1)
    temperature_data.append(water_temperature)

print("Final Water Temperature:",
      round(water_temperature, 2), "°C")

plt.plot(time_data, temperature_data)

plt.xlabel("Time (seconds)")
plt.ylabel("Water Temperature (°C)")
plt.title("Water Heating Digital Twin")

plt.show()