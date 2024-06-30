Agric_science = int(input("enter your agric_science score: "))

Maths = int(input("enter your maths score: "))

Food_science = int(input("enter your food_science score: "))

Chemistry = int(input("enter your chemistry score: "))

English = int(input("enter your english score: "))

Biology = int(input("enter your biology score: "))

Social_science = int(input("enter your social_science score: "))

Mass_com =  int(input("enter your mass_com score: "))

Geography = int(input("enter your geopraphy score: "))

Lab_science = int(input("enter your subject score: "))

Average = (Agric_science + Maths + Food_science + Chemistry + English + Biology + Social_science + Mass_com + Geography + Lab_science)/10

print(Average)
if Average >= 70:
    print("you scored an A")
elif Average >60 < 69:
    print("you got a B")
elif Average >50 < 59:
    print("you got a C")
elif Average >40 < 49:
    print("you got a D")
elif Average >30 < 39:
    print("you got an E")
elif Average >20 < 30:
    print("you got an F")
else:
    print("sorry you failed")


