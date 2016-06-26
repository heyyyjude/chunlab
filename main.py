import sys

from community.miseq_mc_send_cook_fq_to_rtang import SendFqRtang

__author__ = 'jwkim'
'''
any comments?
'''


def main(sample_id, random_num=20000):
    RunClass = SendFqRtang(sample_id, random_num)
    RunClass.main()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('python3 this.py sample_id random_num' )
    main(sys.argv[1], sys.argv[2])
    #test sampleid - 46651
