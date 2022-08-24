from kk_ontology_module import map_data, load_onto, load_data

def test_load_no_col_map():
    onto = load_onto()
    data = load_data()
    data = data.drop(columns=['SITE_ICD10_O2','AGE','SEX','BEHAVIOUR_ICD10_O2'])
    map_data(onto, data)
    assert onto.patient1.PatientID[0] == 810037882