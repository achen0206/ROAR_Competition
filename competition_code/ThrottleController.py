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

      self.brake_test_counter = 0
      self.brake_test_in_progress = False

    

  def cubic_bezier_curve(t: float, P0: np.ndarray, P1: np.ndarray, P2: np.ndarray, P3: np.ndarray) -> np.ndarray:
    return ((1 - t)3 * P0 + 3 * (1 - t)2 * t * P1 + 3 * (1 - t) * t2 * P2 + t3 * P)

  def run()

  
  
  def get_radius(self, wp: [roar_py_interface.RoarPyWaypoint]):
      """Returns the radius of a curve given 3 waypoints using the Menger Curvature Formula

        Args:
            wp ([roar_py_interface.RoarPyWaypoint]): A list of 3 RoarPyWaypoints

        Returns:
            float: The radius of the curve made by the 3 given waypoints
        """

      point1 = (wp[0].location[0], wp[0].location[1])
      point2 = (wp[1].location[0], wp[1].location[1])
      point3 = (wp[2].location[0], wp[2].location[1])

        # Calculating length of all three sides
      len_side_1 = round(math.dist(point1, point2), 3)
      len_side_2 = round(math.dist(point2, point3), 3)
      len_side_3 = round(math.dist(point1, point3), 3)

      small_num = 2

      if len_side_1 < small_num or len_side_2 < small_num or len_side_3 < small_num:
          return self.max_radius
        # sp is semi-perimeter
      sp = (len_side_1 + len_side_2 + len_side_3) / 2
        # Calculating area using Herons formula
      area_squared = sp * (sp - len_side_1) * (sp - len_side_2) * (sp - len_side_3)
      if area_squared < small_num:
          return self.max_radius
        # Calculating curvature using Menger curvature formula
      radius = (len_side_1 * len_side_2 * len_side_3) / (4 * math.sqrt(area_squared))
      return radius


  
