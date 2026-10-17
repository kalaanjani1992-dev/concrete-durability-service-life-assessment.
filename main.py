import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# --- Step 1: Define the Engineering Simulation Parameters ---
years =         # Time intervals to evaluate structural lifespan
depth_grid = np.linspace(0, 100, 500)  # Concrete cover depth grid from 0 to 100 mm
C0 = 4.5                                # Constant surface chloride concentration (kg/m³)
Ccrit = 1.2                             # Critical chloride threshold for rebar depassivation (kg/m³)
cover_depth = 50                        # Physical clear concrete cover depth over rebar (mm)

# Diffusion Coefficient (D) for standard prescriptive mix converted to mm²/year
D_control = 3.15e-8 * 31536000  

plt.figure(figsize=(10, 6))

# --- Step 2: Solve Fick's Second Law of Diffusion using the Error Function ---
for t in years:
    3. ![Chloride Profile](https://githubusercontent.com)
    # Closed-form error function solution to the 1D diffusion equation
    concentration = C0 * erfc(depth_grid / (2 * np.sqrt(D_control * t)))
    plt.plot(depth_grid, concentration, label=f'Year {t}')

# --- Step 3: Plot Structural Design Boundaries and Thresholds ---
plt.axhline(y=Ccrit, color='r', linestyle='--', linewidth=1.5, 
            label=f'Critical Limit ($C_{{crit}}$ = {Ccrit} kg/m³)')
plt.axvline(x=cover_depth, color='k', linestyle=':', linewidth=1.5, 
            label=f'Rebar Cover Depth ({cover_depth} mm)')

# --- Step 4: Format and Export the Engineering Graph ---
plt.title("Chloride Concentration Profile Over Time (Fickian Transport Model)", fontsize=12, fontweight='bold')
plt.xlabel("Depth from Exposed Concrete Surface (mm)", fontsize=10)
plt.ylabel("Chloride Ion Concentration (kg/m³)", fontsize=10)
plt.xlim(0, 100)
plt.ylim(0, 5.0)
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.6)

# Save the final chart asset to the project directory
plt.savefig('chloride_diffusion_profile.png', dpi=300, bbox_inches='tight')
print("Simulation successful. 'chloride_diffusion_profile.png' has been compiled and saved.")
