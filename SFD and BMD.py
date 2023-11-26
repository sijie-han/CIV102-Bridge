import matplotlib.pyplot as plt

OG_LOADING_LOC = [0, 176, 340, 516, 680, 856]
OG_LOADING_LOC = [e-856 for e in OG_LOADING_LOC]
OG_LOADING_LOC = [0, 176, 340, 516, 680, 856]
LOADS = [400/6, 400/6, 400/6, 400/6, 400/6, 400/6]
STEP_SIZE = 12000
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
    for val in loads:
        force_step_list.append(force_step_list[-1] - val)

    SFD_List = []

    for step in range(STEP_SIZE):
        if step == 0:
            SFD_List.append(RA)
            continue
        elif step == STEP_SIZE - 1:
            SFD_List.append(SFD_List[-1] + RH)
            break
        num = 0
        for i in range(len(loads)):
            if LENGTH*step//STEP_SIZE > pos_lists[i]:
                num = i
                #break
        
        if LENGTH*step//STEP_SIZE > pos_lists[-1]:
            num = -1
        SFD_List.append(force_step_list[num])
    return SFD_List

def BMD(SFD):
    Bmd = [0]
    for i in range(len(SFD)-1):
        Bmd.append((SFD[i] + SFD[i+1])/2 * STEP_SIZE + Bmd[-1])
    return Bmd
OG_LOADING_LOC = [e+10 for e in OG_LOADING_LOC]
sfd = SFD(OG_LOADING_LOC, LOADS)
Bmd = BMD(sfd)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(range(STEP_SIZE), sfd, label='Max SFD')
plt.subplot(2,1,2)
plt.plot(range(STEP_SIZE), Bmd, label='Max BMD')

plt.show()