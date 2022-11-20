from brian2 import *
import parameters as parameters
from model_larva import Model
import numpy as np
from AttrDict import AttrDict
import stimulus
import os
from joblib import Parallel, delayed
from elephant.spike_train_generation import homogeneous_gamma_process
from quantities import Hz as qHz
from quantities import ms as qms


def experiment(Parameters, filename):
    """ runs experimental protocol for one virtual larva with a stimulation protocol specified in stimulus.py and a reinforcement protocol specified in reinforcement.py
        Saves data to file as npz

    Parameters:
        Parameters (dict): collection of cellular, synaptic and simulation parameters 
        filename (str): filename results will be saved to

    Returns:

        None

    """


    safe = True
    save_path = Parameters['save_path']
 
    np.random.seed(Parameters['seed'])  # numpy seed for PN-KC and KC-MBON connectivities

    # create model architecture
    NG,c = Model(Parameters)

    np.random.seed(seed=None) 

    # create and deliver input stimulus (odor)
    odor_patterns = Parameters['odor_input']  
    odor_start = Parameters['odor_start'] 
    odor_end = Parameters['odor_end']

    spike_times_odor = []
    spike_index_odor = []

    # generate baseline spikes
    for neuron, value in enumerate(np.arange(Parameters['N_glo'])):
        spikes = homogeneous_gamma_process(Parameters['gamma_shape'],(Parameters['odor_baseline'] * Parameters['gamma_shape']) * qHz, 0 * qms, Parameters['sim_duration'] * qms, as_array=True)
        for elem in spikes:
            spike_times_odor.append(elem)
            spike_index_odor.append(neuron)


    # generate spikes elicited by odor stimulation
    for idx, odor in enumerate(odor_patterns):
        current_odor = odor_patterns[idx]

        for neuron, value in enumerate(current_odor):
            spikes = homogeneous_gamma_process(Parameters['gamma_shape'], (value * Parameters['gamma_shape']) * qHz, odor_start[idx] * qms,odor_end[idx] * qms, as_array=True)
            for elem in spikes:
                 spike_times_odor.append(elem)
                 spike_index_odor.append(neuron)

    # input to SpikeGeneratorGroup is cleaned up to remove multiple spikes of one neuron during a dt
    spike_index_odor = np.array(spike_index_odor)
    spike_times_odor = np.array(spike_times_odor)
    spike_times_odor = np.around(spike_times_odor,decimals=1) 

    temp_index = []
    temp_times = []

    for i, elem in enumerate(np.unique(spike_index_odor)):
        spike_times = spike_times_odor[spike_index_odor == elem]
        clean_spike_times = np.unique(spike_times, return_index=True)[0]
        temp_times.extend(clean_spike_times)
        [temp_index.append(elem) for x in clean_spike_times]

    spike_times_odor = temp_times
    spike_index_odor = temp_index

    # odor input is delivered into the network via a SpikeGeneratorGroup
    NG['ORNinput'] = SpikeGeneratorGroup(Parameters['N_glo'], spike_index_odor, spike_times_odor * ms)

    c['ORNinputORN'] = Synapses(NG['ORNinput'], NG['ORN'], 'w : siemens', on_pre='g_e+=w')
    for i in np.arange(Parameters.get('N_glo')):
        c['ORNinputORN'].connect(i=list(range(i * Parameters.get('ORNperGlo'), (i + 1) * Parameters.get('ORNperGlo'))), j=i)
        c['ORNinputORN'].w = Parameters.get('wORNinputORN')


    # create input reward
    reward = Parameters['reward']
    reward_start = Parameters['reward_start']
    reward_end = Parameters['reward_end']

    spike_times_reward = []

    spikes = homogeneous_gamma_process(Parameters['gamma_shape'], (Parameters['reinforcement_baseline'] * Parameters['gamma_shape']) * qHz, 0 * qms, Parameters['sim_duration'] * qms, as_array=True)
    for elem in spikes:
        spike_times_reward.append(elem)

    for i, trial in enumerate(reward):
        value = reward[i]
        spikes = homogeneous_gamma_process(Parameters['gamma_shape'], (value * Parameters['gamma_shape']) * qHz, reward_start[i] * qms, reward_end[i] * qms, as_array=True)
        for elem in spikes:
            spike_times_reward.append(elem)

    # input to SpikeGeneratorGroup is cleaned up to remove multiple spikes of one neuron during a dt
    spike_index_reward = np.zeros(len(spike_times_reward))
    spike_times_reward = np.array(spike_times_reward)
    spike_times_reward = np.around(spike_times_reward, decimals=1)

    temp_index_reward = []
    temp_times_reward = []

    for i, elem in enumerate(np.unique(spike_index_reward)):
        spike_times = spike_times_reward[spike_index_reward == elem]
        clean_spike_times = np.unique(spike_times, return_index=True)[0]
        temp_times_reward.extend(clean_spike_times)
        [temp_index_reward.append(elem) for x in clean_spike_times]

    # input activation MBINp
    NG['MBINpinput'] = SpikeGeneratorGroup(Parameters['N_MBINp'], spike_index_reward, spike_times_reward * ms)

    c['MBINpinputMBINp'] = Synapses(NG['MBINpinput'], NG['MBINp'], 'w : siemens', on_pre='g_e+=w')
    c['MBINpinputMBINp'].connect()
    c['MBINpinputMBINp'].w = Parameters.get('wMBINpinputMBINp')

    # create punishment input
    punishment = Parameters['punishment']
    punishment_start = Parameters['punishment_start']  
    punishment_end = Parameters['punishment_end']

    spike_times_punishment = []

    spikes = homogeneous_gamma_process(Parameters['gamma_shape'],(Parameters['reinforcement_baseline'] * Parameters['gamma_shape']) * qHz,0 * qms, Parameters['sim_duration'] * qms, as_array=True)
    for elem in spikes:
        spike_times_punishment.append(elem)

    for i, trial in enumerate(punishment):
        value = punishment[i]
        spikes = homogeneous_gamma_process(Parameters['gamma_shape'], (value * Parameters['gamma_shape']) * qHz,punishment_start[i] * qms, punishment_end[i] * qms, as_array=True)
        for elem in spikes:
            spike_times_punishment.append(elem)

    # input to SpikeGeneratorGroup is cleaned up to remove multiple spikes of one neuron during a dt
    spike_index_punishment = np.zeros(len(spike_times_punishment))
    spike_times_punishment = np.array(spike_times_punishment)
    spike_times_punishment = np.around(spike_times_punishment, decimals=1)

    temp_index_punishment = []
    temp_times_punishment = []

    for i, elem in enumerate(np.unique(spike_index_punishment)):
        spike_times = spike_times_punishment[spike_index_punishment == elem]
        clean_spike_times = np.unique(spike_times, return_index=True)[0]
        temp_times_punishment.extend(clean_spike_times)
        [temp_index_punishment.append(elem) for x in clean_spike_times]

    # input activation MBINn
    NG['MBINninput'] = SpikeGeneratorGroup(Parameters['N_MBINn'], spike_index_punishment, spike_times_punishment * ms)

    c['MBINninputMBINn'] = Synapses(NG['MBINninput'], NG['MBINn'], 'w : siemens', on_pre='g_e+=w')
    c['MBINninputMBINn'].connect()
    c['MBINninputMBINn'].w = Parameters.get('wMBINninputMBINn')

    ####################################################################################################################
    ### monitors

    spikemonitors = dict()

    spikemonitors['spikeORN'] = SpikeMonitor(NG['ORN'])
    spikemonitors['spikePN'] = SpikeMonitor(NG['PN'])
    spikemonitors['spikeLN'] = SpikeMonitor(NG['LN'])
    spikemonitors['spikeKC'] = SpikeMonitor(NG['KC'])
    spikemonitors['spikeMBONp'] = SpikeMonitor(NG['MBONp'],variables=['g_e'])
    spikemonitors['spikeMBONn'] = SpikeMonitor(NG['MBONn'],variables=['g_e'])
    spikemonitors['spikeMBONpLN'] = SpikeMonitor(NG['MBONpLN'])
    spikemonitors['spikeMBONnLN'] = SpikeMonitor(NG['MBONnLN'])
    spikemonitors['spikeMBINp'] = SpikeMonitor(NG['MBINp'])
    spikemonitors['spikeMBINn'] = SpikeMonitor(NG['MBINn'])
    spikemonitors['spikeAPL'] = SpikeMonitor(NG['APL'])


    statemonitors = dict()

    statemonitors['KCMBONp'] = StateMonitor(c['KCMBONp'],'w',record=True)
    statemonitors['KCMBONn'] = StateMonitor(c['KCMBONn'], 'w', record=True)

    statemonitors['KCMBONp_trace'] = StateMonitor(c['KCMBONp'], 'el_trace',record=True)
    statemonitors['KCMBONn_trace'] = StateMonitor(c['KCMBONn'], 'el_trace',record=True)



    net = Network(NG.values(),c.values())

    net.add(spikemonitors,statemonitors)

    ####################################################################################################################

    ### Running the simulation

    # Include local variables and Parameters into namespace for simulation
    ParaWithLocals = dict()
    ParaWithLocals.update(Parameters)
    ParaWithLocals.update(locals())

    net.run(Parameters['sim_duration']* ms, namespace=ParaWithLocals)

    ####################################################################################################################

    # safe data

    if safe:

        spikemons = dict()
        statemons = dict()


        spikemons['spikeORN'] = AttrDict({'i': spikemonitors['spikeORN'].i[:],
                                         't': spikemonitors['spikeORN'].t[:]})
        spikemons['spikePN'] = AttrDict({'i': spikemonitors['spikePN'].i[:],
                                          't': spikemonitors['spikePN'].t[:]})
        spikemons['spikeLN'] = AttrDict({'i': spikemonitors['spikeLN'].i[:],
                                        't': spikemonitors['spikeLN'].t[:]})
        spikemons['spikeKC'] = AttrDict({'i': spikemonitors['spikeKC'].i[:],
                                          't': spikemonitors['spikeKC'].t[:]})
        spikemons['spikeMBONp'] = AttrDict({'i': spikemonitors['spikeMBONp'].i[:],
                                          't': spikemonitors['spikeMBONp'].t[:],
                                            'g_e' : spikemonitors['spikeMBONp'].g_e[:]})
        spikemons['spikeMBONn'] = AttrDict({'i': spikemonitors['spikeMBONn'].i[:],
                                            't': spikemonitors['spikeMBONn'].t[:],
                                            'g_e' : spikemonitors['spikeMBONn'].g_e[:]})
        spikemons['spikeMBINp'] = AttrDict({'i': spikemonitors['spikeMBINp'].i[:],
                                            't': spikemonitors['spikeMBINp'].t[:]})
        spikemons['spikeMBINn'] = AttrDict({'i': spikemonitors['spikeMBINn'].i[:],
                                            't': spikemonitors['spikeMBINn'].t[:]})
        spikemons['spikeAPL'] = AttrDict({'i': spikemonitors['spikeAPL'].i[:],
                                           't': spikemonitors['spikeAPL'].t[:]}),
        spikemons['spikeMBONpLN'] = AttrDict({'i': spikemonitors['spikeMBONpLN'].i[:],
                                            't': spikemonitors['spikeMBONpLN'].t[:]})
        spikemons['spikeMBONnLN'] = AttrDict({'i': spikemonitors['spikeMBONnLN'].i[:],
                                            't': spikemonitors['spikeMBONnLN'].t[:]})

        statemons['KCMBONp'] = AttrDict({'w': statemonitors['KCMBONp'].w[:],
                                            't': statemonitors['KCMBONp'].t[:]})
        statemons['KCMBONn'] = AttrDict({'w': statemonitors['KCMBONn'].w[:],
                                       't': statemonitors['KCMBONn'].t[:]})
        statemons['KCMBONp_trace'] = AttrDict({'el_trace': statemonitors['KCMBONp_trace'].el_trace[:],
                                        't': statemonitors['KCMBONp_trace'].t[:]})
        statemons['KCMBONn_trace'] = AttrDict({'el_trace': statemonitors['KCMBONn_trace'].el_trace[:],
                                            't': statemonitors['KCMBONn_trace'].t[:]})


        spikemons = AttrDict(spikemons)
        statemons = AttrDict(statemons)

        data = {'spikemons': spikemons,
                'statemons': statemons,
                'Parameters': Parameters,
                }

        d = AttrDict(data)
        ################################################################################################################

        # save to file
        np.savez(os.path.join(save_path, filename), data=d)

       



sample = np.arange(parameters.Parameters['N']) # sample = number of independet virtual experiments (larvea)

# parellel run of multiple independent networks (sample), saves monitors as npz
Parallel(n_jobs=len(sample))(delayed(experiment)(Parameters=parameters.Parameters, filename=f"Larva_{animal:02}")for animal in sample)




