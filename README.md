# Waddup
HOW TO ACTIVATE VIRTUAL ENVIRONMENT:
After downloading Waddup_App folder, you should see the approximately the following directory structure:

├──Waddup_App
    └── Waddup
        └── blog
        └── db.sqlite3
        └── manage.py
        └── templates
            └── base.html
            └── event_detail.html
            └── index.html
        └── Waddup
    └── waddup_env
        └── bin
        └── include
        └── lib
        └──pyenv.cfg

NOTE: Certain directories were not expanding for the sake of shortening this file, ex. blog within Waddup and the "Waddup" folder within the Waddup folder

To activate the virtual environment, open Terminal/cmd and use the cd command to navigate into the Waddup_App directory, I'm a Mac user so in my case I ran the command "cd Desktop/Waddup_App" as the folder was located on my Desktop, but it may be different for you depending on where you placed it.

Once inside the Waddup_App directory, run the following command:
source waddup_env/bin/activate

This command should add a (waddup_env) to the lefthand side of your command prompt, for example:

Intially, my command prompt said:

    spencerbradkin@Spencers-MBP Waddup %

But after running the "source waddup_env/bin/activate" command, it changes to:

    (waddup_env) spencerbradkin@Spencers-MBP Waddup %

This means I have successfully activated the Waddup environment.


HOW TO RUN SERVER LOCALLY:

Once you have activate the Waddup virtual environment, you can now run the actual server. Django has a built in python file titled manage.py that is created when you create the actual Django application. So, while still inside of the Waddup_App directory, use the command "cd Waddup" to enter the Waddup directory.  Inside of this directory lies the manage.py file as shown in the directory tree structure at the top of this file.  To run the server locally, simply use the command:

python3 manage.py runserver

The output should be something similar to :

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 16, 2023 - 16:38:01
Django version 4.1.7, using settings 'Waddup.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Go into your local browser and type the address given, in my case (and I think your's too) it is http://127.0.0.1:8000

You should now see the home page. I am not sure if events that I create on my system are also displayed on your's, but if there is nothing then proceed to the next step to add events which is to login as an admin.


HOW TO RUN AS ADMIN:
Fortunately for us, Django has a built-in admin functionality.  I initially created a user when making the application, but I have added a separate admin User that we can all use.  I am still not sure if this data changes across all of our computers if one person makes a change, but I have a feeling that it does not.

In any case, to login as admin, simply add "/admin" at the end of the web address.  For example, the URL determined in the previous step is:
http://127.0.0.1:8000

So, the admin login page would simply be:
http://127.0.0.1:8000/admin

Which will bring you to a site with a couple of sections, one being titled "Authentication and Authorization" and the other titled "Blog".  The first section has two subsections, one called "Groups" and one called "Users".  Users is where admin login information can be created and added (I believe it can actually be used to store all user login information, but you can also add a user, enter login information of your choice, and assign yourself admin/staff status if you would like).

I have added the following login information to the system already which should work for everyone:

Username:Waddup
Password:CIS454Mohan

To add an event, simply click the add link in the event subsection, fill in event details, and then the event should be displayed on the home page once you return.  It should also be visible with selected metadata regarding the event being displayed (we can choose this metadata).

NOTES ABOUT THE ACTUAL FILES:
If you want to:

	ADD ATTRIBUTES TO EVENT CLASS:
		Open models.py inside of blog folder and add accordingly

	ADD MORE VIEWS(LIKE WEBPAGES I BELIEVE):
		Open views.py inside of blog folder and add accordingly, examples provided based one
		event class data as well as post class data, even though post class is not used
	
	ADD MORE PAGE TEMPLATES:
		Open templates folder inside of Waddup folder (Waddup folder that is inside of 
		Waddup_App) and create a new HTML file template for the page you would like (ex. 	
		event_detail.html), remember that this template must also be declared in the views.py
		file as seen in the EventDetail class in views.py.  To create the new template, start 
		the file with {% extends 'base.html %} to make your new template inherit the 
		base.html template. Use {% block content %} {% endblock content %} to enter content 
		in the given content block in base.html, and format it as you would like.  See 
		event_detail.html for an example of what output will look like based on the given 
		code

	ADD MORE URLS:
		When a new page is added, there must be a new URL added to the urls.py folder inside 
		of the ../blog/urls.py file.  Comments in this file should show an example of how to format url added, REMBER THAT HIS 
	
		

 
