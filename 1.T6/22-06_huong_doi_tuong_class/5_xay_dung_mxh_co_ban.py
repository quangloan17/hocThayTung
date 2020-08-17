class Person:
    def __init__(self,name):
        self.name = name
        self.friendList = []
        self.requestList = []

    def __repr__(self):
        return self.name

    def sendRequest(self,person):
        if self not in person.requestList:
           person.requestList.append(self)

    def acceptRequest(self,person):
        if person in self.requestList:
            self.friendList.append(person)
            person.friendList.append(self)
            self.requestList.remove(person) 

    def isFriendWith(self,person):
        return self in person.friendList

    def isFriendOfFriend(self,person):
        for p in self.friendList:
            if p.isFriendWith(person):
                return True
            return False

    def getCommonFriends(self,person):
        return[p for p in self.friendList if p.isFriendWith(person)]


A = Person('A');B = Person('B'); C = Person('C')
A.sendRequest(B);B.sendRequest(C)
B.acceptRequest(A);C.acceptRequest(B)

print(A.isFriendWith(B)) #Expect: True
print(A.isFriendWith(C)) #Expect: False
print(A.isFriendOfFriend(C)) #Expect: True
print(A.getCommonFriends(C)) #Expect: [B]


# print('A friends:', A.friendList) #Expect:[B]
# print('B friends:', B.friendList) #Expect:[A,C]
# print('C friends:', C.friendList) #Expect:[B]
