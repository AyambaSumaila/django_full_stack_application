The Movies Hub will be a web-based platform where users access
information about movies and can place orders to purchase them.
Now, let’s outline the application’s scope for this particular app:
The Home page will feature a welcoming message.
The About page will provide details about the Movies Store.
The Movies page will exhibit information on available movies and include a filter to
search movies by name. Additionally, users can click on a specific movie to view its
details and post reviews.
The Cart page will showcase the movies added to the cart, along with the total price
to be paid. Users can also remove movies from the cart and proceed with purchases.
The Register page will present a form enabling users to sign up for accounts.
The Login page will present a form allowing users to log in to the application.
The Orders page will display the orders placed by the logged-in user.
The Admin panel will encompass sections to manage the store’s information,
including creating, updating, deleting, and listing information.




# Setting up postgresql database
#### pip install psycopg2-binary

### sudo -u postgres psql
#### CREATE DATABASE  moviedb
#### CREATE USER testuser WITH PASSWORD test12345

#### ALTER ROLE testuser SET client_encoding TO 'utf8';


##### ALTER ROLE testuser SET default_transaction_isolation TO 'read committed';

##### ALTER ROLE testuser SET timezone TO 'UTC';
### GRANT ALL PRIVILEGES ON DATABASE moviedb TO testuser;


### \q




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movie_db',
        'USER': 'movie_user',
        'PASSWORD': 'userPassword12345',
        'HOST': 'localhost',  # Set to '127.0.0.1' if 'localhost' doesn't work
        'PORT': '5432',       # Default PostgreSQL port
    }
}



Building Microservices by Newman, S. (2015)

NOTE
We suggest storing your app templates under the next directory structure –
app_name/templates/app_name/my_template.html. Sometimes, different apps can
contain templates with the same name, which could lead to potential name conflicts in
template resolution. By using the previous strategy, you can define templates with the same
name in different Django apps without any potential name conflict.


1. Configure the about URL.
2. Define the about function.
3. Create the about template.


pip install python-decouple
