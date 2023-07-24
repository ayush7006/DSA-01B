# import requests

# tender_number = 23062200040

# #the required first parameter of the 'get' method is the 'url':
# url = f"https://bdp.transportsimple.app/tenders/{tender_number}/"
# try:
#     x = requests.get(url)
#     if x.status_code == 200:
#         print(x.text,x.status_code)
#     else:
#         print('none',x.status_code)

# except:
#     print("none2") .replace('\\','')



# import json

# response = 
# }

# result = json.loads(response["result"])
# response["result"] = result

# print(response)


# data = {
#   "_id": "64a7f4654a8583665b8fadcd",
#   "destinationAddress": {
#     "country": "",
#     "zipCode": "",
#     "unlocCode": "AEJEA",
#     "code": "",
#     "city": "",
#     "postalCode": "",
#     "name": "PORT OF JEBEL ALI  UNITED ARAB EMIRATE",
#     "addressLine1": "",
#     "addressLine2": "",
#     "addressLine3": "",
#     "state": ""
#   },
#   "containerSeal1": "NA",
#   "containerSeal2": "",
#   "bdpRepPhone": "",
#   "originAddress": {
#     "country": "AE",
#     "zipCode": "",
#     "unlocCode": "AEJEA",
#     "code": "AE_EXDOWDXB_GF63",
#     "city": "JEBEL ALI",
#     "postalCode": "",
#     "name": "HORIZON TERMINALS",
#     "addressLine1": "JEBEL ALI LIMITED",
#     "addressLine2": "P.O. BOX 16881",
#     "addressLine3": "",
#     "state": ""
#   },
#   "placeOfRcptEstDt": "2023-06-27 00:00:00",
#   "messageType": "BookingRequest",
#   "carrierName": "OCEAN NETWORK EXPRESS PTE LTD",
#   "voyageNumber": "008E",
#   "tenderRequestNumber": 23062200040,
#   "portOfArr": "SADMM",
#   "drayName": "PRIME LINK",
#   "portOfDep": "AEJEA",
#   "specialInstruction": "",
#   "containerTemptype": "",
#   "tariffServiceCode": "PP",
#   "motCd": 1,
#   "containerReefer": "",
#   "carrierScacCode": "ONEY",
#   "customerName": "DOW ME",
#   "shipmentReferenceNumber": "0042241187",
#   "containerNumber": "TBNU01",
#   "methodOfPayment": "PP",
#   "ltstDelCutoffDt": "2023-06-26 00:00:00",
#   "containerMintemp": "",
#   "goodsAvlblShpEstDt": "2023-06-25 00:00:00",
#   "bookingNumber": "DXBD00863500",
#   "docCutoffDt": "2023-02-15 00:00:00",
#   "vesselName": "HMM RAON",
#   "cargoType": "O",
#   "drayEmail": "",
#   "containerProduct": {
#     "hazardousAdnrCode": "",
#     "hazardousMaterialDescription": "UTD.A",
#     "hazardousMaterialUnitedNationsPackingCode": "III",
#     "productPackageCode": "DR",
#     "hazardousMaterialUnitedNationsNumber": 3092,
#     "productBrandName": "DOWANOL(TM) PM GLYCOL ETHER",
#     "hazardousMaterialIndicator": "Y",
#     "hazardousMaterialFlashPointQuantity": "",
#     "hazardousMaterialFlashPointCode": "",
#     "productCode": "00092055",
#     "hazardousTunnelClassCode": "",
#     "grossQuantityUom": "KG",
#     "productPackageCount": 28,
#     "hazardousChemicalName": "1-METHOXY-2-PROPANOL",
#     "hazardousMaterialPackingGroupCode": "III",
#     "hazardousMaterialContactName": "Utd.Arab Emir. 00 971 4883 18 28",
#     "harmonizedCode": "",
#     "hazardousMaterialClassCode": 3,
#     "grossTransactionQuantity": 5772.2
#   },
#   "tenderRequestDate": "2023-06-22 15:05:12",
#   "purpose": "ORIGINAL",
#   "containerMaxtemp": "",
#   "customerCode": 202200064,
#   "stopReasonCode2": "UD",
#   "bdpServiceCode": "E",
#   "stopReasonCode1": "LD",
#   "bdpRepEmail": "karuna.kamble@bdpint.com",
#   "placeOfRec": "AEJEA",
#   "placeOfDel": "",
#   "containerVentstatus": "",
#   "bdpRepFirstName": "Karuna",
#   "bolNumber": "ONEYDXBD00863500",
#   "bdpReferenceNumber": 3121135381,
#   "bdpRepLastName": "Kamble",
#   "containerType": 2000,
#   "drayScacCode": "PRIM",
#   "transferLocation": "",
#   "purchaseOrderNumber": "PO-039674-320-1",
#   "vesselImo": 9869215,
#   "secondaryScacCode": "",
#   "portOfEntryEstDt": "2023-06-28 00:00:00"
# },{
#   "_id": "64a7f4654a8583665b8fadcd",
#   "destinationAddress": {
#     "country": "",
#     "zipCode": "",
#     "unlocCode": "AEJEA",
#     "code": "",
#     "city": "",
#     "postalCode": "",
#     "name": "PORT OF JEBEL ALI  UNITED ARAB EMIRATE",
#     "addressLine1": "",
#     "addressLine2": "",
#     "addressLine3": "",
#     "state": ""
#   },
#   "containerSeal1": "NA",
#   "containerSeal2": "",
#   "bdpRepPhone": "",
#   "originAddress": {
#     "country": "AE",
#     "zipCode": "",
#     "unlocCode": "AEJEA",
#     "code": "AE_EXDOWDXB_GF63",
#     "city": "JEBEL ALI",
#     "postalCode": "",
#     "name": "HORIZON TERMINALS",
#     "addressLine1": "JEBEL ALI LIMITED",
#     "addressLine2": "P.O. BOX 16881",
#     "addressLine3": "",
#     "state": ""
#   },
#   "placeOfRcptEstDt": "2023-06-27 00:00:00",
#   "messageType": "BookingRequest",
#   "carrierName": "OCEAN NETWORK EXPRESS PTE LTD",
#   "voyageNumber": "008E",
#   "tenderRequestNumber": 23062200041,
#   "portOfArr": "SADMM",
#   "drayName": "PRIME LINK",
#   "portOfDep": "AEJEA",
#   "specialInstruction": "",
#   "containerTemptype": "",
#   "tariffServiceCode": "PP",
#   "motCd": 1,
#   "containerReefer": "",
#   "carrierScacCode": "ONEY",
#   "customerName": "DOW ME",
#   "shipmentReferenceNumber": "0042241187",
#   "containerNumber": "TBNU01",
#   "methodOfPayment": "PP",
#   "ltstDelCutoffDt": "2023-06-26 00:00:00",
#   "containerMintemp": "",
#   "goodsAvlblShpEstDt": "2023-06-25 00:00:00",
#   "bookingNumber": "DXBD00863500",
#   "docCutoffDt": "2023-02-15 00:00:00",
#   "vesselName": "HMM RAON",
#   "cargoType": "O",
#   "drayEmail": "",
#   "containerProduct": {
#     "hazardousAdnrCode": "",
#     "hazardousMaterialDescription": "UTD.A",
#     "hazardousMaterialUnitedNationsPackingCode": "III",
#     "productPackageCode": "DR",
#     "hazardousMaterialUnitedNationsNumber": 3092,
#     "productBrandName": "DOWANOL(TM) PM GLYCOL ETHER",
#     "hazardousMaterialIndicator": "Y",
#     "hazardousMaterialFlashPointQuantity": "",
#     "hazardousMaterialFlashPointCode": "",
#     "productCode": "00092055",
#     "hazardousTunnelClassCode": "",
#     "grossQuantityUom": "KG",
#     "productPackageCount": 28,
#     "hazardousChemicalName": "1-METHOXY-2-PROPANOL",
#     "hazardousMaterialPackingGroupCode": "III",
#     "hazardousMaterialContactName": "Utd.Arab Emir. 00 971 4883 18 28",
#     "harmonizedCode": "",
#     "hazardousMaterialClassCode": 3,
#     "grossTransactionQuantity": 5772.2
#   },
#   "tenderRequestDate": "2023-06-22 15:05:12",
#   "purpose": "ORIGINAL",
#   "containerMaxtemp": "",
#   "customerCode": 202200064,
#   "stopReasonCode2": "UD",
#   "bdpServiceCode": "E",
#   "stopReasonCode1": "LD",
#   "bdpRepEmail": "karuna.kamble@bdpint.com",
#   "placeOfRec": "AEJEA",
#   "placeOfDel": "",
#   "containerVentstatus": "",
#   "bdpRepFirstName": "Karuna",
#   "bolNumber": "ONEYDXBD00863500",
#   "bdpReferenceNumber": 3121135381,
#   "bdpRepLastName": "Kamble",
#   "containerType": 2000,
#   "drayScacCode": "PRIM",
#   "transferLocation": "",
#   "purchaseOrderNumber": "PO-039674-320-1",
#   "vesselImo": 9869215,
#   "secondaryScacCode": "",
#   "portOfEntryEstDt": "2023-06-28 00:00:00"
# },{
#   "_id": "64a7f4654a8583665b8fadcd",
#   "destinationAddress": {
#     "country": "",
#     "zipCode": "",
#     "unlocCode": "AEJEA",
#     "code": "",
#     "city": "",
#     "postalCode": "",
#     "name": "PORT OF JEBEL ALI  UNITED ARAB EMIRATE",
#     "addressLine1": "",
#     "addressLine2": "",
#     "addressLine3": "",
#     "state": ""
#   },
#   "containerSeal1": "NA",
#   "containerSeal2": "",
#   "bdpRepPhone": "",
#   "originAddress": {
#     "country": "AE",
#     "zipCode": "",
#     "unlocCode": "AEJEA",
#     "code": "AE_EXDOWDXB_GF63",
#     "city": "JEBEL ALI",
#     "postalCode": "",
#     "name": "HORIZON TERMINALS",
#     "addressLine1": "JEBEL ALI LIMITED",
#     "addressLine2": "P.O. BOX 16881",
#     "addressLine3": "",
#     "state": ""
#   },
#   "placeOfRcptEstDt": "2023-06-27 00:00:00",
#   "messageType": "BookingRequest",
#   "carrierName": "OCEAN NETWORK EXPRESS PTE LTD",
#   "voyageNumber": "008E",
#   "tenderRequestNumber": 23062200042,
#   "portOfArr": "SADMM",
#   "drayName": "PRIME LINK",
#   "portOfDep": "AEJEA",
#   "specialInstruction": "",
#   "containerTemptype": "",
#   "tariffServiceCode": "PP",
#   "motCd": 1,
#   "containerReefer": "",
#   "carrierScacCode": "ONEY",
#   "customerName": "DOW ME",
#   "shipmentReferenceNumber": "0042241187",
#   "containerNumber": "TBNU01",
#   "methodOfPayment": "PP",
#   "ltstDelCutoffDt": "2023-06-26 00:00:00",
#   "containerMintemp": "",
#   "goodsAvlblShpEstDt": "2023-06-25 00:00:00",
#   "bookingNumber": "DXBD00863500",
#   "docCutoffDt": "2023-02-15 00:00:00",
#   "vesselName": "HMM RAON",
#   "cargoType": "O",
#   "drayEmail": "",
#   "containerProduct": {
#     "hazardousAdnrCode": "",
#     "hazardousMaterialDescription": "UTD.A",
#     "hazardousMaterialUnitedNationsPackingCode": "III",
#     "productPackageCode": "DR",
#     "hazardousMaterialUnitedNationsNumber": 3092,
#     "productBrandName": "DOWANOL(TM) PM GLYCOL ETHER",
#     "hazardousMaterialIndicator": "Y",
#     "hazardousMaterialFlashPointQuantity": "",
#     "hazardousMaterialFlashPointCode": "",
#     "productCode": "00092055",
#     "hazardousTunnelClassCode": "",
#     "grossQuantityUom": "KG",
#     "productPackageCount": 28,
#     "hazardousChemicalName": "1-METHOXY-2-PROPANOL",
#     "hazardousMaterialPackingGroupCode": "III",
#     "hazardousMaterialContactName": "Utd.Arab Emir. 00 971 4883 18 28",
#     "harmonizedCode": "",
#     "hazardousMaterialClassCode": 3,
#     "grossTransactionQuantity": 5772.2
#   },
#   "tenderRequestDate": "2023-06-22 15:05:12",
#   "purpose": "ORIGINAL",
#   "containerMaxtemp": "",
#   "customerCode": 202200064,
#   "stopReasonCode2": "UD",
#   "bdpServiceCode": "E",
#   "stopReasonCode1": "LD",
#   "bdpRepEmail": "karuna.kamble@bdpint.com",
#   "placeOfRec": "AEJEA",
#   "placeOfDel": "",
#   "containerVentstatus": "",
#   "bdpRepFirstName": "Karuna",
#   "bolNumber": "ONEYDXBD00863500",
#   "bdpReferenceNumber": 3121135381,
#   "bdpRepLastName": "Kamble",
#   "containerType": 2000,
#   "drayScacCode": "PRIM",
#   "transferLocation": "",
#   "purchaseOrderNumber": "PO-039674-320-1",
#   "vesselImo": 9869215,
#   "secondaryScacCode": "",
#   "portOfEntryEstDt": "2023-06-28 00:00:00"
# },{
#   "_id": "64a7f4654a8583665b8fadcd",
#   "destinationAddress": {
#     "country": "",
#     "zipCode": "",
#     "unlocCode": "AEJEA",
#     "code": "",
#     "city": "",
#     "postalCode": "",
#     "name": "PORT OF JEBEL ALI  UNITED ARAB EMIRATE",
#     "addressLine1": "",
#     "addressLine2": "",
#     "addressLine3": "",
#     "state": ""
#   },
#   "containerSeal1": "NA",
#   "containerSeal2": "",
#   "bdpRepPhone": "",
#   "originAddress": {
#     "country": "AE",
#     "zipCode": "",
#     "unlocCode": "AEJEA",
#     "code": "AE_EXDOWDXB_GF63",
#     "city": "JEBEL ALI",
#     "postalCode": "",
#     "name": "HORIZON TERMINALS",
#     "addressLine1": "JEBEL ALI LIMITED",
#     "addressLine2": "P.O. BOX 16881",
#     "addressLine3": "",
#     "state": ""
#   },
#   "placeOfRcptEstDt": "2023-06-27 00:00:00",
#   "messageType": "BookingRequest",
#   "carrierName": "OCEAN NETWORK EXPRESS PTE LTD",
#   "voyageNumber": "008E",
#   "tenderRequestNumber": 23062200043,
#   "portOfArr": "SADMM",
#   "drayName": "PRIME LINK",
#   "portOfDep": "AEJEA",
#   "specialInstruction": "",
#   "containerTemptype": "",
#   "tariffServiceCode": "PP",
#   "motCd": 1,
#   "containerReefer": "",
#   "carrierScacCode": "ONEY",
#   "customerName": "DOW ME",
#   "shipmentReferenceNumber": "0042241187",
#   "containerNumber": "TBNU01",
#   "methodOfPayment": "PP",
#   "ltstDelCutoffDt": "2023-06-26 00:00:00",
#   "containerMintemp": "",
#   "goodsAvlblShpEstDt": "2023-06-25 00:00:00",
#   "bookingNumber": "DXBD00863500",
#   "docCutoffDt": "2023-02-15 00:00:00",
#   "vesselName": "HMM RAON",
#   "cargoType": "O",
#   "drayEmail": "",
#   "containerProduct": {
#     "hazardousAdnrCode": "",
#     "hazardousMaterialDescription": "UTD.A",
#     "hazardousMaterialUnitedNationsPackingCode": "III",
#     "productPackageCode": "DR",
#     "hazardousMaterialUnitedNationsNumber": 3092,
#     "productBrandName": "DOWANOL(TM) PM GLYCOL ETHER",
#     "hazardousMaterialIndicator": "Y",
#     "hazardousMaterialFlashPointQuantity": "",
#     "hazardousMaterialFlashPointCode": "",
#     "productCode": "00092055",
#     "hazardousTunnelClassCode": "",
#     "grossQuantityUom": "KG",
#     "productPackageCount": 28,
#     "hazardousChemicalName": "1-METHOXY-2-PROPANOL",
#     "hazardousMaterialPackingGroupCode": "III",
#     "hazardousMaterialContactName": "Utd.Arab Emir. 00 971 4883 18 28",
#     "harmonizedCode": "",
#     "hazardousMaterialClassCode": 3,
#     "grossTransactionQuantity": 5772.2
#   },
#   "tenderRequestDate": "2023-06-22 15:05:12",
#   "purpose": "ORIGINAL",
#   "containerMaxtemp": "",
#   "customerCode": 202200064,
#   "stopReasonCode2": "UD",
#   "bdpServiceCode": "E",
#   "stopReasonCode1": "LD",
#   "bdpRepEmail": "karuna.kamble@bdpint.com",
#   "placeOfRec": "AEJEA",
#   "placeOfDel": "",
#   "containerVentstatus": "",
#   "bdpRepFirstName": "Karuna",
#   "bolNumber": "ONEYDXBD00863500",
#   "bdpReferenceNumber": 3121135381,
#   "bdpRepLastName": "Kamble",
#   "containerType": 2000,
#   "drayScacCode": "PRIM",
#   "transferLocation": "",
#   "purchaseOrderNumber": "PO-039674-320-1",
#   "vesselImo": 9869215,
#   "secondaryScacCode": "",
#   "portOfEntryEstDt": "2023-06-28 00:00:00"
# }

