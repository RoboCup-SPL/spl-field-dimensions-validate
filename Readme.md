# RoboCup SPL Field Dimensions Validator

This repository defines an exchange format for the dimensions of a soccer field in the [RoboCup SPL](https://spl.robocup.org/) and contains a program to validate files in that format.

Give `field-validate.py` a list of files on the commandline and it will check all files whether they follow the schema defined by the SPL rules.

This program needs Python 3 to run. No other libraries or dependencies are required.

# Schema

This program uses a [JSON Schema](https://json-schema.org/understanding-json-schema/) to auto-generate validation code. The schema can be found in `generate-validator`. To auto-generate the validation code Python 3 and the Python-dependencies from `requirements.txt` are needed.

# Standard field

In `tests` you find JSON files describing a field constructed to the standard dimensions of the SPL rules.
