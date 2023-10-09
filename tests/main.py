import pymongo
from pprint import pprint 
import datetime
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


    # db=client.i3ms
    # coll = db.users
    # data = coll.find()
    # for i in data:
    #     print(i)



    # page = 2
    # limit = 5
    # tenders =  coll.find().sort([("_id", pymongo.DESCENDING)]).skip((page - 1) * limit).limit(limit)
    # for i in tenders:
    #     print(i)


    db=client['bdpdb']
    #db['tenders'].insert_one({'tender_number': 23062200050, 'tender_status': 'ORIGINAL', 'created_at': datetime.datetime.now(), 'requested': True})
    # coll = db['tenders'].find()
    # print(coll)
    # data = {"milestones":[]} 
    # colla = db['tenders'].update_one({'tender_number': '23062200041'}, {"$set": data})
    # tn = 23062200050
    
    # coll = db['tenders'].find_one({'tender_number':tn })

    # data = {"data":"data","time_log":datetime.datetime.now()}
    # milestone_type = "I1"
    # if "milestones" in coll:
    #     sen = coll['milestones']
    #     new_data = sen[milestone_type]
    #     new_data.append(data)
    #     sen[milestone_type]=new_data
    #     db['tenders'].update_one({'tender_number': tn}, {"$set": {"milestones":sen}})                                   
    # else:
    #     sen =  {"AF":[],"X8":[],"CP":[],"I1":[]}
    #     new_data = sen[milestone_type]
    #     new_data.append(data)
    #     sen[milestone_type]=new_data
    #     db['tenders'].update_one({'tender_number': tn}, {"$set": {"milestones":sen}})

    # sen = coll['milestones'] if "milestones" in coll and coll['milestones'] != None else {"AF":[],"X8":[],"CP":[],"I1":[]} 
    # sen[milestone_type].append(data)
    # db['tenders'].update_one({'tender_number': tn}, {"$set": {"milestones":sen}})

    # coll = db['tenders'].find_one({'tender_number':tn })
    # old_data = coll['milestones']
    # pprint(coll)

#// AF - Empty Pickup / X8 - Empty Drop /CP - Full Pickup /I1 - Full Delivery
# data ={"data":"milestone data",
#        "time":"datetime"}
# type = "AF"
# milestones = {"AF":[data],
#               "X8":[data],
#               "CP":[data],
#               "I1":[data]}

# print(milestones[type])insert_one


# 23062200040
data = {}
tender = db['tender_details'].find_one({"tenderRequestNumber":23062200040})

codes = {'C092': 'CP_000530', 'C093': 'CP_000530', 'C094': 'CP_000530', 'CC12': 'CP_000538',
          'CC13': 'CP_000538', 'CC14': 'CP_000538', 'GH10': 'CP_000540', 'GH11': 'CP_000540',
            'GH12': 'CP_000540', 'C095': 'CP_000554', 'C096': 'CP_000554', 'C097': 'CP_000554',
              'GF61': 'CP_000556', 'GF62': 'CP_000556', 'GF63': 'CP_000556', 'C541': 'CP_000558',
                'C542': 'CP_000558', 'C543': 'CP_000558', 'CD14': 'CP_000560', 'CD15': 'CP_000560',
                  'CD16': 'CP_000560'}

code = tender['originAddress']['code'].split("_")

data['container_Pool_Id'] = codes[code[2]]
data['milestone_Location'] = tender['originAddress']['name']  #  ????
data["carrier_Scac_Code"] = tender['carrierScacCode']
data['shipment_Number'] = tender['shipmentReferenceNumber'] #-u
data["container_Number"] = tender['containerNumber'] #--u
data["booking_Number"] = tender['bookingNumber']
data['container_Type_Code'] = tender['containerType']
# data['tender_Request_Number'] = tender_number
new = data['milestone_Time'].split(" ")[1].split(":")
data['milestone_Time'] =  new[0]+":"+new[1]

# pprint(data)
# request.query_params.get('next_cursor')
# is_account = True if params.get('is_account', False) == "True" else False