import pandas as pd
import numpy as np
from load_onto import load_onto, TEST_ONTO

def to_pandas(df, onto_class, patientIDcolname="LINKNUMBER", onto=load_onto(TEST_ONTO)):
    """
    Arguments: 
    df = full dataframe (containing all data)
    onto_class = can be regimen or tumour subclass that you would like to return individuals of
    patientIDcolname = column name of the PatientID (NHS number, Link number, etc.)
    onto = full ontology

    Takes all instances of the ontology regimen class and returns the pandas df.
    Currently only supports regimen, tumour and patient subclasses.
    """
    patientIDs = []
    for instance in onto_class.instances():
        if onto_class in onto.Regimen.subclasses():
            try:
                patientIDs.append(instance.treats[0].belongs_to_patient[0].PatientID[0])
            except:
                print("Error loading class")
                return
        elif onto_class in onto.Tumour.subclasses():
            try:
                patientIDs.append(instance.belongs_to_patient[0].PatientID[0])
            except:
                print("Error loading class")
                return
        elif onto_class in onto.Patient.subclasses():
            try:
                patientIDs.append(instance.PatientID[0])
            except:
                print("Error loading class")
                return
        else:
            print("Class is not supported. Currently supported subclasses are of type Regimen, Tumour, and Patient.")
            return

    # print(patientIDs)
    # returns the dataframe where patientID is included
    return df[df[patientIDcolname].isin(patientIDs)]



# TODO: Add numpy support