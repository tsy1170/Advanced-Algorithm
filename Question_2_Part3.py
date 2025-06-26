from Question_2_Part1 import UDGraph
from Question_2_Part2 import Person


class SocialApp:
    def __init__(self):
        self.graph = UDGraph()

    def add_user(self, name, age, gender, email):
        person = Person(name, age, gender, email)
        self.graph.addVertex(person)
        return person


    def add_follow(self, from_name, to_name):
        follower = self.find_person_by_name(from_name)
        followee = self.find_person_by_name(to_name)
        if follower and followee:
            self.graph.addEdge(follower, followee)


    def view_followee(self, name):
        person = self.find_person_by_name(name)
        if person:
            followee = self.graph.listOutGoingAdjacentVertex(person)
            return followee


    def view_followers(self, name):
        person = self.find_person_by_name(name)
        if person:
            followers = []
            for user, followings in self.graph.adj_list.items():
                if person in followings:
                    followers.append(user)
            return followers


    def find_person_by_name(self, name):
        for person in self.graph.adj_list:
            if person.name == name:
                return person
        return None


def print_header(g, string):
    print("---------------------------------------------")
    print(string)
    print("---------------------------------------------")
    g.graph.print_adj_list()

def main():
    g = SocialApp()

    alice = g.add_user("Alice", "20", "Female", "alice20@gmail.com")
    ben = g.add_user("Ben", "21", "Male", "ben21@gmail.com")
    chloe = g.add_user("Chloe", "22", "Female", "chloe22@gmail.com")
    alex = g.add_user("Alex", "20", "Male", "alex20@gmail.com")
    emma = g.add_user("Emma", "19", "Female", "emma19@gmail.com")

    g.add_follow(alice.name, ben.name)
    g.add_follow(alice.name, chloe.name)
    g.add_follow(alice.name, emma.name)

    g.add_follow(ben.name, alice.name)
    g.add_follow(ben.name, chloe.name)

    g.add_follow(chloe.name, alice.name)
    g.add_follow(chloe.name, alex.name)

    g.add_follow(alex.name, alice.name)
    g.add_follow(alex.name, ben.name)

    g.add_follow(emma.name, chloe.name)
    g.add_follow(emma.name, ben.name)

    while True:
        print("---------------------------------------------")
        print("Welcome to Social App")
        print("---------------------------------------------")
        print("1. View all profile names")
        print("2. View details of any profile")
        print("3. View followers of any profile")
        print("4. View followed account of any profile")
        print("5. Quit")
        print("---------------------------------------------")

        try:
            option = int(input("Enter your option (1 - 5): "))
            print()
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        user_list = list(g.graph.adj_list.keys())

        if option == 1:
            print_header(g, "View all profile name")
            print()


        elif option == 2:
            print_header(g, "View details of any profile")

            try:
                user_index = int(input(f"Select a user profile to view (1 - {len(user_list)}): "))
                if 1 <= user_index <= len(user_list):
                    selected_person = user_list[user_index - 1]
                    print("---------------------------------------------")
                    print(selected_person.get_person_detail())
                    print()
                else:
                    print("Invalid selection. Please choose a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")


        elif option == 3:
            print_header(g, "View followers of any profile")

            try:
                user_index = int(input(f"Select a user profile to view followers (1 - {len(user_list)}): "))
                if 1 <= user_index <= len(user_list):
                    selected_person = user_list[user_index - 1]
                    followers = g.view_followers(selected_person.name)
                    print("---------------------------------------------")
                    if followers:
                        print(f"{selected_person.name} followers list: ")
                        for person in followers:
                            print(f"- {person}")
                    else:
                        print(f"{selected_person.name} has no followers")
                    print()
                else:
                    print("Invalid selection. Please choose a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")


        elif option == 4:
            print_header(g, "View followed account of a profile")

            try:
                user_index = int(input(f"Select a user profile to view followed account (1 - {len(user_list)}): "))
                if 1 <= user_index <= len(user_list):
                    selected_person = user_list[user_index - 1]
                    followee = g.view_followee(selected_person.name)
                    print("---------------------------------------------")
                    if followee:
                        print(f"{selected_person.name} following list: ")
                        for person in followee:
                            print(f"- {person}")
                    else:
                        print(f"{selected_person.name} doesn't follow any users")
                    print()
                else:
                    print("Invalid selection. Please choose a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")


        elif option == 5:
            print("Thank you for using Social App!")
            break

        else:
            print("Invalid option. Please select from 1 to 5.")




if __name__ == "__main__":
    main()
