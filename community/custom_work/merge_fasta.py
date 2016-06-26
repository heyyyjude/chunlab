import sys
import os
import argparse

__author__ = 'jwkim'
'''
any comments?
'''


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='this is getting worse and worse instead of getting better and better'
    )

    parser.add_argument(
        '-i',
        '--input_fasta',
        type=str,
        required=True,
        metavar='',
        nargs='+',
    )

    parser.add_argument(
        '-o',
        '--out_fasta',
        type=str,
        required=True,
        metavar='',
    )

    args = parser.parse_args()

    for x in args.input_fasta:
        in_fasta = x + '.fasta'
        if not os.path.isfile(in_fasta):
            sys.exit(in_fasta + ' is not found!')
        else:
            cmd = 'cat ' + in_fasta + ' >> ' + args.out_fasta + '.fasta'
            os.system(cmd)


if __name__ == '__main__':
    parse_args(sys.argv[1:])
