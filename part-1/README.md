# Data-Engineering-101 -> PART 1 DOC
### 1. Description
This repo should be your guide in learning by doing modern data engineering (As I know it)

### 2. Getting started
#### 2.1 Prerequisites
1. Install python (I'm using Python 3.11.6)
2. Create virtual env 
    - > Install : pip install virtualenv
    - > Create dedicated forlder for your virtual env (seperated from this project)
    - > Create new folder : mkdir virtual-env
    - > Create Virtual Env insid virtual-env : python -m venv space-env
    - > Activate Virtual Env from root folder : source virtual-env/space-env/bin/activate
3. Install requirements.txt packages ((run from your virtual env))
    - > pip install -r requirements.txt
4. Save requirements.txt for results reproducibility (run from part-1)
    - > pip freeze > requirements.txt

#### 2.2 Run IT
After setting up your ENV, you only need to execute this command from root folder (you can change part-1 with the part you're at)
- > python part-1/main.py

### 3. Src Walkthrough
#### 3.1 Overview
We have input and output folders represents our source and target systems
We have src folder where we have main.py represents our pipeline entrypoint along with config and util folders
1. config package will have all our configuration files for part 1
2. util package will have all we need to deal with files, schedulers, etc.

#### 3.2 Util package
##### 3.2.1 File Handler
This will help us with this workflow : 3.3
1. list all files in input folder each time our scheduler is triggered
2. check registry text file in config folder for a cross-check
3. the new files only will be transfered to output folder
4. the registry will get updated with the new files names

##### 3.2.2 API Handler
This basically for calling the API and getting data as a pandas dataframe

##### 3.2.3 Config Handler
To simplify and centralize configurations, including folder paths, API names, etc.

##### 3.2.4 Scheduler
This for orchestrating the pipelines and control when they will be triggered (we're using it in the early parts, but normally we should use Airflow for example for advanced use cases)

#### 3.3 Config package
##### 3.3.1 Registry
It contains list of processed files to avoid system overload and keep track of when we processed each file

##### 3.3.2 config.ini
It contains list of all our configurations, we're currently using : 
[API] section that contains : API url (url)
[Paths] section that contains : input and registry file name (raw_dir, registry_file)
Please use the same format in the config.init.template with your own values

#### 3.4 Pipelines package
This is to design how we want our pipelines to act, depending on the layer
##### 3.4.1 raw layer
For this layer, we should get data and store it in raw folder in csv formats.
##### 3.4.2 curated layer
For this layer, we should check new files and combine them in one file, this just a simple use case for part-1, 
more transformations will be introduced as we move forward.


### 4. Test Walkthrough
#### 4.1 Unit Tests
For unit testing, we have used Pytest package and it's very simple.
The test cases are designed to verify the behavior of these classes under various conditions, including successful and failed API requests, and file handling operations such as saving data to CSV files.

We have used Fixture to create an instance of ApiHandler for testing.
And Mock to mock behaviour of functions and objects (return, effects, etc.)

Dependencies:
    - util.exceptions.RequestException: Custom exception class for API request failures
    - util.exceptions.InvalidValueException: Custom exception class for invalid input values
Test Cases:
    - TestApiHandler:
    - TestFileHandler:
### 5. Developement  ways
#### 5.1 gitignore
1. to add files that are already tracked, execute this command first then commit your changes
- > git rm -r --cached <file-or-folder-path> (use -r for folders)

### 6. Clean-Up
#### 6.1 Delete files
Make sure you're in the root directory
> rm ./part-1/data/raw/*.csv
> rm ./part-1/data/curated/*.csv

### 7. TODO
ensure that code is comply to python best practices
arguments are following the pythonic way
