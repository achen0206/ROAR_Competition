import math
import numpy as np

class Lateral:
  def steering_angle(current_location, vehicle_orientation, waypoint):
    #calculates steering angle for the car
  
    #Find distance between vehicle and waypoint
    dx = waypoint[0] - current_location[0]
    dy = waypoint[1] - current_location[1]
  
    #Convert to local coordinates
    local_x = dx*math.cos(-vehicle_orientation[2]) - dy*math.sin(-vehicle_orientation[2])
    local_y = dy*math.sin(-vehicle_orientation[2]) + dx*math.cos(-vehicle_orientation[2])

    return (-1.5*np.arctan(4.7* 2*local_y/(np.linalg.norm(waypoint.location - vehicle_location) ** 2)))
  
    
  #Find algo to calculate steering_angle (Pure Pursuit)
