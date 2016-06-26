import os
import sys

__author__ = 'jwkim'
'''
any comments?
'''

from run_by_order import parse_argument
import argparse

def main(args=None):
    tmp_cmd = [
        'python3',
        '/data/chunlab/tool/scripts/MCSyncSid.py',
    ]

    sample_list, random_reads =parse_argument(args=None)

    for sid in sample_list:
        tmp_cmd.append(sid)
        cmd = ' '.join(tmp_cmd)

        os.system(cmd)


if __name__ == '__main__':
    main(sys.argv[1:])