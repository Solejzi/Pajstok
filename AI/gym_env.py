from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


class StockEnv(Env):
    def __init__(self):
        self.action_space = Discrete(3)
        self.observation_space = Box(low=np.array([0]), high=np.array([1000]))
        self.state = 0
        self.buy_periods = 10

    def step(self, action):
        pre_state = self.state
        self.state += action - 1
        self.buy_periods -= 1
        if self.state > pre_state:
            reward = 1
        else:
            reward = -1
        if self.buy_periods <= 0:
            done = True
        else:
            done = False
        info = {}
        return self.state, reward, done, info

    def render(self):
        pass
    def reset(self):
        self.state = 0
        self.buy_periods = 10
        return self.state


def random_action_env_agent():
    episodes = 10
    for episode in range(1,episodes+1):
        state = env.reset()
        done = False
        score = 0

        while not done:
            action = env.action_space.sample()
            n_state, reward, done, info =env.step(action)
            score+=reward
        print(f'Episode:{episode}  Score:{score}')


def build_model(states, actions):

    model = Sequential()
    model.add(Dense(24, activation='relu', input_shape=states))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))

    return model


def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions,
                   nb_steps_warmup=10, target_model_update=1e-3)
    return dqn





env = StockEnv()
states = env.observation_space.shape
actions = env.action_space.n
model = build_model(states, actions)


dqn = build_agent(model, actions)
dqn.compile(Adam(learning_rate=1e-3))
dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)


scores = dqn.test(env, nb_episodes=100, visualize=False)
print(np.mean(scores.history['episode_reward']))
