import instaloader
import getpass

user = input("ENTER YOUR INSTAGRAM ID : ")
try:
    password = getpass.getpass()
except:
    print("ERROR")
    exit()
ig = instaloader.Instaloader()
try:
    ig.login(user=user, passwd=password)
except:
    print("INVALID CREDENTIALS")
    print("ABORTING")
    exit()
person=user
profile = instaloader.Profile.from_username(ig.context, person)

my_followers = []
for follower in profile.get_followers():
    username = follower.username
    my_followers.append(username)

my_following = []
for followee in profile.get_followees():
    username = followee.username
    my_following.append(username)

'''
line = ('_'*50)
print(line)
print('PEOPLE WHO FOLLOW ME:')
for i in my_followers:	
	print(i)
print(line)
print("PEOPLE WHO I FOLLOW")
for i in my_following:
	print(i)
print(line)
print("PEOPLE WHO I FOLLOW BUT THEY DON'T FOLLOW ME BACK")
print(line)
'''
dushmans = []
for followee in my_following:
	if followee not in my_followers:
		dushmans.append(followee)

print()
print("LIST OF CULPRITS: ")
print()
for dushman in dushmans:
    print(dushman)
print()
print("Total Culprits: ",len(dushmans))