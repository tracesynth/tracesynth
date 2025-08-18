from src.tracesynth.synth.memory_relation import *
from src.tracesynth.synth.ppo_def import *
from src.tracesynth.synth.ppo_dict import SinglePPO
from src.tracesynth.synth.ppo_dict import PPOPool


def get_rvwmo_model(remove = -1):
    RVWMO_model = PPOPool()
    ppo1_1 = SinglePPO([R(), PoLoc(), W()])
    ppo1_2 = SinglePPO([W(), PoLoc(), W()])
    ppo2_1 = SinglePPO([R(), PoLoc(), R()])
    ppo2_2 = SinglePPO([R(), PoLoc(), W(), PoLoc(), R()], ppo_flag = PPOFlag.Relaxed)
    ppo2_3 = SinglePPO([R(), Rsw(), R()], ppo_flag = PPOFlag.Relaxed)
    ppo2_4 = SinglePPO([AMO(), PoLoc(), R()], ppo_flag = PPOFlag.Relaxed)
    ppo3_1 = SinglePPO([Sc(), Rfi(), R()])
    ppo3_2 = SinglePPO([AMO(), Rfi(), R()])
    ppo4_1 = SinglePPO([R(), FenceD(FenceAnnotation.R_R), R()])
    ppo4_2 = SinglePPO([R(), FenceD(FenceAnnotation.R_W), W()])
    ppo4_3 = SinglePPO([R(), FenceD(FenceAnnotation.R_RW), R()])
    ppo4_4 = SinglePPO([R(), FenceD(FenceAnnotation.R_RW), W()])
    ppo4_5 = SinglePPO([W(), FenceD(FenceAnnotation.W_R), R()])
    ppo4_6 = SinglePPO([W(), FenceD(FenceAnnotation.W_W), W()])
    ppo4_7 = SinglePPO([W(), FenceD(FenceAnnotation.W_RW), W()])
    ppo4_8 = SinglePPO([W(), FenceD(FenceAnnotation.W_RW), R()])
    ppo4_9 = SinglePPO([R(), FenceD(FenceAnnotation.RW_R), R()])
    ppo4_10 = SinglePPO([W(), FenceD(FenceAnnotation.RW_R), R()])
    ppo4_11 = SinglePPO([R(), FenceD(FenceAnnotation.RW_W), W()])
    ppo4_12 = SinglePPO([W(), FenceD(FenceAnnotation.RW_W), W()])
    ppo4_13 = SinglePPO([R(), FenceD(FenceAnnotation.RW_RW), W()])
    ppo4_14 = SinglePPO([W(), FenceD(FenceAnnotation.RW_RW), R()])
    ppo4_15 = SinglePPO([W(), FenceD(FenceAnnotation.RW_RW), W()])
    ppo4_16 = SinglePPO([R(), FenceD(FenceAnnotation.RW_RW), R()])
    ppo4_17 = SinglePPO([W(), FenceD(FenceAnnotation.TSO), W()])
    ppo4_18 = SinglePPO([R(), FenceD(FenceAnnotation.TSO), W()])
    ppo4_19 = SinglePPO([R(), FenceD(FenceAnnotation.TSO), R()])
    ppo5_1 = SinglePPO([AMO(Annotation.AQ), Po(), W()])
    ppo5_2 = SinglePPO([AMO(Annotation.AQ), Po(), R()])
    ppo6_1 = SinglePPO([W(), Po(), AMO(Annotation.RL)])
    ppo6_2 = SinglePPO([R(), Po(), AMO(Annotation.RL)])
    ppo7 = SinglePPO([AMO(Annotation.RL), Po(), AMO(Annotation.AQ)])
    ppo8 = SinglePPO([Lr(),Rmw(),Sc()])
    ppo9_1 = SinglePPO([R(), AddrD(), W()])
    ppo9_2 = SinglePPO([R(), AddrD(), R()])
    ppo10_1 = SinglePPO([R(), DataD(), W()])
    ppo11_1 = SinglePPO([R(), CtrlD(), W()])
    ppo12_1 = SinglePPO([R(), AddrD(), W(), Rfi(), R()])
    ppo12_2 = SinglePPO([R(), DataD(), W(), Rfi(), R()])
    ppo13_1 = SinglePPO([R(), AddrD(), W(), Po(), W()])
    ppo13_2 = SinglePPO([R(), AddrD(), R(), Po(), W()])
    RVWMO_model.add_ppo(ppo1_1, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo1_2, ppo_init_flag=PPOInitFlag.Init)
    if remove != 2:
        RVWMO_model.add_ppo(ppo2_1, ppo_init_flag=PPOInitFlag.Init)
        RVWMO_model.add_ppo(ppo2_2, ppo_init_flag=PPOInitFlag.Init)
        RVWMO_model.add_ppo(ppo2_3, ppo_init_flag=PPOInitFlag.Init)
        RVWMO_model.add_ppo(ppo2_4, ppo_init_flag=PPOInitFlag.Init)
    else:
        RVWMO_model.add_ppo(ppo2_1, ppo_init_flag=PPOInitFlag.Verified)
    if remove != 3:
        RVWMO_model.add_ppo(ppo3_1, ppo_init_flag=PPOInitFlag.Init)
        RVWMO_model.add_ppo(ppo3_2, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_1, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_2, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_3, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_4, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_5, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_6, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_7, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_8, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_9, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_10, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_11, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_12, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_13, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_14, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_15, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_16, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_17, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_18, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo4_19, ppo_init_flag=PPOInitFlag.Init)
    if remove != 5:
        RVWMO_model.add_ppo(ppo5_1, ppo_init_flag=PPOInitFlag.Init)
        RVWMO_model.add_ppo(ppo5_2, ppo_init_flag=PPOInitFlag.Init)
    if remove != 6:
        RVWMO_model.add_ppo(ppo6_1, ppo_init_flag=PPOInitFlag.Init)
        RVWMO_model.add_ppo(ppo6_2, ppo_init_flag=PPOInitFlag.Init)
    if remove != 7:
        RVWMO_model.add_ppo(ppo7, ppo_init_flag=PPOInitFlag.Init)
    RVWMO_model.add_ppo(ppo8, ppo_init_flag=PPOInitFlag.Init)
    if remove != 9:
        RVWMO_model.add_ppo(ppo9_1, ppo_init_flag=PPOInitFlag.Init)
        RVWMO_model.add_ppo(ppo9_2, ppo_init_flag=PPOInitFlag.Init)
    if remove != 10:
        RVWMO_model.add_ppo(ppo10_1, ppo_init_flag=PPOInitFlag.Init)
    if remove != 11:
        RVWMO_model.add_ppo(ppo11_1, ppo_init_flag=PPOInitFlag.Init)
    if remove != 12:
        RVWMO_model.add_ppo(ppo12_1, ppo_init_flag=PPOInitFlag.Init)
        RVWMO_model.add_ppo(ppo12_2, ppo_init_flag=PPOInitFlag.Init)
    if remove != 13:
        RVWMO_model.add_ppo(ppo13_1, ppo_init_flag=PPOInitFlag.Init)
        RVWMO_model.add_ppo(ppo13_2, ppo_init_flag=PPOInitFlag.Init)

    return RVWMO_model