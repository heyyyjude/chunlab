import glob
import os
import sys
import shutil

__author__ = 'jwkim'
'''
any comments?
'''

from community.miseq_mc_get_sample_info import SampleInfo


class FastqInfo(object):
    def __init__(self, sample_id):
        self._sample_info = SampleInfo(sample_id)
        self.sample_info.main()

        self.redbox_forward_fq_path = None
        self.redbox_reverse_fq_path = None
        self._hulk_fq_forward_path = None
        self._hulk_fq_reverse_path = None
        self._hulk_sample_dir_path = None

    @property
    def sample_info(self):
        return self._sample_info

    def find_path(self):
        default_path = None
        if self.sample_info._data_id :
            default_path = '/mnt/processed_rawdata/{}'.format(self.sample_info.D_data_id)
        else:
            default_path = '/mnt/processed_rawdata/{}'.format(self.sample_info.R_run_id)

        try:
            run_path = [x for x in glob.glob(default_path + '*') if os.path.isdir(x)][0]
        except Exception as e:
            print(e)
            print('The run_id:{} is not found.'.format(self.sample_info.R_run_id))
            sys.exit()
        else:
            run_path = os.path.abspath(run_path)
            self.redbox_forward_fq_path = '{}/{}_1.fastq.gz'.format(run_path, self.sample_info.sample_name)
            self.redbox_reverse_fq_path = '{}/{}_2.fastq.gz'.format(run_path, self.sample_info.sample_name)

        if os.path.exists(self.redbox_forward_fq_path) and os.path.exists(self.redbox_reverse_fq_path):
            pass
        else:
            print('The sample_id:{} and the sample name:{} are not  found in this {} folder.'.format(
                self.sample_info.sample_id,
                self.sample_info.sample_name,
                default_path,
            )
            )
            sys.exit()

    def cp_fastq_hulk_dir(self):
        '''
        set hulk sample dir path
        :return:
        :rtype:
        '''
        default_path = '/data/chunlab/data/order/community'

        hulk_sample_dir_path = os.path.join(
            default_path,
            self.sample_info._order_id,
            self.sample_info.sample_id,
        )

        self._hulk_sample_dir_path = hulk_sample_dir_path

        if not os.path.exists(hulk_sample_dir_path):
            os.makedirs(hulk_sample_dir_path)

        shutil.copy(self.redbox_forward_fq_path, hulk_sample_dir_path)
        shutil.copy(self.redbox_reverse_fq_path, hulk_sample_dir_path)

        self._hulk_fq_forward_path = os.path.join(
            hulk_sample_dir_path,
            os.path.basename(self.redbox_forward_fq_path)
        )
        self._hulk_fq_reverse_path = os.path.join(
            hulk_sample_dir_path,
            os.path.basename(self.redbox_reverse_fq_path)
        )

    @property
    def hulk_sample_dir_path(self):
        return self._hulk_sample_dir_path

    @property
    def hulk_fq_forward_path(self):
        return self._hulk_fq_forward_path

    @property
    def hulk_fq_reverse_path(self):
        return self._hulk_fq_reverse_path

    @property
    def hulk_sample_dir_path(self):
        return self._hulk_sample_dir_path

    def __str__(self):
        return r'the sample_id:{} the sample_name:{} the hulk_fq_forward_path:{} the hulk_fq_reverse_path:{}'.format(
            self.sample_info.sample_id,
            self.sample_info.sample_name,
            self._hulk_fq_forward_path,
            self._hulk_fq_reverse_path,
        )
