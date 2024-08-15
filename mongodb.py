# mongodb shorts
# =========basics==================================================
# mongosh
# exit
# ========usage=========================================================================
# db shows
# use shopping
# show collections
# db.dropDatabase() remove db

# ========crud===========================================================================
# db.users.insertOne( { name: "Chris"}) Add a new document with the name of Chris into the users collection
# db.users.insertMany( { age: "24"},{age: "38"} )Add two new documents with the age of 24 and 38 into the users collection
# db.users.find({status:1,item:1}) Returns matching documents only from state field, item field and, by default, the _id field.
# db.users.find({status:1,item:1,_id:0}) Returns matching documents only from state field and item field. Does not return the _id field.
# db.users.deleteOne({ age: 37 }) Deletes the first user with the age 37.
# db.users.deleteMany({ age: {$lt:18 }}) Deletes all users with the age less than 18..
# db.users.updateOne({ age: 25 },{ $set: { age: 32 } }) Updates all users from the age of 25 to 32.
# db.users.updateMany({ age: 27 },{ $inc: { age: 3 } }) Updates all users with an age of 27 with an increase of 3.
# db.users.replaceOne({ name: Kris }, {name: Chris }) Replaces the first user with the name Kris with a document that has the name Chris in its name field.
# ============comparison===================================================================================================
# db.users.find({ system: { $eq:"macOS" } }) Finds all users with the operating system macOS.
# db.users.deleteMany({ age: { $gt: 99}}) Deletes all users with an age greater than 99.
# db.users.updateMany({age: {$gte:21},{access: "valid"}}) Updates all access to "valid" for all users with an age greater than or equal to 21.
# db.users.find( { place: { $in: ["NYC", "SF"] } }) Find all users with the place field that is either NYC or SF.
# db.users.deleteMany({ age: {$lt:18}}) Deletes all users with the age less than 18..
# db.users.updateMany({ age: { $lte: 17}, {access: "invalid"}}) Updates all access to "invalid" for all users with an age less than or equal to 17.
# db.users.find({ place: {$ne:"‘NYC"}}) Find all users with the place field set to anything other than NYC.
# db.users.find( { place: { $nin: ["NYC", "SF" ] } }) Find all users with the place field that does not equal NYC or SF.
# ==========update=========================================================================
# db.users.updateOne({ age: 22 }, {$inc: { age: 3} })Adds 3 to the age of the first user with the age of 22.
# db.scores.insertOne( { _id: 1,highScore: 800, lowScore: 200 } )Creates a scoles collection and sets the value of highScore to 800 and lowScore to 200.
# db.scores.updateOne( { _id: 1 }, {$min: { lowScore: 150 } } ) $min compares 200 (the current value of lowScore) to the specified value of 150. Because 150 is less than 200, $min will update lowScore to 150.
# db.scores.updateOne( { _id: 1 }, {$max: { highScore: 1000 } } ) $max compares 800 (the current value of highScore) to the specified value of 1000. Because 1000 is more than 800, $max will update highScore to 1000.
# db.scores.updateOne( { $rename: {'highScore': 'high'} }) Renames the field ‘highScores’ to ‘high’,
# db.users.updateOne({ $set: { name:"valid user" } }) Replaces the value of the name field with the specified value valid user.
# db.users.updateOne({ $unset: { name:"" } }) Deletes the specified value valid user from the name field.
# db.users.find({_id:{$type:'objectId'}}) //اگر جنس آیدی آنها پیشفرض آبجکت آیدی هست رو بیار
# db.users.find({age:{$exists:false}}) //اگر فیلد سن نداشتند نشان بده
# load('B:\mongodb/file1.js' )//کد های داخل این فایل را اجرا کن
# show collections // در این دیتابیس لیست تمامی جداول را نمایش بده
# show dbs //برای نمایش لیست دیتابیس ها
# use shopping//برای وارد شدن داخل یک دیتابیس
# db.users.drop()//جدول یوزرز با این دستور پاک میشود
# db.createCollection('name')//برای ساخت کالکشن یا جدول جدید
# db.products.find({color:{$size:2}})//اونهایی که تو لیست رنگ دو رنگ دارند
# db.products.find({color:{$elemMatch:{$eq:'black'}}}) //اونهایی رو برگردون که رنگ مشکی هم دارند 
# db.products.find({color:{$all:['black','blue']}})//چک کن محصولاتی رو بیار که این دوتا رنگ رو داشته باشند 
# db.products.find({},{name:1})//در اینجا فقط فیلد نام این آبجکت برمیگرده
# db.users.updateOne({id:4},{$set:{family:"abbasi"}})//در اینجا فیلد فامیلی آیدی ۴ رو تغییر دادیم 
# db.users.updateOne({id:4},{$set:{family:"abbasi"}},{upsert:true})//در اینجا در صورت پیدا نکردن موردی یک مورد به خودی خود اضافه میگردد 
# db.users.updateOne({id:2},{$inc:{id:100}})//برای اضافه کردن مقدار عددی به فیلدی در یک آبجکت
# db.users.updateOne({id:4},{$max:{id:100}})//برو آبجکتی با آیدی داده شده پیداکن بزرگترین آیدی بین آیدی ای که من دادم و مال خودش رو بزار 
# db.users.updateOne({id:4},{$min:{id:100}})//برو آبجکت رو پیدا کن و کوچکترین مقدار بین اونی که خودش دارو و من دادم رو توی اون فیلد بزار
# db.users.updateMany({name:4},{$min:{price:10000}})//تمامی آبجکت هایی که نامشان ۴ هست رو پیدا کن و قیمتشون رو مقایسه کن با قیمتی که من بهت پاس دادم و کوچکترینش رو جایگذاری کن 
# // اگر فیلدی را معرفی کنید که وجود نداشته باشد این مقدار فیلد به اون آبجکت اضافه میشود
# db.users.updateMany({},{$mul:{id:2}})
# db.users.updateOne({id:300},{$unset:{name:""}}) //برای حذف کردن فیلدی از داخل یک آبجکت از $unsetاستفاده میکنیم 
# db.users.updateOne({id:300},{$unset:{"color.0":""}})//برای حذف کردن قسمتی از یک فیلد یک آبجکت باید آدرس آن قسمت رو به صورت رشته ای بدهیم 
# ==========Modifiers==============================================================================
# db.users.find().sort({ name: 1, age:-1 })  Sorts all users by name in alphabetical orderand then if any names are the same sort by age in reverse order
# db.users.updateMany({}, { $push: {friends: "Chris" } }) Add Chris to the friends array for all users
# db.users.find().limit() all users by name in alphabetical orderand then if any names are the same sort by age in reverse order
# db.products.deleteMany({_id:{$in:[1,2,3,4,5]}})
# db.collectionName.drop() for deleting a collection
# db.dropDatabase(dbname) for delete database
# ==========Aggregation pipline==============================================================================
# db.products.aggregate(
#                                 [
#                                     {$match:{}},                    //فیلتر موارد
#                                     {$group:                        //گروه بندی موارد  
#                                         {                           //
#                                             _id:'$name',            //گروه بندی بر اساس؟ نام 
#                                             Count:{                 // نام لیبل 
#                                                 $count:{}           // کار لیبل
#                                                   }
#                                         }
#                                     }
#                                 ]
#                             )
# db.products.aggregate([{$match:{}},{$group:{_id:"$name",Total:{$sum:"$price"}}}]) //تقسیم بندی کن بر اساس نام  
# db.products.aggregate([{$match:{}},{$group:{_id:null,Sum:{$sum:"$price"}}}])    //قیمت همه رو با هم جمع میکند
# db.products.aggregate([{$match:{}},{$group:{_id:null,minimum:{$min:"$price"}}}])    //کمترین از هر گروه
# db.products.aggregate([{$match:{}},{$group:{_id:null,Summerize:{$sum:"$price"}}}])    //جمع آن گروه
# db.products.aggregate([{$match:{}},{$group:{_id:null,maximum:{$max:"$price"}}}])    //بیشترین از هر گروه 
# db.products.aggregate([{$match:{}},{$group:{_id:null,average:{$avg:"$price"}}},{$sort:{average:1}}])    //میانگین هر گروه بر حسب کوچک به بزرگ
# db.products.aggregate([{$skip:2}])    //از دو گزینه ی اول بپر
# db.products.aggregate([{$limit:2}])    //فقط دو گزینه ی اول رو بیار 
# ==========Backup and restore ==============================================================================
# mongodump -d dbName -o C:/Users/restof/address    this is the way you can have your backup in bison format
# mongorestore C:/Users/backupfile/address    this is the way you can restore bison backup
# =========for backup json file you need a library named : mongo database tools==============
# mongoexport --db=dbName --collection=collectionName --out=filename.json     to make json file backup 
# mongoimport --db=dbName --collection=collectionName --file filename.json --jsonArray    for restore that backup you need to add backup into an array and add comma in last part of each Object
# ==========pymongo==============================================================================
from pymongo import MongoClient
client = MongoClient(host='lcalhost',port=27017)  # the way you can  connect to a db 
dbtest = client['test'] # if dbtest exist it can be used and if its not exist it will be created and used
people = dbtest['People'] #  if collection exists it can be used and if its not exist it will be created and used
people.IntersectionObserverEntry({'name':'mehdi','family':'abbasi','age':42}) # this is how to insert first record
for db in clientInformation.list_database_names(): # this is how you can show dbs
    print(db)
for collection in dbtest.list_collection_names(): # this is how you can show collections
    print(collection)
for doc in people.find():  # this is how you can show records
    print(doc)
people.IntersectionObserverEntry([ # this is how you can import lists of people
    {'name':'mehdi','family':'abbasi','age':42},
    {'name':'ali','family':'rezaee','age':30},
    {'name':'mehdi','family':'mohammadi','age':22},
                                ])

print(people.find().count()) #  counting
print(people.find().limit(2)) #  just first two of them 
people.update({'family':'mohammadi'},{'$set':{'name':'alireza','family':'mohammadi','age':33}}) # this is how to update in py
people.remove({'name':'mehdi'}) # for delete a record 

client.close() # close connection 
