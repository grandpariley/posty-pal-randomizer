class Pair: 
    def __init__(self, userA, userB):
        self.userA = userA
        self.userB = userB

    def __str__(self):
        return str(self.userA) + " and " + str(self.userB)
    
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.userA == other.userA and self.userB == other.userB or self.userA == other.userB and self.userB == other.userA

    def sameLocations(self):
        return self.userA.location == self.userB.location

class User: 
    def __init__(self, username, location):
        self.username = username
        self.location = location

    def __str__(self):
        return self.username + " from " + self.location
    
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.username == other.username and self.location == other.location
