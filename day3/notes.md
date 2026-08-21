# Day 3 - Heat Loss Model

## Objective

Improve the water heating model by including heat loss to the surrounding environment.

A real water-heating system does not only gain heat from the heater. It also loses heat to the surroundings.

## New Variable

- `ambient_temperature` - Temperature of the surrounding environment in °C

## Heat Loss

Heat loss is modeled using a simplified relationship:

Heat Loss = k × (Water Temperature - Ambient Temperature)

Where:

- k = Simplified heat-loss coefficient
- Water Temperature = Current water temperature
- Ambient Temperature = Surrounding temperature

## Important Concept

The greater the difference between the water temperature and ambient temperature, the greater the heat loss.

For example:

Water = 30°C  
Ambient = 25°C  
→ Small temperature difference  
→ Small heat loss

Water = 80°C  
Ambient = 25°C  
→ Large temperature difference  
→ Greater heat loss

## Net Heat

The actual energy added to the water is:

Net Heat = Heat Added - Heat Lost

The net heat is then used to calculate the temperature change.

## Model Flow

Heater Power
→ Heat Added
→ Subtract Heat Loss
→ Net Heat
→ Temperature Change
→ Updated Water Temperature

## Continuous Simulation

The model runs repeatedly over multiple time steps.

Example:

Time → Temperature

1 sec → 25.24°C  
2 sec → 25.48°C  
3 sec → 25.72°C  
...

This allows the model to represent how the water temperature changes over time.

## Digital Twin Concept

The model is becoming more representative of a real physical system because it considers both:

1. Energy supplied by the heater
2. Energy lost to the environment

## Limitation

The heat-loss equation is simplified for this prototype.

A real water-heating system would involve factors such as:

- Container material
- Surface area
- Thermal conductivity
- Convection
- Radiation
- Environmental conditions