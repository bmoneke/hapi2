""" Mappings for SQLite backend of SQLAlchemy """

from ..base import BLOB, String, Float, Integer, Date, Table

from ..base import declarative_base, Column, deferred, PickleType

from ..base import make_session_default

from ..base import commit, query

from hapi2.db.sqlalchemy import models

BLOBTYPE = BLOB
TEXTTYPE = String(255)
VARCHARTYPE = String
DOUBLETYPE = Float
INTTYPE = Integer
DATETYPE = Date

Base = declarative_base()
make_session = make_session_default

engine_meta = None
IS_UNIQUE = True
IS_NULLABLE = True

def search_string(query,cls,field,pattern):
    return query.filter(getattr(cls,field).ilike(pattern+'\0%'))

class PartitionFunction(models.PartitionFunction, models.CRUD_Generic, Base):

    id = Column(INTTYPE,primary_key=True)
    isotopologue_alias_id = Column('isotopologue_alias_id',INTTYPE,nullable=IS_NULLABLE) # ,ForeignKey('molecule_alias.id')
    source_alias_id = Column('source_alias_id',INTTYPE,nullable=IS_NULLABLE) # ,ForeignKey('source_alias.id')
    #Q296 = Column('Q296',DOUBLETYPE)
    tmin = Column('tmin',DOUBLETYPE)
    tmax = Column('tmax',DOUBLETYPE)
    comment = Column('format',VARCHARTYPE(255))
    status = Column('status',VARCHARTYPE(255))
    json = Column('json',VARCHARTYPE(255)) # auxiliary field containing non-schema information
    
    __TT__ = Column('__TT__',BLOBTYPE)
    __QQ__ = Column('__QQ__',BLOBTYPE)

    # additional HITRANonline-compliant parameters
    filename = Column('filename',VARCHARTYPE(255),nullable=IS_NULLABLE) # HITRANonline filename

    __table_args__ = (
        #Index('cross_section__molecule_alias_id', molecule_alias_id),
    )

class CrossSectionData(models.CrossSectionData, models.CRUD_Generic, Base):

    id = Column(INTTYPE,primary_key=True)
    header_id = Column('header_id',INTTYPE,nullable=IS_NULLABLE) # ,ForeignKey('cross_section.id')
    __nu__ = Column('__nu__',BLOBTYPE)
    __xsc__ = Column('__xsc__',BLOBTYPE)

    __table_args__ = (
    )

class CrossSection(models.CrossSection, models.CRUD_Generic, Base):

    id = Column(INTTYPE,primary_key=True)
    molecule_alias_id = Column('molecule_alias_id',INTTYPE,nullable=IS_NULLABLE) # ,ForeignKey('molecule_alias.id')
    source_alias_id = Column('source_alias_id',INTTYPE,nullable=IS_NULLABLE) # ,ForeignKey('source_alias.id')
    numin = Column('numin',DOUBLETYPE)
    numax = Column('numax',DOUBLETYPE)
    npnts = Column('npnts',INTTYPE)
    sigma_max = Column('sigma_max',DOUBLETYPE)
    temperature = Column('temperature',DOUBLETYPE)
    pressure = Column('pressure',DOUBLETYPE)
    resolution = Column('resolution',DOUBLETYPE)
    resolution_units = Column('resolution_units',VARCHARTYPE(5))
    broadener = Column('broadener',VARCHARTYPE(255))
    description = Column('description',VARCHARTYPE(255))
    apodization = Column('apodization',VARCHARTYPE(255))
    json = Column('json',VARCHARTYPE(255)) # auxiliary field containing non-schema information
    format = Column('format',VARCHARTYPE(255))
    status = Column('status',VARCHARTYPE(255))

    # additional HITRANonline-compliant parameters
    filename = Column('filename',VARCHARTYPE(255),unique=IS_UNIQUE) # HITRANonline filename
    
    # cross-section hash for data lineage...
    hash = Column('hash',VARCHARTYPE(255))

    __table_args__ = (
        #Index('cross_section__molecule_alias_id', molecule_alias_id),
    )

class CIACrossSectionData(models.CIACrossSectionData, models.CRUD_Generic, Base):

    id = Column(INTTYPE,primary_key=True)
    header_id = Column('header_id',INTTYPE,nullable=IS_NULLABLE) # ,ForeignKey('cross_section.id')
    __nu__ = Column('__nu__',BLOBTYPE)
    __xsc__ = Column('__xsc__',BLOBTYPE)

    __table_args__ = (
    )

