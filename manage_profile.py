# Question: As a senior backend engineer at jovian, 
# you are tasked with developing a fast in-memory data structure 
# to manage profile information (username, name, and email) 
# for 100 million users. it should allow the following 
# operations to be performed efficiently:

# 1. Insert the profile information of a new user 
# 2. Find the profile information of a user, given their username 
# 3. Update the profile information of a user, given their username
# 4. List all the users of the platform, sorted by username

# You can assume that usernames are unique.

class user:
    
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"{self.username}(username = {self.username}, name = {self.name}, email = {self.email})".format(user)
    def __str__(self):
        return self.__repr__()

user1 = user("allen", "allen naki", "allenak@gits.com")
user2 = user("beth", "beth namu", "bethna@holly.com")
user3 = user("cathy", "cathy jo", "cathyjo@wothry.com")
user4 = user("dick", "dick fat", "dickf@means.com")
user5 = user("emma", "emma seri", "emmas@hanks.com")
user6 = user("james", "james jo", "jajo@kitts.com")
user7 = user("kenio", "kenio one", "ken@html.com")
user8 = user("allen", "cathy joy", "cathyjo@wothry.com")
class user_database():
    
    def __init__(self):
        self.users = []

    def __repr__(self):
        return f"(username={user.username}, user={user})".format(user_database)
    def __str__(self):
        return self.__repr__()
    def insert_profile(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    def find_profile(self, username):
        for user in self.users:
            if user.username == username:
                return user
    def update_profile(self, user):
        target = self.find_profile(user.username)
        target.name, target.email = user.name, user.email
        
    def list_users(self):
        return self.users

database = user_database()
database.insert_profile(user3)
database.insert_profile(user6)
database.insert_profile(user1)
database.insert_profile(user2)
database.insert_profile(user4)
database.insert_profile(user5)
database.insert_profile(user7)

#print(database.list_users())

#print(database.find_profile("cathy"))

#database.update_profile(user8)

#print(database.list_users())