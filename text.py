
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

# list_fields = dict()
# custom_fields = ['ayush']
# list_fields['list_fields'] = None
# new_fields = list_fields['list_fields'] + custom_fields
# print(new_fields)

# TRAN-3978-3979-3980-3981

# format_date_time_am_pm(convert_to_tz(parse_datetime(_['field_value']), timezone))

# import datetime

# def format_extras(extras):
#     for item in extras:
#             try:
#                 formatted_datetime = format_date_time_am_pm(convert_to_tz(parse_datetime(item['value']), timezone))
#                 # parsed_datetime = datetime.datetime.strptime(item['value'], "%Y-%m-%dT%H:%M")
#                 # formatted_datetime = parsed_datetime.strftime("%Y-%m-%d %H:%M")
#                 item['value'] = formatted_datetime
#             except ValueError:
#                 pass
#     return extras

# data = [
#     {
#         "name": "Work Order No",
#         "value": "WO7348"
#     },
#     {
#         "name": "Driver Name",
#         "value": "ayush"
#     },
#     {
#         "name": "t10",
#         "value": "879hyuj"
#     },
#     {
#         "name": "t8",
#         "value": "asiidu793448"
#     },
#     {
#         "name": "testDate",
#         "value": "2023-10-13"
#     },
#     {
#         "name": "date",
#         "value": "2023-10-13T14:49"
#     }
# ]

# formatted_data = format_extras(data)
# print(formatted_data)

#   git branch -m TRAN-3987 TRAN-3987-3988-3989

"""
If the default bank is Bank account type then on selection of “IMPS, NEFT, RTGS, Cheque, UPI“ we will prefill the bank,
call api with is_tenant = False ,is_account = True ,remove_cash_account = True

If user selects cash then we will not prefill anything
If the default bank is Cash account type then on selection of “Cash“ we will prefill the bank
call api with is_tenant = Fale ,is_account = True ,remove_cash_account = False, is_cash_account = True

If user selects bank, then we will prefill tenant bank
call api with is_tenant = True ,is_account = True ,remove_cash_account = True
"""

#    today i worked migrateion script for employess count for salary and did some changers in 
#        salary add and edit api ,



# def scroll_pagination(obj,next_cursor=None,date=None,query_filters=None,search=None,
#                       field_to_search={},fields_to_get=[],date_field=[],due_date_field=[]):
#     num_of_records = 20
#     if next_cursor:
#         if date:
#             last_date ,created_at = base64decode(next_cursor).split(';')
#             date_filter = Q(**{ f'{date}__lte': last_date}) & Q(created_at__lte=created_at)
#             obj = obj.filter(date_filter)
#         else:
#             created_at = base64decode(next_cursor)
#             obj = obj.filter(created_at__lte=created_at)

#     if query_filters != "":
#         obj = filter_table(obj, query_filters, datetime.now().date(),date_field,due_date_field)

#     if search:
#         or_condition = Q()
#         for key, value in field_to_search.items():
#             or_condition.add(Q(**{ f'{key}__icontains': value}), Q.OR)
#             obj = obj.filter(or_condition)

#     try:
#         if date:
#             obj = obj.order_by(f'-{date}', '-created_at')
#         else:
#             obj = obj.order_by('-created_at')
#         obj = obj.values(*(fields_to_get))[0:num_of_records+1]
#     except IndexError:
#         obj = []

#     next_cursor = ""
#     try:
#         if len(obj) == num_of_records+1:
#             last_obj = obj[-1]
#             if date:
#                 next_cursor = base64encode(f"{str(last_obj[f'{date}'])};{str(last_obj['created_at'])}")
#             else:
#                 next_cursor = base64encode(f"{str(last_obj['created_at'])}")
#             obj = obj[:num_of_records]
#     except IndexError:
#         pass

#     return obj, next_cursor










