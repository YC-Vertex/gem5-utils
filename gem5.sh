#!/bin/bash

Gem5=~/gem5
Exec=${Gem5}/build/POWER64/gem5.opt
Conf=${Gem5}/configs/example/se.py
Cmd=${Gem5}/tests/test-progs/power-demo/hello_le

Util=~/gem5-utils
Log=${Util}/log/temp.log

touch ${Log}
${Exec} --debug-flags=Registers,O3CPUAll ${Conf} -c ${Cmd} > ${Log} 2>&1
cat ${Log}

