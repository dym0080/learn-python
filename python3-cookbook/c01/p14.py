from operator import attrgetter

class User:
    def __init__(self,user_id):
        self.user_id=user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    print(users)
    print(sorted(users,key = lambda t: t.user_id))

users = [User(23),User(3),User(99)]
sort_notcompare()

print('fa')
print(sorted(users, key=attrgetter('user_id')))