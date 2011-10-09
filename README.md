Build a working blog site
-------------------------

Your task, should you choose to accept, is to build a simple blogging site using Python, Django, PostgreSQL, and Apache. You will need to checkin your code to Github, so we can pull down the final result and run it locally. This means the entire codebase and any configuration files should be checked in. The following conditions must be met:

- create a public github repository and checkin your code there  
<span style="color: green">done</span>
- the blog should be written using Django & Python  
<span style="color: green">done</span>
- the database powering your blog should be PostgreSQL  
<span style="color: green">done, heroku shared DB is postgres</span>
- the blog should allow multple users to log in  
<span style="color: green">done, via normal django authentication/admin</span>
- staff users can write blog articles
<span style="color: green">done, any user in 'editors' group can write articles and admin comments (edit/delete)</span>  
- all users can comment on blog articles  
<span style="color: green">done, used Django Comments</span>
- a blog article consists of a three parts: title, body, slug, and date    
<span style="color: green">done, see Entry model in /admin/. Note that the Entry model has not been optimized for presentation in /admin/.  I can address if needed.</span>
- the index page should be a list of all articles  
<span style="color: green">done</span>
- each blog article should have a link to a post page, where the URL is mysite.com/slug/  
<span style="color: green">done</span>
- site should be served via Apache and WSGI  
<span style="color: orange">used heroku</span>
- server configuration, should be included in the github repo  
<span style="color: orange">heroku config included (see requirements.txt)</span>

Extra credit
------------

Completing any of the following, in addition to the tasks above, will not only make your blog cooler, but also impress us:

- run your software on a public webserver  
<span style="color: green">done, w/ heroku</span>
- pagination on the index page  
<span style="color: green">done, w/ django paginator</span>
- AJAX form submission  
<span style="color: red">TODO</span>
- any caching to reduce DB lookups
- support comment threading
- support thumbnails for users  
<span style="color: green">done w/ gravatar</span>
- add a user profile and place for them to edit
- fancy CSS  
<span style="color: green">done w/ twitter bootstrap (not a CSS expert, but... it's functional)</span>

Feel free to email if you find any of this ambiguous.