# filter_set = {
#     "bill_number": {
#         "field": "bill_number", "display": "Bill Number", 
#         "type": "value", "values": ["Bill Number 1", "Bill Number 2"]
#     },
#     "vendor__display_name": {
#         "field": "vendor__display_name", "display": "Vendor", 
#         "type": "value", "values": ["Vendor 1", "Vendor 2"]
#     },    
#     "due_date": {
#         "field": "due_date", "display": "Date",
#         "type": "value", "values": ["Within 15 days","Within 15 to 30 days",
#                                     "Within 30 to 45 days","Overdue",]
#     },
#     "bill_date": {
#         "field": "bill_date", "display": "Bill Date",
#         "type": "value", "values": ["In 15 days", "15-30 Days", 
#                                     "30-45 days", "Over 45 Days"]
#     },
#     "new_payment_status": {
#         "field": "new_payment_status", "display": "Payment Status",
#         "type": "value", "values": ["Paid", "UnPaid", 
#                                      "Partial Paid"]}
# }




# def filter_table(queryset, _filter_set, todaydate):

#     if isinstance(_filter_set, str) and _filter_set == '[]':
#         return queryset

#     if not _filter_set:
#         return queryset
    
#     try:
#         _filter_set = json.loads(_filter_set)
#         for _ in _filter_set:
#             filter_set[_['key']]
#     except:
#         raise InvalidDataError
    
#     conditions = Q()
#     kwargs = {}
#     for _ in _filter_set:
#         if _['key'] == 'due_date':
#             if "Within 15 days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__range": [todaydate, todaydate + timedelta(days=15)]}), Q.AND)
#             if "Within 15 to 30 days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__range": [todaydate + timedelta(days=15), 
#                     todaydate + timedelta(days=30)]}), Q.AND)
#             if "Within 30 to 45 days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__range": [todaydate + timedelta(days=30), 
#                     todaydate + timedelta(days=45)]}), Q.AND)
#             if "Overdue" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__lte": todaydate}), Q.AND) 
#         elif _['key'] == 'bill_date':
#             if "In 15 days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__range": [todaydate - timedelta(days=15), todaydate]}), Q.AND)
#             if "15-30 Days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__range": [todaydate - timedelta(days=30), 
#                     todaydate - timedelta(days=15)]}), Q.AND)
#             if "30-45 days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__range": [todaydate - timedelta(days=45), 
#                     todaydate - timedelta(days=30)]}), Q.AND)
#             if "Over 45 Days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__lt": todaydate - timedelta(days=45)}), Q.AND)
#         else:
#             kwargs[f"{_['key']}__in"] = _['values']
#             conditions.add(Q(**{f"{_['key']}__in":  _['values']}), Q.AND)

#     try:
#         q = queryset.filter(conditions)
#     except :
#         raise InvalidDataError
#     return q


# import json
# from datetime import timedelta, datetime
# from django.db.models import Q
# from transportsimple.base.utils import base64decode, base64encode
# from transportsimple.base.exception_handler import InvalidDataError


# def filter_table(queryset, _filter_set,list_of_filters):

#     if isinstance(_filter_set, str) and _filter_set == '[]':
#         return queryset

#     if not _filter_set:
#         return queryset
    
#     try:
#         _filter_set = json.loads(_filter_set)
#         for _ in _filter_set:
#             if _['key'] in list_of_filters:
#                 pass
#             else:
#                 raise InvalidDataError
#     except:
#         raise InvalidDataError
    
#     conditions = Q()
#     for _ in _filter_set:
#         conditions.add(Q(**{f"{_['key']}__in":  _['values']}), Q.AND)

#     try:
#         q = queryset.filter(conditions)
#     except :
#         raise InvalidDataError
#     return q


# def filter_table(queryset, _filter_set, list_of_filters, added_filters):

#     if isinstance(_filter_set, str) and _filter_set == '[]':
#         return queryset
    
#     if not _filter_set:
#         return queryset
    
#     try:
#         _filter_set = json.loads(_filter_set)
#         for _ in _filter_set:
#             if _['key'] in list_of_filters:
#                 pass
#             else:
#                 raise InvalidDataError
#     except:
#         raise InvalidDataError
    
