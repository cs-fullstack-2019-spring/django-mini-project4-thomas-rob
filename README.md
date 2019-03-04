# django-mini-project4

## Create an app to show off games
Your index page should either ask a user to log in, or take them to the logged in user's collection.

### If logged out
**Index Page:** User will see a welcome message and a link to log in and a link to create a new user.

**Log In Page:** The log in page will have a form to log in and redirect the user to the index as a logged in user.

**Create a New User Page:** The create-a-new-user page allows a user to create a new user and redirects to the index.

### If logged in
**Index Page:** A logout and new game link should be near the top of the page. If the user has 0 games, show "No games". Otherwise list all games in their account. Next to each game in the user's account should be an edit and delete link. 

### Point Scale
1 pt: Index while Logged Out/Create User/Log in pages
1 pt: List all games and add a new game
1 pt: Edit and delete games
1 pt: Make it aesthetically pleasing

### Models
The user should have the following:
- username
- Password
- dateAccountCreated (not user created)
- rank (not user created. default is "grunt")

The games they add should have the following:
- name
- developer
- dateMade (with validation)
- ageLimit (with validation)
- foreignKey to user

### Challenge:
A user's rank is "grunt" by default. Their rank should change based off of the information below:
- After 5 games: Captain
- After 10 games: Major
- After 14 games: Colonel
- After 20 games: Major General
- After 50 games: General