class CIACrossSection(models.CIACrossSection, models.CRUD_Generic, Base):

    id = Column(INTTYPE,primary_key=True)
    collision_complex_alias_id = Column('collision_complex_alias_id',INTTYPE,nullable=IS_NULLABLE) # ,ForeignKey('collision_complex_alias.id')
    source_alias_id = Column('source_alias_id',INTTYPE,nullable=IS_NULLABLE) # ,ForeignKey('source_alias.id')
    local_ref_id = Column('local_ref_id',INTTYPE)
    numin = Column('numin',DOUBLETYPE)
    numax = Column('numax',DOUBLETYPE)
    npnts = Column('npnts',INTTYPE)
    cia_max = Column('cia_max',DOUBLETYPE)
    temperature = Column('temperature',DOUBLETYPE)
    resolution = Column('resolution',DOUBLETYPE)
    resolution_units = Column('resolution_units',VARCHARTYPE(5))
    comment = Column('comment',VARCHARTYPE(255))
    description = Column('description',VARCHARTYPE(255))
    apodization = Column('apodization',VARCHARTYPE(255))
    json = Column('json',VARCHARTYPE(255)) # auxiliary field containing non-schema information
    format = Column('format',VARCHARTYPE(255))
    status = Column('status',VARCHARTYPE(255))

    # additional HITRANonline-compliant parameters
    #filename = Column('filename',VARCHARTYPE(255),unique=IS_UNIQUE) # HITRANonline filename
    filename = Column('filename',VARCHARTYPE(255),unique=False) # HITRANonline filename

    # cia cross-section hash for data lineage...
    hash = Column('hash',VARCHARTYPE(255))

    __table_args__ = (
        #Index('cross_section__collision_complex_id', collision_complex_id),
    )

class SourceAlias(models.SourceAlias, models.CRUD_Generic, Base):

    id = Column(INTTYPE,primary_key=True)
    source_id = Column('source_id',INTTYPE,nullable=True) # ,ForeignKey('source.id')
    alias = Column('alias',VARCHARTYPE(255),unique=IS_UNIQUE,nullable=IS_NULLABLE)
    type = Column('type',VARCHARTYPE(255))

    __table_args__ = (
    )

class Source(models.Source, models.CRUD_Generic, Base):

    id = Column(INTTYPE,primary_key=True)
    short_alias = Column('short_alias',VARCHARTYPE(255),nullable=IS_NULLABLE,unique=IS_UNIQUE)
    type = Column('type',VARCHARTYPE(255))
    authors = Column('authors',TEXTTYPE)
    title = Column('title',TEXTTYPE)
    journal = Column('journal',VARCHARTYPE(255))
    volume = Column('volume',VARCHARTYPE(255))
    page_start = Column('page_start',VARCHARTYPE(255))
    page_end = Column('page_end',VARCHARTYPE(255))
    year = Column('year',INTTYPE)
    institution = Column('institution',VARCHARTYPE(255))
    note = Column('note',TEXTTYPE)
    doi = Column('doi',VARCHARTYPE(255))
    bibcode = Column('bibcode',VARCHARTYPE(255))
    url = Column('url',TEXTTYPE)

    __table_args__ = (
    )

class ParameterMeta(models.ParameterMeta, models.CRUD_Generic, Base):

    id = Column(INTTYPE, primary_key=True)
    name = Column('name',VARCHARTYPE(255),unique=IS_UNIQUE,nullable=IS_NULLABLE)
    type = Column('type',VARCHARTYPE(255))
    description = Column('description',VARCHARTYPE(255))
    format = Column('format',VARCHARTYPE(255))
    units = Column('units',VARCHARTYPE(255))

    __table_args__ = (
    )

linelist_vs_transition = Table('linelist_vs_transition', Base.metadata,
    Column('linelist_id', INTTYPE), #, ForeignKey('linelist.id')
    Column('transition_id', INTTYPE), #, ForeignKey('transition.id')
    #Index('linelist_vs_transition__linelist_id','linelist_id'), # fast search for transitions for given linelist
)

class Linelist(models.Linelist, models.CRUD_Generic, Base):

    id = Column('id',INTTYPE,primary_key=True)
    name = Column('name',VARCHARTYPE(255),unique=IS_UNIQUE,nullable=False)
    description = Column('description',VARCHARTYPE(255))

    __table_args__ = (
    )

class Transition(models.Transition, models.CRUD_Dotpar, Base):

    id = Column(INTTYPE,primary_key=True)
    isotopologue_alias_id = Column('isotopologue_alias_id',INTTYPE,nullable=IS_NULLABLE) #,ForeignKey('isotopologue_alias.id')
    molec_id = Column('molec_id',INTTYPE)
    local_iso_id = Column('local_iso_id',INTTYPE)
    nu = Column('nu',DOUBLETYPE)
    sw = Column('sw',DOUBLETYPE)
    a = Column('a',DOUBLETYPE)
    gamma_air = Column('gamma_air',DOUBLETYPE)
    gamma_self = Column('gamma_self',DOUBLETYPE)
    elower = Column('elower',DOUBLETYPE)
    n_air = Column('n_air',DOUBLETYPE)
    delta_air = Column('delta_air',DOUBLETYPE)
    global_upper_quanta = Column('global_upper_quanta',VARCHARTYPE(15))
    global_lower_quanta = Column('global_lower_quanta',VARCHARTYPE(15))
    local_upper_quanta = Column('local_upper_quanta',VARCHARTYPE(15))
    local_lower_quanta = Column('local_lower_quanta',VARCHARTYPE(15))
    ierr = Column('ierr',VARCHARTYPE(6))
    iref = Column('iref',VARCHARTYPE(12))
    line_mixing_flag = Column('line_mixing_flag',VARCHARTYPE(1))
    gp = Column('gp',INTTYPE)
    gpp = Column('gpp',INTTYPE)
    
    # Simplest solution possible: all "non-standard" parameters are stored 
    # in the main Transition table as a keys of a picklable dictionary.
    extra = deferred(Column('extra',PickleType,default={}))

    __table_args__ = (
        #Index('transition__isotopologue_alias_id', isotopologue_alias_id),
    )

