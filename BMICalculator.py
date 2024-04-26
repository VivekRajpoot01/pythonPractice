# Write code below 💖
#print("Enter your weight in kg: ")
weight = float(input("Enter your weight in kg: "))
#print("Enter your height in metre: ")
height = float(input("Enter your height in metre: "))
bmi = weight/(height*height)
if (bmi<18):
  print("Your bmi is: ",bmi," and you are in Underweight range")
  print("Eat healthy food and be Happy!!")
  print("And don't compare yourself with others you are Hero in your own Life!!")
  print("Have a nice Day!")
elif (bmi>=18 and bmi<=25):
  print("Your bmi is: ",bmi," and you are in Healthy weight range")
  print("Eat healthy food and be Happy!!")
  #print("And don't compare yourself with others you are Hero in your own Life!!")
  print("Have a nice Day!")
else:
  print("Your bmi is: ",bmi," and you are in Overweight range")
  print("Eat healthy food and be Happy!!")
  print("And don't compare yourself with others you are Hero in your own Life!!")
  print("Have a nice Day!")
