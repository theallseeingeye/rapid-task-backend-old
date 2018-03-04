ARCHITECTURE DESIGN AND GUIDELINES
===================================

This is a guideline that has design principles and description of the build. This provides understanding how things
evolved as the project grows and ages.

RULES
=====

Styling
-------

####Backend Styling
* This project must adhere and follow the **PEP 8** style guide.
        For more info see http://legacy.python.org/dev/peps/pep-0008/  
* Every time we add code, we must make sure our test coverage is improving, not decreasing.  

####Frontend Styling
* We will be using Styled-Components with react to implement css in the JavaScript. This decision will help keep the 
data contained by each React Components. The css names will have unique id's, which avoids naming conflicts. The Theme
Provider is implemented for global styles. Injected a normalized css
styling to the whole app. Three levels of styling: ```Injected Global > global-styles/DefaultTheme.js > local component
styling```. The Styled-Components can become powerful by using JavaScript functions with css.  
    * Only main concerns were for potential bugs and performance. Have found that we can fall back to regular style sheets
     if we are stuck with certain css implementation. When we do, we will have to watch our css names as it gets 
     compiled to one style sheet by webpack causing css name conflicts. It is hard to find benchmark results for the first paint
     performance of Styled-Components. With some on the web were able to set-up their own benchmark test and found 
     marginal ms differences comparing vanilla css and styled-components. If all fails, it won't be
     difficult to fall back to css style sheets, as most of it is already written in css and can copy/paste with small
     edits.
* Use Google's Styling guide: https://google.github.io/styleguide/htmlcssguide.html


Database
--------
* Do not record logs into the database. This slows it down. There are third party resources that can help handle this.
* No Ephemeral data. This means any data that needs constant rewrites, which is not ideal for relational databases.
    Move the data to applications such as memcached or redis.
* Every incoming data must be validated!
* Any external/public sharing of data must be identified with an UUID. Hide the primary keys. Important for scalability of the database. Keep the original 
    sequential primary keys that the database creates then add a new table with UUID's.

Security
--------
* Never use eval(), exec() and execfile() built-ins, using these will leave our system open to attack
* Avoid the use of Meta.exclude when using the ModelForms. This leaves the mass assignment vulnerable. Only list the
    fields of the model we want to use.
* Do not use ModelForms.Meta.fields="__all__"
* Never store credit card data. Use a third party to handle the data. MUST follow PCI Security Standards Council
    link: https://www.kencochrane.net/blog/2012/01/developers-guide-to-pci-compliant-web-applications/
* Complex passwords does not equate to better security. Length vs complexity: https://xkcd.com/936/
* Never display database sequential primary keys. It informs rivals or hackers of our volume. Use models.UUIDField for
    public lookups.
* Never publicly display the database id's. This can lead to information leak of our company growth.
    We want to add UUID's to our databases and only use those when the data is shared
    publicly. 
    https://blog.lightrail.com/prevent-business-intelligence-leaks-by-using-uuids-instead-of-database-ids-on-urls-and-in-apis-17f15669fd2e
* JSON JWT Tokens will be used for both server and client side servers.  

Features to Consider for the Future
-----------------------------------
We want to keep this project scalable. Keep these features in mind as we add sections/modules to the project and ensure
that they can accommodate these in the future.  
    * We may want to consider implementing two-factor authentication option for users who wants more security.


Installed Packages Explanation
------------------------------
The installed packages must be written here with explanation for it's use. You must state the license use.
        *Before adding any packages, they must have a license and is approved by our Management*  
        
**BACKEND**

* Django REST Framework 3.7.1   
    This framework sets up the Django project nicely for building web APIs. Required for React.js and third parties.
    Documentation: http://www.django-rest-framework.org/
    * License: BSD 2 or "Simplified BSD License"   
* markdown-2.6.9  
    Markdown support for the browsable REST API.  
    * License: BSD 
* django-filter-1.1.0  
    Filtering support for REST API. Allows users to declaratively add dynamic QuerySet Filtering from URL patterns.  
    * License: BSD
* psycopg2 2.7.3.2
    This is a PostgreSQL adapter for the python. Connects the database, postgres.
    * License: GPL
* django-rest-framework-jwt 1.11.0   
    This attaches the JWT tokens throught the REST Framework. This includes the pyJWT. http://getblimp.github.io/django-rest-framework-jwt/
    * License: MIT
* awsebcli
    NOT TO BE IN THE PACKAGE- ENSURE! OR DEPLOYMENT WILL CAUSE ISSUES. Install into the global environment
    This is Amazon's command line interface. Required to host the backend.  
* django-admin-honeypot  
    This is to hide the default admin link for the django. This will log anyone who tries to access  /admin/ site  
    * License: MIT  

Working on adding these:
* djoser  
    This is a package that handles the basic registration and user authentication info in REST format.
    https://github.com/sunscrapers/djoser  
    * License: MIT

* django-cors-headers 2.1.0
    This allows the CORS headers to the frontend. Easy implementation of cross-domain requests for REST.
    * License: Free and open