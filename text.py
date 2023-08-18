
# async def update_tender_milestones(db, tender_number, data):
#     coll = await db['tenders'].find_one({'tender_number': tender_number})
    
#     if coll:
#         milestones = coll.get('milestones', [])
#         new_milestone = {'milestone_number': len(milestones) + 1, 'data': data, 'time_log': datetime.datetime.now()}
#         milestones.append(new_milestone)
#         await db['tenders'].update_one({'tender_number': tender_number}, {"$set": {"milestones": milestones}})
#     else:
#         new_milestone = {'milestone_number': 1, 'data': data, 'time_log': datetime.datetime.now()}
#         await db['tenders'].insert_one({'tender_number': tender_number, 'milestones': [new_milestone]})
# {"1":{'data': {'data': 'data'},
#         'time_log': datetime(2023, 8, 7, 12, 58, 37, 946000)}},
# "2": {'data': {'data': 'data'},
#         'time_log': datetime(2023, 8, 7, 12, 58, 37, 946000)}}
# }
# res = "783246"
# a = 9283467
# print(a if res else None)
# db['bdp_request_logs'].insert_one(log_entry)

# class BDPRequestlogger:
#     def bdp_request_logs(self,sub,data,res=None,err=None):
#         print(sub,data,res,err)
#         return [1,"success"]


# @handle_exceptions
# def put_tender_status(request,tender_number,tender_status):
#     # url = f"https://bdp.transportsimple.app/tenders/status/{tender_number}/{tender_status}/"
#     url = f"http://localhost:3000/tenders/status/{tender_number}/{tender_status}/"
#     params = {"token": Token}
#     try:
#         res = requests.put(url,params=params)
#         if res.status_code == 200:
#             res_ = json.loads(res.text)
#             return get(res_, SUCCESS)
#     except:
#         pass


# @handle_exceptions
# def put_milestone_status(request,tender_number):
#     data=request.data
 
    # data = {
        # # "feature" : "BOTH", # Always BOTH
        # # "dray_Scac" : "PRIM", # Always PRIM
        # "empty_Indicator" : "Empty", # E - Empty/F - Full
        # "carrier_Scac_Code" : "HLCU", # carrierScacCode
        # "container_Number" : "TBNU01", # containerNumber PRIME LINK will enter
        # "booking_Number" : "3645546646", # bookingNumber
        # "shipment_Number" : "0042239933", # shipmentReferenceNumber
        # "container_Pool_Id" : "", # containerNumber -- doubt
        # "container_Type_Code" : "4010", # containerType
        # "tender_Request_Number" : 23071800001, # tenderRequestNumber
        # "shipper_Name" : "", # Not Required
        # "milestone" : "Full Delivery", # AF - Empty Pickup / X8 - Empty Drop /CP - Full Pickup /I1 - Full Delivery
        # "milestone_Timestamp" : "2023-Aug-05 10:25:00",
        # "milestone_Time" : "10:25",
        # "milestone_Location" : "DP World" 




# sen =  {"AF":[1,2,3,4,5],"X8":[6,7,8,9],"CP":[11,23,25],"I1":[44,55,66]}
# data = []
# for i in sen:
    # print(sen[i][-1])
    # data.append({f"{i}":sen[i][-1]})
    # for j in  sen[i]:
    #     print(i,j)

# print(data)
# sen["AF"].append(6)
# print(sen)

# s=[1,2,3,4,5,6]
# j="".join(map(str,s))
# print(s[::-1])



import operator

import numpy


nums = [1,2,3,4]
k=3

# sen = {}
# for ch in nums:
#     sen.setdefault(ch,0)
#     sen[ch]+=1
# lis = []
# sen = dict(sorted(sen.items(), key=operator.itemgetter(1),reverse=True))
# for key in sen:
#     lis.append(key)
#     if len(lis)>=k:
#         break

# print(lis)
lis = []
for k in range(len(nums)):
    lis.append(numpy.prod((nums[:k]+nums[k+1:])))
print(lis)
