# Sorting Hat 💖
print("Help us to choose which house will best suit for you!!")
print("Don't Worry! you can again change your house as your wish!!")
print("--------------Four Houses are----------------")
print("🦁 Gryffindor")
print("🦅 Ravenclaw")
print("🦡 Hufflepuff")
print("🐍 Slytherin")
print("----------Answer some questions by choosing the options-----------")
gry=0
raven=0
huff=0
sly=0
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print(" 2) Dusk")
choose_1 = int(input("Choose one option from the above question: "))
if (choose_1==1):
  gry+=1
  raven+=1
elif (choose_1==2):
  huff+=1
  sly+=1
else:
  print("Wrong Input")

## question 2
print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

choose_2 = int(input("Choose one option from the above question: "))

if (choose_2==1):
  huff+=2
elif (choose_2==2):
  sly+=2
elif (choose_2==3):
  raven+=2
elif (coose_2==4):
  gry+=2
else:
  print("Wrong Input")

## Question 3

print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

choose_3 = int(input("Choose one option from the above question: "))

if (choose_3==1):
  sly+=4
elif (choose_3==2):
  huff+=4
elif (choose_3==3):
  raven+=4
elif (choose_3==4):
  gry+=4
else:
  print("Wrong Input")

## Final Output
if (gry>raven and gry>huff and gry>sly):
  print("Your house is: 🦁 Gryffindor")
elif (raven>gry and raven>huff and raven>sly):
  print("Your house is:  🦅 Ravenclaw")
elif (huff>gry and huff>raven and huff>sly):
  print("Your house is: 🦡 Hufflepuff")
elif (sly>huff and sly>raven and sly>gry):
  print("Your house is: 🐍 Slytherin")
else:
  print("Not able to choose your house this time. Please try again!!")
