#we need to import functions from libraries and modules to execute the code
import tkinter as tk #library used for basic graphics
import PIL #library designed for image processing
from PIL import Image, ImageTk
import random
import pygame  # For playing background music
import os #calls modules to load data/images from subdirectory (here "data")

# Dimensions of the world, defined global constants
WIDTH = 50  # number of columns
HEIGHT = 30  # Number of rows
CELL_SIZE = 15  # cell size in pixels
STEP_DELAY = 50  # delay between each step in ms

# Initialize running state
running = False
after_id = None  # Store the after callback ID

# loading images (pinetree/flame) and rescaling to cell size
def load_images():
    # specifies the path to the images
    image_dir = "data"
    pinetree_path = os.path.join(image_dir, "pinetree.png")
    flame_path = os.path.join(image_dir, "flame.png")
    
    #rescaling
    pinetree_image = Image.open(pinetree_path).resize((CELL_SIZE, CELL_SIZE), PIL.Image.Resampling.LANCZOS)
    flame_image = Image.open(flame_path).resize((CELL_SIZE, CELL_SIZE), PIL.Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(pinetree_image), ImageTk.PhotoImage(flame_image)

# 34.1.1 initialization 
def init_world():
    return [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Initialize pygame mixer for music 
pygame.mixer.init()

#  34.1.2 displaying the world in a grid rather than using print world (see README.txt)
def display_world_in_canvas(world):
    canvas.delete("all")  # deletes cell grid 
    # initialization of fire sound
    fire_sound_playing = False
    # constructing the grid, trees and fire
    for l in range(HEIGHT):
        for c in range(WIDTH):
            x0 = c * CELL_SIZE
            y0 = l * CELL_SIZE
            if world[l][c] == "F":
                canvas.create_image(x0, y0, anchor="nw", image=flame_photo)
                fire_sound_playing = True  # A flame is displayed, so play fire sound
            elif world[l][c] == "T":
                canvas.create_image(x0, y0, anchor="nw", image=pinetree_photo)
            else:
                canvas.create_rectangle(x0, y0, x0 + CELL_SIZE, y0 + CELL_SIZE, fill="beige", outline="beige")
    
    # Plays or stops fire sound based on presence of flame images
    if fire_sound_playing:
        play_fire_sound()
    else:
        stop_fire_sound()

# 34.1.3 planting trees
def plant(world, nb_trees):
    planted = 0
    while planted < nb_trees:
        l, c = random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1)
        if world[l][c] == " ":
            world[l][c] = "T"
            planted += 1

# 34.2.1 inside the world
def is_in_world(l, c):
    return 0 <= l < HEIGHT and 0 <= c < WIDTH

# 34.2.2 neighboring fire
def close_to_fire(world, l, c):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0) and is_in_world(l + i, c + j):
                if world[l + i][c + j] == "F":
                    return True
    return world[l][c] == "F"

# 34.2.3 cell evolution and probabilities
def cell_evolution(world, l, c):
    if world[l][c] == " ":
        return "T" if random.randint(1, 1000) <= 3 else " "
    elif world[l][c] == "T":
        if random.randint(1, 10000) <= 1 or close_to_fire(world, l, c):
            return "F"
        else:
            return "T"
    elif world[l][c] == "F":
        return " "

# 34.2.4 world evolution
def world_evolution(world):
    new_world = [[cell_evolution(world, l, c) for c in range(WIDTH)] for l in range(HEIGHT)]
    return new_world

# 34.3 the world moves using a loop with step delay
def update_world():
    global world, running, after_id
    if running:
        world = world_evolution(world)
        display_world_in_canvas(world)
        after_id = root.after(STEP_DELAY, update_world)  # Store the callback ID

# Functions to control the simuation
def start_simulation():
    global running
    running = True
    play_music()  
    update_world() # runs the infinite loop and updates the world

def pause_simulation():
    global running
    running = False #pauses the simulation (loop)
    pause_music()
    stop_fire_sound()

def resume_simulation():
    global running
    running = True #restarts the loop
    resume_music()
    update_world()

def exit_simulation():
    global running, after_id
    running = False  # Stop the simulation loop first
    
    # Cancel any pending after callbacks
    if after_id is not None:
        root.after_cancel(after_id)
    
    pygame.mixer.music.stop()  # Stop background music
    stop_fire_sound()  # Stop fire sound
    pygame.mixer.quit()  # Properly shutdown pygame mixer
    root.destroy()  # Destroy the window

# Handle window close button (X)
def on_closing():
    exit_simulation()

# Functions for music from pygame module
def play_music():
    music_path = os.path.join("data", "fireball.mp3")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.2) 
    pygame.mixer.music.play(-1)  # the value -1 will loop the music indefinitely

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

# functions for controlling fire sound
def play_fire_sound():
    if not pygame.mixer.Channel(1).get_busy():  # Plays only if the sound is not already playing
        pygame.mixer.Channel(1).set_volume(1)
        pygame.mixer.Channel(1).play(fire_sound, loops=-1)  # Loops the fire sound

# Loading the fire sound from subdirectory "data"    
fire_sound_path = os.path.join("data", "fire.mp3")
fire_sound = pygame.mixer.Sound(fire_sound_path)

def stop_fire_sound():
    pygame.mixer.Channel(1).stop()  # Stops the fire sound

# initialization of the simulation window/title
root = tk.Tk()
root.title("Simulation Forest Fires")

# Register the window close handler
root.protocol("WM_DELETE_WINDOW", on_closing)

# size of the simulation window (grid) according to the size of the world
canvas_width = WIDTH * CELL_SIZE
canvas_height = HEIGHT * CELL_SIZE
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# creating start, pause, resume and exit buttons in simuation window
btn_start = tk.Button(root, text="Start", command=start_simulation)
btn_start.pack(side=tk.LEFT, padx=10, pady=10)

btn_pause = tk.Button(root, text="Pause", command=pause_simulation)
btn_pause.pack(side=tk.LEFT, padx=10, pady=10)

btn_resume = tk.Button(root, text="Resume", command=resume_simulation)
btn_resume.pack(side=tk.LEFT, padx=10, pady=10)

btn_exit = tk.Button(root, text="Exit", command=exit_simulation)
btn_exit.pack(side=tk.LEFT, padx=10, pady=10)

# loading images
pinetree_photo, flame_photo = load_images()

# Initialization of the world before display
world = init_world() 
plant(world, 500) #starts the simulation with 500 trees
display_world_in_canvas(world)

# starts the main simulation window and loop until destroyed (exit button)
root.mainloop()