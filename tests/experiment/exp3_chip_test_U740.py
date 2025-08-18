import os
import sys
import time

from src.tracesynth import config
from src.tracesynth.analysis import RVWMO
from src.tracesynth.comp.parse_result import parse_herd_log, parse_chip_log
from src.tracesynth.litmus.load_litmus import get_litmus_by_policy, GetLitmusPolicy, sort_litmus_by_weight
from src.tracesynth.synth.model.ppo_pool_rvwmo import get_rvwmo_model
from src.tracesynth.synth.model.ppo_pool_rvwmo_init import get_rvwmo_init_model
from src.tracesynth.synth.pattern_synth import synth_by_test_pattern_online
from src.tracesynth.utils.file_util import search_file, read_file
from src.tracesynth.utils.herd_util import herd_run_all_valid_litmus, get_model_diff
from src.tracesynth.utils.litmus7_util import litmus_run_until_match, integrate_chip_log, litmus_run

filter_litmus_list = [

]
exp_3_output_log_path = os.path.join(config.TEST_DIR,'results/exp3_synth_Sifive.log')
exp_3_output_result_file_path = os.path.join(config.TEST_DIR,'results/exp3_synth_Sifive_result.txt')
exp_3_test_ppo_path = os.path.join(config.TEST_DIR,'results/exp3_synth_Sifive_tested_ppo.txt')
sifive_litmus_dir = os.path.join(config.TEST_DIR,'experiment/exp3_sifive')
def delete_history():
    if os.path.exists(exp_3_output_log_path):
        print(f'deleting exp_3_output_log_path: {exp_3_output_log_path}')
        os.remove(exp_3_output_log_path)
    if os.path.exists(exp_3_output_result_file_path):
        print(f'deleting exp_3_output_result_file_path: {exp_3_output_result_file_path}')
        os.remove(exp_3_output_result_file_path)
    if os.path.exists(exp_3_test_ppo_path):
        print(f'deleting exp_3_test_ppo_path: {exp_3_test_ppo_path}')
        os.remove(exp_3_test_ppo_path)


class TestChipSifive:

    def get_dif_litmus_datasets_for_chips(self, src_cat, src_log, tgt_log, dif_log):
        filter_litmus_suite = []
        for root, dirs, files in os.walk(sifive_litmus_dir):
            for file in files:
                full_path = os.path.join(root, file)
                filter_litmus_suite.append(full_path)
        print(len(filter_litmus_suite))
        if not os.path.exists(src_log):
            herd_run_all_valid_litmus(src_cat, filter_litmus_suite, src_log)
        if not os.path.exists(tgt_log):
            for litmus_file_path in filter_litmus_suite:
                litmus_name = os.path.splitext(os.path.basename(litmus_file_path))[0]
                base_log_path = litmus_run(litmus_name, litmus_file_path, 100000)
            integrate_chip_log(tgt_log)

        if not os.path.exists(dif_log):
            dif_litmus_suite = get_model_diff(src_log, tgt_log, mode1= 'herd', mode2= 'chip')
            dif_litmus_suite = [item for item in dif_litmus_suite if item not in filter_litmus_suite]
            litmus_suite = sort_litmus_by_weight(dif_litmus_suite)
            model_1_dict = {r.name: r.states for r in parse_herd_log(src_log)}
            model_2_dict = {r.name: r.states for r in parse_chip_log(tgt_log)}
            with open (dif_log, 'w') as f:
                for litmus in litmus_suite:
                    f.write(litmus)
                    f.write('\n')


        else:
            with open(dif_log, 'r') as f:
                litmus_suite = f.readlines()
                litmus_suite = [litmus.strip ()for litmus in litmus_suite]
        return litmus_suite




    def synth(self):
        start = time.time()
        src_cat = os.path.join(config.CAT_DIR,'riscv-complete.cat')
        src_log = os.path.join(config.INPUT_DIR,'herd/herd_results_rvwmo_U740.log')
        tgt_log = os.path.join(config.INPUT_DIR,'chip_execution_logs/U740/chip_log.txt')
        dif_log = os.path.join(config.HERD_LOG_DIR_PATH,'dif_litmus_U740_RVWMO.log')
        litmus_test_suite = self.get_dif_litmus_datasets_for_chips(src_cat, src_log, tgt_log, dif_log)
        # print(len(litmus_test_suite))
        litmus_test_suite = [search_file(litmus, sifive_litmus_dir, '.litmus') for litmus in litmus_test_suite]

        # synth
        with open(exp_3_output_log_path, 'w') as f:
            ori = sys.stdout
            sys.stdout = f
            config.init()
            config.set_var('reg_size',64)

            cur_mm = get_rvwmo_model()
            patch, ppo_list = synth_by_test_pattern_online(None, cur_mm, litmus_test_suite, None, mode='chip', chip_log_path = tgt_log, iterate_count = 2)
            time_cost = time.time() - start
            sys.stdout = ori
            f.close()

        with open(exp_3_output_result_file_path, 'w') as f:
            ori = sys.stdout
            sys.stdout = f
            if patch is not None:
                for _,ppo,_,_ in patch:
                    print(ppo)
            print('time:', time_cost)
            sys.stdout = ori
            f.close()

        with open(exp_3_test_ppo_path, 'w') as f:
            ori = sys.stdout
            sys.stdout = f
            for ppo in ppo_list:
                print(ppo)
            sys.stdout = ori
            f.close()


if __name__ == '__main__':
    bar = "=" * 60
    header = f"Experiment 3: synth sifive"
    centered_header = header.center(60)
    print(f"\n{bar}\n{centered_header}\n{bar}\n")
    delete_history()
    test = TestChipSifive()
    test.synth()

