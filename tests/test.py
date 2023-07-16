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



import json

response = {
    "result": "{\"_id\":\"64a7f4654a8583665b8fadcd\",\"destinationAddress\":{\"country\":\"\",\"zipCode\":\"\",\"unlocCode\":\"AEJEA\",\"code\":\"\",\"city\":\"\",\"postalCode\":\"\",\"name\":\"PORT OF JEBEL ALI  UNITED ARAB EMIRATE\",\"addressLine1\":\"\",\"addressLine2\":\"\",\"addressLine3\":\"\",\"state\":\"\"},\"containerSeal1\":\"NA\",\"containerSeal2\":\"\",\"bdpRepPhone\":\"\",\"originAddress\":{\"country\":\"AE\",\"zipCode\":\"\",\"unlocCode\":\"AEJEA\",\"code\":\"AE_EXDOWDXB_GF63\",\"city\":\"JEBEL ALI\",\"postalCode\":\"\",\"name\":\"HORIZON TERMINALS\",\"addressLine1\":\"JEBEL ALI LIMITED\",\"addressLine2\":\"P.O. BOX 16881\",\"addressLine3\":\"\",\"state\":\"\"},\"placeOfRcptEstDt\":\"2023-06-27 00:00:00\",\"messageType\":\"BookingRequest\",\"carrierName\":\"OCEAN NETWORK EXPRESS PTE LTD\",\"voyageNumber\":\"008E\",\"tenderRequestNumber\":23062200040,\"portOfArr\":\"SADMM\",\"drayName\":\"PRIME LINK\",\"portOfDep\":\"AEJEA\",\"specialInstruction\":\"\",\"containerTemptype\":\"\",\"tariffServiceCode\":\"PP\",\"motCd\":1,\"containerReefer\":\"\",\"carrierScacCode\":\"ONEY\",\"customerName\":\"DOW ME\",\"shipmentReferenceNumber\":\"0042241187\",\"containerNumber\":\"TBNU01\",\"methodOfPayment\":\"PP\",\"ltstDelCutoffDt\":\"2023-06-26 00:00:00\",\"containerMintemp\":\"\",\"goodsAvlblShpEstDt\":\"2023-06-25 00:00:00\",\"bookingNumber\":\"DXBD00863500\",\"docCutoffDt\":\"2023-02-15 00:00:00\",\"vesselName\":\"HMM RAON\",\"cargoType\":\"O\",\"drayEmail\":\"\",\"containerProduct\":{\"hazardousAdnrCode\":\"\",\"hazardousMaterialDescription\":\"UTD.A\",\"hazardousMaterialUnitedNationsPackingCode\":\"III\",\"productPackageCode\":\"DR\",\"hazardousMaterialUnitedNationsNumber\":3092,\"productBrandName\":\"DOWANOL(TM) PM GLYCOL ETHER\",\"hazardousMaterialIndicator\":\"Y\",\"hazardousMaterialFlashPointQuantity\":\"\",\"hazardousMaterialFlashPointCode\":\"\",\"productCode\":\"00092055\",\"hazardousTunnelClassCode\":\"\",\"grossQuantityUom\":\"KG\",\"productPackageCount\":28,\"hazardousChemicalName\":\"1-METHOXY-2-PROPANOL\",\"hazardousMaterialPackingGroupCode\":\"III\",\"hazardousMaterialContactName\":\"Utd.Arab Emir. 00 971 4883 18 28\",\"harmonizedCode\":\"\",\"hazardousMaterialClassCode\":3,\"grossTransactionQuantity\":5772.2},\"tenderRequestDate\":\"2023-06-22 15:05:12\",\"purpose\":\"ORIGINAL\",\"containerMaxtemp\":\"\",\"customerCode\":202200064,\"stopReasonCode2\":\"UD\",\"bdpServiceCode\":\"E\",\"stopReasonCode1\":\"LD\",\"bdpRepEmail\":\"karuna.kamble@bdpint.com\",\"placeOfRec\":\"AEJEA\",\"placeOfDel\":\"\",\"containerVentstatus\":\"\",\"bdpRepFirstName\":\"Karuna\",\"bolNumber\":\"ONEYDXBD00863500\",\"bdpReferenceNumber\":3121135381,\"bdpRepLastName\":\"Kamble\",\"containerType\":2000,\"drayScacCode\":\"PRIM\",\"transferLocation\":\"\",\"purchaseOrderNumber\":\"PO-039674-320-1\",\"vesselImo\":9869215,\"secondaryScacCode\":\"\",\"portOfEntryEstDt\":\"2023-06-28 00:00:00\"}",
    "message": "success",
    "status": "success"
}

result = json.loads(response["result"])
response["result"] = result

print(response)