import gzip
import logging
import os
import sys
import shutil

from Bio import SeqIO

from community.miseq_mc_cp_rawdata import FastqInfo
from community.seq_tools.fastq_parser import parse_fastq

__author__ = 'jwkim'
'''
any comments?
'''


class PreProcess(FastqInfo):
    def __init__(self, sample_id, random_num):
        super().__init__(sample_id)
        self.find_path()
        self.cp_fastq_hulk_dir()

        self._preprocess_jar_cmd = None
        self.fq_for_path = None
        self.fq_rev_path = None
        self._logfile = None
        self._random_num = random_num

        # processed fastq after the miseq_bact job
        self._processed_fa_path = None
        self._hulk_sample_submit_path = None

        # deprecated
        # self.survived_reads = 0

    @property
    def random_num(self):
        return self._random_num

    def rename_fastq_gz(self):
        cur_dir = os.getcwd()

        os.chdir(self.hulk_sample_dir_path)
        cmd = "rename -v 's/_S\d+_L001_R(\d+)_001/_$1/' *.gz"
        os.system(cmd)

        os.chdir(cur_dir)

    def standard_out_fastq_gz(self):
        # This is for making /data/order~/SampleID/SampleName.fastq
        self.fq_for_path = os.path.splitext(self.hulk_fq_forward_path)[0]
        self.fq_rev_path = os.path.splitext(self.hulk_fq_reverse_path)[0]

        with gzip.open(self.hulk_fq_forward_path)as fqgz, open(self.fq_for_path, 'w')as fout:
            for line in fqgz:
                line = str(line, 'utf-8')
                fout.write(line)

        with gzip.open(self.hulk_fq_reverse_path, 'r')as fqgz, open(self.fq_rev_path, 'w')as fout:
            for line in fqgz:
                line = str(line, 'utf-8')
                fout.write(line)

    def generate_preprocess_jar_cmd(self):
        preprocess_jar_cmd = [
            'java -jar /chunlab/app/community/bi-community/bi-community.jar -j miseq_bact'
        ]

        preprocess_argv = '-f1 {} -f2 {} -s {} -o {} -rlc {} -lc {} -fp {} -rp {}'.format(
            self.fq_for_path,
            self.fq_rev_path,
            self.sample_info.sample_name,
            self.hulk_sample_dir_path,
            150,
            300,
            self.sample_info.barcode_forward,
            self.sample_info.barcode_reverse,
        )
        preprocess_jar_cmd.append(preprocess_argv)
        self._preprocess_jar_cmd = ' '.join(str(x) for x in preprocess_jar_cmd)

    @property
    def preprocess_jar_cmd(self):
        return self._preprocess_jar_cmd

    def run_preprocess_jar(self):
        print(self.preprocess_jar_cmd)
        os.system(self.preprocess_jar_cmd)

    def run_random_select(self):
        # java SeqRandomSampling does not seem to take the abs path for fastq files
        merged_fq = '{}{}'.format(
            self.sample_info.sample_name,
            '.merged.primer_trim.len_trim.fastq'
        )

        cur_dir = os.getcwd()
        os.chdir(self.hulk_sample_dir_path)

        merged_fa = os.path.splitext(merged_fq)[0] + '.fasta'
        SeqIO.convert(merged_fq, 'fastq', merged_fa, 'fasta')

        if not os.path.exists(merged_fq):
            print('{} is not found in {}'.format(
                merged_fq,
                self.hulk_sample_dir_path,
            )
            )

        jar_cmd = ['java SeqRandomSampling',
                   '-c ',
                   self.random_num,
                   '-i',
                   merged_fa,
                   ]

        final_jar_cmd = ' '.join(str(x) for x in jar_cmd)
        os.system(final_jar_cmd)
        os.chdir(cur_dir)

    def rename_processed_fq(self):
        merged_primer_trim_len_trim_fasta = os.path.join(
            self.hulk_sample_dir_path,
            '{}{}'.format(
                self.sample_info.sample_name,
                '.merged.primer_trim.len_trim_random.fasta'
            )
        )

        if not os.path.exists(merged_primer_trim_len_trim_fasta):
            print('the merged.primer_trim.len_trim_random.fasta is not found in {} and the file name is {} '.format(
                self.hulk_sample_dir_path,
                merged_primer_trim_len_trim_fasta,
            ))
            sys.exit()

        self._processed_fa_path = os.path.join(
            self.hulk_sample_dir_path,
            self.sample_info.sample_name + '.fasta'
        )

        os.renames(
            merged_primer_trim_len_trim_fasta,
            self._processed_fa_path
        )

        if not os.path.exists(self._processed_fa_path):
            print('the cooked fastq is not found! it is supposed to be in {} '.format(
                self.hulk_sample_dir_path
            )
            )
            sys.exit()

        self._logfile = os.path.join(
            self.hulk_sample_dir_path,
            'PreProcessingMiSeq_{}.log'.format(
                self.sample_info.sample_name
            )
        )

    @property
    def logfile(self):
        return self._logfile

    def writing_log(self):
        if not os.path.exists(self.logfile):
            print('the log.file is not found! it is supposed to be in {} '.format(
                self.hulk_sample_dir_path
            )
            )
            sys.exit()

        with open(self.logfile, 'a')as fout:
            num_lines = sum(1 for line in open(self._processed_fa_path) if line.startswith('>'))
            fout.write('Random selection\tNA\tNA\tNA\t' + str(num_lines) + '\n')
            fout.write('ForwardBarcode\t' + self.sample_info.barcode_forward + '\n')
            fout.write('ReverseBarcode\t' + self.sample_info.barcode_reverse + '\n')

    @property
    def processed_fa_path(self):
        return self._processed_fa_path

    def make_submit_dir(self):
        self._hulk_sample_submit_path = os.path.join(self.hulk_sample_dir_path, 'submit')
        if not os.path.exists(self._hulk_sample_submit_path):
            os.makedirs(self._hulk_sample_submit_path)
        shutil.copy(self.processed_fa_path, self._hulk_sample_submit_path)

    @property
    def hulk_sample_submit_path(self):
        return self._hulk_sample_submit_path

    # deprecated functions.
    def length_trim(self):
        if os.path.exists(self.processed_fa_path):
            pass
        else:
            print('{} is not found.'.format(
                self.processed_fa_path
            )
            )
            sys.exit()

        self.survived_reads = 0
        shutil.copy(self.processed_fa_path, self.processed_fa_path + '.length_trim.bak')
        for head, seq, strand, qual in parse_fastq(self.processed_fa_path):
            with open(self.processed_fa_path, 'w')as fout:
                if len(seq) >= 300:
                    self.survived_reads += 1
                    fout.write(head)
                    fout.write(seq)
                    fout.write(strand)
                    fout.write(qual)

    def PreProcessMain(self):
        self.rename_fastq_gz()
        logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

        self.standard_out_fastq_gz()
        logging.info('generating fastq from fastq.gz is done.')

        self.generate_preprocess_jar_cmd()
        self.run_preprocess_jar()
        self.run_random_select()

        self.rename_processed_fq()
        self.writing_log()
        logging.info(self.logfile)
        logging.info('rename_processed_fq is done.')

        self.make_submit_dir()
