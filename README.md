## Query my-ip in Dynamo from AWS CloudShell

CloudShell will have credentials for Dynamo already, no need to set up long lived access token on local machine.

`python` and `pip` should already be installed.

### Installing packages

Ideally should use `pipenv` but it's quite a bit of hassle getting the correct Python version. Assuming CloudShell is not being used to manage other Python projects, just run the following:

`pip install boto3`

### Running

`python run.py`