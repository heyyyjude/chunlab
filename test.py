__author__ = 'jwkim'
'''
any comments?
'''

import unittest

from community.miseq_mc_get_sample_info import SampleInfo
from community.miseq_mc_send_cook_fq_to_rtang import SendFqRtang


# test id  44179
class MiseqMC(unittest.TestCase):
    def test_get_sample_info(self):
        Test = SampleInfo('44179')
        Test.main()
        self.assertEqual(Test.sample_id.__str__(), '44179')
        self.assertEqual(Test.sample_name, 'HSY')
        self.assertEqual(Test._run_id.__str__(), '2632')

    def test_preprocess_jar_cmd(self):
        Test = SendFqRtang('44179', '20000')
        Test.PreProcessMain()
        Test.generate_cmd()
        self.assertEqual(Test.preprocess_jar_cmd.strip(),
                         'java -jar /chunlab/app/community/bi-community/bi-community.jar -j miseq_bact -f1 /data/chunlab/data/order/community/3922/44179/HSY_1.fastq -f2 /data/chunlab/data/order/community/3922/44179/HSY_2.fastq -s HSY -o /data/chunlab/data/order/community/3922/44179 -rlc 150 -lc 300 -fp CCTACGGGNGGCWGCAG -rp GACTACHVGGGTATCTAATCC')
        self.assertEqual(Test.rtang_jar_cmd.strip(),
                         'java -Dspring.profiles.active=rtang -jar /chunlab/app/community/bulk-client/sdk.cli.client.jar -cmd excuteBulkCommunityOnDir -id 1076 -loc /data/chunlab/data/order/community/3922/44179/submit -t Bacteria -priority HIGH -tag O3922_R2632_S44179 -name O3922_R2632_S44179 -channel ORDER')


if __name__ == '__main__':
    unittest.main()
