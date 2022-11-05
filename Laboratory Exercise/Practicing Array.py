print(f'{"*** Programmed by ***": ^40}')
print(f'{"*** Nicolas Fabillar ***": ^40}\n')

NumberList = [10, 12, 15, 9, 14, 30, 50, 17, 21]

Counter = 0
while True:
       if Counter == 1:
              print("This is the new array:", NumberList)
       if Counter == 0:
              print("Array:", NumberList)

       print("Menu: \n\t 1 -> Add an element \n\t 2 -> Insert an element \n\t 3 -> Modify an element "
             "\n\t 4 -> Delete an element \n\t 5 -> Arrange in ascending order \n\t 6 -> Arrange in descending order"
             "\n\t 7 -> Exit")
       try:
              Choice = int(input("\nWhat do you want to do? (1-6): "))
       except ValueError:
              print("\n\tInvalid input, enter an integer. \n")
       else:
              if Choice in [1, 2, 3, 4, 5, 6, 7]:
                     if Choice == 1:
                            while True:
                                   try:
                                          Number = int(input("\tEnter a number to add: "))
                                   except ValueError:
                                          print("\tInvalid input, enter an integer.\n")
                                   else:
                                          NumberList.append(Number)
                                          print("\n\tNumber Added.")
                                          break
                     if Choice == 2:
                            while True:
                                   try:
                                          Index = int(input("\tEnter the index where to insert it: "))
                                   except ValueError:
                                          print("\tInvalid input, enter an integer.\n")
                                   else:
                                          if Index < len(NumberList):
                                                 break
                                          else:
                                                 print("\tInvalid input, index out of range.\n")
                            while True:
                                   try:
                                          Number2 = int(input("\tEnter a number to insert: "))
                                   except ValueError:
                                          print("\tInvalid input, enter an integer.\n")
                                   else:
                                          NumberList.insert(Index, Number2)
                                          print("\n\tNumber Inserted.")
                                          break

                     if Choice == 3:
                            while True:
                                   try:
                                          Index2 = int(input("\tEnter the index of the number you want to change: "))
                                   except ValueError:
                                          print("\tInvalid input, enter an integer.\n")
                                   else:
                                          if Index2 < len(NumberList):
                                                 break
                                          else:
                                                 print("\tInvalid input, index out of range.\n")
                            while True:
                                   try:
                                          Number3 = int(input("\tEnter the new number: "))
                                   except ValueError:
                                          print("\tInvalid input, enter an integer.\n")
                                   else:
                                          NumberList[Index2] = Number3
                                          print("\n\tNumber Changed.")
                                          break
                     if Choice == 4:
                            while True:
                                   try:
                                          Index3 = int(input("\tEnter the index of the number you want to delete: "))
                                   except ValueError:
                                          print("\tInvalid input, enter an integer.\n")
                                   else:
                                          if Index3 < len(NumberList):
                                                 NumberList.pop(Index3)
                                                 print("\n\tNumber Deleted.")
                                                 break
                                          else:
                                                 print("\tInvalid input, index out of range.\n")
                     if Choice == 5:
                            NumberList.sort()
                            print("\n\tNumber sorted in ascending order.")

                     if Choice == 6:
                            NumberList.sort()
                            NumberList.reverse()
                            print("\n\tNumber sorted in descending order.")

                     if Choice == 7:
                            print("\n** Program Terminated **")
                            exit()
                     Counter = 1
              else:
                     print("\n\tInvalid Choice! \n ")


