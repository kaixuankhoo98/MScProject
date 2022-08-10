import pandas as pd
import numpy as np
from owlready2 import *

def to_pandas(df, regimen):
    """
    Arguments: 
    df = full dataframe (containing all data)
    regimen = the regimen subclass that you would like to return individuals of

    Takes all instances of the ontology regimen class and returns the pandas df.
    TODO: Make this function suitable for regimens
    """
    patientIDs = []
    for instance in regimen.instances():
        patientIDs.append(instance.treats[0].belongs_to_patient[0].PatientID[0])

    # print(patientIDs)
    # returns the dataframe where patientID is included
    return df[df['LINKNUMBER'].isin(patientIDs)]



# TODO: Add numpy support