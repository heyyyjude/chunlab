import sys

__author__ = 'jwkim'
'''
any comments?
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_info.corp_chunlab import TblSample
from database_info.database_info import corp_chunlab_url


class FetchSampleID(object):
    def __init__(self, order_id=None, run_id=None, data_id=None):
        admin_engine = create_engine(
            corp_chunlab_url,
            convert_unicode=True,
        )
        admin_session = sessionmaker(bind=admin_engine)
        admin_session.configure(bind=admin_engine)
        self.session = admin_session()
        self._sample_id_list = list()
        self._order_id = order_id
        self._run_id = run_id
        self._data_id = data_id

    def fetch_sample_info_by_order_run(self):
        query = self.session.query(
            TblSample.f_sample_uid,
        ).filter(
            TblSample.f_order_uid == self._order_id
        ).filter(
            TblSample.f_run_id.like('%' + self._run_id.__str__())
        ).filter(
            TblSample.f_sample_type.in_(['B', 'A'])
        ).order_by(TblSample.f_sample_uid.desc())

        for item in query:
            self._sample_id_list.append(item.f_sample_uid)
        self.session.close()

    def fetch_sample_info_by_order_data(self):
        query = self.session.query(
            TblSample.f_sample_uid,
        ).filter(
            TblSample.f_order_uid == self._order_id
        ).filter(
            TblSample.f_data_id == self._data_id
        ).filter(
            TblSample.f_sample_type.in_(['B', 'A'])
        ).order_by(TblSample.f_sample_uid.desc())

        for item in query:
            self._sample_id_list.append(item.f_sample_uid)
        self.session.close()

    def fetch_sample_info_by_only_order(self):
        query = self.session.query(
            TblSample.f_sample_uid,
        ).filter(
            TblSample.f_order_uid == self._order_id
        ).filter(
            TblSample.f_sample_type.in_(['B', 'A'])
        ).order_by(TblSample.f_sample_uid.desc())

        for item in query:
            self._sample_id_list.append(item.f_sample_uid)
        self.session.close()

    def fetch_sample_info_by_only_run(self):
        query = self.session.query(
            TblSample.f_sample_uid,
        ).filter(
            TblSample.f_run_id.like('%' + self._run_id.__str__())
        ).filter(
            TblSample.f_sample_type.in_(['B', 'A'])
        ).order_by(TblSample.f_sample_uid.desc())

        for item in query:
            self._sample_id_list.append(item.f_sample_uid)
        self.session.close()

    @property
    def sample_id_list(self):
        if self._order_id and self._run_id:
            self.fetch_sample_info_by_order_run()
        elif self._order_id and self._data_id:
            self.fetch_sample_info_by_order_data()
        elif self._order_id:
            self.fetch_sample_info_by_only_order()
        elif self._run_id:
            self.fetch_sample_info_by_only_run()
        else:
            sys.exit("at least either an order_id or a run_id is required!")
        return self._sample_id_list
