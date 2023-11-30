from brian2 import *
import stimulus



Parameters = dict(

    odor_input=[],
    sim_duration=0,
    odor_start=[],
    odor_end=[],

    reward_start=[],
    reward_end=[],
    punishment_start=[],
    punishment_end=[],
    reward=[], 
    punishment=[],

    learning_rate= 0.3 * nS,
    save_path=,
    seed=None,  
    N=0,  # number of model instances 
    odor_baseline=185,  
    gamma_shape = 3.0,
    reinforcement_baseline=0.0001, 

    # sparseness mechanisms
    lateral_inhibition_enabled=1, 
    APL_inhibition= 1, 
    KC_SFA=0.02* nS,



    # Neuron Parameters
    C=100 * pF, 
    CMBON = 100*pF,
    CKC=30 * pF,  
    gLKC=0.5 * nS,  
    CPN=30 * pF, 
    CLN=50 *pF,
    CAPL=200 * pF,
    gLPN=2.5 * nS,  
    gL=5 * nS, 
    EL=-60 * mV,  
    ELPN=-59 * mV,  
    ELLN=-59 * mV, 
    ELKC=-55 * mV, 
    VT=-35 * mV,  
    VTPN=-30 * mV, 
    VTLN=-30 * mV, 
    VTKC=-35 * mV,  
    VTAPL=-30 * mV,  
    Vr=-60 * mV,  
    VrPN=-59 * mV, 
    VrLN=-59 * mV, 
    VrKC=-55 * mV,  
    VrAPL=-60 * mV,  

    tau_ref=2 * ms, 
    delay_KCAPL=0 * ms,  
    delay_APLKC=0 * ms,
    ORN_SFA= 0.1 * nS, 
    MBON_SFA=0.1 * nS,
    MBIN_SFA=0.1 * nS,

    # Dimensions
    N_glo=21,  
    ORNperGlo=1,
    N_MBINp=1,  
    N_MBINn=1,  
    N_KC=72,
    N_MBON=2,

    # Synaptic Parameters
    Ee=0 * mV,  # exitatory synaptic potential
    Ei=-75 * mV,  # inibitory synaptic potential
    tau_syn_e=5 * ms,
    tau_syn_i=10 * ms,
    tau_eligibility = 5000 * ms,


    # weights
    wORNinputORN= 3 * nS,wORNPN=10 * nS, wORNLN=4 * nS, wLNPN=1 * nS,
    wPNKC=1 * nS,  wKCAPL=20* nS, wAPLKC=50* nS,
    wKCMBONp=80 * nS, wKCMBONn=80* nS,

    wMBINpinputMBINp=2.5* nS, wMBINninputMBINn=2.5* nS,


    wMBONMBINex = 4*nS, #4
    wMBONMBINin = 70*nS, #70
    wMBONMBON_LN = 35*nS,

    normalization_factor = 0.0001, # factor for weight normalization 

    # Adaptation current Parameters
    tau_Ia = 1000*ms, 
    EIa = -90*mV, 

    # simulation
    dt = 0.1*ms)
