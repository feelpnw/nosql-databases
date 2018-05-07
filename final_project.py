# Put the use case you chose here. Then justify your database choice:
#	Use Case : Photo Sharing Application  
#	My database choice is MongoDB. 
#	MongoDB is selected because, first of all, it is easy to use with having all functionalities for this photo sharing application. 
#	Since all fields are easily accessable and writable, it is suitable for the search and post functions which is the main feature of this application. 
#	The relatively faster query speed and good scalability for the future expansion are also considered.

# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# The data will be still safe due to the feature of replication to store multiple copies of data in multiple servers.

# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
# The data in users collection is the most important data in this application. If the data is lost, it cannot track the user information unless the user put the information again. 
# One of the ways to mitigate the risk is to set a configuration in that write operation to users collection has a higher priority and stronger write concerns are used for that.

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import random
client = MongoClient()
database = client.finalproj

# create at least 3 users 
collection_users = database.users 
collection_users.insert([
{
	"username": "user1",
	"email": "user1@gmail.com",
	"name": "D.W. Griffith",
	"age": 47,
	"gender": "m",
	"country": "USA",
	"password": "pw1",
	"following": [],
	"followed": [],
	"posts": [],
	"comments": [],
	"saved": [],
	"liked": [],
	"messages": []
},
{
	"username": "user2",
	"email": "user2@gmail.com",
	"name": "Laurence Trimble",
	"age": 27,
	"gender": "m",
	"country": "Denmark",
	"password": "pw2",
	"following": [],
	"followed": [],
	"posts": [],
	"comments": [],
	"saved": [],
	"liked": [],
	"messages": []
},
{
	"username": "user3",
	"email": "user3@gmail.com",
	"name": "Urban Gad",
	"age": 21,
	"gender": "m",
	"country": "USA",
	"password": "pw3",
	"following": [],
	"followed": [],
	"posts": [],
	"comments": [],
	"saved": [],
	"liked": [],
	"messages": []
},
{
	"username": "user4",
	"email": "user4@gmail.com",
	"name": "Jane Locke",
	"age": 25,
	"gender": "f",
	"country": "USA",
	"password": "pw4",
	"following": [],
	"followed": [],
	"posts": [],
	"comments": [],
	"saved": [],
	"liked": [],
	"messages": []
},
{
	"username": "user5",
	"email": "user5@gmail.com",
	"name": "Julia Kim",
	"age": 31,
	"gender": "f",
	"country": "USA",
	"password": "pw5",
	"following": [],
	"followed": [],
	"posts": [],
	"comments": [],
	"saved": [],
	"liked": [],
	"messages": []
}
])

# create at least 15 other objects other than users 
# create objects of post collection 
# photo is stored as a string for a convenient purpose of this assignment
collection_posts = database.posts
collection_posts.insert([
{
	"username": "user2",
	"photos": "photo123", 
	"liked_by": [],
	"comments": [],
	"time": datetime.now(),
	"hashtag": ["#travel", "#food"]
},
{
	"username": "user4",
	"photos": "photo323", 
	"liked_by": [],
	"comments": [],
	"time": datetime.now(),
	"hashtag": ["#food", "#pizza"]
},
{
	"username": "user3",
	"photos": "photo984", 
	"liked_by": [],
	"comments": [],
	"time": datetime.now(),
	"hashtag": ["#food", "#socialmedia"]
},
{
	"username": "user5",
	"photos": "photo323", 
	"liked_by": [],
	"comments": [],
	"time": datetime.now(),
	"hashtag": ["#pizza", "#yummy"]
},
{
	"username": "user4",
	"photos": "photo913", 
	"liked_by": [],
	"comments": [],
	"time": datetime.now(),
	"hashtag": ["#pizza", "#styleblogger"]
}
])


# # sample code to implement the action 
tmp_postIDs = []
tmp_cursor = collection_posts.find({},{"_id":1})
for document in tmp_cursor:
	tmp_postIDs.append(str(document)[18:-3])

# create objects of comments collection 
collection_comments = database.comments
collection_comments.insert([
{
	"post_id": tmp_postIDs[0],
	"context": "nice photo!",
	"username": "user5"
},
{
	"post_id": tmp_postIDs[1],
	"context": "hello, my bag", 
	"username": "user3"
},
{
	"post_id": tmp_postIDs[0],
	"context": "Lovely!", 
	"username": "user1"
}
])

# create objects of messages collection 
collection_messages = database.messages
collection_messages.insert([
{
	"to_username": "user2",
	"from_username": "user1", 
	"time": datetime.now(),
	"context": "Hey, please call me later"
},
{
	"to_username": "user1",
	"from_username": "user2", 
	"time": datetime.now(),
	"context": "Alright, see you!"
}, 
{
	"to_username": "user3",
	"from_username": "user4", 
	"time": datetime.now(),
	"context": "Can you share the location of the restaurant?"
}
])

