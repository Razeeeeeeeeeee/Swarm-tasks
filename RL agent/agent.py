import numpy as np

from solver import Solver
from visualiser import Visualiser

path = Solver(1, 0.9, 10000)
q_table1 = path.q_learning()
N = 1000
rewards = []
paths = []
for _ in range(N):
    pathq1, rewardq1 = path.get_path(q_table1)
    rewards.append(rewardq1)
    paths.append(pathq1)
avg_rewards = np.mean(rewards)
highest_reward = np.max(rewards)
pathq1 = paths[rewards.index(highest_reward)]
print("-------------------------------------")
print("average reward:", avg_rewards)
print("highest reward:", highest_reward)

visualise = Visualiser()
grid = visualise.draw()
visualise.show(grid, pathq1)
