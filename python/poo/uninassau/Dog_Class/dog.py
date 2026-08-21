class Animal:
    def __init__(self):
        self.name = input("What is your animal name? ")
        self.age = int(input("What is your animal age? "))

    def make_sound(self):
        print("This animal is making a sound!")

    def show_info(self):
        print("Your animal's info is: "
              f"Name: {self.name}\n"
              f"Age: {self.age}")
        
    def change_name(self):
        print(f"Your current animal name is: {self.name}.\n")
        new_name = input("Type your animal's new name: ")
        self.name = new_name


class Dog(Animal):
    def __init__(self, animal):
        self.animal = animal
        self.race = input("Input the race of you dog: ")

    def make_sound(self):
        print("bark bark!!")

    def show_info(self):
        print("Your dog's info is: "
              f"Name: {self.animal.name}\n"
              f"Age: {self.animal.age}\n"
              f"Race: {self.race}")
        
if __name__ == "__main__":
    animal = Animal()
    dog = Dog(animal)

    while True:
        action = input("What do you want to do?\n" \
        "1 - Make a sound\n" \
        "2 - Show info\n" \
        "3 - Change name\n" \
        "4 - Leave\n")

        if action == "1":
            dog.make_sound()
        elif action == "2":
            dog.show_info()
        elif action =="3":
            dog.animal.change_name()
        elif action == "4":
            print("Leaving...")
            break
        else:
            action = input("Please, just 1, 2, 3 or 4.\n" \
        "1 - Make a sound\n" \
        "2 - Show info\n" \
        "3 - Change name\n" \
        "4 - Leave")
