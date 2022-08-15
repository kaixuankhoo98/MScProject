from owlready2 import *
import pandas as pd

class Instances():
    patients = []
    tumours = []
    drugs = []
    regimens = []

i = Instances()

def map_data(onto, data_to_map):
    
    def fec(instances, regimen):
        instances.drugs.append(onto.Drug(has_drug_reference=[onto.Fluorouracil5REF], part_of_regimen=[regimen]))
        instances.drugs.append(onto.Drug(has_drug_reference=[onto.EpirubicinREF], part_of_regimen=[regimen]))
        instances.drugs.append(onto.Drug(has_drug_reference=[onto.CyclophosphamideREF], part_of_regimen=[regimen]))

    def create_drug_instances(string, regimen):
        if "capecitabine" in string.lower():
            i.drugs.append(onto.Drug(has_drug_reference=[onto.CapecitabineREF], part_of_regimen=[regimen]))
        if "carboplatin" in string.lower():
            i.drugs.append(onto.Drug(has_drug_reference=[onto.CarboplatinREF], part_of_regimen=[regimen]))
        if "cyclophosphamide" in string.lower():
            i.drugs.append(onto.Drug(has_drug_reference=[onto.CyclophosphamideREF], part_of_regimen=[regimen]))
        if "docetaxel" in string.lower():
            i.drugs.append(onto.Drug(has_drug_reference=[onto.DocetaxelREF], part_of_regimen=[regimen]))
        if "epirubicin" in string.lower():
            i.drugs.append(onto.Drug(has_drug_reference=[onto.EpirubicinREF], part_of_regimen=[regimen]))
        if "fluorouracil" in string.lower():
            i.drugs.append(onto.Drug(has_drug_reference=[onto.Fluorouracil5REF], part_of_regimen=[regimen]))
        if "paclitaxel" in string.lower():
            i.drugs.append(onto.Drug(has_drug_reference=[onto.PaclitaxelREF], part_of_regimen=[regimen]))
        if "pertuzumab" in string.lower():
            i.drugs.append(onto.Drug(has_drug_reference=[onto.PertuzumabREF], part_of_regimen=[regimen]))
        if "trastuzumab" in string.lower():
            i.drugs.append(onto.Drug(has_drug_reference=[onto.TrastuzumabREF], part_of_regimen=[regimen]))
        if "FEC" in string:
            fec(i, regimen)
        
    def create_instances(data):
        for index, row in data.iterrows():
            # print(row['MERGED_REGIMEN_ID'], row['MERGED_TUMOUR_ID'], row['MERGED_PATIENT_ID_x'], row['PRIMARY_DIAGNOSIS'], row['MAPPED_REGIMEN'])

            # Create a new patient instance
                ## TODO: We might want to check if patient already in ontology
            today = datetime.date.today()
            yearBorn = datetime.date(today.year-row['AGE'],1,1).year
            vital = row['NEWVITALSTATUS']
            thisPatient = onto.Patient(PatientID = [row['LINKNUMBER']], ## equivalent of NHS number 
                                        DateOfBirth = [yearBorn],
                                        VitalStatus = [vital],
                                        PrimaryDiagnosis = [row['PRIMARY_DIAGNOSIS']], ## patient primary tumour icd10
                                        Sex = [row['SEX']]
                                        )
            i.patients.append(thisPatient)

            # Create a new tumour instance
            thisTumour = onto.Tumour(TumourID = [row['MERGED_TUMOUR_ID']],
                                        DiagnosisDate = [row['DIAGNOSISDATEBEST']],
                                        ICD10_Code = [row['SITE_ICD10_O2']], ## tumour icd10
                                        belongs_to_patient = [thisPatient]
                                        )
            i.tumours.append(thisTumour)

            # Create a new regimen instance
            thisRegimen = onto.Regimen(RegimenID = [row['MERGED_REGIMEN_ID']], 
                                        treats = [thisTumour]
                                        )
            i.regimens.append(thisRegimen)

            # Create new drug instances in a for loop using names, then all drugs part of this regimen
            create_drug_instances(row['MAPPED_REGIMEN'], thisRegimen)
    
    create_instances(data_to_map)