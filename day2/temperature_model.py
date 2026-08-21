water_temperature = 25 #starting temperature in Celsius
heater_power = 1000 #heater power in watts
water_mass = 1  #mass of water in kilograms
specific_heat = 4186 #specific heat capacity of water in J/(kg·°C)
time = 1 #time in seconds

#using the formula Q = mcΔT, where Q is heat energy, m is mass, c is specific heat capacity, and ΔT is the change in temperature

heat_energy = heater_power * time

temperature_change = heat_energy / (water_mass * specific_heat)

water_temperature = water_temperature + temperature_change

print("Water Temperature:", water_temperature)