#     conditions = Q()
#     if added_filters is None:
#         for _ in _filter_set:
#             conditions.add(Q(**{f"{_['key']}__in":  _['values']}), Q.AND)
#     else:
#         conditions = added_filters(_filter_set,conditions)

#     try:
#         q = queryset.filter(conditions)
#     except :
#         raise InvalidDataError
#     return q


# class Set_Filters:

#     def __init__(self,obj):
#         self.obj = obj
#         self.filters = {}
    

#     def create(self,items):
#         filters = dict()
#         for key, display in items.items():
#             list_of_value = []
#             for _ in self.obj:
#                 if _[f'{key}'] and _[f'{key}'] not in list_of_value:
#                     list_of_value.append(_[f'{key}'])
#             filters[f'{key}']  = {"field": f'{key}', "display": f'{display}',
#                                     "type": "value", "values": list_of_value}
#         self.filters = filters
#         return self.filters
    

#     def add_custom_filters(self,custom_filters):
#         self.filters = {**self.filters, **custom_filters}
#         return self.filters

# class Scroll_Pagination:

#     def __init__(self,obj):
#         self.obj = obj
#         self.date = None
#         self.num_of_records = 20


#     def next_cursor(self,next_cursor=None,date=None):
#         self.date = date
#         if next_cursor:
#             if date:
#                 last_date ,created_at = base64decode(next_cursor).split(';')
#                 date_filter = Q(**{ f'{date}__lte': last_date}) & Q(created_at__lte=created_at)
#                 self.obj = self.obj.filter(date_filter)
#             else:
#                 created_at = base64decode(next_cursor)
#                 self.obj = self.obj.filter(created_at__lte=created_at)
#         return self.obj


#     def filter_obj(self,query_filters=None,list_of_filters=[]):
#         if query_filters != "":
#             self.obj = filter_table(self.obj, query_filters,list_of_filters)
#         return self.obj
    

#     def filter_obj(self,query_filters=None,list_of_filters=[],added_filters=None):
#         if query_filters != "":
#             self.obj = filter_table(self.obj, query_filters, list_of_filters, added_filters)
#         return self.obj


#     def search_obj(self,search=None,field_to_search={}):
#         if search:
#             or_condition = Q()
#             for key, value in field_to_search.items():
#                 or_condition.add(Q(**{ f'{key}__icontains': value}), Q.OR)
#                 self.obj = self.obj.filter(or_condition)
#         return self.obj
    

#     def over_write_obj(self, new_obj):
#         self.obj = new_obj


#     def get_values(self,fields_to_get=[]):
#         num_of_records = self.num_of_records
#         date = self.date
#         try:
#             if date:
#                 self.obj = self.obj.order_by(f'-{date}', '-created_at')
#             else:
#                 self.obj = self.obj.order_by('-created_at')
#             self.obj = self.obj.values(*(fields_to_get))[0:num_of_records+1]
#         except IndexError:
#             self.obj = []
#         return self.obj


#     def get_next_cursor(self):
#         num_of_records = self.num_of_records
#         next_cursor = ""
#         try:
#             if len(self.obj) == num_of_records+1:
#                 last_obj = self.obj[-1]
#                 if self.date:
#                     next_cursor = base64encode(f"{str(last_obj[f'{self.date}'])};{str(last_obj['created_at'])}")
#                 else:
#                     next_cursor = base64encode(f"{str(last_obj['created_at'])}")
#                 obj = obj[:num_of_records]
#         except IndexError:
#             pass
#         return next_cursor
    
