# Ising Model Simulation

A simple Python implementation of the 2D Ising model with interactive visualization.

## Overview

This program simulates the Ising model, which is a mathematical model used in statistical mechanics to study ferromagnetism. The model consists of a lattice of "spins" that can be in one of two states (up/down or +1/-1). Each spin interacts with its nearest neighbors, with the system evolving according to thermodynamic principles.

## Features

- Interactive visualization of the 2D Ising model using Matplotlib
- Real-time temperature adjustment via a slider
- Live magnetization calculation and display
- Periodic boundary conditions to eliminate edge effects
- Metropolis algorithm for Monte Carlo simulation
- Customizable parameters (lattice size, temperature, interaction strength)

## Requirements

- Python 3.6 or higher
- NumPy
- Matplotlib

## Installation

1. Ensure you have Python installed on your system
2. Install the required dependencies:

```bash
pip install numpy matplotlib
```

3. Download the `ising_model_simulation.py` file

## Usage

Run the program from the command line:

```bash
python ising_model_simulation.py
```

When prompted, you can enter custom values for:
- Lattice size (default: 50)
- Temperature (default: 2.0)
- Interaction strength J (default: 1.0)

Or simply press Enter to use the default values.

## Understanding the Simulation

### Parameters

- **Lattice Size**: Controls the dimensions of the square grid. Larger values provide more detailed simulations but require more computation.
- **Temperature (T)**: Controls the thermal energy in the system. 
  - At low temperatures (T < 2.27), the system tends toward order (ferromagnetic phase).
  - At high temperatures (T > 2.27), the system tends toward disorder (paramagnetic phase).
  - Near T ≈ 2.27 (the critical temperature), the system exhibits interesting phase transition behavior.
- **Interaction Strength (J)**: Controls the strength of coupling between neighboring spins. Positive values (default) encourage spins to align in the same direction.

### Visualization

- **Black/White Grid**: Represents the spin configuration. Black cells are spins in the -1 state, white cells are in the +1 state.
- **Magnetization**: The average spin value across the lattice. Values close to +1 or -1 indicate ordered states, while values near 0 indicate disordered states.

### Interactive Controls

- **Temperature Slider**: Adjust this to see how the system behaves at different temperatures. Moving the slider up (higher temperature) will introduce more randomness, while moving it down will promote order.

## Physics Background

The Ising model simulates the behavior of magnetic materials:

- Each cell represents a magnetic dipole (or "spin")
- Neighboring spins interact with energy E = -J × s₁ × s₂
- The Metropolis algorithm simulates thermal fluctuations according to the Boltzmann distribution
- The system tends to minimize energy while maximizing entropy

At low temperatures, energy minimization dominates, leading to ordered configurations. At high temperatures, entropy maximization dominates, leading to disordered configurations.

## License

This code is provided for educational purposes and is free to use and modify.
