from owlready2 import *
from kk_ontology_module.load_data import load_data, TEST_DATA
from kk_ontology_module.load_onto import load_onto, TEST_ONTO
from kk_ontology_module.map_data import map_data

test_onto = load_onto() # default ontology
test_data = load_data() # default data

## Defining class cancer ontology
class CancerOntology:
    def __init__(self, onto=test_onto):
        self.onto = onto
        self.default_world = World()
        self.world = default_world

        # setting the default column names: these should be able to be edited
        self.patient_id_col = 'LINKNUMBER'
        self.tumour_id_col = 'MERGED_TUMOUR_ID'
        self.tumour_icd10_col = 'SITE_ICD10_O2'
        self.tumour_behaviour_col = 'BEHAVIOUR_ICD10_O2'
        self.regimen_id_col = 'MERGED_REGIMEN_ID'
        self.patient_age = 'AGE'
        self.vital_status = 'NEWVITALSTATUS'
        self.patient_primary_diagnosis = 'PRIMARY_DIAGNOSIS'
        self.sex_col = 'SEX'
        self.diagnosis_date_col = 'DIAGNOSISDATEBEST'
        self.regimen_string_col = 'MAPPED_REGIMEN'

    def reason(self):
        """
        Reasons with HermiT. From the Owlready2 Package.
        """
        with self.onto: sync_reasoner(self.world)

    def reload(self):
        """
        Function to reload the ontology
        TODO: Unfortunately this doesn't work...
        """
        print("Previous ontology deleted.")
        self.world = default_world
        print("New ontology loaded.")
    
    def define_data(self, data):
        
        self.data = data
        map_data(self.onto, data,
                 patient_id_col = self.patient_id_col, 
                 tumour_id_col = self.tumour_id_col,
                 tumour_icd10_col = self.tumour_icd10_col,
                 tumour_behaviour_col = self.tumour_behaviour_col,
                 regimen_id_col = self.regimen_id_col,
                 patient_age = self.patient_age,
                 vital_status = self.vital_status,
                 patient_primary_diagnosis = self.patient_primary_diagnosis,
                 sex_col = self.sex_col,
                 diagnosis_date_col = self.diagnosis_date_col,
                 regimen_string_col = self.regimen_string_col)
    
    def set_gliocova_column_names(self):
        self.patient_id_col = 'PSEUDO_PATIENTID'
        self.tumour_id_col = 'PSEUDO_TUMOURID'
        self.regimen_id_col = 'REGIMEN_NUMBER'
        self.vital_status = 'VITALSTATUS'
        self.diagnosis_date_col = 'DIAGNOSISYEAR'
        self.regimen_string_col = 'BENCHMARK_GROUP'
        return


# def test1():
#     o1 = CancerOntology()
#     o1.onto.Drug("test_drug", Dose = [100], has_drug_reference = [o1.onto.CyclophosphamideREF])
#     print(o1.onto.test_drug)
#     o1.reload(test_onto)
#     print(o1.onto.test_drug)

# def test2():
#     o2 = CancerOntology()
#     o2.define_data(test_data)
#     # print(o2.onto.Regimen.instances())

# def test3():
#     o3 = CancerOntology()
#     o3.define_data(test_data)
#     o3.reason()
#     print(o3.onto.DocetaxelDrug.instances())

# def test4():
#     # data = load_data("extras/m2dummyB_med.csv")
#     o4 = CancerOntology()
#     o4.define_data(test_data)
#     o4.reason()
#     print(to_pandas(test_data, o4.onto.TaxaneContainingRegimen))
#     # print(to_pandas(test_data, o4.onto.TaxaneContainingRegimen, IDcolname='MERGED_REGIMEN_ID', returns='regimen'))
#     # print(to_pandas(test_data, o4.onto.TaxaneContainingRegimen, IDcolname='MERGED_TUMOUR_ID', returns='tumour'))

# def test5():
#     o5 = CancerOntology()
#     o5.define_data(test_data)
#     o5.reason()
#     print(has_morphology_code(test_data))

# def test6():
#     o6 = CancerOntology()
#     o6data = load_data('extras/m2dummy_med.csv')
#     o6.define_data(o6data)
#     # o6.define_data
#     o6.reason()
#     # print(o6.onto.search(subclass_of = o6.onto.Tumour))
#     print(to_pandas(o6data, o6.onto.PlatinumBasedRegimen, IDcolname='MERGED_REGIMEN_ID', returns='regimen'))

# def test7():
#     o7 = CancerOntology()
#     o7.define_data(test_data)
#     o7.reason()
#     # print(o6.onto.search(subclass_of = o6.onto.Tumour))
#     print(to_pandas(test_data, o7.onto.Tumour_C43_C44))

# test1()

# o1.reason()
# print(o1.onto.E1.has_drug_reference)
# print(o1.onto.EpirubicinDrug.instances())