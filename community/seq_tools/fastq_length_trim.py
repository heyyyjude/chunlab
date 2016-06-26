__author__ = 'jwkim'
'''
any comments?
'''

from community.seq_tools.fastq_parser import parse_fastq

def trim_length_cutoff(fastq, hulk_sample_path):
    outfile = hulk_sample_path + '/'+ fastq.rsplit('.', 1)[0] + '.length_cutoff.fastq'
    survived_reads = 0

    for head, seq, strand, qual in parse_fastq(fastq):
        with open(outfile, 'w')as fout:
            if len(seq) >= 300:
                survived_reads+=1
                fout.write(head)
                fout.write(seq)
                fout.write(strand)
                fout.write(qual)


