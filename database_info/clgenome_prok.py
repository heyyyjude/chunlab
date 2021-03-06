# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, Index, Integer, String, Text, text
from sqlalchemy.dialects.mysql.base import MEDIUMBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Contig(Base):
    __tablename__ = 'contig'

    project_uid = Column(Integer, nullable=False, index=True)
    contig_index = Column(Integer, nullable=False)
    mol_type = Column(Integer, server_default=text("'0'"))
    mol_shape = Column(String(100))
    gi = Column(Integer, server_default=text("'-1'"))
    acc_ver = Column(String(100), primary_key=True, unique=True)
    definition = Column(Text, nullable=False)
    title = Column(String(200))
    sequence = Column(MEDIUMBLOB, nullable=False)


class ContigCopy(Base):
    __tablename__ = 'contig_copy'

    project_uid = Column(Integer, nullable=False, index=True)
    contig_index = Column(Integer, nullable=False)
    mol_type = Column(Integer, server_default=text("'0'"))
    mol_shape = Column(String(100))
    gi = Column(Integer, server_default=text("'-1'"))
    acc_ver = Column(String(100), primary_key=True, unique=True)
    definition = Column(Text, nullable=False)
    title = Column(String(200))
    sequence = Column(MEDIUMBLOB, nullable=False)


class Feature(Base):
    __tablename__ = 'feature'
    __table_args__ = (
        Index('project_uid_feature_key_feature_index', 'project_uid', 'feature_key', 'feature_index'),
        Index('project_uid_feature_index', 'project_uid', 'feature_index'),
        Index('project_uid_ref_feature_name_domain', 'project_uid', 'ref_feature_name_domain')
    )

    feature_uid = Column(Integer, primary_key=True)
    project_uid = Column(Integer, nullable=False, server_default=text("'0'"))
    feature_key = Column(String(100, u'latin1_general_ci'), nullable=False)
    feature_name = Column(String(200, u'latin1_general_ci'))
    feature_index = Column(Integer, nullable=False, server_default=text("'-1'"))
    sub_feature_index = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    contig_index = Column(Integer, nullable=False, server_default=text("'-1'"))
    contig_acc = Column(String(100, u'latin1_general_ci'))
    location = Column(Text(collation=u'latin1_general_ci'), nullable=False)
    begin = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)
    iscomp = Column(Integer, nullable=False, server_default=text("'0'"))
    seq_dna = Column(String(collation=u'latin1_general_ci'))
    translation = Column(String(collation=u'latin1_general_ci'))
    length = Column(Integer, nullable=False, server_default=text("'-1'"))
    db_xref_gi = Column(Integer, nullable=False, server_default=text("'0'"))
    db_xref_GeneID = Column(Integer, nullable=False, server_default=text("'0'"))
    ref_feature_name = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_genus = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_genus = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_phylum = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_phylum = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_domain = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_domain = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    go_id = Column(Text(collation=u'latin1_general_ci'))
    go_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    seed_figfam_id = Column(String(100, u'latin1_general_ci'))
    seed_function = Column(Text(collation=u'latin1_general_ci'))
    seed_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    eggnog_id = Column(String(100, u'latin1_general_ci'))
    eggnog_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    CDD_id = Column(Integer, nullable=False, server_default=text("'-1'"))
    kegg_id = Column(Text(collation=u'latin1_general_ci'))
    kegg_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ann_source = Column(String(200, u'latin1_general_ci'))
    ann_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    cyc_id = Column(Text(collation=u'latin1_general_ci'))
    others = Column(Text(collation=u'latin1_general_ci'))
    allele = Column(Text(collation=u'latin1_general_ci'))
    anticodon = Column(Text(collation=u'latin1_general_ci'))
    artificial_location = Column(Text(collation=u'latin1_general_ci'))
    bound_moiety = Column(Text(collation=u'latin1_general_ci'))
    citation = Column(Text(collation=u'latin1_general_ci'))
    codon_start = Column(Integer, nullable=False, server_default=text("'-1'"))
    compare = Column(Text(collation=u'latin1_general_ci'))
    db_xref = Column(Text(collation=u'latin1_general_ci'))
    direction = Column(Text(collation=u'latin1_general_ci'))
    EC_number = Column(Text(collation=u'latin1_general_ci'))
    estimated_length = Column(Text(collation=u'latin1_general_ci'))
    exception = Column(Text(collation=u'latin1_general_ci'))
    experiment = Column(Text(collation=u'latin1_general_ci'))
    frequency = Column(Text(collation=u'latin1_general_ci'))
    function = Column(Text(collation=u'latin1_general_ci'))
    gene = Column(String(100, u'latin1_general_ci'))
    gene_synonym = Column(Text(collation=u'latin1_general_ci'))
    inference = Column(String(collation=u'latin1_general_ci'))
    locus_tag = Column(String(100, u'latin1_general_ci'))
    map = Column(Text(collation=u'latin1_general_ci'))
    mobile_element_type = Column(Text(collation=u'latin1_general_ci'))
    mod_base = Column(Text(collation=u'latin1_general_ci'))
    ncRNA_class = Column(Text(collation=u'latin1_general_ci'))
    note = Column(String(collation=u'latin1_general_ci'))
    number = Column(Text(collation=u'latin1_general_ci'))
    old_locus_tag = Column(Text(collation=u'latin1_general_ci'))
    operon = Column(Text(collation=u'latin1_general_ci'))
    partial = Column(Integer, nullable=False, server_default=text("'0'"))
    phenotype = Column(Text(collation=u'latin1_general_ci'))
    product = Column(Text(collation=u'latin1_general_ci'))
    protein_id = Column(String(100, u'latin1_general_ci'))
    pseudo = Column(Integer, nullable=False, server_default=text("'0'"))
    region_name = Column(Text(collation=u'latin1_general_ci'))
    replace = Column(Text(collation=u'latin1_general_ci'))
    ribosomal_slippage = Column(Integer, nullable=False, server_default=text("'0'"))
    rpt_family = Column(Text(collation=u'latin1_general_ci'))
    rpt_type = Column(Text(collation=u'latin1_general_ci'))
    rpt_unit_range = Column(Text(collation=u'latin1_general_ci'))
    rpt_unit_seq = Column(Text(collation=u'latin1_general_ci'))
    satellite = Column(Text(collation=u'latin1_general_ci'))
    site_type = Column(Text(collation=u'latin1_general_ci'))
    standard_name = Column(Text(collation=u'latin1_general_ci'))
    tag_peptide = Column(Text(collation=u'latin1_general_ci'))
    transcript_id = Column(String(100, u'latin1_general_ci'))
    transl_except = Column(Text(collation=u'latin1_general_ci'))
    transl_table = Column(Integer, nullable=False, server_default=text("'-1'"))
    trans_splicing = Column(Integer, nullable=False, server_default=text("'0'"))


