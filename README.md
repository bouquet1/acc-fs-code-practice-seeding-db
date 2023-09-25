# acc-fs-code-practice-seeding-db

STEP by STEP CODE ALONG DETAILS

1. start with
   pipenv install
   pipenv shell

2. run migrations (it is in the file already) and create (populate) the db
   alembic upgrade head
   that created meals and users

3. go to seeds.py and work in it
   USE FAKER to seed 10 users
   we added: from faker import Faker and fake = Faker()
   Tom like to use for loop that what we did seeds.py line 22-38 then we executed the file and print it just to see what it's look like
   python3 seeds.py

   error verdi pip install faker diyip run
   print gave us 10 fake user like:
   <User id=None, first_name=David, last_name=Payne, username=David_Payne, email=emilymartinez@lee-adams.biz, created_at=None, updated_at=None >

   <User id=None, first_name=Caitlin, last_name=Stone, username=Caitlin_Stone, email=andersonalyssa@wu-nielsen.org, created_at=None, updated_at=None >

   then add and persist data
   session.add(user)
   session.commit()

then in terminal we typed
ipdb> session.query(User).all()
to see what is returned

bir iki bir sey denedim fix icin
I have tried to add and commit like so:

try:
session.add(user)
session.commit()
except Exception as e:
session.rollback()

# Rollback the transaction if an exception occurs

print(f"Error: {str(e)}")

as a result of this I got 1 fake user in my DB instead of 10 as I've asked in my code in seeds.py. Interesting couldn't figure out more so I pass for now to save time and move on in the module.

4. Another day trying faker again.
   in the virutalenv (pipenv sheell) pyhton3 seeds.py
   -> printed 10 fake user bc of print(user)
   -> exit from ipdb (you can debug errors here mesela Tom ladt_name = first_name yapmisti onu yakaladi print ile duzeltti)
   -> python3 seeds.py again afterfixing a problem (if any) to check the result
   ->ipdb arayuzundesin tekrar run yaptim session.add and session.commit i eklediktan sonra
   -> ipdb> session.query(User).all()
   -> this time faker worked I don't know why it didn't last time
   Now I have 12 users in my DB including the 2 form first try
   -> ipdb> exit

5. now, External API
   seeds.py line 39-49. run the file pyhton3 seeds.py
   kinda self exploratory I'll take notes if I feel needed
   ->print(meal_data)
   prints all of the information with the random letter, this time it was g. it's json data so we can access keys so run:
   ipdb> exit
   change print command in seeds.py
   -> print(len(meal_data["meals"]))
   print(meal_data["meals"][0])
   so we can check how many meals are going to be in this and we can grab the first one cuz the list is long
   so the first result in terminal 38 so with this random letter(b this time) we have 38 recipes and the first one is Bakewell tart object a long return with evrything about that recipe
   ->we chnage the print command and run one more time to grab just the number of recipes and the name of the first recipe with (which random letter will be this time)
   print(len(meal_data["meals"]))
   print(meal_data["meals"][0]["strMeal"])
   -> result: 🌱 Seeding DB...
   7
   Garides Saganaki
   ✅ Done seeding!

# I'm tired taking notes and code along as I watch cuz it takes all day to finish the video. Need to move on so the list of the actions with time stamps to refer back

1. time stamp 1:35
   looping through the meal lists we grab by using external API
   adding the meal to the DB

2. time stamp 1:38
   one-to-many relationship
   CODE DEMO time stamp 1:48
   making the connection between tables with foreignkey time stamp 1:50
   test DB 1:55
