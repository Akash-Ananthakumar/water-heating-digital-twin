# Day 4 - Temperature Data and Visualization

## Objective

Store the simulated water temperature over time and visualize the behavior of the water-heating system using a graph.

## New Concept

Instead of only calculating the final temperature, the simulation now records the temperature at every time step.

Two lists are used:

- `time_data` - Stores simulation time
- `temperature_data` - Stores water temperature

## Data Collection

At every simulation step:

```python
time_data.append(second + 1)
temperature_data.append(water_temperature)