# itmes = []
# for da in data:
#     itme = {"tenderRequestNumber": da["tenderRequestNumber"],
#             "tenderRequestDate": da["tenderRequestDate"],
#             "destinationAddress": da["destinationAddress"],
#             "originAddress": da["originAddress"]}
#     itmes.append(itme)

# print(itmes)


# @router.get("/tenders_list/{page}/{limit}/")
# async def get_tenders_list(page: int,limit: int,token: str) -> JSONResponse:
#     if Token != token:
#         print(token,page,limit)
#         return JSONResponse({"token":token,"page":page,"limit":limit})

#     url = f"https://bdp.transportsimple.app/tenders_list/{page}/{limit}/"
#     params = {"token": Token}
#     try:
#         res = requests.get(url,params=params)
#         if res.status_code == 200:
#             tenders_list = json.loads(res.text)
#             # tenders_list = res.text
#             return get(tenders_list, SUCCESS)
#     except:
#         pass


# i = {"name":"ayush","lastname": ''}
# name = i["name"] if i["name"] else None
# lastname= i["lastname"] if i["lastname"] else None
# print(name,lastname)



# importing datetime
from datetime import datetime

# importing timezone from pytz module
from pytz import timezone

# giving the format of datetime
format = "%Y-%m-%d %H:%M:%S %Z%z"

