# Tuples1
# words=("spam","white","black")
#
# # words[0]="red"
# print(words[2])
#
# person=("Alice",30,'Engineer')
#
# name,age,profession=person
#
# print(name, "'s", "profession is",profession,"and she is",age,"years old")
from PIL.DdsImagePlugin import item1

# Dictionaries2

contact_info={
    "Alice":"555-1234",
    "Bob":"5559875"
}

alice_phone=contact_info['Alice']
print(alice_phone)

contact_info['Daris']='045889191'

print(contact_info)

# del contact_info["Bob"]
# print(contact_info)

# keys=contact_info.keys()
# print(keys)
#
# values=contact_info.values()
# print(values)
#
# items=contact_info.items()
# print(items)

# contact_info={
#     "Alice":{
#         "phone":"555 1245",
#         "email":"alice@gmail.com"
#     }
# }

contact_info={
    "Alice":("555 1245","alice@gmail.com")
}

alice_info=contact_info['Alice']
phone=alice_info[0]
print(phone)