class FeatureCopy(Base):
    __tablename__ = 'feature_copy'
    __table_args__ = (
        Index('project_uid_feature_key_feature_index', 'project_uid', 'feature_key', 'feature_index'),
        Index('project_uid_feature_index', 'project_uid', 'feature_index'),
        Index('project_uid_ref_feature_name_domain', 'project_uid', 'ref_feature_name_domain')
    )

    feature_uid = Column(Integer, primary_key=True)
    project_uid = Column(Integer, nullable=False, server_default=text("'0'"))
    feature_key = Column(String(100, u'latin1_general_ci'), nullable=False)
    feature_name = Column(String(200, u'latin1_general_ci'))
    feature_index = Column(Integer, nullable=False, server_default=text("'-1'"))
    sub_feature_index = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    contig_index = Column(Integer, nullable=False, server_default=text("'-1'"))
    contig_acc = Column(String(100, u'latin1_general_ci'))
    location = Column(Text(collation=u'latin1_general_ci'), nullable=False)
    begin = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)
    iscomp = Column(Integer, nullable=False, server_default=text("'0'"))
    seq_dna = Column(String(collation=u'latin1_general_ci'))
    translation = Column(String(collation=u'latin1_general_ci'))
    length = Column(Integer, nullable=False, server_default=text("'-1'"))
    db_xref_gi = Column(Integer, nullable=False, server_default=text("'0'"))
    db_xref_GeneID = Column(Integer, nullable=False, server_default=text("'0'"))
    ref_feature_name = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_genus = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_genus = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_phylum = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_phylum = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ref_feature_name_domain = Column(String(200, u'latin1_general_ci'))
    ref_feature_sim_domain = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    go_id = Column(Text(collation=u'latin1_general_ci'))
    go_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    seed_figfam_id = Column(String(100, u'latin1_general_ci'))
    seed_function = Column(Text(collation=u'latin1_general_ci'))
    seed_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    eggnog_id = Column(String(30, u'latin1_general_ci'))
    eggnog_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    CDD_id = Column(Integer, nullable=False, server_default=text("'-1'"))
    kegg_id = Column(Text(collation=u'latin1_general_ci'))
    kegg_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ann_source = Column(String(200, u'latin1_general_ci'))
    ann_evalue = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    cyc_id = Column(Text(collation=u'latin1_general_ci'))
    others = Column(Text(collation=u'latin1_general_ci'))
    allele = Column(Text(collation=u'latin1_general_ci'))
    anticodon = Column(Text(collation=u'latin1_general_ci'))
    artificial_location = Column(Text(collation=u'latin1_general_ci'))
    bound_moiety = Column(Text(collation=u'latin1_general_ci'))
    citation = Column(Text(collation=u'latin1_general_ci'))
    codon_start = Column(Integer, nullable=False, server_default=text("'-1'"))
    compare = Column(Text(collation=u'latin1_general_ci'))
    db_xref = Column(Text(collation=u'latin1_general_ci'))
    direction = Column(Text(collation=u'latin1_general_ci'))
    EC_number = Column(Text(collation=u'latin1_general_ci'))
    estimated_length = Column(Text(collation=u'latin1_general_ci'))
    exception = Column(Text(collation=u'latin1_general_ci'))
    experiment = Column(Text(collation=u'latin1_general_ci'))
    frequency = Column(Text(collation=u'latin1_general_ci'))
    function = Column(Text(collation=u'latin1_general_ci'))
    gene = Column(String(100, u'latin1_general_ci'))
    gene_synonym = Column(Text(collation=u'latin1_general_ci'))
    inference = Column(String(collation=u'latin1_general_ci'))
    locus_tag = Column(String(100, u'latin1_general_ci'))
    map = Column(Text(collation=u'latin1_general_ci'))
    mobile_element_type = Column(Text(collation=u'latin1_general_ci'))
    mod_base = Column(Text(collation=u'latin1_general_ci'))
    ncRNA_class = Column(Text(collation=u'latin1_general_ci'))
    note = Column(String(collation=u'latin1_general_ci'))
    number = Column(Text(collation=u'latin1_general_ci'))
    old_locus_tag = Column(Text(collation=u'latin1_general_ci'))
    operon = Column(Text(collation=u'latin1_general_ci'))
    partial = Column(Integer, nullable=False, server_default=text("'0'"))
    phenotype = Column(Text(collation=u'latin1_general_ci'))
    product = Column(Text(collation=u'latin1_general_ci'))
    protein_id = Column(String(100, u'latin1_general_ci'))
    pseudo = Column(Integer, nullable=False, server_default=text("'0'"))
    region_name = Column(Text(collation=u'latin1_general_ci'))
    replace = Column(Text(collation=u'latin1_general_ci'))
    ribosomal_slippage = Column(Integer, nullable=False, server_default=text("'0'"))
    rpt_family = Column(Text(collation=u'latin1_general_ci'))
    rpt_type = Column(Text(collation=u'latin1_general_ci'))
    rpt_unit_range = Column(Text(collation=u'latin1_general_ci'))
    rpt_unit_seq = Column(Text(collation=u'latin1_general_ci'))
    satellite = Column(Text(collation=u'latin1_general_ci'))
    site_type = Column(Text(collation=u'latin1_general_ci'))
    standard_name = Column(Text(collation=u'latin1_general_ci'))
    tag_peptide = Column(Text(collation=u'latin1_general_ci'))
    transcript_id = Column(String(100, u'latin1_general_ci'))
    transl_except = Column(Text(collation=u'latin1_general_ci'))
    transl_table = Column(Integer, nullable=False, server_default=text("'-1'"))
    trans_splicing = Column(Integer, nullable=False, server_default=text("'0'"))
    gene_map = Column(String(50, u'latin1_general_ci'), nullable=False, server_default=text("'0'"))


