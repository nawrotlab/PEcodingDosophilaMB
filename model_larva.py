from brian2 import *


def Model(Parameters):

    """ Creates the network model architecture including NeuronGroups, Synapses and initializations.

    Parameters:
        Parameters (dict): collection of cellular parameters and synaptic weights

    Returns:
        NG(dict): NeuronGroups
        c (dict): Synapses

    """


    #ORN
    ORN_eqs = '''
        dv/dt = (g_l*(E_l-v) + g_e*(E_e-v) - g_i*(E_i-v) - g_Ia*(E_Ia-v) + I0)/C_m    : volt (unless refractory) 
        dg_e/dt = -g_e/tau_e  : siemens  # post-synaptic exc. conductance # synapses
        dg_i/dt = -g_i/tau_i  : siemens  # post-synaptic inh. conductance
        dg_Ia/dt = -g_Ia/tau_Ia : siemens # conductance adaptation current
        I0 : amp
        '''

    neuron_modelORN = dict()
    neuron_modelORN['model'] = Equations(ORN_eqs, DeltaT=1 * mV, g_l=Parameters['gL'], E_l=Parameters['EL'], E_e=Parameters['Ee'], E_i=Parameters['Ei'], E_Ia=Parameters['EIa'], C_m=Parameters['C'],
    tau_e=Parameters['tau_syn_e'],tau_i=Parameters['tau_syn_i'], tau_Ia=Parameters['tau_Ia'])
    neuron_modelORN['threshold'] = 'v > VT'
    neuron_modelORN['reset'] = '''v = Vr; g_Ia-=ORN_SFA'''  
    neuron_modelORN['refractory'] = Parameters.get('tau_ref')



    #PN
    PN_eqs = '''
        dv/dt = (g_l*(E_l-v) + g_e*(E_e-v) - g_i*(E_i-v) - g_Ia*(E_Ia-v) + I0)/C_m    : volt (unless refractory)
        dg_e/dt = -g_e/tau_e  : siemens  # post-synaptic exc. conductance 
        dg_i/dt = -g_i/tau_i  : siemens  # post-synaptic inh. conductance
        dg_Ia/dt = -g_Ia/tau_Ia : siemens # conductance adaptation current
        I0 : amp
        '''

    neuron_modelPN = dict()
    neuron_modelPN['model'] = Equations(PN_eqs, DeltaT=1 * mV, g_l=Parameters['gLPN'], E_l=Parameters['ELPN'], E_e=Parameters['Ee'], E_i=Parameters['Ei'], E_Ia=Parameters['EIa'],C_m=Parameters['CPN'],
                                        tau_e=Parameters['tau_syn_e'], tau_i=Parameters['tau_syn_i'], tau_Ia=Parameters['tau_Ia'])
    neuron_modelPN['threshold'] = 'v > VTPN'
    neuron_modelPN['reset'] = 'v = VrPN'
    neuron_modelPN['refractory'] = Parameters.get('tau_ref')



    #LN
    LN_eqs = '''
       dv/dt = (g_l*(E_l-v) + g_e*(E_e-v) - g_i*(E_i-v) - g_Ia*(E_Ia-v) + I0)/C_m    : volt (unless refractory) 
       dg_e/dt = -g_e/tau_e  : siemens  # post-synaptic exc. conductance # synapses
       dg_i/dt = -g_i/tau_i  : siemens  # post-synaptic inh. conductance
       dg_Ia/dt = -g_Ia/tau_Ia : siemens # conductance adaptation current
       I0 : amp
       '''

    neuron_modelLN = dict()
    neuron_modelLN['model'] = Equations(LN_eqs, DeltaT=1 * mV, g_l=Parameters['gLPN'], E_l=Parameters['ELLN'], E_e=Parameters['Ee'], E_i=Parameters['Ei'], E_Ia=Parameters['EIa'],
                                        C_m=Parameters['CLN'], tau_e=Parameters['tau_syn_e'], tau_i=Parameters['tau_syn_i'], tau_Ia=Parameters['tau_Ia'])
    neuron_modelLN['threshold'] = 'v > VTLN'
    neuron_modelLN['reset'] = 'v = VrLN'
    neuron_modelLN['refractory'] = Parameters.get('tau_ref')




    #KC
    KC_eqs = '''
        dv/dt = (g_l*(E_l-v) + g_e*(E_e-v) - g_i*(E_i-v) - g_Ia*(E_Ia-v) + I0)/C_m    : volt (unless refractory) 
        dg_e/dt = -g_e/tau_e  : siemens  # post-synaptic exc. conductance # synapses
        dg_i/dt = -g_i/tau_i  : siemens  # post-synaptic inh. conductance
        dg_Ia/dt = -g_Ia/tau_Ia : siemens # conductance adaptation current
        I0 : amp
      
        '''

    neuron_modelKC = dict()
    neuron_modelKC['model'] = Equations(KC_eqs, DeltaT=1 * mV, g_l=Parameters['gLKC'], E_l=Parameters['ELKC'], E_e=Parameters['Ee'], E_i=Parameters['Ei'], E_Ia=Parameters['EIa'],
                                        C_m=Parameters['CKC'],tau_e=Parameters['tau_syn_e'], tau_i=Parameters['tau_syn_i'], tau_Ia=Parameters['tau_Ia'])
    neuron_modelKC['threshold'] = 'v > VTKC'
    neuron_modelKC['reset'] = '''v = VrKC; g_Ia-=KC_SFA '''
    neuron_modelKC['refractory'] = Parameters.get('tau_ref')


    #MBON
    MBON_eqs = '''
       dv/dt = (g_l*(E_l-v) + g_e*(E_e-v) - g_i*(E_i-v) - g_Ia*(E_Ia-v) + I0)/C_m    : volt (unless refractory) 
       dg_e/dt = -g_e/tau_e  : siemens  # post-synaptic exc. conductance # synapses
       dg_i/dt = -g_i/tau_i  : siemens  # post-synaptic inh. conductance
       dg_Ia/dt = -g_Ia/tau_Ia : siemens # conductance adaptation current
       I0 : amp
       sumw : siemens
       w_init : siemens
       norm_factor :1
       '''



    neuron_modelMBON = dict()
    neuron_modelMBON['model'] = Equations(MBON_eqs, DeltaT=1 * mV, g_l=Parameters['gL'], E_l=Parameters['EL'],
                                        E_e=Parameters['Ee'], E_i=Parameters['Ei'], E_Ia=Parameters['EIa'],
                                        C_m=Parameters['CMBON'], tau_e=Parameters['tau_syn_e'],
                                        tau_i=Parameters['tau_syn_i'], tau_Ia=Parameters['tau_Ia'])
    neuron_modelMBON['threshold'] = 'v > VT'
    neuron_modelMBON['reset'] = '''v = Vr; g_Ia-=MBON_SFA '''
    neuron_modelMBON['refractory'] = Parameters.get('tau_ref')

    # MBON interneurons (convey inhibitory MBON feedback onto MBINs)
    MBON_LN_eqs = '''
           dv/dt = (g_l*(E_l-v) + g_e*(E_e-v) - g_i*(E_i-v) - g_Ia*(E_Ia-v) + I0)/C_m    : volt (unless refractory) 
           dg_e/dt = -g_e/tau_e  : siemens  # post-synaptic exc. conductance # synapses
           dg_i/dt = -g_i/tau_i  : siemens  # post-synaptic inh. conductance
           dg_Ia/dt = -g_Ia/tau_Ia : siemens # conductance adaptation current
           I0 : amp
           '''

    neuron_modelMBON_LN = dict()
    neuron_modelMBON_LN['model'] = Equations(MBON_LN_eqs, DeltaT=1 * mV, g_l=Parameters['gL'], E_l=Parameters['EL'],
                                          E_e=Parameters['Ee'], E_i=Parameters['Ei'], E_Ia=Parameters['EIa'],
                                          C_m=Parameters['C'], tau_e=Parameters['tau_syn_e'],
                                          tau_i=Parameters['tau_syn_i'], tau_Ia=Parameters['tau_Ia'])
    neuron_modelMBON_LN['threshold'] = 'v > VT'
    neuron_modelMBON_LN['reset'] = '''v = Vr; g_Ia-=0.1*nS '''
    neuron_modelMBON_LN['refractory'] = Parameters.get('tau_ref')



    # MBIN
    MBIN_eqs = '''
        dv/dt = (g_l*(E_l-v) + g_e*(E_e-v) - g_i*(E_i-v) - g_Ia*(E_Ia-v) + I0)/C_m    : volt (unless refractory) 
        dg_e/dt = -g_e/tau_e  : siemens  # post-synaptic exc. conductance # synapses
        dg_i/dt = -g_i/tau_i  : siemens  # post-synaptic inh. conductance
        dg_Ia/dt = -g_Ia/tau_Ia : siemens # conductance adaptation current
        I0 : amp
        '''

    neuron_modelMBIN = dict()
    neuron_modelMBIN['model'] = Equations(MBIN_eqs, DeltaT=1 * mV, g_l=Parameters['gL'], E_l=Parameters['EL'],
                                        E_e=Parameters['Ee'], E_i=Parameters['Ei'], E_Ia=Parameters['EIa'],
                                        C_m=Parameters['C'], tau_e=Parameters['tau_syn_e'],
                                        tau_i=Parameters['tau_syn_i'], tau_Ia=Parameters['tau_Ia'])
    neuron_modelMBIN['threshold'] = 'v > VT'
    neuron_modelMBIN['reset'] = '''v = Vr; g_Ia-=MBIN_SFA'''
    neuron_modelMBIN['refractory'] = Parameters.get('tau_ref')


    # APL
    APL_eqs = '''
        dv/dt = (g_l*(E_l - v) +g_e*(E_e-v)- g_i*(E_i-v))/C_m : volt (unless refractory)
        dg_e/dt = -g_e/tau_e: siemens
        dg_i/dt = -g_i/tau_i : siemens
        '''

    neuron_modelAPL = dict()
    neuron_modelAPL['model'] = Equations(APL_eqs, Delta=1*mV, g_l=Parameters['gL'],E_l=Parameters['EL'],
                                        E_e=Parameters['Ee'],E_i=Parameters['Ei'],C_m=Parameters['CAPL'],tau_e=Parameters['tau_syn_e'],
                                        tau_i=Parameters['tau_syn_i'])
    neuron_modelAPL['threshold'] = 'v > VTAPL'
    neuron_modelAPL['reset'] = '''v = VrAPL'''
    neuron_modelAPL['refractory'] = Parameters['tau_ref']

    # create neuron groups and initialize
    NG = dict()

    NG['ORN'] = NeuronGroup(Parameters.get('N_glo'), **neuron_modelORN, method='euler', namespace=Parameters)
    NG['PN'] = NeuronGroup(Parameters.get('N_glo'), **neuron_modelPN, method='euler', namespace=Parameters)
    NG['LN'] = NeuronGroup(Parameters.get('N_glo'), **neuron_modelLN, method='euler', namespace=Parameters)
    NG['KC'] = NeuronGroup(Parameters.get('N_KC'), **neuron_modelKC, method='euler', namespace=Parameters)
    NG['MBONp'] = NeuronGroup(1, **neuron_modelMBON, method='euler', namespace=Parameters)
    NG['MBONn'] = NeuronGroup(1, **neuron_modelMBON, method='euler', namespace=Parameters)
    NG['MBINp'] = NeuronGroup(Parameters.get('N_MBINp'), **neuron_modelMBIN, method='euler', namespace=Parameters)
    NG['MBINn'] = NeuronGroup(Parameters.get('N_MBINn'), **neuron_modelMBIN, method='euler', namespace=Parameters)
    NG['APL'] = NeuronGroup(1, **neuron_modelAPL, method='euler', namespace=Parameters)
    NG['MBONpLN'] = NeuronGroup(1, **neuron_modelMBON_LN, method='euler', namespace=Parameters)
    NG['MBONnLN'] = NeuronGroup(1, **neuron_modelMBON_LN, method='euler', namespace=Parameters)



    # initialize voltage at the beginning of the simulation to Vresting
    NG['ORN'].v = Parameters.get('Vr')
    NG['PN'].v = Parameters.get('VrPN')
    NG['LN'].v = Parameters.get('VrLN')
    NG['KC'].v = Parameters.get('VrKC')
    NG['MBONp'].v = Parameters.get('Vr')
    NG['MBONp'].w_init = Parameters.get('wKCMBONp')
    NG['MBONp'].norm_factor = Parameters.get('normalization_factor')
    NG['MBONn'].v = Parameters.get('Vr')
    NG['MBONn'].w_init = Parameters.get('wKCMBONn')
    NG['MBONn'].norm_factor = Parameters.get('normalization_factor')
    NG['MBINp'].v = Parameters.get('Vr')
    NG['MBINn'].v = Parameters.get('Vr')
    NG['APL'].v = Parameters.get('VrAPL')
    NG['MBONpLN'].v = Parameters.get('Vr')
    NG['MBONnLN'].v = Parameters.get('Vr')

    ### synaptic connectivity
    c = dict()

    c['ORNPN'] = Synapses(NG['ORN'], NG['PN'], 'w : siemens', on_pre='g_e += w')
    for i in np.arange(Parameters.get('N_glo')):
        c['ORNPN'].connect(i=list(range(i * Parameters.get('ORNperGlo'), (i + 1) * Parameters.get('ORNperGlo'))), j=i)
        c['ORNPN'].w = Parameters.get('wORNPN')

    # ORN - LN
    c['ORNLN'] = Synapses(NG['ORN'], NG['LN'], 'w : siemens', on_pre='g_e += w')
    for i in np.arange(Parameters.get('N_glo')):
        c['ORNLN'].connect(i=list(range(i * Parameters.get('ORNperGlo'), (i + 1) * Parameters.get('ORNperGlo'))), j=i)
        c['ORNLN'].w = Parameters.get('wORNLN')

    # LN - PN
    c['LNPN'] = Synapses(NG['LN'], NG['PN'], 'w : siemens', on_pre='g_i -= w')  
    c['LNPN'].connect(p=Parameters['lateral_inhibition_enabled']) 
    c['LNPN'].w = Parameters.get('wLNPN')

    # PN - KC
    connectivity = np.zeros((72, 21))   
    for KC in range(Parameters['N_KC']):
       a = np.random.choice(21, size=np.random.randint(2, 7),replace=False)
       connectivity[KC, a] = 1
    targets, sources = connectivity.nonzero()  

    c['KC'] = Synapses(NG['PN'], NG['KC'], 'w : siemens', on_pre='g_e += w')
    c['KC'].connect(i=sources, j=targets)  
    c['KC'].w = Parameters.get('wPNKC')

    # KC-APL
    c['KCAPL'] = Synapses(NG['KC'], NG['APL'], 'w:siemens', on_pre='g_e+=w', delay=Parameters['delay_KCAPL'])
    c['KCAPL'].connect()
    c['KCAPL'].w = Parameters['wKCAPL']

    # APL-KC
    c['APLKC'] = Synapses(NG['APL'], NG['KC'], 'w:siemens',on_pre='g_i -= w', delay=Parameters['delay_APLKC'])
    c['APLKC'].connect(p=Parameters['APL_inhibition'])
    c['APLKC'].w = Parameters['wAPLKC']

    # KC - MBONn
    sourcesKCn = np.arange(0, 71, 1)  # all KC
    
    c['KCMBONn'] = Synapses(NG['KC'], NG['MBONn'], '''w : siemens
                                                    sumw_post = w : siemens (summed)
                                                    del_trace/dt = -el_trace/(tau_eligibility) : 1 ''',
                                                    on_pre='''g_e+=w
                                                    el_trace = 1''',
                                                    on_post=' w=w+(w_init_post-w)*norm_factor')
    c['KCMBONn'].connect()
    c['KCMBONn'].w = Parameters.get('wKCMBONn')

    # KC - MBONp   
    sourcesKCp = np.arange(0, 71, 1) # all KC
   
    c['KCMBONp'] = Synapses(NG['KC'], NG['MBONp'], '''w : siemens
                                                    sumw_post = w : siemens (summed)
                                                    del_trace/dt = -el_trace/(tau_eligibility) : 1 ''',
                                                    on_pre='''g_e+=w
                                                    el_trace = 1''',
                                                    on_post=' w=w+(w_init_post-w)*norm_factor')

    c['KCMBONp'].connect()
    c['KCMBONp'].w = Parameters.get('wKCMBONp')


    # reward modulation: the modulation of the KC-MBONp synapses 
    # learning rule: weight change if pre-synaptic activation (KC) and activation of MBIN (here done via on_pre code)

    c['reward_modulation'] = Synapses(NG['MBINp'], c['KCMBONn'],
                                      on_pre='w-=learning_rate*el_trace_post')  # modulation only if presynaptic activity (MBIN) and trace= 1 (activation of KC)
    c['reward_modulation'].connect(i=0, j=c['KCMBONn'][sourcesKCn, 0])  #
    c['reward_modulation'].w = Parameters.get('wKCMBONn')

    # punishment modulation
    c['punish_modulation'] = Synapses(NG['MBINn'], c['KCMBONp'],
                                      on_pre='w-=learning_rate*el_trace_post')  # modulation only if presynaptic activity (MBIN) and trace= 1 (activation of KC)
    c['punish_modulation'].connect(i=0, j=c['KCMBONp'][sourcesKCp, 0])
    c['punish_modulation'].w = Parameters.get('wKCMBONp')

    # MBON feedback onto MBIN to allow MBIN to code prediction error
    # excitatory
    # MBONn - MBINp
    c['MBONnMBINp'] = Synapses(NG['MBONn'], NG['MBINp'], 'w:siemens', on_pre='g_e+=w')
    c['MBONnMBINp'].connect()
    c['MBONnMBINp'].w = Parameters.get('wMBONMBINex')

    # MBONp - MBINn
    c['MBONpMBINn'] = Synapses(NG['MBONp'], NG['MBINn'], 'w:siemens', on_pre='g_e+=w')
    c['MBONpMBINn'].connect()
    c['MBONpMBINn'].w = Parameters.get('wMBONMBINex')

    # inhbitory feedback via interneurons
    # MBONn - MBONnLN
    c['MBONnMBONnLN'] = Synapses(NG['MBONn'], NG['MBONnLN'], 'w:siemens', on_pre='g_e+=w')
    c['MBONnMBONnLN'].connect()
    c['MBONnMBONnLN'].w = Parameters.get('wMBONMBON_LN')

    # MBONp - MBONpLN
    c['MBONpMBONpLN'] = Synapses(NG['MBONp'], NG['MBONpLN'], 'w:siemens', on_pre='g_e+=w')
    c['MBONpMBONpLN'].connect()
    c['MBONpMBONpLN'].w = Parameters.get('wMBONMBON_LN')

    # MBONnLN - MBINn
    c['MBONnMBINn'] = Synapses(NG['MBONnLN'], NG['MBINn'], 'w:siemens', on_pre='g_i-=w')
    c['MBONnMBINn'].connect()
    c['MBONnMBINn'].w = Parameters.get('wMBONMBINin')

    # MBONpLN - MBINp
    c['MBONpMBINp'] = Synapses(NG['MBONpLN'], NG['MBINp'], 'w:siemens', on_pre='g_i-=w')
    c['MBONpMBINp'].connect()
    c['MBONpMBINp'].w = Parameters.get('wMBONMBINin')



    Parameters['connectivityPNKC'] = connectivity

    return NG,c


