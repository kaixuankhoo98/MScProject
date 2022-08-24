from kk_ontology_module import CancerOntology, test_data
import pandas as pd

def test_gliocova():
    o = CancerOntology()
    df = test_data.rename(columns={'LINKNUMBER': 'PSEUDO_PATIENTID', 'MERGED_TUMOUR_ID': 'PSEUDO_TUMOURID', 
        'NEWVITALSTATUS':'VITALSTATUS', 'MERGED_REGIMEN_ID':'REGIMEN_NUMBER'})
    o.set_gliocova_column_names()
    o.define_data(df)
    o.reason()
    assert o.onto.patient1.PatientID == [810037882]