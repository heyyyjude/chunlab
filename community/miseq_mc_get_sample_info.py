from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_info.corp_chunlab import TblSample
from database_info.corp_chunlab import TblOrderList
from database_info.database_info import corp_chunlab_url

__author__ = 'jwkim'
'''
any comments?
'''


class SampleInfo(object):
    def __init__(self, sample_id):
        admin_engine = create_engine(
            corp_chunlab_url,
            convert_unicode=True,
        )
        admin_session = sessionmaker(bind=admin_engine)
        admin_session.configure(bind=admin_engine)
        self.session = admin_session()

        self._barcode_forward = 'CCTACGGGNGGCWGCAG'
        self._barcode_reverse = 'GACTACHVGGGTATCTAATCC'
        self._sample_id = sample_id.__str__()
        self._order_id = None
        self._run_id = None
        self._sample_name = None
        self._cus_id = None
        self._data_id = None

    def fetch_sample_info_by_sample_id(self):
        '''
        fetch order-id, run-id, sample-name, customer_user_uid
        :return:
        :rtype:
        '''
        query = self.session.query(
            TblSample.f_order_uid,
            TblSample.f_run_id,
            TblSample.f_sample_uid,
            TblSample.f_sample_name,
            TblSample.f_sample_machine_name,
            TblOrderList.customer_user_uid,
            TblSample.f_sample_description,
            TblSample.f_sample_type,
            TblSample.f_data_id,
        ).filter(
            TblOrderList.uid == TblSample.f_order_uid
        ).filter(
            TblSample.f_sample_uid == self.sample_id)

        for item in query:
            # get sample_name
            if item.f_sample_machine_name:
                self._sample_name = item.f_sample_machine_name.__str__()
            else:
                self._sample_name = item.f_sample_name.__str__()

            # get the latter run_id
            if item.f_data_id:
                self._data_id = item.f_data_id.__str__()
            elif item.f_run_id.__contains__(','):
                self._run_id = item.f_run_id.split(',')[-1].__str__()
            else:
                self._run_id = item.f_run_id.__str__()

            self._cus_id = item.customer_user_uid.__str__()
            self._order_id = item.f_order_uid.__str__()

            # this is for the taxon and the primers
            if item.f_sample_description.__contains__(':'):
                self._barcode_forward, self._barcode_reverse = item.f_sample_description.split(':')
            elif item.f_sample_type.strip() == 'B':
                pass
            elif item.f_sample_type.strip() == 'A':
                self._barcode_forward = 'CAGCCGCCGCGGTAA'
                self._barcode_reverse = 'TACNVGGGTATCTAATCC'
            # this is for its
            else:
                pass

        self.session.close()

    @property
    def barcode_forward(self):
        return self._barcode_forward

    @property
    def barcode_reverse(self):
        return self._barcode_reverse

    @property
    def sample_id(self):
        return self._sample_id.__str__()

    @property
    def order_id(self):
        return self._order_id.__str__()

    @property
    def R_run_id(self):
        return 'Run' + self._run_id.__str__()

    @property
    def sample_name(self):
        return self._sample_name.__str__()

    @property
    def cus_id(self):
        return self._cus_id.__str__()

    @property
    def D_data_id(self):
        return 'Data0' + self._data_id.__str__()

    def __str__(self):
        return 'sample_id:{} sample_name:{} _order_id:{} run_id:{} _cus_id:{}'.format(
            self.sample_id, self.sample_name, self.order_id, self.R_run_id, self.cus_id
        )

    def main(self):
        self.fetch_sample_info_by_sample_id()
