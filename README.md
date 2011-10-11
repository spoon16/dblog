Install/Setup Instructions
--------------------------

https://github.com/spoon16/dblog/blob/master/INSTALL.md

Build a working blog site
-------------------------

Your task, should you choose to accept, is to build a simple blogging site using Python, Django, PostgreSQL, and Apache. You will need to checkin your code to Github, so we can pull down the final result and run it locally. This means the entire codebase and any configuration files should be checked in. The following conditions must be met:

- create a public github repository and checkin your code there  
**done**
- the blog should be written using Django & Python  
**done**
- the database powering your blog should be PostgreSQL  
**done, heroku shared DB is postgres**
- the blog should allow multple users to log in  
**done, via normal django authentication/admin**
- staff users can write blog articles  
**done, any user in 'editors' group can write articles and admin comments (edit/delete)**
- all users can comment on blog articles  
**done, used Django Comments**
- a blog article consists of a three parts: title, body, slug, and date    
**done, see Entry model in /admin/**
- the index page should be a list of all articles  
**done**
- each blog article should have a link to a post page, where the URL is mysite.com/slug/  
**done**
- site should be served via Apache and WSGI  
**used heroku, I can deploy onto EC2 if desired**
- server configuration, should be included in the github repo  
**heroku config included directions to setup a new environment are in INSTALL.md**

Extra credit
------------

Completing any of the following, in addition to the tasks above, will not only make your blog cooler, but also impress us:

- run your software on a public webserver  
**done, w/ heroku**
- pagination on the index page  
**done, w/ django paginator**
- AJAX form submission  
**TODO**
- any caching to reduce DB lookups  
**TODO**
- support comment threading  
**thinking about just using Facebook for this (see fbcomments branch)**
- support thumbnails for users  
**done w/ gravatar**
- add a user profile and place for them to edit  
**authors can use /admin/ and if using Facebook than not applicable for readers*
- fancy CSS  
**done w/ twitter bootstrap (not a CSS expert, but... it's functional)**

Feel free to email if you find any of this ambiguous.
