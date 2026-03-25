users = []
def addproject(name , age):
    users.append({"name":name,"age":age})
def removeproject(name):
    global users
    users=[user for user in users if user["name"] != name]
def updateproject(name , newname=None , newage = None):
    for i in users:
        if i["name"] == name:
            if newname:
                i["name"]=newname
            if newage:
                i["age"]=newage
        else:
            print("Can't find user")
def serchproject(name):
    for i in users:
        if i["name"] == name:
            print(f"Find user {i["name"]} age:{i["age"]}")
        else:
            print("Can't find user")
def usersdate():
    return users
while True:
    a=int(input("1/增加用户\n2/删除用户\n3/修改数据\n4/查找用户\n5/显示所有用户"))
    if a==1:
        name=input("name")
        age=input("age")
        addproject(name,age)
    elif a==2:
        name=input("你想删的name")
        removeproject(name)
    elif a==3:
        name=input("name")
        newnam=input("newname")
        newage=input("newage")
        updateproject(name=name,newname=newnam,newage=newage)
    elif a==4:
        name=input("name")
        serchproject(name=name)
    elif a==5:
        print(usersdate())
    else:
        break 

