import numpy as np
from brian2 import *




def reward_activation():
    baseline = 0.0000001  # spontaneous activation

    reward = np.array([10])
    reward = reward + baseline

    return reward, baseline


def punishment_activation():
    baseline = 0.0000001  # spontaneous activation

    punishment = np.array([10])
    punishment = punishment + baseline

    return punishment, baseline







