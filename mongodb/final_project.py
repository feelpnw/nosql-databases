# Put the use case you chose here. Then justify your database choice:
#	Use Case : Photo Sharing Application  
#	My database choice is MongoDB. 
#	
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# 
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
# 
# 

import pymongo
from pymongo import MongoClient
from datetime import datetime
import random
client = MongoClient()
database = client.finalproj


# create at least 3 users 
collection_users = database.users 
# collection_users.insert([
# {
# 	"username": "user1",
# 	"email": "user1@gmail.com",
# 	"name": "D.W. Griffith",
# 	"age": 47,
# 	"gender": "m",
# 	"country": "USA",
# 	"password": "pw1",
# 	"following": [],
# 	"followed": [],
# 	"posts": [],
# 	"comments": [],
# 	"saved": [],
# 	"liked": [],
# 	"messages": []
# },
# {
# 	"username": "user2",
# 	"email": "user2@gmail.com",
# 	"name": "Laurence Trimble",
# 	"age": 27,
# 	"gender": "m",
# 	"country": "Denmark",
# 	"password": "pw2",
# 	"following": [],
# 	"followed": [],
# 	"posts": [],
# 	"comments": [],
# 	"saved": [],
# 	"liked": [],
# 	"messages": []
# },
# {
# 	"username": "user3",
# 	"email": "user3@gmail.com",
# 	"name": "Urban Gad",
# 	"age": 21,
# 	"gender": "m",
# 	"country": "USA",
# 	"password": "pw3",
# 	"following": [],
# 	"followed": [],
# 	"posts": [],
# 	"comments": [],
# 	"saved": [],
# 	"liked": [],
# 	"messages": []
# },
# {
# 	"username": "user4",
# 	"email": "user4@gmail.com",
# 	"name": "Jane Locke",
# 	"age": 25,
# 	"gender": "f",
# 	"country": "USA",
# 	"password": "pw4",
# 	"following": [],
# 	"followed": [],
# 	"posts": [],
# 	"comments": [],
# 	"saved": [],
# 	"liked": [],
# 	"messages": []
# },
# {
# 	"username": "user5",
# 	"email": "user5@gmail.com",
# 	"name": "Julia Kim",
# 	"age": 31,
# 	"gender": "f",
# 	"country": "USA",
# 	"password": "pw5",
# 	"following": [],
# 	"followed": [],
# 	"posts": [],
# 	"comments": [],
# 	"saved": [],
# 	"liked": [],
# 	"messages": []
# }
# ])

# create at least 15 other objects other than users 
# create objects of post collection 
collection_posts = database.posts
# collection_posts.insert([
# {
# 	"username": "user2",
# 	"photos": "photo123", 
# 	"liked_by": [],
# 	"comments": [],
# 	"time": datetime.now(),
# 	"hashtag": ["#travel", "#food"]
# },
# {
# 	"username": "user4",
# 	"photos": "photo323", 
# 	"liked_by": [],
# 	"comments": [],
# 	"time": datetime.now(),
# 	"hashtag": ["#gym", "#exercise"]
# },
# {
# 	"username": "user3",
# 	"photos": "photo984", 
# 	"liked_by": [],
# 	"comments": [],
# 	"time": datetime.now(),
# 	"hashtag": ["#marketing", "#socialmedia"]
# },
# {
# 	"username": "user5",
# 	"photos": "photo323", 
# 	"liked_by": [],
# 	"comments": [],
# 	"time": datetime.now(),
# 	"hashtag": ["#pizza", "#yummy"]
# },
# {
# 	"username": "user4",
# 	"photos": "photo913", 
# 	"liked_by": [],
# 	"comments": [],
# 	"time": datetime.now(),
# 	"hashtag": ["#shopaholics", "#styleblogger"]
# }
# ])

collection_comments = database.comments
# collection_comments.insert([
# {
# 	"post_id": "5aef9dd16438eabd6cbe1696",
# 	"context": "nice photo!",
# 	"username": "user5"
# },
# {
# 	"post_id": "5aef9dd16438eabd6cbe169a",
# 	"context": "hello, my bag", 
# 	"username": "user3"
# },
# {
# 	"post_id": "5aef9dd16438eabd6cbe169a",
# 	"context": "Lovely!", 
# 	"username": "user1"
# }
# ])

collection_messages = database.messages
# collection_messages.insert([
# {
# 	"to_username": "user2",
# 	"from_username": "user1", 
# 	"time": datetime.now(),
# 	"context": "Hey, please call me later"
# },
# {
# 	"to_username": "user1",
# 	"from_username": "user2", 
# 	"time": datetime.now(),
# 	"context": "Alright, see you!"
# }, 
# {
# 	"to_username": "user3",
# 	"from_username": "user4", 
# 	"time": datetime.now(),
# 	"context": "Can you share the location of the restaurant?"
# }
# ])

