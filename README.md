# MScProject
Repository containing code for my MSc Project: Using Ontology-Based Tooling to Improve Cancer Data Analysis
Here you will find jupyter notebook files and Protege files amongst other files.
This project uses the Simulacrum dataset (simulated cancer data in the UK) as the primary source of data: https://simulacrum.healthdatainsight.org.uk/using-the-simulacrum/requesting-data/

## Breast Cancer Analysis (Jupyter Notebook)
A first step in understanding the cancer dataset is to understand the regimens for treatment of a cancer. To start off, I have chosen to use the simulacrum dataset and look only at patients with breast cancer (IDC10 codes between C500-C509), and show the most common regimens. This will help to design the ontology for breast cancer treatments.

## TestOwlPython (Jupyter Notebook)
This is the playground for me to mess around with OwlReady2. Here you will find the functions I created to create instances. Currently, with the version available here, I am able to load a csv file into pandas, then create individual patients, tumours, regimens, and drug instances and connect them. The next step is to refine the functions, especially the drug-instance creating function. 

## Next steps:
- Create a GUI, either in python or as a plugin for Protege, for cancer researchers to be able to query their ABox
- Map the ontology to existing ontologies such as SNOMED-CT