# getting the current time in UTC timezone
now_utc = datetime.now(timezone('UTC'))

# Format the above DateTime using the strftime()
print('Current Time in UTC TimeZone:',now_utc.strftime(format))

# Converting to Asia/Kolkata time zone
# now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
print(now_utc.timestamp())
print(now_utc)

# Format the above datetime using the strftime()
# print('Current Time in Asia/Kolkata TimeZone:',now_asia.strftime(format))





# def reset_password_link_create(request):
#     try:
#         data = request.data
#         if not data.get('email') or not data.get('app_access'):
#             raise MissingDataError()
#         email = data.get('email').lower()

#         if data['app_access'] == 'main_portal':
#             user = User.objects.get_user_by_email(email)
#             host_name = f'webapp.{HOST_NAME}'
#         elif data['app_access'] == 'party_portal':
#             user = User.objects.get_client_portal_by_email(email)
#             host_name = HOST_NAME_CLIENT_PORTAL
#         else:
#             raise InvalidDataError    
        
#         if not user:
#             raise EmailNotExists()
        
#         reset_password_key = hash_key()
#         activation_key = generate_random_hash_v2(
#             email=email, access=data['app_access'],
#             reset_password_key=reset_password_key)
#         user.reset_password_key = activation_key
#         user.save()
#         email = user.email

