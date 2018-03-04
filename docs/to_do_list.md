THINGS TO DO
============

* Setup django as REST, using django REST framework

Monitoring
----------
* Find and install some monitoring tools. Check server access and log errors regularly.

Security
--------
* On domain/server options redirect all http links to https services for deployment
* Obtain a SSL certificate- Try www.letsencrypt.org
* Configure web server to use HSTS- Strict Transport Security
* Set the ALLOWED_HOSTS in settings to the right limited host addresses
* Find a third party that can handle credit card data. We are not to store them. Look at stripe, braintree, adyen...
* Install Pyup https://pyup.io/ - Automatic security updates and dependencies.
* Setup Clickjacking prevention: https://docs.djangoproject.com/en/1.11/ref/clickjacking/
* Publish a section where users can report security vulnerabilities to us. Provide reward to users who reports.
* Write an emergency procedure.
    * Security Failure
        * Shut everything down or put it in read-only mode
        * Put up a static HTML page.
        * Back everything up
        * After reading docs.djangoproject.com/en/dev/internals/security/, email security@djangoproject.com about your
            security-related problem, even if it's your fault
        * start looking into the problem
* Setup the admin honey pot. It is already installed, just need to set it up
    * also change the default site.com/admin path to something that is long and difficult to guess
    * change the admin docs to something other than site.com/admin/doc/



