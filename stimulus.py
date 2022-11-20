
import numpy as np


### creates different stimuli to be used for stimulation of the larval network


def amylacetate():

    gamma_baseline = 0.000000001  # because elephant.homogenous_gamma() won't take 0 as a rate parameter

    input_activation_pattern = np.array([2.73, 2.67, 0.0, 4.39, 0.19, 0.0, 3.38, 0.0, 0.0, 3.24, 3.92, 2.91, 5.76, 0.78, 1.47, 1.51, 0.26, 0.0, 0.0,0.0, 0.0],dtype=np.float)  # ORN activation pattern derived from  Si et al. (2019) https://www.sciencedirect.com/science/article/pii/S0896627318311504
    input_activation_pattern = input_activation_pattern * 500 # achieve realistic spike frequency (Kreher et al (2005) from Si et al (2019) Calcium data
    input_activation_pattern = input_activation_pattern + gamma_baseline

    return input_activation_pattern

def amylacetate_stronger():

    gamma_baseline = 0.000000001  # because elephant.homogenous_gamma() won't take 0 as a rate parameter

    input_activation_pattern = np.array([2.73, 2.67, 0.0, 4.39, 0.19, 0.0, 3.38, 0.0, 0.0, 3.24, 3.92, 2.91, 5.76, 0.78, 1.47, 1.51, 0.26, 0.0, 0.0,0.0, 0.0],dtype=np.float)  # ORN activation pattern derived from  Si et al. (2019) https://www.sciencedirect.com/science/article/pii/S0896627318311504
    input_activation_pattern = input_activation_pattern * 700
    input_activation_pattern = input_activation_pattern + gamma_baseline

    return input_activation_pattern

def odor1():

    gamma_baseline = 0.000000001

    input_activation_pattern = np.array([0.5, 1.0, 2.0, 3.0, 4.0, 4.0, 3.0, 2.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],dtype=np.float)
    input_activation_pattern = input_activation_pattern * 700
    input_activation_pattern = input_activation_pattern + gamma_baseline

    return input_activation_pattern

def odor2():
    gamma_baseline = 0.000000001

    input_activation_pattern = np.array([0.0, 0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 4.0, 3.0, 2.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],dtype=np.float)
    input_activation_pattern = input_activation_pattern * 700
    input_activation_pattern = input_activation_pattern + gamma_baseline

    return input_activation_pattern

def odor3():
    gamma_baseline = 0.000000001

    input_activation_pattern = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 4.0, 3.0, 2.0, 2.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0],dtype=np.float)
    input_activation_pattern = input_activation_pattern * 700
    input_activation_pattern = input_activation_pattern + gamma_baseline

    return input_activation_pattern

def odor4():
    gamma_baseline = 0.000000001

    input_activation_pattern = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 2.0, 3.0, 4.0, 4.0, 3.0, 2.0, 1.0, 0.5],dtype=np.float)
    input_activation_pattern = input_activation_pattern * 700
    input_activation_pattern = input_activation_pattern + gamma_baseline

    return input_activation_pattern

def odor1_4():
    gamma_baseline = 0.000000001

    input_activation_pattern = np.array([0.5, 1.0, 2.0, 3.0, 4.0, 4.0, 3.0, 2.0, 1.0, 0.5, 0.0,0.5, 1.0, 2.0, 3.0, 4.0, 4.0, 3.0, 2.0, 1.0, 0.5],
        dtype=np.float)
    input_activation_pattern = input_activation_pattern * 700
    input_activation_pattern = input_activation_pattern + gamma_baseline

    return input_activation_pattern

def three_octanol():

    gamma_baseline = 0.000000001  # because elephant.homogenous_gamma() won't take 0 as a rate parameter

    input_activation_pattern = np.array([5.53, 3.18, 0, 3.67, 0, 0, 1.33, 0, 0, 0.50, 1.43, 3.08, 4.09, 0, 0, 0, 0, 0, 0, 0,0])  # ORN activation pattern derived from  Si et al. (2019) https://www.sciencedirect.com/science/article/pii/S0896627318311504
    input_activation_pattern = input_activation_pattern * 500 # achieve realistic spike frequency (Kreher et al (2005) from Si et al (2019) Calcium data
    input_activation_pattern = input_activation_pattern + gamma_baseline

    return input_activation_pattern