class IsotopologueAlias(models.IsotopologueAlias, models.CRUD_Generic, Base):

    id = Column(INTTYPE, primary_key=True)
    isotopologue_id = Column('isotopologue_id',INTTYPE) # , ForeignKey('molecule.id')
    alias = Column('alias',VARCHARTYPE(255),unique=IS_UNIQUE,nullable=IS_NULLABLE)
    type = Column('type',VARCHARTYPE(255))

    __table_args__ = (
    )

class Isotopologue(models.Isotopologue, models.CRUD_Generic, Base):
    
    id = Column(INTTYPE,primary_key=True)
    molecule_alias_id = Column('molecule_alias_id',INTTYPE,nullable=IS_NULLABLE) #,ForeignKey('molecule_alias.id')
    isoid = Column('isoid',INTTYPE)
    inchi = Column('inchi',VARCHARTYPE(255), unique=IS_UNIQUE)
    inchikey = Column('inchikey',VARCHARTYPE(255), unique=IS_UNIQUE)
    iso_name = Column('iso_name',VARCHARTYPE(255), unique=IS_UNIQUE)
    iso_name_html = Column('iso_name_html',VARCHARTYPE(255))
    abundance = Column('abundance',DOUBLETYPE, nullable=True)
    mass = Column('mass',DOUBLETYPE)
    afgl_code = Column('afgl_code',VARCHARTYPE(255))

    __table_args__ = (
        #Index('isotopologue__molecule_alias_id', molecule_alias_id),
    )

molecule_alias_vs_molecule_category = Table('molecule_alias_vs_molecule_category', Base.metadata,
    Column('molecule_alias_id', INTTYPE), #, ForeignKey('molecule_alias.id')
    Column('molecule_category_id', INTTYPE), #, ForeignKey('molecule_category.id')
    #Index('molecule_alias_vs_molecule_category__molecule_alias_id','molecule_alias_id'), # fast search for molecule aliases for given category
)      

class MoleculeCategory(models.MoleculeCategory, models.CRUD_Generic, Base):
    
    id = Column(INTTYPE,primary_key=True)
    category = Column('category',VARCHARTYPE(255),unique=IS_UNIQUE,nullable=IS_NULLABLE)

    __table_args__ = (
    )

class MoleculeAlias(models.MoleculeAlias, models.CRUD_Generic,Base):
    
    id = Column(INTTYPE, primary_key=True)
    molecule_id = Column('molecule_id',INTTYPE,nullable=True) # , ForeignKey('molecule.id')
    alias = Column('alias',VARCHARTYPE(255),unique=IS_UNIQUE,nullable=IS_NULLABLE)
    type = Column('type',VARCHARTYPE(255))

    __table_args__ = (
    )
    
class Molecule(models.Molecule, models.CRUD_Generic, Base):
    
    id = Column(INTTYPE,primary_key=True)
    common_name = Column('common_name',VARCHARTYPE(255))
    ordinary_formula = Column('ordinary_formula',VARCHARTYPE(255))
    ordinary_formula_html = Column('ordinary_formula_html',VARCHARTYPE(255))
    stoichiometric_formula = Column('stoichiometric_formula',VARCHARTYPE(255))
    inchi = Column('inchi',VARCHARTYPE(255))
    inchikey = Column('inchikey',VARCHARTYPE(255),unique=IS_UNIQUE)
    csid = Column('csid',INTTYPE)

    __table_args__ = (
    )

class CollisionComplexAlias(models.CollisionComplexAlias, models.CRUD_Generic,Base):
    
    id = Column(INTTYPE, primary_key=True)
    collision_complex_id = Column('collision_complex_id',INTTYPE,nullable=True) # , ForeignKey('collision_complex.id')
    alias = Column('alias',VARCHARTYPE(255),unique=IS_UNIQUE,nullable=IS_NULLABLE)
    type = Column('type',VARCHARTYPE(255))

    __table_args__ = (
    )

class CollisionComplex(models.CollisionComplex, models.CRUD_Generic, Base):
    
    id = Column(INTTYPE,primary_key=True)
    chemical_symbol = Column('chemical_symbol',VARCHARTYPE(255))

    __table_args__ = (
    )
