
from src.tracesynth.synth.memory_relation import *
from src.tracesynth.synth.ppo_def import *
from src.tracesynth.synth.ppo_dict import SinglePPO
from src.tracesynth.synth.ppo_dict import PPOPool



def get_rvtso_model():
    RVTSO_model = PPOPool()
    ppo1 = SinglePPO([R(), Po(), W()])
    ppo2 = SinglePPO([W(), Po(), W()])
    ppo3 = SinglePPO([R(), Po(), R()])
    ppo4_13 = SinglePPO([R(), FenceD(FenceAnnotation.RW_RW), W()])
    ppo4_14 = SinglePPO([W(), FenceD(FenceAnnotation.RW_RW), R()])
    ppo4_15 = SinglePPO([W(), FenceD(FenceAnnotation.RW_RW), W()])
    ppo4_16 = SinglePPO([R(), FenceD(FenceAnnotation.RW_RW), R()])
    RVTSO_model.add_ppo(ppo1, ppo_init_flag=PPOInitFlag.Init)
    RVTSO_model.add_ppo(ppo2, ppo_init_flag=PPOInitFlag.Init)
    RVTSO_model.add_ppo(ppo3, ppo_init_flag=PPOInitFlag.Init)
    RVTSO_model.add_ppo(ppo4_13, ppo_init_flag=PPOInitFlag.Init)
    RVTSO_model.add_ppo(ppo4_14, ppo_init_flag=PPOInitFlag.Init)
    RVTSO_model.add_ppo(ppo4_15, ppo_init_flag=PPOInitFlag.Init)
    RVTSO_model.add_ppo(ppo4_16, ppo_init_flag=PPOInitFlag.Init)
    return RVTSO_model