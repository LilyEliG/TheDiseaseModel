# TheDiseaseModel

Welcome to the Disease Spread Simulation project! In this project, you will implement a simulation to model the spread of a disease through a population. The simulation uses functions to represent the various aspects of disease transmission, recovery, and population dynamics.

## Project Goals

- Practice procedural programming and organizing code with functions.
- Explore how programming can be used to model or simulate a real-world process.

## Approach Overview

The simulation tracks the condition of each person in a population using the SIR model. People are classified as Susceptible ('S'), Infected ('I'), or Recovered ('R'). The simulation progresses through days, with infected individuals coming into contact with others, possibly leading to new infections or recoveries.

## Task 1: Implementing the Simulation

You'll write implementations for several functions in a Python file named `disease_model.py`. Each function focuses on a specific aspect of the simulation.

### Key Functions:
- `infect`: Determines if an infection occurs based on a given infection probability.
- `recover`: Simulates recovery of an infected person based on a recovery probability.
- `contact_indices`: Finds indices of people in contact with an infected person.
- `apply_recoveries`: Simulates recoveries for the entire population.
- `contact`: Simulates an infected person coming into contact with others.
- `apply_contacts`: Simulates infected people contacting others in the population.
- `population_SIR_counts`: Counts the number of susceptible, infected, and recovered individuals.

### Simulation Functions:
- `simulate_day`: Simulates one day of disease progression.
- `initialize_population`, `simulate_disease`, `peak_infections`, and `display_results`: Provided functions to complete the simulation.

Ensure to add type annotations, docstrings, and comments to your functions.

## Task 2: Using the Simulation

Answer questions in the `project9_template.txt` file regarding the impact of contact range on the peak number of infections.

## Additional Notes

The basic simulation can be improved in various ways. Consider factors such as permanent immunity, mortality rates, individual susceptibility, and community dynamics for a more realistic representation.

Enjoy exploring the world of disease spread simulation! If you encounter long simulation times, review your functions for errors or inefficiencies. Feel free to seek assistance if needed.
