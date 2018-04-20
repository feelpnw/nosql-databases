<<<<<<< HEAD
# mongoimport --db users --collection contacts --file contacts.json
mongoimport --db hw3 --collection movies --file movies.bson
# mongorestore -d db_name -c collection_name path/file.bson

# require the driver package
# Create a client
# client = ...
=======
# import the data file : in terminal, in the folder, type the follow: 
# mongorestore -d hw3 -c movies movies.bson
# which means that the database used for all except E is hw3

>>>>>>> homework-3
import pymongo
from pymongo import MongoClient

# use default host&port 
<<<<<<< HEAD
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
=======
client = MongoClient()
database = client.hw3
collection = database.movies

# A. Update all movies with "NOT RATED" at the "rated" key to be "Pending rating". The operation must be in-place and atomic.
collection.update_many(
	{"rated": "NOT RATED", "$isolated": 1}, {"$set": {"rated":"Pending rating"}}
)

# B. Find a movie with your genre in imdb and insert it into your database with the fields listed in the hw description.
database2 = client.myDB
database2.b.drop()

myGenre = "Short"
cursor = collection.find({"genres":myGenre})
for document in cursor: 
	countries = []
	try: 
		for element in document["countries"]:
			countries.append(element)
	except KeyError:
		countries.append("USA")
		
	genres = []
	for element in document["genres"]:
		genres.append(element) 

	directors = []
	try:
		for element in document["directors"]:
			directors.append(element)
	except KeyError:
		directors.append("Steven Spielberg")

	database2.b.insert(
		{	
			"title": document["title"],
			"year": document["year"],
			"countries": countries,
			"genres": genres,
			"directors": directors,
			"imdb": {"id":document["imdb"]["id"], "rating":document["imdb"]["rating"], "votes":document["imdb"]["votes"]} 
		}
	)

# C. Use the aggregation framework to find the total number of movies in your genre.
# Example result:
#  => [{"_id"=>"Comedy", "count"=>14046}]
re = collection.aggregate([
	{
		"$match": {"genres":myGenre}
	},
	{
		"$group": 
			{"_id":myGenre, "count": {"$sum": 1}}
	}
])
for document in re: 
	print(document)

# D. Use the aggregation framework to find the number of movies made in the country you were born in with a rating of "Pending rating".
# Example result when country is Hungary:
#  => [{"_id"=>{"country"=>"Hungary", "rating"=>"Pending rating"}, "count"=>9}]
#  since there is no record about my country, I use China instead
myCountry = "China"
re2 = collection.aggregate([
	{
		"$match": {"genres":myGenre, "countries":myCountry}
	},
	{
		"$group": 
			{"_id": {"country":myCountry, "rating":"Pending rating"}, "count": {"$sum": 1}}
	}
])
for document in re2: 
	print(document)

# E. Create an example using the $lookup pipeline operator. See hw description for more info.

# create a collection and add some documents
database.directors.drop()
database.directors.insert([
{
	"name": "D.W. Griffith",
	"age": 47,
	"country": "USA"
},
{
	"name": "Laurence Trimble",
	"age": 57,
	"country": "Denmark"
},
{
	"name": "Urban Gad",
	"age": 47,
	"country": "Denmark"
}
])

# create another collection and add some documents
database.movies2.drop()
database.movies2.insert([
{
	"title": "Alice in Wonderland",
	"director": "D.W. Griffith",
	"year": 1915,
	"country": "USA"
},
{
	"title": "By the Sea",
	"director": "Laurence Trimble",
	"year": 1915,
	"country": "Denmark"
},
{
	"title": "Cabiria",
	"director": "Louis Feuillade",
	"year": 1914,
	"country": "France"
},
{
	"title": "The Dead Man Who Killed",
	"director": "D.W. Griffith",
	"year": 1913,
	"country": "USA"
}
])

pipeline = [
	{
		"$unwind": "$director"
	},
	{
		"$lookup":
			{
				"from": "directors",
				"localField": "director",
				"foreignField": "name",
				"as": "directorInfo"
			}

	}
]

result = database.movies2.aggregate(pipeline)

# print the documents of the result 
for document in result: 
	print(document)



>>>>>>> homework-3
