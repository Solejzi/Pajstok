import gym
import gym_anytrading
from gym_anytrading.envs import TradingEnv, ForexEnv, StocksEnv, Actions, Positions
from gym_anytrading.datasets import FOREX_EURUSD_1H_ASK, STOCKS_GOOGL
import matplotlib.pyplot as plt

class LejziGym(TradingEnv):
    def __init__(self, df, window_size):
        super().__init__(df, window_size)


    def _process_data(self):
        pass


    def _calculate_reward(self, action):
        pass


    def _update_profit(self, action):
        pass


    def max_possible_profit(self):  # trade fees are ignored
        pass



