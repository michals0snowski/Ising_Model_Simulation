import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

class IsingModel:
    def __init__(self, size=50, temp=2.0, J=1.0):
        """
        Initialize the Ising model.
        
        Parameters:
        size (int): Size of the square lattice
        temp (float): Temperature (in units where k_B=1)
        J (float): Interaction strength between spins
        """
        self.size = size
        self.temp = temp
        self.J = J
        
        # Initialize random spin configuration
        self.spins = np.random.choice([-1, 1], size=(size, size))
        
        # For animation
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.img = self.ax.imshow(self.spins, cmap='binary', interpolation='nearest')
        self.ax.set_title(f'Ising Model at T={self.temp:.2f}')
        
        # Add temperature slider
        self.fig.subplots_adjust(bottom=0.15)
        self.temp_slider_ax = self.fig.add_axes([0.25, 0.05, 0.65, 0.03])
        self.temp_slider = Slider(
            self.temp_slider_ax, 'Temperature', 0.1, 5.0, 
            valinit=self.temp, valstep=0.1
        )
        self.temp_slider.on_changed(self.update_temp)
        
        # Status text
        self.status_text = self.ax.text(
            0.02, 0.95, f"Magnetization: {self.calculate_magnetization():.3f}", 
            transform=self.ax.transAxes,
            color='white', backgroundcolor='black'
        )
    
    def update_temp(self, val):
        """Update temperature when slider is adjusted"""
        self.temp = val
        self.ax.set_title(f'Ising Model at T={self.temp:.2f}')
    
    def calculate_energy(self, i, j):
        """Calculate energy for a spin at position (i, j)"""
        neighbors_sum = (
            self.spins[(i+1) % self.size, j] + 
            self.spins[(i-1) % self.size, j] + 
            self.spins[i, (j+1) % self.size] + 
            self.spins[i, (j-1) % self.size]
        )
        return -self.J * self.spins[i, j] * neighbors_sum
    
    def metropolis_step(self):
        """Perform one step of the Metropolis algorithm"""
        for _ in range(self.size * self.size):
            # Choose a random spin
            i, j = np.random.randint(0, self.size, 2)
            
            # Calculate energy change if this spin is flipped
            current_energy = self.calculate_energy(i, j)
            self.spins[i, j] *= -1  # Flip the spin
            new_energy = self.calculate_energy(i, j)
            delta_E = new_energy - current_energy
            
            # Metropolis acceptance criterion
            if delta_E > 0 and np.exp(-delta_E / self.temp) < np.random.random():
                self.spins[i, j] *= -1  # Flip back if not accepted
    
    def calculate_magnetization(self):
        """Calculate the average magnetization of the system"""
        return np.mean(self.spins)
    
    def update_plot(self, frame):
        """Update function for animation"""
        self.metropolis_step()
        self.img.set_array(self.spins)
        mag = self.calculate_magnetization()
        self.status_text.set_text(f"Magnetization: {mag:.3f}")
        return [self.img, self.status_text]
    
    def run_simulation(self):
        """Run the simulation with animation"""
        ani = animation.FuncAnimation(
            self.fig, self.update_plot, frames=100,
            interval=50, blit=True
        )
        plt.show()

def main():
    # Get user input for parameters
    print("Ising Model Simulation")
    print("=====================")
    try:
        size = int(input("Enter lattice size (default=50): ") or 50)
        temp = float(input("Enter temperature (default=2.0): ") or 2.0)
        J = float(input("Enter interaction strength J (default=1.0): ") or 1.0)
    except ValueError:
        print("Invalid input. Using default values.")
        size, temp, J = 50, 2.0, 1.0
    
    # Create and run simulation
    model = IsingModel(size=size, temp=temp, J=J)
    model.run_simulation()

if __name__ == "__main__":
    main()