#         email_subject = 'Reset password'
#         activation_url = "{0}/reset-password?t={1}".format(host_name, activation_key)
        
#         message = render_to_string(
#             'emails/reset_password_link.html', {
#                 'name': '%s %s' % (
#                     user.first_name, user.last_name),
#                 'activation_url': activation_url})
        
#         res = {'success': 'Check your email to reset password.'}
#         msg = 'User password reset link generated'
#         if ENABLE_PASSWORD_SEND:
#             email_status = SystemEmail().send_email(
#                 email_subject, message, [user.email], is_html=True)
#             if not email_status:
#                 raise EmailFailedError()
#         else:
#             res['activation_link'] = activation_url
#         return created(res, SUCCESS)
#     except User.DoesNotExist:
#         msg = 'User does not exist'
#         logger.error(str(email) + " - " + msg)
#         raise MissingObjectError(User.__name__)



def hash_key():
    RANDOM_STRING_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    string  = ''.join(secrets.choice(RANDOM_STRING_CHARS) for i in range(12))
    return hashlib.sha1(string.encode('utf-8')).hexdigest()[:30]

def generate_random_hash_v2(email, **kwargs):
    salt = hash_key()
    created_time = datetime.now(timezone('UTC'))
    # created_time = timezone.datetime.strptime('2019-04-22',
    #                                           "%Y-%m-%d").replace(second=5)

    seconds = created_time.timestamp()
    reset_password_key = kwargs.get('reset_password_key', None)

    if not reset_password_key:
        first_name = kwargs.get('first_name', '')
        last_name = kwargs.get('last_name', '')
        key = email + '~' + access + '~' + salt
        key = key + '~' + first_name + '~' + last_name
        key = str(seconds) + '~' + key
    elif reset_password_key:
        access = kwargs.get('access', '')
        key = email + '~' + access
        key = key + '~' + salt + '~' + reset_password_key
        key = str(seconds) + '~' + key
    else:
        key = str(seconds) + '~' + email + '~' + salt
    # activation_key = encode(key).decode('utf-8')
    activation_key = base64.urlsafe_b64encode(
        key.encode('ascii')).decode('utf-8')
    return activation_key