// $match all celestial bodies, not equal to Star
db.solarSystem.aggregate([{
  "$match": { "type": { "$ne": "Star" } }
}]).pretty()

// same query using find command
db.solarSystem.find({ "type": { "$ne": "Star" } }).pretty();

// count the number of matching documents
db.solarSystem.count();

// using $count
db.solarSystem.aggregate([{
  "$match": { "type": { "$ne": "Star"} }
}, {
  "$count": "planets"
}]);

// matching on value, and removing ``_id`` from projected document
db.solarSystem.find({"name": "Earth"}, {"_id": 0});

var pipeline = [ { $match: { $and:[{imdb.rating:{$gte:7}},{genres:{$ne:["Crime","Horror"]}},{$or:[{rated:{$eq:"PG"}},{rated:{$eq:"G"}}]},{languages:{$eq:["English","Japanese"]}}] } } ]

var pipeline = [ {
                   $match: {
                            $and:[
                                  {
                                    "imdb.rating": {
                                                  $gte:7
                                                 }
                                  },
                                  {
                                    genres: {
                                             $nin:["Crime","Horror"]
                                             }
                                   },
                                   {
                                    $or:[
                                         {
                                           rated:{
                                                  $eq:"PG"
                                                 }
                                         },
                                         {
                                           rated:{
                                                  $eq:"G"
                                                  }
                                         }
                                         ]
                                    },
                                   {
                                     languages: {
                                                 $eq:["English","Japanese"]
                                                 }
                                   }
                                 ]
                           }
                  }
               ]


var pipeline1 = [ {
                   $match: {
                            $and:[
                                  {
                                    "imdb.rating": {
                                                  $gte:7
                                                 }
                                  }
                                 ]
                           }
                  }
               ]

var pipeline1 = [ {
                   $match: {
                            $and:[
                                  {
                                    "imdb.rating": {
                                                  $gte:7
                                                 }
                                  },
                                  {
                                    genres: {
                                             $nin:["Crime","Horror"]
                                             }
                                   },
                                   {
                                    rated: {
                                             $in:["PG","G"]
                                             }
                                   },
                                   {
                                     languages: {
                                                 $eq:["English","Japanese"]
                                                 }
                                   }
                                 ]
                           }
                  }
               ]


db.movies.aggregate(pipeline1).itcount()

db.movies.aggregate(pipeline).itcount()