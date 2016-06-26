import os
import sys

__author__ = 'jwkim'
'''
any comments?
'''

from run_by_order import parse_argument


def main(args=None):
    sample_list, random_reads = parse_argument(args=None)

    for sid in sample_list:
        print(sid)


if __name__ == '__main__':
    main(sys.argv[1:])
