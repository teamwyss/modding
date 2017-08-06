#in development .
from turtle import *
import time
damage = 342
iWoodOwned = 0
sWoodOwned = str(iWoodOwned)
iMeatOwned = 0
iYouHealth = 10
iFurOwned = 0
iIronOwned = 0
iSteelOwned = 0
iMedicineOwned = 0
iTeethOwned = 0
iBonesOwned = 0
iClothOwned = 0
iScalesOwned = 0
iBulletsOwned = 0
iTorchesOwned = 0
sBasket = 'no'
sWdnSword = 'no'
sBonSword = 'no'
sIrnSword = 'no'
sStlSword = 'no'
sBonSpr = 'no'
sWhip = 'no'
sRifle = 'no'
sLethrArmor = 'no'
sBoneArmor = 'no'
sIronArmor = 'no'
sSteelArmor = 'no'
sForestUnlock = 'no'
sCaveUnlock = 'no'
Perks = []
pensize(10)
# Chapter 1
print("Chapter 1")
print("You notice a stray turtle. You want to make it your pet!")
iDistance = int(input('How far? '))
from random import randint
# first try
if randint(12, 13) == 13:
  print('Turtle rampage!!!')
  forward(randint(0, 100))
  left(randint(0, 360))
  forward(randint(0, 100))
  right(randint(0, 180))
  forward(randint(0, 100))
  forward(randint(0, 100))
  right(randint(0, 180))
  forward(randint(0, 200))
  left(randint(15, 360))
  print("Oh dear. Looks like it doesn't want you as it's rider! Bad luck!")
  iTurtlePet = 3
else:
  forward(iDistance)
  backward(iDistance)
  # second try
  iDistance2 = int(input('How far? '))
  if randint(12, 14) == 13:
    print('Turtle rampage!!!')
    forward(randint(0, 100))
    left(randint(0, 360))
    forward(randint(0, 100))
    right(randint(0, 180))
    forward(randint(0, 100))
    forward(randint(0, 100))
    right(randint(0, 180))
    forward(randint(0, 200))
    left(randint(15, 360))
    print("Oh dear. Looks like it doesn't want you as it's rider! Bad luck!")
    iTurtlePet = 3
  else:
    forward(iDistance2)
    backward(iDistance2)

    # third try
    iDistance3 = int(input('How far? '))
    if randint(12, 15) == 13:
      print('Turtle rampage!!!')
      forward(randint(0, 100))
      left(randint(0, 360))
      forward(randint(0, 100))
      right(randint(0, 180))
      forward(randint(0, 100))
      forward(randint(0, 100))
      right(randint(0, 180))
      forward(randint(0, 200))
      left(randint(15, 360))
      print("Oh dear. Looks like it doesn't want you as it's rider! Bad luck!") 
      iTurtlePet = 3
    else:
      forward(iDistance3)
      backward(iDistance3)
      print("Congrats! You tamed him!")
      iTurtlePet = 5
      iTurtlePetHealth = 5
# Chapter 2
for i in range(2):
  if sForestUnlock != "yes":
    sForest = input('Do you want to explore?(Yes/No) ')
    if sForest == "Yes":
      print("You wander around and come to a forest, leaves rustling in a gentle breeze.")
      sForestUnlock == "yes"
      iWoodOwned = iWoodOwned + 30
      sWoodOwned = str(iWoodOwned)
      print('You now have ' + sWoodOwned + ' Wood.')
    if iWoodOwned >= 30 and sBasket != "yes":
      sBasket = input('Craft basket?(costs: 30 wood) ')
      if sBasket == "Yes":
        iWoodOwned = iWoodOwned - 30
        print('The basket will carry more wood from the forest.')
  Action = input('What do you want to do now? ')
  if Action == 'Gather wood':
    #Battling a monster
    if randint(1, 2) == 1:
      print("A hound leaps out from behind a bush, it's teeth bared.")
      iEnemyHealth = 6
      while iEnemyHealth > 0:
        time.sleep(1)
        iYouHealth = iYouHealth - 2
        print('You: ' + str(iYouHealth) + '/10')
        time.sleep(1)
        damage = randint(0, 1) + iStrength
        iEnemyHealth = iEnemyHealth - damage
        iEnemyHealth = iEnemyHealth - damage
        print('Enemy: ' + str(iEnemyHealth) + '/6')
        if iYouHealth == 0 and iTurtlePet == 5 and randint(4, 5) == 4:
          print('You know all is lost... but something leaps out of the trees - your turtle! It is your only hope.')
          while iEnemyHealth != 0:
            iEnemyHealth = iEnemyHealth - 1
            time.sleep(1)
            iTurtleHealth = iTurtleHealth - 2
            time.sleep(1)
            if iTurtleHealth == 0:
              print('Your turtle sprawls onto the ground, dead. All hope really is lost now...')
            if iEnemyHealth == 0:
              print('Your turtle did it!')
        else:
          print('The world fades...')
          if iTurtlePet != 5:
            print('The world fades... ')
            iWoodOwned = 0
            sWoodOwned = str(iWoodOwned)
            iMeatOwned = 0
            iYouHealth = 10
            iFurOwned = 0
            iIronOwned = 0
            iSteelOwned = 0
            iMedicineOwned = 0
      else:
        print('Take:')
        Drops = ['3 Fur', '2 Bones', '5 Teeth', '3 Meat']
        for x in Drops:
          print(x)
          ChosenDrops = input()
        if Drops[0] in ChosenDrops:
          iFurOwned = iFurOwned + 3
        if Drops[1] in ChosenDrops:
          iBonesOwned = iBonesOwned + 2
        if Drops[2] in ChosenDrops:
          iTeethOwned = iTeethOwned + 5
        if Drops[3] in ChosenDrops:
          iMeatOwned = iMeatOwned + 3
        if ChosenDrops == 'Take all' and str(Drops) not in ChosenDrops:
          iFurOwned = iFurOwned
          iFurOwned = iMeatOwned
    print('Dry brush and dead branches litter the forest floor.')
    iWoodOwned = iWoodOwned + 30
    if sBasket == "Yes":
      iWoodOwned = iWoodOwned + 20
  if Action == 'Explore' and randint (1, 3) == 1:
    print("You stumble across a cave, the gloomy blackness striking fear in to your heart.")
    sCaveUnlock = 'yes'
    Choice = input('Do you want to go inside?')
    if Choice == 'Yes' and iTorchesOwned >= 0:
      print("You carefully creep in to it's depths, a torch guiding you through the darkness.")
if iBonesOwned >= 2 and iTeethOwned >= 3 and iWoodOwned >= 50:
  sBonSpr = input('Do you want to make a bone spear($: 2 Bones, 3 Teeth, 50 Wood)? ')
if sBonSpr == 'Yes':
  print("The spear's tip is crude but deadly.")
  iStrength = 2
