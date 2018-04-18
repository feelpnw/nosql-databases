# mongoimport --db users --collection contacts --file contacts.json
mongoimport --db hw3 --collection movies --file movies.bson
# mongorestore -d db_name -c collection_name path/file.bson

# require the driver package
# Create a client
# client = ...
import pymongo
from pymongo import MongoClient

# use default host&port 
client = MongoClient() 
dbObj = client.database1
collectionObj = dbObj.collection1

# A. Update all movies with "NOT RATED" at the "rated" key to be "Pending rating". The operation must be in-place and atomic.

# @ all movies?


# B. Find a movie with your genre in imdb and insert it into your database with the fields listed in the hw description.

# @ your genre : Short

# C. Use the aggregation framework to find the total number of movies in your genre.

# Example result:
#  => [{"_id"=>"Comedy", "count"=>14046}]


# D. Use the aggregation framework to find the number of movies made in the country you were born in with a rating of "Pending rating".

# Example result when country is Hungary:
#  => [{"_id"=>{"country"=>"Hungary", "rating"=>"Pending rating"}, "count"=>9}]

# E. Create an example using the $lookup pipeline operator. See hw description for more info.


# collectionObj.find({"items.fruit": "banana"}).count()


post = {"title": "Avatar",
	"genre": "adventure",
	"tags": ["mongodb", "python", "pymongo"] }

posts = dbObj.posts
post_id = posts.insert_one(post).inserted_id

dbObj.collection1(include_system_collections=False)





# reload like ruby homework? 
# 