collection_saved = database.saved
# collection_saved.insert([
# {
# 	"post_id": "5aef9dd16438eabd6cbe1696",
# 	"collection": 0
# },
# {
# 	"post_id": "5aef9dd16438eabd6cbe1698",
# 	"collection": 0
# },
# {
# 	"post_id": "5aef9dd16438eabd6cbe1698",
# 	"collection": 0
# }
# ])

# collection_users.update(
# 	{"username": "user1", "$isolated": 1}, {"$push": {"saved":"5aefa5916438eac2959c05ad"}}
# )
# collection_users.update(
# 	{"username": "user5", "$isolated": 1}, {"$push": {"saved":"5aefa5916438eac2959c05ae"}}
# )
# collection_users.update(
# 	{"username": "user5", "$isolated": 1}, {"$push": {"saved":"5aefa5916438eac2959c05af"}}
# )

collection_hashtag = database.hashtag
# collection_hashtag.insert([
# {
# 	"tagname": "#travel",
# 	"post_id": "5aef9dd16438eabd6cbe1696", 
# },
# {
# 	"tagname": "#food",
# 	"post_id": "5aef9dd16438eabd6cbe1696", 
# },
# {
# 	"tagname": "#gym",
# 	"post_id": "5aef9dd16438eabd6cbe1697", 
# },
# {
# 	"tagname": "#exercise",
# 	"post_id": "5aef9dd16438eabd6cbe1697", 
# },
# {
# 	"tagname": "#pizza",
# 	"post_id": "5aef9dd16438eabd6cbe1699", 
# },
# {
# 	"tagname": "#yummy",
# 	"post_id": "5aef9dd16438eabd6cbe1699", 
# }
# ])


# Action 1: As a new user, I create a new account to use the application.
# use createUser(username, email, name, age, gender, country, password) to execute
# gender should be either 'm' for male or 'f' for female 
def createUser(username, email, name, age, gender, country, password):
	collection_users.insert(
	{
		"username": username,
		"email": email,
		"name": name,
		"age": age,
		"gender": gender,
		"country": country,
		"password": password,
		"following": [],
		"followed": [],
		"posts": [],
		"comments": [],
		"saved": [],
		"liked": [],
		"messages": []
	})

# sample code to implement the action 
# createUser("user6", "u6@gmail.com", "Tom Neilson", 30, 'm', 'Canada', 'u6pw')


# Action 2: As a user, I search username(s) of people who are from USA. 
def searchUsernameWithCountry(country):
	cursor = collection_users.find({"country": country}, {"username":1, "_id":0})
	for document in cursor:
		print(document)

# sample code to implement the action 
# searchUsernameWithCountry("USA")


# Action 3: As a user, I follow another user.
# use following(your_username, username_you_want_follow) to execute
def following(username, following_id):
	collection_users.update(
		{"username": username, "$isolated": 1}, {"$push": {"following":following_id}}
	)	

# sample code to implement the action 
# following("user6", "user4")

# Action 4: As a user, I send a message to another user. 
# use sendMessage(your_username, to_username, message) to execute 
def sendMessage(username, to_username, message):
	time = datetime.now()
	collection_messages.insert({
		"to_username": to_username,
		"from_username": username, 		
		"time": time,
		"context": message
	})
	cursor = collection_messages.find({"time":time, "to_username":to_username, "from_username":username},{"_id":1})
	for document in cursor: 
		uid = document
		uidstr = str(uid)
	collection_users.update(
		{"username": username, "$isolated": 1}, {"$push": {"messages":uidstr[8:-1]}}
	)	

# sample code to implement the action 
# sendMessage("user6", "user4", "hello!")

# Action 5: As a user, I save a post another user makes. 
# use savePost(your_username, post_id) to execute
def savePost(username, post_id): 
	time = datetime.now()
	collection_saved.insert({
		"post_id": post_id,
		"time": time,
		"collection": 0
	})	
	cursor = collection_saved.find({"time":time, "post_id":post_id},{"_id":1})
	for document in cursor: 
		sid = document
		sidstr = str(sid)
	collection_users.update(
		{"username": username, "$isolated": 1}, {"$push": {"saved":sidstr[8:-1]}}
	)	

# sample code to implement the action 
# savePost("user4", "5aef9dd16438eabd6cbe1697")

# Action 6: As a user, I check the posts I saved. 
def checkMySaved(username):
	savedID = []
	cursor = collection_users.find({"username":username},{"saved":1, "_id":0})
	for document in cursor:
		for element in document["saved"]:
			savedID.append(element)
			
	print(savedID)
	for i in savedID:
		cursor3 = collection_saved.find({"_id":i},{"post_id":1, "_id":0})