# {
#             "id": "64423c2f-acbc-4aeb-b512-b7d8e062a828",
#             "party": {
#                 "id": "8fdc87e9-e935-4ab7-8bf2-2e0995753b34",
#                 "display_name": "p333"
#             },
#             "invoice_number": "PI2023002",
#             "due_date": "2023-11-02",
#             "total_amount": 25.0,
#             "balance": 25.0,
#             "created_at": "2023-11-02",
#             "invoice_date": "2023-11-02",
#             "due_amount": 25.0,
#             "has_invoice": false,
#             "status": {
#                 "index": 1,
#                 "label": "Finalise"
#             }
#         }

        # fields = ("id", "reg_number", "owner", "owner_type", "brand",
        #           "vehicle_type", "engine_number", "assign_driver",
        #           "chassis_number", "gps_imei_no", "odo_reading",
        #           "odo_reading_date", "remark", "date_of_purchase", "reg_date",
        #           "purchase_value", "deprecated_value", "deprecated_date",
        #           "is_active_status", "is_archived_status", "warranty",
        #           "finance", "insurance", "trip_count", "loop_count",
        #           "trip_revenue", "documents", "tyres", "total_maintenance",
        #           "unassigned", "reminder_list", "trip_summary", "market_owner",
        #           "mechanic_summary", 'total_fuel', "bills", "emi_amount",
        #           "is_market_vehicle", "emi_start_date", "mobile", "mobile_country_code",
        #           "emi_remind_me", "emi_reminder_frequency", "emi_last_date",
        #           "fuel_reading", "average_cost_per_unit", "total_fuel_cost",
        #           "fuel_reading_date", "market_driver")

        # fields = ("id", "reg_number", "brand", "documents", "market_owner",
        #         "vehicle_type", "assign_driver", "is_market_vehicle", "mobile",
        #         "mobile_country_code", "remark", "emi_amount", "owner", "owner_type",
        #         "emi_reminder_frequency", "emi_last_date", "emi_start_date", "market_driver")

        # VehicleAllDetailsSerializer(ModelSerializer)

#         @choices
# class ExpenseStatus:
#     class Meta:
#         Unpaid = [1, 'Pay later'] 
#         Partially_Paid = [2, 'Partially Paid']
#         Paid = [3, 'Paid']


# from datetime import datetime
# print(datetime.now().date())
# aa = datetime.strptime(str(datetime.now().date()), "%Y-%m-%d").strftime("%d-%m-%Y") 
# print(aa)

# def create_annexure(_data):
#                      'from-to': f"{each['trip']['from_loc']} - "
#                                 f"{each['trip']['to_loc']}",

# 'from-to':shorten_from_to(each['trip']['from_loc'],each['trip']['to_loc']),

        # def shorten_from_to(from_loc,to_loc):
        #     loc1 = from_loc.split(", ") if len(from_loc.split(", ")) != 1 \
        #         else from_loc.split(" - ")
        #     loc2 = to_loc.split(", ") if len(to_loc.split(", ")) != 1 \
        #         else to_loc.split(" - ")

        #     loc1.reverse()
        #     loc2.reverse()
        #     i = 0
        #     while i < min(len(loc1), len(loc2)):
        #         if loc1[i] == loc2[i]:
        #             loc1.pop(i)
        #             loc2.pop(i)
        #         else:
        #             i += 1
        #     loc1.reverse()
        #     return ", ".join(loc1) + " - " + to_loc if len(from_loc.split(", ")) != 1 \
        #         else " - ".join(loc1) + ", " + to_loc

        # def employee_documents_get(request, employee_uuid):

# TRAN-4240
# def get_today_date(tz_str):   
#     now_local = datetime.now(tz=pytz.timezone(tz_str)) - timedelta(hours=27)
#     today_utc = now_local.astimezone(pytz.utc).replace(hour=0, minute=0, second=0, microsecond=0)
#     return today_utc.date()


# "can_comment": true,
# v1/quotation/
# v1/party/portal/access/

#     def has_portal_access(self):
#         if hasattr(self, 'partyclientportal'):
#             return self.partyclientportal.is_disabled
#         return False


# git branch -m TRAN-4240 TRAN-4240-4230

# v1/operation/vendor_credit/
# v1/operation/payment_made/




# filter_set = {
#    "clearance_date": {
#         "field": "clearance_date", "display": "Clearance Date",
#         "type": "value", "values": ["In 15 days", "15-30 Days", 
#                                     "30-45 days", "Over 45 Days"]
#     },
#     "payment_settlement__date_of_payment": {
#         "field": "payment_settlement__date_of_payment", "display": "Payment Date",
#         "type": "value", "values": ["In 15 days", "15-30 Days", 
#                                     "30-45 days", "Over 45 Days"]
#     },"cheque_date": {
#         "field": "cheque_date", "display": "pc Date",
#         "type": "value", "values": ["In 15 days", "15-30 Days", 
#                                     "30-45 days", "Over 45 Days"]
#     }
# }


