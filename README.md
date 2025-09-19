The sales tracker displays sales across different stores on one platform. 
Users can browse sales happening at the moment by category or popularity.

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