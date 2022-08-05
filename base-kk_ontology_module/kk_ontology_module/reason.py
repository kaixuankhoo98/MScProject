from owlready2 import *
from load_data import load_data, TEST_DATA
from load_onto import load_onto, TEST_ONTO
from map_data import map_data
import gc

test_onto = load_onto(TEST_ONTO) #default ontology
test_data = load_data(TEST_DATA)

## Defining class cancer ontology
class CancerOntology:
    def __init__(self, onto=test_onto):
        self.onto = onto
    
    def reason(self):
        """
        Reasons with pellet.
        """
        with self.onto: sync_reasoner_pellet()

    def reload(self, onto):
        """
        Function to reload the ontology
        TODO: This doesn't work...
        """
        del self.onto
        print("Previous ontology deleted.")
        gc.collect()
        self.onto = onto
        print("New ontology loaded.")
    
    def add_data(self, data):
        self.data = data
        map_data(self.onto, data)

def test1():
    o1 = CancerOntology()
    o1.onto.Drug("test_drug", Dose = [100], has_drug_reference = [o1.onto.CyclophosphamideREF])
    print(o1.onto.test_drug)
    o1.reload(test_onto)
    print(o1.onto.test_drug)

def test2():
    o2 = CancerOntology()
    o2.add_data(test_data)
    # print(o2.onto.Regimen.instances())

test2()

# o1.reason()
# print(o1.onto.E1.has_drug_reference)
# print(o1.onto.EpirubicinDrug.instances())