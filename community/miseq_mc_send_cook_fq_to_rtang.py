import logging
import os

__author__ = 'jwkim'
'''
any comments?
'''

from community.miseq_mc_preprocess import PreProcess


class SendFqRtang(PreProcess):
    def __init__(self, sample_id, random_num):
        super().__init__(sample_id, random_num)
        self._tag = None
        self.rtang_jar_cmd = None

    def generate_cmd(self):

        if self.sample_info._data_id:
            self._tag = 'O{}_D{}_S{}'.format(
                self.sample_info.order_id,
                self.sample_info._data_id,
                self.sample_info.sample_id,
            )
        else:
            self._tag = 'O{}_R{}_S{}'.format(
                self.sample_info.order_id,
                self.sample_info._run_id,
                self.sample_info.sample_id,
            )

        jar_cmd = [
            'java -Dspring.profiles.active=rtang -jar /chunlab/app/community/bulk-client/sdk.cli.client.jar',
            '-cmd',
            'excuteBulkCommunityOnDir',
            '-id',
            self.sample_info.cus_id,
            '-loc',
            self._hulk_sample_submit_path,
            '-t Bacteria',
            '-priority HIGH',
            '-tag',
            self._tag,
            '-name',
            self._tag,
            '-channel',
            'ORDER',
        ]
        self.rtang_jar_cmd = ' '.join(str(x) for x in jar_cmd)

    @property
    def tag(self):
        return self._tag

    def run_rtang_jar_cmd(self):
        os.system(self.rtang_jar_cmd)

    def write_jar_cmd_logs(self):
        cur_dir = os.getcwd()
        os.chdir(self.hulk_sample_submit_path)

        with open(self.sample_info.sample_name + '.txt', 'w')as fout:
            fout.write(self.preprocess_jar_cmd + '\n')
            fout.write(self.rtang_jar_cmd + '\n')

        os.chdir(cur_dir)

    def main(self):
        logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
        self.PreProcessMain()
        self.generate_cmd()
        self.run_rtang_jar_cmd()

        logging.info('jar cmd - {}'.format(
            self.preprocess_jar_cmd
        )
        )
        logging.info('rtang jar cmd - {}'.format(
            self.rtang_jar_cmd
        )
        )
        self.write_jar_cmd_logs()