class Project(Base):
    __tablename__ = 'project'

    project_uid = Column(Integer, primary_key=True)
    project_acc = Column(String(50), nullable=False, unique=True)
    acc_others = Column(String(50), index=True, server_default=text("''"))
    project_type = Column(Integer, nullable=False, server_default=text("'-1'"))
    checksum = Column(String(32))
    status = Column(Integer, nullable=False, server_default=text("'-1'"))
    priority = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_tax_id = Column(Integer, nullable=False, server_default=text("'-1'"))
    ncbi_name = Column(String(100), nullable=False, index=True, server_default=text("''"))
    taxon_name = Column(String(100), nullable=False, index=True, server_default=text("''"))
    strain_property = Column(String(100))
    strain_name = Column(String(100))
    strain_type = Column(Integer, nullable=False, index=True, server_default=text("'-1'"))
    superkingdom = Column(String(20))
    taxonomy = Column(String(200))
    prefix = Column(String(50))
    WGS = Column(String(10))
    tag = Column(Text)
    gf_ref_acc = Column(String(50))
    gf_ref_acc_genus = Column(String(50))
    gf_ref_acc_phylum = Column(String(50))
    genome_size = Column(Integer, nullable=False, server_default=text("'-1'"))
    gc_content = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    n_chromosomes = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_plasmids = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_organelles = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_contigs = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_scaffolds = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_cds = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_features = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_tRNA = Column(Integer, nullable=False, server_default=text("'-1'"))
    n_rRNA = Column(Integer, nullable=False, server_default=text("'-1'"))
    genbank_released_date = Column(Date, nullable=False, server_default=text("'1970-01-02'"))
    genbank_created_date = Column(Date, nullable=False, server_default=text("'1970-01-02'"))
    genbank_modified_date = Column(Date, nullable=False, server_default=text("'1970-01-02'"))
    clg_created_date = Column(Date, nullable=False, server_default=text("'1970-01-02'"))
    publications = Column(Text)
    ssurrn_seq = Column(Text)
    ssurrn_acc = Column(String(30))
    ssurrn_match_acc = Column(String(30))
    ssurrn_match_sim = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ssurrn_match_tax = Column(Text)
    comment = Column(Text)
    year = Column(String(50), server_default=text("''"))
    source = Column(String(500), server_default=text("''"))
    geo_origin = Column(String(500), server_default=text("''"))
    country = Column(String(50), server_default=text("''"))
    coordinate = Column(String(50), server_default=text("''"))
    altitude = Column(String(50), server_default=text("''"))
    N25 = Column(Integer, nullable=False, server_default=text("'-1'"))
    N50 = Column(Integer, nullable=False, server_default=text("'-1'"))
    N75 = Column(Integer, nullable=False, server_default=text("'-1'"))
    stamp_insert = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    ssurrn_completeness = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    ssurrn_lack_begin = Column(Integer, nullable=False, server_default=text("'-1'"))
    ssurrn_lack_end = Column(Integer, nullable=False, server_default=text("'-1'"))
    taxon_type_acc = Column(String(50), server_default=text("''"))
    taxon_type_anib = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    biosample_acc = Column(String(50), server_default=text("''"))
    assembler = Column(String(250))
    chunlab_tag = Column(Text)
    coverage = Column(Float(asdecimal=True), nullable=False, server_default=text("'-1'"))
    method = Column(String(250), server_default=text("''"))
    method_coverage = Column(Text)
    method_mapped_reads = Column(Text)
    method_rawreads = Column(Text)
    run_uid = Column(Text)
    agp = Column(String)
    n_ssurrn_copy = Column(Integer, nullable=False, server_default=text("'-1'"))
    ssurrn_match_eztaxon_version = Column(String(50))


