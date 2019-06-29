# D&D Planner
This is the development repository for D&D Planner, a tool to aid Dungeon Masters in planning their campaign, managing initiative and damage in combat, and more. This web app is written mostly in Python with some JavaScript through the [Django](https://www.djangoproject.com/) framework. The front end is mostly designed using the [Materialize CSS](https://materializecss.com/) framework.

### Installation Instructions:
1. Ensure that you have python and pip on your machine and that they are up to date.
1. From your terminal, run `pip install django`.
1. Change directory to the directory in which you want to store the server and run `git clone https://github.com/sithon512/DnD-Planner`.
1. From the newly created root directory for the server, change the GitHub directory to `/DnDPlanner/`.
1. From your terminal, run `python manage.py collectstatic`.
1. From your terminal, run `python manage.py runserver`.
1. You should then end the server by typing `ctrl + C`, then run `python manage.py makemigrations` and `python manage.py migrate` to build the database.

You should now see in your terminal that the server has started and is listening on `127.0.0.1:8000`. If you type that address into your web browser of choice, you will be able to see the server running for you.

**Important Note:** The database used during the development of this project is *not* published on GitHub, so you'll create your own simply by running the server. It will be automatically created when during the `runserver` command as described above.

### Current Features:
* Quick Initiative Tracker
	* Allows adding a creature to the initiative tracker and automatically sorts by the initiative roll.
	* The **next turn** button highlights the next creature in the initiative order.
	* The **clear initiative** button ends the tracking and removes all current creatures from the initiative order.
* Login/Logout Features
	* The installation instructions alone do not give you the a user login, you can create an account with full access by running `python manage.py createsuperuser` and following the prompts. This account will have all of the permissions and allow you to try out all features of the site. There is also a small collection of automatically generated administration pages that you can access at the `/admin` url under the default `127.0.0.1:8000` url.

### Planned Features:
* Campaign Planning
	* Create campaigns
		* created campaigns act as containers to group together encounters, creatures (including characters), plot beats, and items in order to organize
	* Create encounters
		* created encounters are for planning a meeting of PC's with creatures/NPC's in your world
		* encounters are created under a campaign
		* relationships can be created between encounters and creatures, characters, items, locations and/or plot beats
	* Create custom creatures
		* creatures are for designing either templates for creating other characters or individual NPC's that can be dropped into encounters
		* creatures can be created under a campaign or stand alone
		* relationships can be created between creatures and encounters, items, locations, and/or plot beats
	* Create plot beats
		* created plot beats are for reminding dm's of plans that they had for a given location, encounter, creature, or item
		* plot beats are created under a campaign
		* relationships can be created between plot beats and encounters, creatures, items, and/or locations
	* Create items
		* created items are simply for organization and keeping track of items that you give your players
		* items can be created under a campaign or stand alone
		* relationships can be created between items and plot beats, encounters, creatures, and/or locations
	* Create location
		* created locations are for grouping together other features
		* locations are created under a campaign 
		* relationships can be created between locations and encounters, creatures, plot beats, and/or items
	* Initiative tracker
		* like the quick initiative tracker, but encounters can be preloaded with creatures from an encounter
		* additionally, this will allow you to track individual HP of creatures (and PC's if you'd like), resistances, armor class, and record status text from a combat so that you can read what happened in a combat after the fact and save this to the campaign.
* Publish Campaigns/Encounters
	* This will allow you to make the campaigns that you've created (as well as any features inside of them) viewable and accessible to the public so that you can share the work you've done with the world.