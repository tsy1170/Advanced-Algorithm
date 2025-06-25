from Question_2_Part2 import Person

class SocialGraph:
    def __init__(self):
        self.adj_list = dict()

    def add_person(self, person):
        if person.name not in self.adj_list:
            self.adj_list[person] = []
        else:
            print(f"User '{person}' already exists.")

    def add_follow(self, from_person, to_person):
        if from_person in self.adj_list and to_person in self.adj_list:
            self.adj_list[from_person].append(to_person)
        else:
            raise ValueError("One or both usernames not found!")

    def get_following(self, person):
        return self.adj_list.get(person, [])

    def get_followers(self, person):
        followers = []
        for user in self.adj_list:
            if person in self.adj_list[user]:
                followers.append(user)
        return followers

    def print_adj_list(self):
        for person in self.adj_list:
            following = ', '.join(str(p) for p in self.adj_list[person])
            print(f"{person} follows -> {following}")


alice = Person("Alice", "20", "Female", "alice20@gmail.com")
ben = Person("Ben", "21", "Male", "ben21@gmail.com")
chloe = Person("Chloe", "22", "Female", "chloe22@gmail.com")
alex = Person("Alex", "20", "Male", "alex20@gmail.com")
emma = Person("Emma", "19", "Female", "emma19@gmail.com")

g = SocialGraph()

for i in [alice, ben, chloe, alex, emma]:
    g.add_person(i)

g.add_follow(alice, ben)
g.add_follow(alice, chloe)
g.add_follow(ben, alex)
g.add_follow(ben, emma)
g.add_follow(chloe, alex)
g.add_follow(alex, alice)
g.add_follow(emma, chloe)

print(alice.get_person_detail())