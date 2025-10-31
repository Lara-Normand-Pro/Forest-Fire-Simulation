README.txt - Forest Fire Simulation - Cellular Automaton Model
=======================================================================

Project title:
----------------
Forest Fire Simulation - Cellular Automaton Model

Objective:
----------------
This project presents an interactive simulation of a forest ecosystem's life cycle, 
including natural growth and destruction by fire. The program uses a cellular automaton 
model to visualize the dynamic evolution of a forest over time, demonstrating emergent 
behavior from simple probabilistic rules. The simulation features real-time graphical 
rendering with visual and audio effects for an immersive educational experience.

-----------------------------------------------------------------------
Key Features:
-----------------------------------------------------------------------
* Interactive GUI: Real-time visualization with Start, Pause, Resume, and Exit controls.
* Visual Effects: Pine tree and flame images displayed on a 50x30 grid (750 cells).
* Audio Integration: Background music and fire sound effects synchronized with simulation state.
* Probabilistic Model: Tree growth (0.3%), spontaneous combustion (0.01%), and fire propagation (100% adjacency).
* Customizable Parameters: Grid size, cell size, simulation speed, and initial tree count.

-----------------------------------------------------------------------
Simulation Rules:
-----------------------------------------------------------------------
Each cell can exist in three states:
* Empty (beige): 0.3% probability per step that a tree will grow.
* Tree (pine image): 0.01% probability of spontaneous fire; 100% burn rate if adjacent to fire.
* Fire (flame image): Automatically becomes empty at next step; triggers fire sound effect.

Result: The forest experiences natural cycles of growth and destruction. Fire propagation 
patterns vary with each run, creating unique ecosystem dynamics every time.

-----------------------------------------------------------------------
Recommendation for Use:
-----------------------------------------------------------------------
The default parameters (50x30 grid, 500 initial trees, 50ms step delay) provide a balanced 
simulation suitable for classroom demonstrations or personal exploration. For faster 
observation of long-term patterns, reduce STEP_DELAY to 20-30ms. For detailed observation 
of fire propagation, increase to 100-200ms.

Environmental Considerations:
* Demonstrates ecosystem fragility and resilience.
* Models real-world forest fire dynamics at a simplified scale.
* Educational tool for understanding cellular automata and emergent behavior.
* Illustrates the stochastic nature of natural disasters.

-----------------------------------------------------------------------
File Contents:
-----------------------------------------------------------------------
* level3_V2.py - Main Python program with simulation logic and GUI.
* README.txt - This documentation file.
* data/pinetree.png - Visual asset for tree representation.
* data/flame.png - Visual asset for fire representation.
* data/fireball.mp3 - Background music for simulation.
* data/fire.mp3 - Fire crackling sound effect.

-----------------------------------------------------------------------
Requirements:
-----------------------------------------------------------------------

Python 3.x
Recommended environment: Thonny IDE
Python Libraries: tkinter (GUI), PIL/Pillow (image processing), pygame (audio), random, os

-----------------------------------------------------------------------
Dependencies
-----------------------------------------------------------------------
Install dependencies using Thonny:
Tools > Manage packages > Search and install:
- Pillow
- pygame

Note: tkinter, random, and os are included with standard Python distribution.

-----------------------------------------------------------------------
File Structure:
-----------------------------------------------------------------------
your_folder/
|-- level3_V2.py (main program)
|-- README.txt (this file)
|-- data/ (required subdirectory)
    |-- pinetree.png
    |-- flame.png
    |-- fireball.mp3
    |-- fire.mp3

IMPORTANT: The data folder must be in the same directory as level3_V2.py

-----------------------------------------------------------------------
How to Run:
-----------------------------------------------------------------------
1. Ensure Python 3.x and Thonny are installed.

2. Install required packages:
   - Open Thonny
   - Tools > Manage packages
   - Install "Pillow" and "pygame"

3. Verify file structure:
   - level3_V2.py and data/ folder at same level
   - All assets present in data/ folder