# def custom_filters(_filter_set):
#     conditions = Q()
#     todaydate = datetime.now().date()
#     for _ in _filter_set:
#         if _['key'] in ['payment_settlement__date_of_payment',
#                         'cheque_date', 'clearance_date']:
#             if "In 15 days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__range": [todaydate - timedelta(days=15), todaydate]}), Q.AND)
#             if "15-30 Days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__range": [todaydate - timedelta(days=30), 
#                     todaydate - timedelta(days=15)]}), Q.AND)
#             if "30-45 days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__range": [todaydate - timedelta(days=45), 
#                     todaydate - timedelta(days=30)]}), Q.AND)
#             if "Over 45 Days" in _['values']:
#                 conditions.add(Q(**{f"{_['key']}__lt": todaydate - timedelta(days=45)}), Q.AND)
#         else:
#             conditions.add(Q(**{f"{_['key']}__in":  _['values']}), Q.AND)

#     return conditions


# @handle_exceptions
# def payment_cheque_filters(request):
#     tenant = request.tenant
#     pc_obj = PaymentModeCheque.objects.filter(tenant=tenant, is_active=True)
    
#     pc = Set_Filters(pc_obj)
#     items = [{'key':'party__display_name','display':'Party Name'},
#              {'key':'cheque_status__label','display':'Status'}]
#     filters = pc.create(items,'cheque_date')
#     filters = pc.add_custom_filters(filter_set)
#     return get(filters.values())
    

# @handle_exceptions
# def payment_cheque_list(request):
#     num_of_records = 20
#     tenant = request.tenant
#     params = request.query_params
#     start_date = params.get('start_date', "")
#     end_date = params.get('end_date', "")
#     search = params.get('search', "")
#     query_filters = params.get('filters', "")
#     next_cursor = params.get('next_cursor', "")
#     status = params.get('status', '0')

#     if status not in ['0', '1', '2', '3', '4']:
#         raise InvalidDataError

#     pc_obj = PaymentModeCheque.objects.filter(
#         tenant=tenant, is_active=True, cheque_date__range=[start_date, end_date])
    
#     if status in ['1', '2', '3', '4']:
#         status_otp = {'1': 'Cancelled', '2': 'Cleared',
#                        '3': 'Uncleared', '4': 'Post-Dated Cheque',}
#         pc_obj = pc_obj.filter(cheque_status__label=status_otp['status'])
    
#     pc = Scroll_Pagination(pc_obj,num_of_records)
#     pc.next_cursor(next_cursor,"cheque_date")

#     list_of_filters = ['party__display_name', 'clearance_date',
#                        'payment_settlement__date_of_payment', 'cheque_date']
#     pc.filter_obj(query_filters,list_of_filters,custom_filters)

#     field_to_search = ['party__display_name','payment_settlement__payment_number'
#                        'cheque_no', 'cheque_date', 'account__name']
#     pc.search_obj(search,field_to_search)

#     fields_to_get = ['id', 'cheque_date', 'cheque_no', 'payment_settlement__payment_number',
#                       'party_id', 'party__display_name', 'payment_settlement__date_of_payment',
#                       'payment_settlement_id','cheque_status__label', 'account__name',
#                         'account_id', 'clearance_date', 'amount_paid']
#     pc_obj = pc.get_values(fields_to_get)

#     new_pc_obj = []
#     for _ in pc_obj:
#         new_pc_obj.append({
#             "id": _['id'],
#             "cheque_date": _['cheque_date'],
#             "cheque_no": _['cheque_no'],
#             "payment_settlement": _['payment_settlement_id'],
#             "cheque_status": _['cheque_status__label'],
#             "account": {
#                 "id": _['account_id'],
#                 "label": _['account__name'],
#             },
#             "clearance_date": _['clearance_date'],
#             "amount_paid": _['amount_paid'],
#             "payment_no": _['payment_settlement__payment_number'],
#             "party": _['party__display_name'],
#             "party_id": _['party_id'],
#             "payment_date": _['payment_settlement__date_of_payment'],
#         })

