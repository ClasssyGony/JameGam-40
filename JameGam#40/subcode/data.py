""" GLOBAL VARIABLES """
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800

# Colours
COLOUR = {"Black" : (0,0,0),
          "White" : (255,255,255),
          "Green" : (0,255,0),
          "Blue" : (0,0,255)}

# FPS
FPS = 120
FIXED_FPS = 60

# Camera
CAMERA_SPEED = 5

# Enemy
ENEMY_TYPES = ["Zombie", "Skeleton"]

ENEMY_SPEED = {"Zombie" : 2,
               "Skeleton" : 1}

ENEMY_COLOUR = {"Zombie" : COLOUR["Green"],
                "Skeleton" : COLOUR["White"]}

ENEMY_STATES = ["Idle", "Hunt"]

# Boundaries 
BOUNDARIES = [100,700]