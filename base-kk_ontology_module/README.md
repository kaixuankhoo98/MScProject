# kk_ontology_module
The link to the python package on PyPI is here:
https://pypi.org/project/kk-ontology-module/

## Installation 
To install it on your laptop, ensure you have pip installed:
`python3 -m pip install --upgrade pip setuptools wheel` for Unix/MacOS
`py -m pip install --upgrade pip setuptools wheel` for Windows 
For a full tutorial on pip, please see the [documentation](https://packaging.python.org/en/latest/tutorials/installing-packages/)

After this, although not entirely necessary, I suggest running:
`pip install cython`
to avoid any dependency issues with owlready2.

Finally, you can run:
`pip install kk_ontology_module`

## Use and functionality
...
An example script is shown below:
`from kk_ontology_module import *` to import the package
`o = CancerOntology()` creating the cancer ontology object
`o.define_data(test_data)` using the in-built test dataset from simulacrum
`o.reason()` runs the reasoner (HermiT, or Pellet) from owlready2
`to_pandas(test_data, o.onto.TaxaneContainingRegimen)` returns the dataframe of only TaxaneContainingRegimens