#     return  get({'pc':new_pc_obj, 'next_cursor' : pc.get_next_cursor()})



# import re

# def remove_dates_from_string(input_string):
#     # Define a regular expression pattern to match dates in the format YYYY-MM-D
    
#     # Use re.sub to replace all occurrences of the date pattern with an empty string
#     result_string = re.sub(r'\b\d{4}-\d{2}-\d{2}\b', '', input_string)
    
#     return result_string

# # Example usage
# vp_due = "Vp (yu) is due on 2023-11-28,"
# c_test_due = "C-Test (INV2023050) is due on 2023-11-28,"
# dl_expiring = "Reminder: Yesh has Driving License (DL908) expiring on 2023-11-28,"
# doc1_expiring = "Reminder: Yesh has Doc 1 (14568) expiring on 2023-11-28,"
# fitness_expiring = "Reminder: Sample Display has Fitness (1234) expiring on 2023-11-28,"

# vp_due_cleaned = remove_dates_from_string(vp_due)
# c_test_due_cleaned = remove_dates_from_string(c_test_due)
# dl_expiring_cleaned = remove_dates_from_string(dl_expiring)
# doc1_expiring_cleaned = remove_dates_from_string(doc1_expiring)
# fitness_expiring_cleaned = remove_dates_from_string(fitness_expiring)

# # Print the cleaned strings
# print(vp_due_cleaned)
# print(c_test_due_cleaned)
# print(dl_expiring_cleaned)
# print(doc1_expiring_cleaned)
# print(fitness_expiring_cleaned)

# from django.db.models import Q, F, Case, When, Value, CharField, \
#     DateTimeField
# from django.db.models.functions import Concat, Cast
# from django.utils.dateparse import parse_datetime
    
#     i_obj = i_obj.annotate(
#         invoice_datetime=
#             Cast(Concat(F('invoice_date'), Value(' '), F('created_at__time')), 
#             output_field=DateTimeField()))

#     if next_cursor:
#         date = base64decode(next_cursor)
#         i_obj = i_obj.filter(invoice_datetime__lte=parse_datetime(date))


# label': instance.get_payment_status_display() \
#                 if instance.get_payment_status_display() != "Unpaid" else "Pay Later"




# from transportsimple.base.utils import format_duration
# from transportsimple.base.utils import format_date
# def format_extras(self, extras):

# from datetime import datetime, timedelta


# temp_first_date = datetime(2023, 10, 15)
# last_date = datetime(2024, 1, 15)
# emi_dates = []

# while temp_first_date <= last_date:
#     emi_dates.append(temp_first_date.date())
#     temp_first_date = temp_first_date + timedelta(days=30)  # Assuming each month has 30 days

# print(emi_dates)

#  {"id":"5e6d8449-8c94-4111-992a-a01ebdad8a87","key":"employee-designation","label":"Driver & Helper"},
#  {"id":"152fd076-2244-4eae-85e1-794d59d5d329","key":"employee-designation","label":"Driver & Helper"},
#  {"id":"aed434e8-ddde-4e25-9c44-a94df13ae086","key":"employee-designation","label":"Accounts"},
#  {"id":"7bd4406a-b4b4-40ef-9ba4-7adb90dfbe66","key":"employee-designation","label":"Others"},
#  {"id":"092553a2-6021-4597-b550-a5bb6bf6403e","key":"employee-designation","label":"Others"},
#  {"id":"026bb22a-0979-42cd-836b-101f573f3656","key":"employee-designation","label":"Others"},
#  {"id":"9e0926f1-e286-4d4b-a26c-c352b58ccd0a","key":"employee-designation","label":"Manager"},
#  {"id":"1669edac-8324-4c42-9da2-c469bac66114","key":"employee-designation","label":"Others"},
#  {"id":"c8dea449-7b0c-4c6a-84a8-c6031eac7010","key":"employee-designation","label":"Others"},

