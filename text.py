
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

# today i fix date time issue in trip list than did changes in get default bank than worked Pagination Framework


import json
from datetime import timedelta, datetime
from django.db.models import Q
from transportsimple.base.utils import base64decode, base64encode
from transportsimple.base.exception_handler import InvalidDataError


def filter_table(queryset, _filter_set,list_of_filters):

    if isinstance(_filter_set, str) and _filter_set == '[]':
        return queryset

    if not _filter_set:
        return queryset
    
    try:
        _filter_set = json.loads(_filter_set)
        for _ in _filter_set:
            if _['key'] in list_of_filters:
                pass
            else:
                raise InvalidDataError
    except:
        raise InvalidDataError
    
    conditions = Q()
    for _ in _filter_set:
        conditions.add(Q(**{f"{_['key']}__in":  _['values']}), Q.AND)

    try:
        q = queryset.filter(conditions)
    except :
        raise InvalidDataError
    return q


def filter_table(queryset, _filter_set, list_of_filters, added_filters):

    if isinstance(_filter_set, str) and _filter_set == '[]':
        return queryset
    
    if not _filter_set:
        return queryset
    
    try:
        _filter_set = json.loads(_filter_set)
        for _ in _filter_set:
            if _['key'] in list_of_filters:
                pass
            else:
                raise InvalidDataError
    except:
        raise InvalidDataError
    
    conditions = Q()
    if added_filters is None:
        for _ in _filter_set:
            conditions.add(Q(**{f"{_['key']}__in":  _['values']}), Q.AND)
    else:
        conditions = added_filters(_filter_set,conditions)

    try:
        q = queryset.filter(conditions)
    except :
        raise InvalidDataError
    return q


class Set_Filters:

    def __init__(self,obj):
        self.obj = obj
        self.filters = {}
    

    def create(self,items):
        filters = dict()
        for key, display in items.items():
            list_of_value = []
            for _ in self.obj:
                if _[f'{key}'] and _[f'{key}'] not in list_of_value:
                    list_of_value.append(_[f'{key}'])
            filters[f'{key}']  = {"field": f'{key}', "display": f'{display}',
                                    "type": "value", "values": list_of_value}
        self.filters = filters
        return self.filters
    

    def add_custom_filters(self,custom_filters):
        self.filters = {**self.filters, **custom_filters}
        return self.filters

class Scroll_Pagination:

    def __init__(self,obj):
        self.obj = obj
        self.date = None
        self.num_of_records = 20


    def next_cursor(self,next_cursor=None,date=None):
        self.date = date
        if next_cursor:
            if date:
                last_date ,created_at = base64decode(next_cursor).split(';')
                date_filter = Q(**{ f'{date}__lte': last_date}) & Q(created_at__lte=created_at)
                self.obj = self.obj.filter(date_filter)
            else:
                created_at = base64decode(next_cursor)
                self.obj = self.obj.filter(created_at__lte=created_at)
        return self.obj


    def filter_obj(self,query_filters=None,list_of_filters=[]):
        if query_filters != "":
            self.obj = filter_table(self.obj, query_filters,list_of_filters)
        return self.obj
    

    def filter_obj(self,query_filters=None,list_of_filters=[],added_filters=None):
        if query_filters != "":
            self.obj = filter_table(self.obj, query_filters, list_of_filters, added_filters)
        return self.obj


    def search_obj(self,search=None,field_to_search={}):
        if search:
            or_condition = Q()
            for key, value in field_to_search.items():
                or_condition.add(Q(**{ f'{key}__icontains': value}), Q.OR)
                self.obj = self.obj.filter(or_condition)
        return self.obj
    

    def over_write_obj(self, new_obj):
        self.obj = new_obj


    def get_values(self,fields_to_get=[]):
        num_of_records = self.num_of_records
        date = self.date
        try:
            if date:
                self.obj = self.obj.order_by(f'-{date}', '-created_at')
            else:
                self.obj = self.obj.order_by('-created_at')
            self.obj = self.obj.values(*(fields_to_get))[0:num_of_records+1]
        except IndexError:
            self.obj = []
        return self.obj


    def get_next_cursor(self):
        num_of_records = self.num_of_records
        next_cursor = ""
        try:
            if len(self.obj) == num_of_records+1:
                last_obj = self.obj[-1]
                if self.date:
                    next_cursor = base64encode(f"{str(last_obj[f'{self.date}'])};{str(last_obj['created_at'])}")
                else:
                    next_cursor = base64encode(f"{str(last_obj['created_at'])}")
                obj = obj[:num_of_records]
        except IndexError:
            pass
        return next_cursor
    
