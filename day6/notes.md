# Day 6 - Target Temperature

## Objective

Improve the water-heating digital twin by allowing the user to specify a target temperature.

The simulation continues heating the water until the target temperature is reached.

## New Inputs

- `heater_power` - Power supplied by the heater in Watts
- `target_temperature` - Desired water temperature in °C

## Heating Logic

The model checks the current water temperature against the target temperature.

If:

`water_temperature < target_temperature`

The heater supplies energy to the water.

If:

`water_temperature >= target_temperature`

The simulation stops because the target temperature has been reached.

## Model Flow

User Input
→ Heater Power + Target Temperature
→ Heating Simulation
→ Calculate Heat Loss
→ Calculate Temperature Change
→ Update Water Temperature
→ Compare With Target
→ Target Reached?

## Example

Starting temperature: 25°C

Target temperature: 60°C

The simulation continues heating:

25°C → 30°C → 40°C → 50°C → 60°C

Once the target temperature is reached, the simulation stops.

## Digital Twin Concept

The model now has a desired operating condition.

Instead of simply calculating temperature, the digital twin can determine whether the simulated system has reached its target state.

## Day 6 Outcome

A target-temperature based heating simulation was implemented successfully.