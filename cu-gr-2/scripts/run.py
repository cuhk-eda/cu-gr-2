#!/usr/bin/env python3

import argparse
import os
import datetime
from run_base import *
from visualize_heatmap import visualize

# constants
binary = 'route'

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('benchmarks', choices=all_benchmarks.get_choices(), nargs='+', metavar='BENCHMARK',
                    help='Choices are ' + ', '.join(all_benchmarks.get_choices()))
parser.add_argument('-m', '--mode', choices=modes)
parser.add_argument('-s', '--steps', choices=['route', 'eval', 'view', 'nano'], nargs='+', default=['route'])
parser.add_argument('-p', '--benchmark_path')
parser.add_argument('-t', '--threads', type=int, default=8)
parser.add_argument('-i', '--rrr_iters', type=int)
parser.add_argument('-e', '--eval_all_rrr_iters', action='store_true')
parser.add_argument('-o', '--others', default='')
parser.add_argument('-l', '--log_dir')
args = parser.parse_args()
cmd_suffix = args.others
if args.eval_all_rrr_iters:
    cmd_suffix += ' -rrrWriteEachIter 1'

if args.rrr_iters is not None:
    cmd_suffix += ' -rrrIters {}'.format(args.rrr_iters)

# seleted benchmarks
bms = all_benchmarks.get_selected(args.benchmarks)
bm_path = args.benchmark_path
if bm_path is None:
    bm_path = os.environ.get('BENCHMARK_PATH')
    if bm_path is None:
        print('Benchmark path is not specified.')
        quit()

# mode cmd_prefix
cmd_prefix = mode_prefixes[args.mode]
if args.mode == 'valgrind':
    print('Please make sure the binary is not compiled with static linking to avoid false alarm')

# run
if args.log_dir is None:
    now = datetime.datetime.now()
    log_dir = 'run{:02d}{:02d}'.format(now.month, now.day)
else:
    log_dir = args.log_dir

run('mkdir -p {}'.format(log_dir))
print('The following benchmarks will be ran: ', bms)


def route():
    guide_file = '{0}/{1}.solution.guide'.format(bm_log_dir, bm.full_name)
    log_file = '{0}/{1}.log'.format(bm_log_dir, bm.full_name)

    run('{cmd_prefix} ./{0} -lef {1}.input.lef -def {1}.input.def -threads {2} -output {3} {5} |& tee {4}'.format(
        binary, file_name_prefix, args.threads, guide_file, log_file, cmd_suffix, cmd_prefix=cmd_prefix))

    if args.mode == 'gprof':
        run('gprof {} > {}.gprof'.format(binary, bm.full_name))
        run('./gprof2dot.py -s {0}.gprof | dot -Tpdf -o {0}.pdf'.format(bm.full_name))
    
    # visualize grid graph heatmap
    heatmap_name = 'heatmap.txt'
    if os.path.exists(heatmap_name):
        visualize(heatmap_name)
        run('rm {}'.format(heatmap_name))
        # update figs
        run('rm -rf {}/figs'.format(bm_log_dir))
        run('mv -f figs {}'.format(bm_log_dir))
        
    run('mv *.solution.guide* *.solution.def* *.gprof *.pdf {} 2>/dev/null'.format(bm_log_dir))


def evaluate():
    guide_file = '{0}/{1}.solution.guide'.format(bm_log_dir, bm.full_name)
    sol_file = '{0}/{1}.solution.def'.format(bm_log_dir, bm.full_name)
    dr_log_file = '{0}/{1}_dr_eval.log'.format(bm_log_dir, bm.full_name)
    log_file = '{0}/{1}_eval.log'.format(bm_log_dir, bm.full_name)
    dr_file = 'drcu'
    bm_yy = int(bm.full_name[4:6])
    run('cp eval/ispd{0}eval/ispd{0}eval* ./'.format(bm_yy))

    def evaluate_once():
        run('./{0} -lef {1}.input.lef -def {1}.input.def -guide {2} -threads {3} -tat 2000000000 -output {4} |& tee {5}'.format(
            dr_file, file_name_prefix, guide_file, args.threads, sol_file, dr_log_file))
        # run('gdb --args ./drcu_debug -lef {1}.input.lef -def {1}.input.def -guide {2} -threads {3} -tat 2000000000 -output {4} |& tee {5}'.format(
        #     dr_file, file_name_prefix, guide_file, args.threads, sol_file, dr_log_file))

        if bm_yy == 18:
            run('./ispd{0}eval.sh -lef {1}.input.lef -guide {2} -def {3} -thread {4} |& tee {5}'.format(
                bm_yy, file_name_prefix, guide_file, sol_file, args.threads, log_file))
        else:
            run('./ispd{0}eval.sh -lef {1}.input.lef -guide {2} -idef {1}.input.def -odef {3} -thread {4} |& tee {5}'.format(
                bm_yy, file_name_prefix, guide_file, sol_file, args.threads, log_file))

    evaluate_once()

    if args.eval_all_rrr_iters:
        for i in range(args.rrr_iters):
            sol_file = '{}/iter{}_{}.solution.def'.format(bm_log_dir, i, bm.full_name)
            log_file = 'iter{}_{}_eval.log'.format(i, bm.full_name)
            evaluate_once()
    run('rm ispd{0}eval_bin ispd{0}eval.sh ispd{0}eval.tcl ispd{0}eval.w *.def.v eval.def'.format(bm_yy))
    run('mv innovus.* *.solution.def* eval.*.rpt {} 2>/dev/null'.format(bm_log_dir))


def view():
    file = open('tmp.tcl', 'w')
    file.write('loadLefFile {}.input.lef\n'.format(file_name_prefix))
    file.write('loadDefFile {}/{}.solution.def\n'.format(bm_log_dir, bm.full_name))
    file.write('setMultiCpuUsage -localCpu {}\n'.format(args.threads))
    file.write('win\n')
    file.close()
    run('innovus -init tmp.tcl')
    run('rm innovus.* *.drc.rpt *.solution.def.v tmp.tcl')


for bm in bms:
    bm_log_dir = '{}/{}'.format(log_dir, bm.abbr_name)
    file_name_prefix = '{0}/iccad2019c/{1}/{1}'.format(bm_path, bm.full_name)

    run('mkdir -p {}'.format(bm_log_dir))
    if 'route' in args.steps:
        route()
    if 'eval' in args.steps:
        evaluate()
    if 'view' in args.steps:
        view()
