from numba import njit
import numpy as np
import glm
import math

# Resolution
WIN_RES = glm.vec2(1600, 900) 

# Colours
BG_COLOUR = glm.vec3(0.1, 0.16, 0.25)