# create objects of saved collection 
collection_saved = database.saved
collection_saved.insert([
{
	"post_id": tmp_postIDs[0],
	"time": datetime.now(),
	"collection": 0
},
{
	"post_id": tmp_postIDs[1],
	"time": datetime.now(),
	"collection": 0
},
{
	"post_id": tmp_postIDs[2],
	"time": datetime.now(),
	"collection": 0
}
])

tmp_savedID0 = []
cursor = collection_saved.find({},{"_id":1})
for document in cursor: 
	tmp_savedID0.append(str(document)[18:-3])

# update users collection because saved field in users collection and saved collection are relevant to each other 
collection_users.update(
	{"username": "user1", "$isolated": 1}, {"$push": {"saved":tmp_savedID0[0]}}
)
collection_users.update(
	{"username": "user5", "$isolated": 1}, {"$push": {"saved":tmp_savedID0[1]}}
)
collection_users.update(
	{"username": "user5", "$isolated": 1}, {"$push": {"saved":tmp_savedID0[2]}}
)


tmp_pizzahash = []
cursor = collection_posts.find({"hashtag":"#pizza"},{"_id":1})
for document in cursor: 
	tmp_pizzahash.append(str(document)[18:-3])

# create objects for #pizza hashtag in hashtag collection 
collection_hashtag = database.hashtag
for i in tmp_pizzahash:
	collection_hashtag.insert({
		"tagname": "#pizza",
		"post_id": i 
	})

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
createUser("user6", "u6@gmail.com", "Tom Neilson", 30, 'm', 'Canada', 'u6pw')

# Action 2: As a user, I search username(s) of people who are from USA. 
def searchUsernameWithCountry(country):
	cursor = collection_users.find({"country": country}, {"username":1, "_id":0})
	for document in cursor:
		print(str(document)[14:-2])

# sample code to implement the action 
searchUsernameWithCountry("USA")


# Action 3: As a user, I follow another user.
# use following(your_username, username_you_want_follow) to execute
def following(username, following_id):
	collection_users.update(
		{"username": username, "$isolated": 1}, {"$push": {"following":following_id}}
	)	

# sample code to implement the action 
following("user6", "user4")

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
sendMessage("user6", "user4", "hello!")

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
# tmp_postIDs[0] is arbitrarily selected for the sample code
savePost("user6", tmp_postIDs[0])

# Action 6: As a user, I check the photos of the posts I saved. 
# (photo is stored as a string for a convenient purpose of this assignment)
# use checkMySaved(your_username) to execute
def checkMySaved(username):
	savedID = []
	postID = []
	cursor = collection_users.find({"username":username},{"saved":1, "_id":0})
	for document in cursor:
		for element in document["saved"]:
			savedID.append(element)
	for i in savedID:
		idd = i[10:-2]
		cursor3 = collection_saved.find({"_id":ObjectId(idd)},{"post_id":1, "_id":0})
		for element in cursor3:
			postID.append(element)
	for i in postID:
		idd = str(i)[13:-2]
		cursor2 = collection_posts.find({"_id":ObjectId(idd)}, {"photos":1, "_id":0})
		for photo in cursor2:
			print(str(photo)[12:-2])
			
# sample code to implement the action 
checkMySaved("user6")

# Action 7: As a user, I search the photos of the posts with tag named "pizza".
def checkWithHashtag(hashtag):
	postID = []
	cursor = collection_hashtag.find({"tagname":hashtag},{"post_id":1,"_id":0})
	for document in cursor:
		postID.append(document)
	for i in postID:
		idd = str(i)[13:-2]
		cursor2 = collection_posts.find({"_id":ObjectId(idd)}, {"photos":1, "_id":0})
		for photo in cursor2:
			print(str(photo)[12:-2])

# sample code to implement the action 
checkWithHashtag("#pizza")

# Action 8: As a user, I save one of posts in my saved library to my collection named 'favorite'. 
# use moveToCollection(targeted_saved_id, collection_name) to execute 
collection_collection = database.collection 
def moveToCollection(saved_id, collection_name):
	cursor2 = collection_saved.find({"_id":ObjectId(saved_id)}, {"post_id":1, "_id":0})
	for document in cursor2:
		post_id = str(document)[13:-2]
	collection_saved.update(
		{"_id": ObjectId(saved_id), "$isolated": 1}, {"$set": {"collection":1}}
	)

	collection_collection.insert({
		"saved_id ": saved_id,
		"post_id": post_id,
		"collectionname": collection_name
	})

# sample code to implement the action 
tmp_savedID = []
cursor = collection_saved.find({},{"_id":1})
for document in cursor: 
	tmp_savedID.append(str(document)[18:-3])
# savedID[0] is the arbitrary target that goes to my collection named 'favorite'
moveToCollection(tmp_savedID[0], "favorite")







