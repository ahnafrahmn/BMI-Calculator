

#---------------------------------(          BMI Calculator           )-----------------------
#
# Md Ahnafur Rahman.
#
#
#---------------------------------------------------------------------------------------------
# w = weight 
# h = height 
# bmi = Body Mass Index (BMI)
# g = gender
# n = name
# ft = feet
# i= inch

#---------------------------------------------------------------------------------------------

n = input("Enter your name :: ")

n = str(n)

while True:
    g = input("Are you Male ?   :: ")
    if g == "yes":
        print("Hello Mr.", n)
        break
    elif g== "no":
        print("Hello Ms.", n)
        break
    else:
        print("Please type 'yes' or 'no'")
        continue
    

w = input("Enter your weight in kilograms :: ")


print("Give a spapce between feets and inches")
ft,i = input("Enter your height (ft inch) :: ").split()
ft = int(ft)
i = int(i)
h = ft*0.3048 + i*0.0254
h = float(h)


w = int(w)

bmi = w/(h*h)

print("Your BMI is :", format(bmi,".2f"))

if bmi < 18.5 :
    print("Oh! You're underweight.")
elif ((bmi >= 18.5) and (bmi<=24.99)):
    print("Great! your weight is normal.")
elif ((bmi >= 25.00) and (bmi<=29.99)):
    print("Oh! You're overweight.")
elif ((bmi >= 30.00) and (bmi<=34.99)):
    print("Class I obesity")
elif ((bmi >= 35.00) and (bmi<=39.99)):
    print("Class II obesity")
else:
    print("Class III obesity")


#---------------------------------------------------------------------------------------------

