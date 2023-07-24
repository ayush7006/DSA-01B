import pymongo
if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    # db = client.ayush #
    # collection = db['mysample']
    # dict = {"name":"ayush","marks": "45"}
    # data = collection.find({'name':'ayush'}, {'name': 1, '_id': 0})
    # for i in data:
    #     print(i)
    # # print(data[0]['_id'])
 #.skip((page - 1) * limit).limit(limit)


    db=client.i3ms
    coll = db.users
    data = coll.find()
    for i in data:
        print(i)



    # page = 2
    # limit = 5
    # tenders =  coll.find().sort([("_id", pymongo.DESCENDING)]).skip((page - 1) * limit).limit(limit)
    # for i in tenders:
    #     print(i)


#     db=client['bdpdb']
#     coll = db['tender_details']
