from owlready2 import *
import pandas as pd

class Instances():
    patients = []
    tumours = []
    drugs = []
    regimens = []

i = Instances()

def map_data(onto, data_to_map):
    ## --------------------- HELPER FUNCTIONS ---------------------
    def fec(instances, regimen):
        '''
        For handling the case where "FEC" is included in the regimen
        '''
        instances.drugs.append(onto.Drug(has_drug_reference=[onto.Fluorouracil5REF], part_of_regimen=[regimen]))
        instances.drugs.append(onto.Drug(has_drug_reference=[onto.EpirubicinREF], part_of_regimen=[regimen]))
        instances.drugs.append(onto.Drug(has_drug_reference=[onto.CyclophosphamideREF], part_of_regimen=[regimen]))

    def create_drug_instances(string, regimen):
        '''
        Creating drug instances beased on the string (string describes the drugs)
        '''
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
    
    def onto_behaviour_code(onto, code):
        '''
        Converts an integer (behaviour code) into the BehaviourCodeREF instance in ontology
        '''
        if code == 0:
            return onto.BehaviourCode0REF
        if code == 1:
            return onto.BehaviourCode1REF
        if code == 2:
            return onto.BehaviourCode2REF
        if code == 3:
            return onto.BehaviourCode3REF
        if code == 5:
            return onto.BehaviourCode5REF
        if code == 6:
            return onto.BehaviourCode6REF
        if code == 9:
            return onto.BehaviourCode9REF
        return 0 # error case
    
    ## --------------------- MAIN FUNCTION ---------------------
    def create_instances(data, 
                         patient_id_col='LINKNUMBER', 
                         tumour_id_col='MERGED_TUMOUR_ID',
                         tumour_icd10_col = 'SITE_ICD10_O2',
                         tumour_behaviour_col='BEHAVIOUR_ICD10_O2',
                         regimen_id_col = 'MERGED_REGIMEN_ID'):
        '''
        Mapping instances of data to individuals in the ontology.
        Optional parameters are PatientID, TumourID, Tumour behaviour, RegimenID columns
        '''

        for index, row in data.iterrows():
            # Create a new patient instance, but checks if patient has been created before
            patient_search = onto.search(PatientID = str(row[patient_id_col])+"*")
            if not patient_search:
                today = datetime.date.today()
                yearBorn = datetime.date(today.year-row['AGE'],1,1).year
                vital = row['NEWVITALSTATUS']
                thisPatient = onto.Patient(PatientID = [row[patient_id_col]], ## equivalent of NHS number 
                                            DateOfBirth = [yearBorn],
                                            VitalStatus = [vital],
                                            PrimaryDiagnosis = [row['PRIMARY_DIAGNOSIS']], ## patient primary tumour icd10
                                            Sex = [row['SEX']]
                                            )
            else:
                thisPatient = patient_search[0]
            i.patients.append(thisPatient)

            # Create a new tumour instance
            thisTumour = onto.Tumour(TumourID = [row[tumour_id_col]],
                                        DiagnosisDate = [row['DIAGNOSISDATEBEST']],
                                        ICD10_Code = [row[tumour_icd10_col]], ## tumour icd10
                                        has_behaviour_code = [onto_behaviour_code(onto, row[tumour_behaviour_col])], # behaviour code
                                        belongs_to_patient = [thisPatient]
                                        )
            i.tumours.append(thisTumour)

            # Create a new regimen instance
            thisRegimen = onto.Regimen(RegimenID = [row[regimen_id_col]], 
                                        treats = [thisTumour]
                                        )
            i.regimens.append(thisRegimen)

            # Create new drug instances in a for loop using names, then all drugs part of this regimen
            create_drug_instances(row['MAPPED_REGIMEN'], thisRegimen)
    
    # ----------- CREATING INSTANCES FUNCTION CALLED -----------------
    create_instances(data_to_map)