__author__ = 'jwkim'
'''
any comments?
'''

import glob
import os
from concurrent.futures import ProcessPoolExecutor
from subprocess import Popen
from subprocess import PIPE


def count_line_num(fastq):
    tmp_cmp = [
        'gunzip -c',
        fastq,
        ' | wc -l',
    ]
    cmd = ' '.join(tmp_cmp)
    popen = Popen(cmd, shell=True, stdout=PIPE)
    output, error = popen.communicate()
    return fastq, int(str(output.strip(), 'utf-8'))/4


def make_file_list():
    file_list = sorted([x for x in glob.glob('*.fastq.gz') if not x.startswith('Undetermined')])
    result = list()

    with ProcessPoolExecutor(max_workers=10) as executor:
        for fastq in file_list:
            if os.path.exists(fastq):
                result = (executor.map(count_line_num, file_list))

    for file_name, reads in sorted(result, key=lambda x: x[1]):
        print('{} > {}'.format(file_name, reads))


def main():
    make_file_list()


if __name__ == '__main__':
    main()
