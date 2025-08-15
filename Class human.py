class Human:
    head = 1
    hand = 2
    foot = 2

    def Info(self):
        print("Head:", self.head,"\n" "Hand:", self.hand,"\n" "Foot:", self.foot)

    def __init__(self, name, age, gender, work, experience, education):
        self.name = name
        self.age = age
        self.gender = gender
        self.work = work
        self.experience = experience
        self.education = education

    def FullInfo(self):
        if self.work != "Student":
            print ("Name:", self.name, "\n"
              "Age:", self.age, "\n"
              "Gender:", self.gender, "\n"
              "Post:", self.work, "\n"
              "Worck experience:", self.experience, "\n"
              "Education:", self.education, "\n")
        else:
            print("Name:", self.name, "\n"
              "Age:", self.age, "\n"
              "Gender:", self.gender, "\n"
              "Post:", self.work, "\n")

human1 = Human("Alisa",24,"Ж","Secretary",2, "Basic")
human2 = Human("Bob",42,"M","Teacher",12, "Higher")
human3 = Human("Mike", 17, "M", "Student", None, None)
human4 = Human("Viola", 17, "Ж", "Student", None, None)
human5 = Human("Frank",55,"M","Director",24, "Higher")


#human1.FullInfo()
human2.FullInfo()
human3.FullInfo()
#human4.FullInfo()
#human5.FullInfo()

#human1.Info()
