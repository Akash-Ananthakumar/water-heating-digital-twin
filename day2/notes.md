# Day 2 - Basic Water Heating Model

## Objective

Build a simple mathematical model to calculate how the temperature of water changes when heat is supplied by a heater.

## Variables

- `water_temperature` - Current temperature of the water in °C
- `heater_power` - Heater power in Watts (W)
- `water_mass` - Mass of water in kilograms (kg)
- `specific_heat` - Specific heat capacity of water
- `time` - Heating time in seconds

## Important Concepts

### Heat Energy

The energy supplied by the heater is:

Q = P × t

Where:

- Q = Heat energy in Joules
- P = Heater power in Watts
- t = Time in seconds

### Temperature Change

Temperature change is calculated using:

ΔT = Q / (m × c)

Where:

- ΔT = Change in temperature
- Q = Heat energy
- m = Mass of water
- c = Specific heat capacity

For water:

c ≈ 4186 J/(kg·°C)

## Model Flow

Heater Power
→ Heat Energy
→ Temperature Change
→ Updated Water Temperature

## Result

The model calculates the water temperature after a given amount of heating time.

## Digital Twin Concept

This is the first basic physics model of the water heating system.

The mathematical model represents the behavior of the physical water-heating system.