4. Launch the program:
   - Open level3_V2.py in Thonny
   - Press F5 or click Run button
   - Simulation window opens with initial forest

5. Control the simulation:
   - Click "Start" to begin (music starts)
   - Click "Pause" to freeze simulation
   - Click "Resume" to continue from pause
   - Click "Exit" to close properly

-----------------------------------------------------------------------
Customization (Optional):
-----------------------------------------------------------------------

Modify these constants in level3_V2.py (lines 11-15):

WIDTH = 50          # Grid columns (default: 50)
HEIGHT = 30         # Grid rows (default: 30)
CELL_SIZE = 15      # Cell size in pixels (default: 15)
STEP_DELAY = 50     # Milliseconds between steps (default: 50)

Other adjustable parameters:
* Line 272: plant(world, 500) - Initial tree count (default: 500)
* Line 91: Growth probability - Currently 3/1000 (0.3%)
* Line 94: Spontaneous fire probability - Currently 1/10000 (0.01%)

-----------------------------------------------------------------------
Results Summary:
-----------------------------------------------------------------------

Outputs:
* Real-time visual simulation of forest ecosystem
* Emergent fire propagation patterns
* Synchronized audio feedback (music + fire sounds)
* Infinite simulation loop with user control

-----------------------------------------------------------------------
Interpretation:
-----------------------------------------------------------------------

This simulation demonstrates how complex ecosystem behaviors emerge from simple rules. 
The balance between growth, spontaneous combustion, and propagation creates realistic 
forest fire dynamics. Each simulation run produces unique patterns, illustrating the 
chaotic nature of natural systems.

Educational Value:
* Introduction to cellular automata
* Probabilistic modeling concepts
* Ecological system dynamics
* Python programming with GUI and multimedia

-----------------------------------------------------------------------
Troubleshooting:
-----------------------------------------------------------------------

Problem: Window does not open
Solution: Verify tkinter is installed (included with Python by default)

Problem: "No module named PIL"
Solution: Install Pillow via Thonny: Tools > Manage packages > Pillow

Problem: "No module named pygame"
Solution: Install pygame via Thonny: Tools > Manage packages > pygame

Problem: "Cannot identify image file" or "file not found"
Solution: Ensure data/ folder exists with all required files at correct location

Problem: No audio
Solution: Check system volume; verify .mp3 files are present in data/ folder

Problem: Simulation too fast/slow
Solution: Modify STEP_DELAY constant (line 14): lower = faster, higher = slower

-----------------------------------------------------------------------
Technical Architecture:
-----------------------------------------------------------------------

Core Components:
* Cellular Automaton Engine: Computes next state based on current state and neighborhood
* Tkinter GUI: Provides canvas rendering and button controls
* PIL/Pillow: Loads and scales PNG images to match cell dimensions
* Pygame Audio: Manages background music and conditional fire sound effects
* Event Loop: root.mainloop() with after() callbacks for timed updates

Algorithm Flow:
1. Initialize 50x30 grid with empty cells
2. Plant 500 trees at random positions
3. Display initial state with images on canvas
4. On "Start": Begin infinite update loop
5. Each step: Calculate new grid state using evolution rules
6. Render updated grid with appropriate images
7. Trigger/stop fire sound based on flame presence
8. Schedule next update after STEP_DELAY milliseconds
9. Continue until "Exit" button pressed

-----------------------------------------------------------------------
Author & Notes:
-----------------------------------------------------------------------
Prepared by: Lara Normand

This project is based on the Level 3 - Forest Fire guidelines (Chapter 34).
Developed as part of programming coursework with enhanced visualization and audio.

The simulation uses probabilistic cellular automaton principles to model ecological dynamics.
All code is open for educational modification and experimentation.

Version: V2
Date: 2024-2025 Academic Year

-----------------------------------------------------------------------
License & Usage:
-----------------------------------------------------------------------
This code is provided for educational purposes.
Feel free to modify parameters and experiment with different configurations.
For questions or improvements, contact the author.

Enjoy the simulation!
