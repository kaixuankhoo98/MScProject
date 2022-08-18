from kk_ontology_module import map_data, load_onto, load_data

def test_map():
    onto = load_onto('src/kk_ontology_module/extras/CancerOntology.owl')
    data = load_data('src/kk_ontology_module/extras/m2dummyB_small.csv')
    map_data(onto, data)
    assert onto.patient1.PatientID[0] == 810037882