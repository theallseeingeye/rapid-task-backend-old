INSTRUCTIONS TO DEPLOY
======================

Items to put into gitignore file
--------------------------------
secrets.json - If you are handling a local secrets key file- ensure this is on gitignore (it should already be).

BACK-END DEPLOYMENT
===================

Before doing any deployment, please run your tests ```python manage.py test``` and check 
deployment security ```python manage.py check --deploy```

### To Re-Deploy to Existing

Simply in the environment type: `eb deploy`

### New Deployment Steps

## Gotchas to watch for:
* Make sure we do NOT install awebcli into the local environment, but globally.
* Make sure you are deactivated and not in the environment when applying eb commands.
* Make sure you make commits to any changes for `eb deploy` to register changes.


* Now we need to use the EB Command Line Interface  

Requirements: awsebcli and a `.ebextension` folder with appropriate settings to deploy.

awsebcli should be installed globally, NOT in the virtual environment. Verify by ```eb --version``` if not, 
```pip install awsebcli```. 
   
   
* FIRST TIME -Setting up the Elastic Beanstalk Environment 
    Use the command ```eb init``` (Make sure you are deactivated from the environment)   
    Then follow the steps:
    * Select a default region: `3`  
    * Enter your aws IAM user credentials - If you do not have one- see Jay 
    * Select: Create a new application
    * enter application name (`rapid_task_backend`)
    * It will ask if you are using python, say `y`
    * Select the correct python version (this case is 3.6)
    * will ask about codeCommit- just skip for now `n`
    * Agree to set up the SSH- `y`
    * Create a keypair name- Used the default name `aws-eb`
    * (error) Ran into the error: ERROR: CommandError - SSH is not installed. You must install SSH before continuing.
        * To resolve:  
            * For Windows, install PuTTY from https://www.ssh.com/ssh/putty/download 
            (for more information: https://www.ssh.com/ssh/putty/windows/puttygen)
            * Follow Through PuTTY installation
            * Follow AWS steps: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html
                * Note: You do not need to worry about the window after you click `open` to start the PuTTY Session. 
                It will throw a connection timed out error. It will have created your key, and when you go through
                the process of `eb init` and when the `ssh` option shows, when you select `yes` and it will show the named
                keypair you have created. Select that key and it should work.
            * The steps above should show you how to create a key. Go through the `eb init` steps and say yes to ssh
                and the keypair you have created should show. You now select it.
    * Now you have built an virtual environment instance for AWS
    * Next you need to create a webserver in the environment
    * Type `eb create`, and give a name for each.
    * All done! You have created it!
    * run `eb open` to make sure django is working.
    * If you need to make changes or update the django- type `eb deploy` to apply them.
    
* Deploying to EXISTING Elastic Beanstalk Environments
    * Make sure you are deactivated from the virtual environment.
    * Use the command `eb init`
    * Follow the steps- Select the region 3- or the Oregon location
    * Select the Environment you wish to deploy to.
    * Then it is time to deploy- type `eb deploy` to deploy the changes. Make sure you are on the right environment.
    
* There are multiple environments to choose from from testing to staging and production.  
    1. `rapid-task-backend-env-test` This is where you test the newly changed code to ensure that everything is working.
        This environment uses a simple generic AWS server- Not our official database.  
    2. `rapid-task-backend-env-staging` This is where you have production ready settings and want to make sure its ready
        before deploying to production. This is where we practice test merging a copied backup of production database  
    3. `rapid-task-backend-env-production` ONLY for code that passed staging can be applied here. USES PRODUCTION DATABASE.  
   
## Deployment Common Errors:
* If you `eb deploy` and receive a git submodules error that it may be broken. In your `.elasticbeanstalk/config.yml`
    folder you need to change the settings `include_git_submodules:`  to `false`. AWS automatically sets the setting to 
    true  
* If you receive _Envrion doesn't exist error: You need to log into the console interface of the AWS Elastic Beanstalk 
    environment you wish to deploy to. Go to `Configuriation/SoftwareConfiguration` and under `Evironment Properties`
    ensure that the property names are included for the missing environment variables and are spelled correctly. When you
    set your os.environ['keyvalue], ensure you have `import os` and square brackets, not round brackets.
    
 
Test staging before deployment
------------------------------
Before full production, lets deploy the site to staging and test for vulnerabilities.
    * Use this https://www.ponycheckup.com which probes the site from the outside and reports back.
    * Run Mozilla's security scan https://observatory.mozilla.org/ This is non-django specific and seems underdeveloped

Security Notices
----------------
* Make sure DEBUG = FALSE in the settings before deployment
* Make sure the SECRET_KEY is hidden
* Make sure all the API keys are hidden
* Make sure we are deploying on HTTPS, to block credentials sniffers between the site and end users.
