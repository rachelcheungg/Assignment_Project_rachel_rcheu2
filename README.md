My project idea is to create a social app called SaleMate that allows users
to create an account and add their favorite websites and their favorite
items/finds from those websites. 
Users can also browse other users' storefronts.
In essence, each user effectively has a personalized storefront page showcasing their favorite online finds.

⸻

Week 3: \
Why these models/fields?
* First, I created different folders for each of my features.
  The main project folder I created last week was renamed from "sales_tracker" to "login".
  I also created two new folders names "search" and "personalization".
* The "login" folder contains the "User" model, which stores basic information like first and last name,
  username, email, and phone number. I haven't added a password field yet, but that's something for the future.
  The username serves as the primary key, since it should be unique. This way, I don't have to create a separate user_id field.
  Every field in the "User" model is required except for phone number because I think websites don't always require phone numbers as long as there's an email.
  Lastly, I added string representation (__str__) for readability.
* The "personalization" folder contains the "Favorite" model, which is meant to contain the websites each user favorites.
  I still need to create a composite primary key for this model (which is just a combination of "username" from the "User" model and "website_address" from the "Website" model).
  I also added string representation (__str__) for readability.
* The "search" folder contains two models: "Category" and "Website".
  The "Category" model has "category_name" as the primary key so there are no duplicate categories.
  The "Website" model has "website_address" as the primary key since this web addresses are unique.
  It also has "website_name" so users know which store/website it is, and "category" that maps it to the category.
  I also added string representation (__str__) for readability for both models.

Your relationship choices (ForeignKey, on_delete rationale)
* The "Category" and "Website" model has a 1-to-many relationship since a category can have multiple website.
  I set the "category" variable in "Website" model to be a foreign key, and on_delete = model.SET_NULL so that it will preserve the website even if the category is deleted.
  Additionally, in the "Favorite" model, both "username" and "website_address" serve as a foreign key.
  on_delete = models.CASCADE here because if either a user deletes their account or the website gets deleted from the database, it will take it out of the favorite websites page.

Any constraints (unique, ordering)
* There are a few fields that I made unique. Any field that was assigned to be a primary key is unique (username, website_address, category_name).
  Other fields like email and phone number are also unique but not primary keys.
  I think I want all the models to be ordered alphabetically, but I haven't figured out how to do that yet.

How you seeded test data.
* I added test data through the admin page.

Week 4: \
I added the views for my user data using HttpResponse, render(), and a class-based list view.
I added a base.html file with the general structure of the website.
I also added an html template for my login feature that extends base.html.
Lastly, I needed to route each of my views. They all use the same html file (user_list.html),
so I created a unique url pattern for each of the views. These were the main changes I added for the week.

Week 5: \
This week, I implemented base CBV onto my website model, implemendted generic CBV onto my categories model, and implemented detail view for my users model.
I also added a new html file for my user detail view, and configured the urls respectively.

Week 6: \
In assignment 6, I added data aggregation features to display summary statistics using Django ORM. 
Specifically, I implemented counts of websites favorited by each user and counts of websites per category. These additions demonstrate the use of `annotate()` and `Count()` to compute grouped summaries in Django views.

Week 7: \
In assignment 7, I implemented a data visualization feature using Matplotlib. 
I added ORM aggregations in views.py to generate summary statistics and display them as a bar chart on the site. 
I also set up a custom /static/ folder with a global CSS file (style.css) to apply a consistent color theme and layout across all pages.

Week 8: \
This week, I created a GET search method for searching users, and I implemented two forms using the POST method with function-based views and class-based view.
This week's assignment taught me the difference between using GET and POST, and when we would use FBVs vs. CBVs.
GET is used for retrieving data or displaying information that doesn't change the server's state.
It's ideal for actions that are safe, replicable, and shareable.
On the other hand, POST is used to send data to the server (e.g., creating, updating, or deleting).
POST is ideal when your action is changing something.
CBVs help to reduce boilerplate by handling common patterns like form rendering and validation automatically.
FBVs are generally used when you need simple or highly customized logic.

Week 9: \
This week, I added new API endpoints for user favorites and chart visualization.
`/api/user_favorites/` returns JSON data about each user’s number of favorite websites.
`/personalization/charts/favorites.png` generates a bar chart of the count of favorite websites per user from the API data.

Week 11: \
**Part 1**: \
This week, I added CSV and JSON export functionality that allows users to download a list of websites in either CSV or JSON format.
I also added a reports page that summarizes information about the websites.
Users can now easily download a website list and view grouped summaries directly from the web interface.

URLs:
* http://127.0.0.1:8000/search/reports/
* http://127.0.0.1:8000/search/export/websites.csv
* http://127.0.0.1:8000/search/export/websites.json

**Part 2**: \
I believe all the main routes in my project are protected because they're not things I would want the public/anyone to have access to.
If I were to leave a route unprotected, essentially, it would probably be the one that directs the user to the 
Open Library Search page since it's not exactly something I would consider to be sensitive information.

The only public endpoints were the login and signup page since users would need to be able to log in without being 
authenticated, and similarly, new users would need to register a new account.

After logging in, users are directed to the "User List" page. If a user originally visited a protected page, Django
redirects them back to the correct URL using the `next` query parameter. After logging out, users are redirected to the login page.

Instructor credentials:
* **Username**: mohitg2
* **Password**: graingerlibrary

How signup works is that it uses a simple Django form that collects a username, email, password, and password confirmation. 
If successful, a new user is created as a regular user (non-staff, non-superuser). 
Immediately after creation, Django automatically logs the user in and redirects them inside the app to the user list page. 
The form also ensures username uniqueness and performs basic password confirmation checks.