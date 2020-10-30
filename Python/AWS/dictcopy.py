new_keys = ["user_name","user_id","user_email"]

old_dict = {"name":"testname",
            "id":123,
            "email":"test@example.com"}

print(dict(zip(new_keys,old_dict.values())))

print({k:v for k,v in old_dict.items()})

print(old_dict.values())