class ProjectCheck(Base):
    __tablename__ = 'project_check'

    project_uid = Column(Integer, primary_key=True)
    released_date = Column(Date, nullable=False)
    ready = Column(Integer, nullable=False, server_default=text("'-1'"))
    set_seq = Column(Integer, nullable=False, server_default=text("'-1'"))
    insert_contig = Column(Integer, nullable=False, server_default=text("'-1'"))
    insert_feature = Column(Integer, nullable=False, server_default=text("'-1'"))
    set_stat = Column(Integer, nullable=False, server_default=text("'-1'"))
    ssu_extracted = Column(Integer, nullable=False, server_default=text("'-1'"))
    proc_gene = Column(Integer, nullable=False, server_default=text("'-1'"))
    project_property_cds = Column(Integer, nullable=False, server_default=text("'-1'"))
    set_ref_feature_domain = Column(Integer, nullable=False, server_default=text("'-1'"))
    set_project_gene = Column(Integer, nullable=False, server_default=text("'-1'"))
    annotate_kegg = Column(Integer, nullable=False, server_default=text("'-1'"))
    annotate_eggnog = Column(Integer, nullable=False, server_default=text("'-1'"))
    annotate_seed = Column(Integer, nullable=False, server_default=text("'-1'"))
    annotate_go = Column(Integer, nullable=False, server_default=text("'-1'"))
    set_sub_feature_index = Column(Integer, nullable=False, server_default=text("'-1'"))
