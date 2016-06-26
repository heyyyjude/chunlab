# coding: utf-8
from sqlalchemy import Column, DateTime, Enum, Integer, String, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TblOrderList(Base):
    __tablename__ = 'tbl_order_list'

    uid = Column(Integer, primary_key=True)
    job_type = Column(String(100))
    order_type = Column(String(100))
    f_original_order_uid = Column(Integer, server_default=text("'0'"))
    method = Column(String(100), nullable=False)
    customer_info = Column(String(200), index=True)
    customer_user_uid = Column(Integer, server_default=text("'-1'"))
    customer_info_cc = Column(String(400))
    customer_contect = Column(String(200))
    customer_id = Column(String(10))
    sample_sheet_file = Column(String(200))
    sample_count = Column(String(10))
    sample_cancel_count = Column(String(10))
    sample_cancel_count_dna = Column(String(10))
    sample_cancel_count_macro = Column(String(10), nullable=False, server_default=text("'0'"))
    sample_cancel_count_nicem = Column(String(10), nullable=False, server_default=text("'0'"))
    creator = Column(String(20))
    order_create_date = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    sample_received_date = Column(String(10))
    reExp_count = Column(String(10))
    analyzer = Column(String(100))
    experimenter = Column(String(100))
    project_manager = Column(String(100))
    sample_name = Column(String(4000))
    etc = Column(String(4000))
    sample_payment = Column(String(10))
    experiment_first_start_date = Column(String(10))
    experiment_final_start_date = Column(String(10))
    is_project = Column(String(1), server_default=text("'N'"))
    send_back = Column(String(1), server_default=text("'N'"))
    sequencing_type = Column(String(50))
    qc_date = Column(String(50))
    qc_pass = Column(String(10))
    sample_return = Column(String(1))
    customer_sample_return = Column(String(1))
    classification = Column(String(1), server_default=text("'D'"))
    f_version = Column(Integer, server_default=text("'1'"))
    f_progress = Column(Integer, server_default=text("'1'"))
    f_samples_count = Column(String(10), server_default=text("''"))
    f_responsibility = Column(String(10), server_default=text("''"))
    f_taxon_type = Column(Integer, server_default=text("'1'"))
    f_guide = Column(Integer, server_default=text("'0'"))
    f_customer_info_cc_check = Column(Integer, server_default=text("'0'"))
    mis_doc_no = Column(String(16), server_default=text("''"))
    mis_item_uid = Column(String(14), server_default=text("''"))
    mis_item_select = Column(String(14), server_default=text("''"))
    is_del = Column(Enum(u'Y', u'N'), index=True, server_default=text("'N'"))
    del_desc = Column(Text)
    is_send_mail = Column(Enum(u'Y', u'N'), server_default=text("'N'"))
    order_amount = Column(Integer, server_default=text("'0'"))


class TblRunDate(Base):
    __tablename__ = 'tbl_run_date'

    uid = Column(Integer, primary_key=True)
    f_run_uid = Column(Integer, index=True)
    f_run_date = Column(String(10), index=True)


class TblSample(Base):
    __tablename__ = 'tbl_samples'

    f_sample_uid = Column(Integer, primary_key=True)
    f_order_uid = Column(Integer, nullable=False, index=True, server_default=text("'-1'"))
    f_sample_name = Column(String(100), server_default=text("''"))
    f_sample_machine_name = Column(String(100), server_default=text("''"))
    f_source_keywords = Column(String(100), server_default=text("''"))
    f_reference_name = Column(String(100), server_default=text("''"))
    f_sample_description = Column(String(200), server_default=text("''"))
    f_runner = Column(String(50), server_default=text("''"))
    f_type = Column(String(50), server_default=text("''"))
    f_rcv_date = Column(String(10), server_default=text("''"))
    f_sample_type = Column(String(1), nullable=False, server_default=text("''"))
    f_start_date = Column(String(10), server_default=text("''"))
    f_step = Column(Integer, server_default=text("'0'"))
    f_step_status = Column(Integer, server_default=text("'0'"))
    f_data_id = Column(String(100), server_default=text("''"))
    f_run_id = Column(String(100), server_default=text("''"))
    f_org_sample_uid = Column(Integer, server_default=text("'-1'"))
    f_proc_person = Column(String(50), server_default=text("'|-1|'"))
    f_pcr_finish_date = Column(String(10), server_default=text("''"))
    f_seq_finish_date = Column(String(10), server_default=text("''"))
    f_analy_finish_date = Column(String(10), server_default=text("''"))
    f_cus_delivery_date = Column(String(10), server_default=text("''"))
    f_machine = Column(String(50), server_default=text("''"))
    f_download = Column(String(500))
