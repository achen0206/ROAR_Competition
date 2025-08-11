import numpy as np
import math
import roar_py_interface
from SpeedData import SpeedData

class ThrottleController:

  def __init__(self):
     self.max_radius = 10000
      self.max_speed = 300
      self.intended_target_distance = [0, 30, 60, 90, 120, 140, 170]
      self.target_distance = [0, 30, 60, 90, 120, 150, 180]
      self.close_index = 0
      self.mid_index = 1
      self.far_index = 2
      self.tick_counter = 0
      self.previous_speed = 1.0
      self.brake_ticks = 0

      
        self.current_t = 0.0  # Parameter along Bezier curve [0,1]
        self.dt = 0.1         # Time step between calls in seconds

        self.current_speed = 0.0  # current speed (m/s)

    
      self.brake_test_counter = 0
      self.brake_test_in_progress = False

    

  def cubic_bezier_curve(t: float, P0: np.ndarray, P1: np.ndarray, P2: np.ndarray, P3: np.ndarray) -> np.ndarray:
    return ((1 - t)3 * P0 + 3 * (1 - t)2 * t * P1 + 3 * (1 - t) * t2 * P2 + t3 * P)

  
  def curvature(t: float, P0: np.ndarray, P1: np.ndarray, P2: np.ndarray, P3: np.ndarray):
    curve = cubic_bezier_curve(t, P0, P1, P2, P3)
    
  
  def max_acceleration(v: float, P_max: float, mu: float, m: float, p, C, A, g=9.8):
  
  def run(velocity, ):
    

  