# {"id":"5e6d8449-8c94-4111-992a-a01ebdad8a87","key":"employee-designation","label":"Driver"},
#  {"id":"152fd076-2244-4eae-85e1-794d59d5d329","key":"employee-designation","label":"Helper"},
#  {"id":"aed434e8-ddde-4e25-9c44-a94df13ae086","key":"employee-designation","label":"Accountant"},
#  {"id":"7bd4406a-b4b4-40ef-9ba4-7adb90dfbe66","key":"employee-designation","label":"Managing Partner"},
#  {"id":"092553a2-6021-4597-b550-a5bb6bf6403e","key":"employee-designation","label":"Partner"},
#  {"id":"026bb22a-0979-42cd-836b-101f573f3656","key":"employee-designation","label":"Director"},
#  {"id":"9e0926f1-e286-4d4b-a26c-c352b58ccd0a","key":"employee-designation","label":"Manager"},
#  {"id":"1669edac-8324-4c42-9da2-c469bac66114","key":"employee-designation","label":"Associate"},
#  {"id":"c8dea449-7b0c-4c6a-84a8-c6031eac7010","key":"employee-designation","label":"Others"},



# Define the number of hexagons
# num_hexagons = 96
# # Create an empty array to store led numbers
# hexagons = [[0 for _ in range(20)] for _ in range(num_hexagons)]
# # Alternatively, directly initialize each hexagon with LED numbers
# hexagons = [list(range(i * 20, i * 20 + 20)) for i in range(num_hexagons)]
# print(hexagons)



# import numpy as np
# import time

# def find_coordinates_for_box_number(box_number, width, height):
#     box_number -= 1  # Subtracting 1 to convert from box number to 0-based index
#     x = box_number // height
#     y = box_number % height
#     return x, y

# def generate_circular_wave_box_numbers(center_box_number, matrix_width, matrix_height, delay):
#     center_x, center_y = find_coordinates_for_box_number(center_box_number, matrix_width, matrix_height)
    
#     all_waves = []

#     # First wave
#     first_wave_box_numbers = set()
#     for angle in range(360):
#         x = int(center_x + np.cos(np.radians(angle)))
#         y = int(center_y + np.sin(np.radians(angle)))

#         if 0 <= x < matrix_width and 0 <= y < matrix_height:
#             box_number = x * matrix_height + y + 1
#             first_wave_box_numbers.add(box_number)
#             time.sleep(delay / 1000)  # Convert delay from ms to seconds
#     all_waves.append(list(first_wave_box_numbers))

#     used_box_numbers = set(first_wave_box_numbers)

#     # Subsequent waves
#     for radius in range(1, min(matrix_width, matrix_height)):
#         wave_box_numbers = set()  # Using a set to avoid repetition
#         for angle in range(360):
#             x = int(center_x + radius * np.cos(np.radians(angle)))
#             y = int(center_y + radius * np.sin(np.radians(angle)))
            
#             if 0 <= x < matrix_width and 0 <= y < matrix_height:
#                 box_number = x * matrix_height + y + 1  # Adding 1 to start box numbers from 1
#                 if box_number not in used_box_numbers:
#                     wave_box_numbers.add(box_number)
#                     used_box_numbers.add(box_number)
#                     time.sleep(delay / 1000)  # Convert delay from ms to seconds
#         all_waves.append(list(wave_box_numbers))

#     return all_waves

# # Example usage:
# desired_box_number = 4  # Replace with the box number you want to use as the center
# matrix_width = 16
# matrix_height = 16
# delay_ms = 5

# resulting_waves = generate_circular_wave_box_numbers(
#     desired_box_number, matrix_width, matrix_height, delay_ms
# )

# for i, wave in enumerate(resulting_waves):
#     print(f"Wave {i + 1} box numbers:", wave)


# full_name = "ayush gurjar uk"
# first_name, last_name = full_name.split(" ")[0], " ".join((full_name.split(" ")[1:]))
# print(first_name, last_name)
# number = 12.51
# print(f'{number:.0f}')