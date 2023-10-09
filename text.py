
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



# import operator

# import numpy


# nums = [1,2,3,4]
# k=3

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
# lis = []
# for k in range(len(nums)):
#     lis.append(numpy.prod((nums[:k]+nums[k+1:])))
# print(lis)

# CONT = [11, "Containers"]

# import uuid
# from uuid import UUID

# myuuid = uuid.uuid4()

# print('Your UUID is: ' + str(myuuid))
# __ = dict()
# extra_paths= []
# extra_paths.append({'location': __['location'],
#                                     #'point_type':{'id' : __['new_point_type__id'],'label' : __['new_point_type__label']}
#                                     })


# X-Client-Id     9d73d97e-b05e-4f33-a050-d035e8c1cb71


# JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMjQyNjczZTMtODEwNi00NWI5LTkxNDktYjI2YmIxNjYwYmZjIiwidXNlcm5hbWUiOiJheXVzaEBnbWFpbC5jb20iLCJleHAiOjE2OTUzNTg4NDEsImVtYWlsIjoiYXl1c2hAZ21haWwuY29tIn0.GnXoRGiJ6UeiR9NFPBYJqG5EXWhJ8gbvL6oZOGKfFdQ



# Create Work Order, Work Order Detail GET, Work Order Detail in Trip,
# Quotation Create, Quotation GET, Quotation Update Path, Quoation Work Order Detail
# Add Trip, Get Path, Trip List V2, Get Routes, Update Path



# from transportsimple.revenue.tasks import trip_update_status


# trip_update_status.delay(trip_obj.id)


        ############ check DocumentName is created or not ##############

        # doc_name = DocumentName.objects.all().count()
        # print(doc_name)

        ################ get doc id ###################
        # ids = Document.objects.filter(document_belongs=DocumentBelongsTo.DRIVER_APP_TRIP).values('id')
        # for id in ids:
        #     print(id)


        ################ create fake doc #############################
        # import random
        # import string
        # letters = string.ascii_lowercase
        # docs = []
        # for _ in range(10):
        #     docs.append(Document(
        #         tenant_id = "9d73d97e-b05e-4f33-a050-d035e8c1cb71",
        #         s3_key = "fake key",
        #         file_name = "fake name",
        #         document_belongs=DocumentBelongsTo.DRIVER_APP_TRIP,
        #         note = ''.join(random.choice(letters) for i in range(10))
        #     ))
        # Document.objects.bulk_create(docs)

# "document" : {"document": "", "note": ""}

#   "result": ,
#     "message": "success",
#     "status": "success"
# }


# set_preferred_payment_mode_by_party_bank.delay(party_id, bank_id)
# set_preferred_payment_mode_by_party_account.delay(party_id, acc_id)
#     bank_id = request_data['bank_account']
#     party_id = request_data['customer']

# from transportsimple.revenue.tasks import set_preferred_payment_mode_by_party_bank, \
#                             
# from transportsimple.revenue.tasks import set_default_bank_in_tenant_by_account, set_default_bank_in_tenant


    # acc_id = request_data['payment_mode']
    # party_id = request_data['party']

    # if is_export == 'true':
    #     export_get_fields = ['start_date__date', 'c_vehicle__reg_number',
    #         'a_vtype', 'trip_id', 'customer__display_name', 'a_status']
    #     try:
    #         trips = trips. \
    #             order_by('-start_date', '-created_at'). \
    #             values(*export_get_fields)
    #     except IndexError:
    #         trips = []

    #     exports = ExcelExports(
    #             tenant=tenant, filename="Trip-List", report_type="Trips")
    #     excel_data = [["Start Date", "Vehicle No", "Vehicle Type", "Trip ID",
    #             "Customer", "Status"], []]
    #     excel_rows = []
    #     for excel_entry in trips:
    #         temp = [
    #             {'merge_rows': 0, "data": str(excel_entry['start_date__date'])},
    #             {'merge_rows': 0, "data": excel_entry['c_vehicle__reg_number']},
    #             {'merge_rows': 0, "data": excel_entry['a_vtype']},
    #             {'merge_rows': 0, "data": excel_entry['trip_id']},
    #             {'merge_rows': 0, "data": excel_entry['customer__display_name']},
    #             {'merge_rows': 0, "data": excel_entry['a_status']}]
    #         excel_rows.append(temp)
    #     excel_data[1] = excel_rows
    #     return export_excel(*exports.generate_excel(data=excel_data, multi=True))


"74fe0aee-3828-4f49-ac4e-680b43393cbe"

# Quotation Screen - bank by party   /
# Vehicle payment  -  account by party  /
# Trip Expense  - account by party     
# Employee others - account by tenant   /
# Invoice - bank by party  / 
# BoS -  bank by party   /
# Payment received - ignore  
# Advance - account by party  /
# Refund - account by party   /
# Cheque Payment - ignore   
# Add Maintenance -  account by party  /
# Fueling - account by party 
# Salary - account by tenant   /
# Other Bills - account by party   /
# Petty Expense - account by tenant  /
# Pay Later - account by tenant   /
# Vendor Advance - account by party  /
