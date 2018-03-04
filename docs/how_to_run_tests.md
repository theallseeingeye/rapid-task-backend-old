How To Run Tests
================

This step is crucial to running before deploying or finalizing changes for uploads to github.

      

Back-End
--------


#### For check of code coverage by tests

##### Requirements:  
 coverage.py https://coverage.readthedocs.io/en/coverage-4.5.1/

Should be already include in the requirements- simply type ```pip install```. If not, then install directly ```pip install coverage```  

For a list of commands:  ```coverage help```  
        
Start and run a test at the command-line in the project root directory:   
   * ```coverage run manage.py test --settings=config.settings.test``` 
     
For test results without admin:  
   * ```coverage html --omit="admin.py"```  
        * Then this will create a directory with html that has the coverage report.
   
To look at the generated html report (after using html) go to website/htmlcov/index.html. it shows the coverage report.