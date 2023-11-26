import matplotlib.pyplot as plt

OG_LOADING_LOC = [-857, -681, -517, -341, -177, -1]
LOADS = [400/6, 400/6, 400/6, 400/6, 400/6, 400/6]
STEP_SIZE = 120
LENGTH = 1200



def RF(pos_lists, loads):
    M = 0
    for i in range(len(pos_lists)):
        M += pos_lists[i]*loads[i]
    RH = M/LENGTH
    RA = sum(loads) - RH
    return RA, RH

def SFD(pos_lists, loads):


    RA, RH = RF(pos_lists, loads)
    force_step_list = [RA]
    for i, val in enumerate(loads):
        if pos_lists[i] == 0:
            force_step_list[0] -= val
        else:
            force_step_list.append(force_step_list[-1] - val)
    
    SFD_List = []

    for step in range(STEP_SIZE):
        if step == 0:
            SFD_List.append(RA)
            continue
        num = 0
        for i in range(len(pos_lists)):
            if LENGTH*step/STEP_SIZE > pos_lists[i]:
                num = i + 1
        
        if len(pos_lists) > 0 and LENGTH*step/STEP_SIZE > pos_lists[-1]:
            num = -1
        SFD_List.append(force_step_list[num])
    return SFD_List

def BMD(sfd):
    Bmd = [0]
    cumsum = 0
    for i in range(len(sfd)-1):
        cumsum += sfd[i] * LENGTH / STEP_SIZE / 1000 / 1000
        Bmd.append(cumsum)
    #print(Bmd[0])
    #print(Bmd[-2])
    return Bmd

def envolelopes(pos_lists, loads):
    sfd_env = [0]*STEP_SIZE
    bmd_env = [0]*STEP_SIZE

    for step in range(STEP_SIZE*2):
        filter_pos = []
        filter_loads = []
        for k in range(len(pos_lists)):
            if pos_lists[k] >= 0 and pos_lists[k] <= LENGTH:
                filter_pos.append(pos_lists[k])
                filter_loads.append(loads[k])
        sf = SFD(filter_pos, filter_loads)
        bm = BMD(sf)

        if step == 700:
            pass

        sfd_env = [max(sfd_env[i], abs(e)) for i,e in enumerate(sf)]
        bmd_env = [max(bmd_env[i], e) for i,e in enumerate(bm)]
        pos_lists = [e + LENGTH/STEP_SIZE for e in pos_lists]

    return sfd_env, bmd_env


sfd, Bmd = envolelopes(OG_LOADING_LOC, LOADS)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(range(STEP_SIZE), sfd, label='Max SFD')
plt.subplot(2,1,2)
plt.plot(range(STEP_SIZE), Bmd, label='Max BMD')

plt.show()