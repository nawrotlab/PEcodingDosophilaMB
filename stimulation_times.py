


########################################### absolute paired single trial ###################################

# 1 min
sim_duration=300300,
odor_start=[300,120300],
odor_end=[60300,300300],

# 2 min
sim_duration=360300,
odor_start=[300,180300],
odor_end=[120300,360300],

# 2.5 min
sim_duration=390300,
odor_start=[300,210300],
odor_end=[150300,390300],

# 4 min
sim_duration=480300,
odor_start=[300,300300],
odor_end=[240300,480300],

# 8 min
sim_duration=720300,
odor_start=[300,540300],
odor_end=[480300,720300],


########################################### absolute unpaired single trial ################################

# odor first

# 1 min
sim_duration=420300,
odor_start=[300,240300],
odor_end=[60300,420300],
reward_start=[120300],
reward_end=[180300],

# 2 min
sim_duration=540300,
odor_start=[300,360300],
odor_end=[120300,540300],
reward_start=[180300],
reward_end=[300300],

# 2.5 min
sim_duration=600300,
odor_start=[300,420300],
odor_end=[150300,600300],
reward_start=[210300],
reward_end=[360300],

# 4 min
sim_duration=780300,
odor_start=[300,600300],
odor_end=[240300,780300],
reward_start=[300300],
reward_end=[540300],

# 8 min
sim_duration=1260300,
odor_start=[300,1080300],
odor_end=[480300,1260300],
reward_start=[540300],
reward_end=[1020300],

# reward first

sim_duration=420300,
odor_start=[120300,240300],
odor_end=[180300,420300],
reward_start=[300],
reward_end=[60300],

# 2 min
sim_duration=540300,
odor_start=[180300,360300],
odor_end=[300300,540300],
reward_start=[300],
reward_end=[120300],

# 2.5 min
sim_duration=600300,
odor_start=[210300,420300],
odor_end=[570300,600300],
reward_start=[300],
reward_end=[150300],

# 4 min
sim_duration=780300,
odor_start=[300300,600300],
odor_end=[540300,780300],
reward_start=[300],
reward_end=[240300],

# 8 min
sim_duration=1260300,
odor_start=[540300,1080300],
odor_end=[1020300,1260300],
reward_start=[300],
reward_end=[480300],


################################## trace conditioning ###############################################################
 # ISI 0
sim_duration=450300,
odor_start=[300,90300,180300,270300],
odor_end=[30300,120300,210300,450300],
reward_start=[300,90300,180300],
reward_end=[30300,120300,210300],

# ISI 10
sim_duration = 480300,
odor_start = [300, 100300,200300,300300],
odor_end = [30300, 130300,230300,480300],
reward_start=[10300,110300,210300],
reward_end=[40300,140300,240300],

# ISI 30
sim_duration = 540300,
odor_start = [300, 120300,240300,360300],
odor_end = [30300,150300,270300,540300],
reward_start=[30300,150300,270300],
reward_end=[60300,180300,300300],

# ISI 60
sim_duration = 600300,
odor_start = [300,150300,300300,420300],
odor_end = [30300,180300,330300,600300],
reward_start=[60300,210300,360300],
reward_end=[90300,240300,390300],

# ISI 120
sim_duration = 810300,
odor_start = [300,210300,420300,630300],
odor_end = [30300,240300,450300,810300],
reward_start=[120300,330300,540300],
reward_end=[150300,360300,570300],

# trace conditioning unpaired (odor first)
sim_duration = 720300,
odor_start = [300,180300,360300,540300],
odor_end = [30300,210300,390300,720300],
reward_start=[90300,270300,450300],
reward_end=[120300,300300,480300],

# trace conditioning unpaired (reward first)
sim_duration = 720300,
odor_start = [90300,270300,450300,540300],
odor_end = [120300,300300,480300,720300],
reward_start=[300,180300,360300],
reward_end=[30300,210300,390300],



############################## absolute paired with 600 s pre-training ###############################################
# 1 min
sim_duration=960300,
odor_start=[300,660300,780300],
odor_end=[600300,720300,960300],

# 2 min
sim_duration=1020300,
odor_start=[300,660300,840300],
odor_end=[600300,780300,1020300],

# 2.5 min
sim_duration=1050300,
odor_start=[300,660300,870300],
odor_end=[600300,810300,1050300],

# 4 min
sim_duration=1140300,
odor_start=[300,660300,960300],
odor_end=[600300,900300,1140300],

# 8 min
sim_duration=1380300,
odor_start=[300,660300,1200300],
odor_end=[600300,1140300,1380300],



########################################### absolute with 600s pre training unpaired single trial ################################

# odor first

# 1 min
sim_duration=1020300,
odor_start=[300,600300,840300],
odor_end=[600300,660300,1020300],
reward_start=[300,720300],
reward_end=[600300,780300],

# 2 min
sim_duration=1140300,
odor_start=[300,600300,960300],
odor_end=[600300,720300,1140300],
reward_start=[300,780300],
reward_end=[600300,900300],

# 2.5 min
sim_duration=1200300,
odor_start=[300,600300,1020300],
odor_end=[600300,750300,1200300],
reward_start=[300,810300],
reward_end=[600300,960300],

# 4 min
sim_duration=1380300,
odor_start=[300,600300,1200300],
odor_end=[600300,840300,1380300],
reward_start=[300,900300],
reward_end=[600300,1140300],

# 8 min
sim_duration=1860300,
odor_start=[300,600300,1680300],
odor_end=[600300,1080300,1860300],
reward_start=[300,1140300],
reward_end=[600300,1620300],


# reward first

# 1 min
sim_duration=1080300,
odor_start=[300,780300,900300],
odor_end=[600300,840300,1080300],
reward_start=[300,660300],
reward_end=[600300,720300],

# 2 min
sim_duration=1200300,
odor_start=[300,840300,1020300],
odor_end=[600300,960300,1200300],
reward_start=[300,660300],
reward_end=[600300,780300],

# 2.5 min
sim_duration=1260300,
odor_start=[300,870300,1080300],
odor_end=[600300,1020300,1260300],
reward_start=[300,660300],
reward_end=[600300,810300],

# 4 min
sim_duration=1440300,
odor_start=[300,960300,1260300],
odor_end=[600300,1200300,1440300],
reward_start=[300,660300],
reward_end=[600300,900300],

# 8 min
sim_duration=1920300,
odor_start=[300,1200300,1740300],
odor_end=[600300,1680300,19200300],
reward_start=[300,660300],
reward_end=[600300,1140300],



