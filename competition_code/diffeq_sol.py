import numpy as np
import torch
import torch.nn as nn

N = 1000 # timesteps
m = 80 # mass
l = 2.5 # length of wheelbase
F_a = 5 # acceleration pedal max force
F_b = 10 # brake pedal max force
track = [] # placeholder

x0, y0, theta0, v0 = 0, 0, 0, 0 # initial condition

def x(x0, v, theta, dt):
    return x0 + (v * torch.cos(theta)) * dt

def y(y0, v, theta, dt):
    return y0 + (v * torch.sin(theta)) * dt

def theta(theta0, v, delta, dt):
    return theta0 + v / l * torch.tan(delta) * dt

def v(v0, a, dt):
    return v0 + a * dt

def a(acc, brake):
    return acc * F_a - brake * F_b

# mandatory
def pos_loss(x, y, track): # track will return 1 if point is inside and 0 if it is outside
    return ~track(x, y) * 1000 # big penalty

def acc_brake_loss(a, b):
    return torch.sum((a * b) ** 2)

def smoothness_loss(a, b, delta):
    return torch.sum((a[1:] - a[:-1]) ** 2) + torch.sum((b[1:] - b[:-1]) ** 2) + torch.sum((delta[1:] - delta[:-1]) ** 2)

# what we want to optimize
def time_loss(dt):
    return torch.sum(dt)

def total_loss(a, b, delta, dt, x, y, track):
    return pos_loss(x, y, track) + acc_brake_loss(a, b) + smoothness_loss(a, b, delta) + time_loss(dt)

# generate path
def get_path(acc, brake, delta, dt):
    path = []
    
    for t in range(N):
        path.append((x(x0, v, theta, dt[t]), y(y0, v, theta, dt[t]), theta(theta0, v, delta, dt[t]), v(v0, a(acc, brake), dt)))
    
    path = torch.stack([torch.stack(p) for p in zip(*path)], dim = 1)
    return path

# define parameters
acc = nn.Parameter(torch.zeros(N))
brake = nn.Parameter(torch.zeros(N))
delta = nn.Parameter(torch.zeros(N))
dt = nn.Parameter(0.01 * torch.ones(N))

# gradient descent
optimizer = torch.optim.Adam([acc, brake, delta, dt], lr = 0.001)

for i in range(1000):
    optimizer.zero_grad()
    path = get_path(acc, brake, delta, dt)
    
    x, y, theta, v = path
    
    loss = total_loss(acc, brake, delta, dt, x, y, track)
    
    loss.backward()
    optimizer.step()