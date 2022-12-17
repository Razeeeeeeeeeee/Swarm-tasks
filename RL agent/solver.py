import numpy as np

from gridworld import GridWorld


class Solver():
    def __init__(self, gamma, alpha, n):
        self.world = GridWorld()
        self.gamma = gamma
        self.alpha = alpha
        self.n = n

    def action_choice(self, state, q_table, epsilon):
        if(np.random.random() < epsilon):
            action = np.random.choice(self.world.ACTIONS)
        else:
            action = np.argmax(q_table[state[0], state[1], :])
        return action

    def q_learning(self):
        q_table = np.zeros(
            (self.world.WORLD_HEIGHT, self.world.WORLD_WIDTH, len(self.world.ACTIONS)))
        q_table[self.world.GOAL[0], self.world.GOAL[1],
                self.world.ACTIONS] = 100.0

        for i in range(self.n):
            state = self.world.START
            while(state != self.world.GOAL):
                epsilon = 0.01
                action = self.action_choice(state, q_table, epsilon)
                state_prime, reward = self.world.step(state, action)
                action_max = np.argmax(q_table[state[0], state[1], :])
                q_table[state[0], state[1], action] = q_table[state[0], state[1], action] + self.alpha*(
                    reward+self.gamma*q_table[state_prime[0], state_prime[1], action_max]-q_table[state[0], state[1], action])
                state = state_prime
        return q_table

    def get_path(self, q_table):
        path = []
        treward = 0
        state = self.world.START
        while(state != self.world.GOAL):
            action = np.argmax(q_table[state[0], state[1], :])
            state_prime, reward = self.world.step(state, action)
            path.append(state)
            state = state_prime
            treward += reward
        return path, treward
