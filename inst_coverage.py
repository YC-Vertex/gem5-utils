from src.BaseUtil import parser
from src.LogParser import LogParser
from src.IsaParser import IsaParser

if __name__ == '__main__':

    parser.add_argument('--log', type=str, default='',
        help='log file')
    parser.add_argument('--output', type=str, default='',
        help='output csv file')
    args = parser.parse_args()


    # get implemented and covered instructions

    ip = IsaParser()
    lp = LogParser(args.log)

    inst_list = ip.getInstList()
    inst_trace = lp.getInstTrace()
    inst_trace_s = list(zip(*inst_trace))[0]
    inst_cover = list(set(inst_trace_s))

    if inst_cover.count('unknown') != 0:
        inst_cover.remove('unknown')


    # calculate instruction coverage
    
    ninsts = len(inst_list)
    ncover = len(inst_cover)
    cpc = ncover / ninsts * 100 # coverage percentage
    print(f'Number of insts implemented = {ninsts}')
    print(f'Number of insts covered in log file(s) = {ncover}')
    print(f'Instruction coverage = {cpc:.2f}%')


    # generate detailed stats and export as a csv file

    stats = [inst_cover.count(i) for i in inst_list]
    stats = list(zip(inst_list, stats))

    if args.output != '':
        with open(args.output, 'w') as f:
            for s in stats:
                f.write(f'{s[0]}, {s[1]}\n')
        print(f'Statistics exported to \'{args.output}\'.')

