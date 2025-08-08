import math

class Lateral:
  def steering_angle(current_location, vehicle_orientation,waypoint):
    #calculates steering angle for the car
  
    #Find distance between vehicle and waypoint
    dx = waypoint[0] - current_location[0]
    dy = waypoint[1] - current_location[1]
  
    #Convert to local coordinates
    local_x = dx*math.cos(-vehicle_orientation) - dy*math.sin(-vehicle_orientation)
    local_y = dy*math.sin(-vehicle_orientation) + dx*math.cos(-vehicle_orientation)

  #Find algo to calculate steering_angle
