import logging
import sys

__author__ = 'jwkim'
'''
any comments?
'''

from community.miseq_mc_run_by_order import FetchSampleID
from community.miseq_mc_send_cook_fq_to_rtang import SendFqRtang
import argparse


def parse_argument(args=None):
    parser = argparse.ArgumentParser(
        description='This is getting ridiculous',
        epilog='example : python this.py -o [order_id] -d|-r [data_id|run_id] -n [random reads]',
    )
    parser.add_argument(
        '-o', '--order_id',
        type=int,
        default=None,
        metavar='',
        dest='order_id',
    )
    parser.add_argument(
        '-r', '--run_id',
        type=int,
        default=None,
        metavar='',
        dest='run_id',
    )
    parser.add_argument(
        '-d', '--data_id',
        type=int,
        default=None,
        metavar='',
        dest='data_id',
    )

    parser.add_argument(
        '-n', '--random_reads',
        type=int,
        default=20000,
        metavar='',
    )

    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
    logging.info(args)

    if args.order_id and args.run_id and args.data_id is None:
        Runclass = FetchSampleID(order_id=args.order_id, run_id=args.run_id)
        sample_list = Runclass.sample_id_list
    elif args.order_id and args.data_id and args.run_id is None:
        Runclass = FetchSampleID(order_id=args.order_id, data_id=args.data_id)
        sample_list = Runclass.sample_id_list
    elif args.order_id and args.data_id is None and args.run_id is None:
        Runclass = FetchSampleID(order_id=args.order_id)
        sample_list = Runclass.sample_id_list
    elif args.run_id and args.order_id is None and args.data_id is None:
        Runclass = FetchSampleID(run_id=args.run_id)
        sample_list = Runclass.sample_id_list
    else:
        sys.exit('python this.py -h')

    return sample_list, args.random_reads


def run_mc_pipleline(sample_id_list, random_reads):
    for sample_id in sample_id_list:
        RunClass = SendFqRtang(sample_id, random_num=random_reads)
        RunClass.main()


if __name__ == '__main__':
    sample_list, random_reads = parse_argument(sys.argv[1:])
    run_mc_pipleline(sample_list, random_reads)
