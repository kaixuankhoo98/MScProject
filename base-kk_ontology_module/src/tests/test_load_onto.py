from kk_ontology_module import load_onto

def test_load_onto():
    onto = load_onto('src/kk_ontology_module/extras/CancerOntology.owl')
    assert onto.Thing == onto.Thing