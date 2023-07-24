
# #-------------------for django----------------------------------
# import json
# # from transportsimple.users.repo.detail.models import User


# def export_django_data_to_json(filename):
#     # django_users = User.objects.all()
#     users_data = []
#     for user in django_users:
#         user_data = {"username":user["username"],
#                     "first_name":user["first_name"],
#                     "last_name":user["last_name"],
#                     "id":user["id"],
#                     "email":user["email"],
#                     "raw_password":user["raw_password"],
#                     "password":user["password"],
#                     "reset_password_key":user["reset_password_key"],
#                     "date_joined":user["date_joined"],
#                     "is_onboarded":user["is_onboarded"],
#                     "primary_mobile_number":user["primary_mobile_number"],
#                     "primary_mobile_number_code":user["primary_mobile_number_code"],
#                     "alternate_mobile_number":user["alternate_mobile_number"],
#                     "alternate_mobile_number_code":user["alternate_mobile_number_code"],
#                     "profile_image":user["profile_image"],
#                     "is_active":user["is_active"],
#                     "is_driver":user["is_driver"],
#                     "is_client_portal":user["is_client_portal"],
#                     "is_main":user["is_main"],
#                     "last_login":user["last_login"],
#                     "USERNAME_FIELD":user["USERNAME_FIELD"],
#                     "modified_at":user["modified_at"],
#                     "created_at":user["created_at"],
#                     "REQUIRED_FIELDS":user["REQUIRED_FIELDS"]}
        

        
#         users_data.append(user_data)


#     with open(filename, "w") as file:
#         json.dump(users_data, file)

# export_django_data_to_json("django_users_data.json")

#--------------for flask------------------------------
import json
# import os
# # from app import users # users = db['users'] in main app


# def import_json_data_to_flask(filename):
#     filepath = os.path.join( base_path , filename)
#     with open(filepath, "r") as file:
#         data = json.load(file)

#     for user_data in data:
#         users.insert_one(user_data)




# import_json_data_to_flask("django_users_data.json")
with open("django_users_data.json", "r") as file:
    data = json.load(file)
    for da in data['result']:
        print(da)