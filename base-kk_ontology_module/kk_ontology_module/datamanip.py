import pandas as pd
import numpy as np

def to_pandas(df, onto_class, regimen=True):
    """
    Arguments: 
    df = full dataframe (containing all data)
    onto_class = can be regimen or tumour subclass that you would like to return individuals of
    regimen = set to True if Regimen subclass, set to false if Tumour subclass

    Takes all instances of the ontology regimen class and returns the pandas df.
    """
    patientIDs = []
    for instance in onto_class.instances():
        if regimen:
            patientIDs.append(instance.treats[0].belongs_to_patient[0].PatientID[0])
        else:
            patientIDs.append(instance.belongs_to_patient[0].PatientID[0])

    # print(patientIDs)
    # returns the dataframe where patientID is included
    return df[df['LINKNUMBER'].isin(patientIDs)]



# TODO: Add numpy support