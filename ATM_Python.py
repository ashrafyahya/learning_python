print("This is an ATM!\n")
# learning how to use functions

actuell_value = 0 #start capital
old_value = 0

#check if the gaven password correct!
def check_password(input_password):
  authorized = False
  if input_password == saved_password:
    authorized = True
  else:
    authorized = False
    print("Password is rong!\n")
  return authorized

#deposit into account
def deposit(deposited_value):
  global actuell_value
  actuell_value += deposited_value
  return actuell_value

#paying out from account
def payout(payedout_value):
  global actuell_value
  actuell_value -= payedout_value
  return actuell_value

#output for current amount
def Budget_Infos():
  global actuell_value
  return actuell_value

#changing password
def change_password(new_password):
  global saved_password
  saved_password = new_password
  print("Password successfully updated!\n")

#check if starting input correct
def check_input():
  global start
  start = int(input("Press 1 for again or 0 for end! "))
  if start == 1:
      pass
  elif start == 0:
      pass
  else:
      print("Try again!\n")
      check_input()

#current saved password
saved_password = 12345
#1 for starting, 0 for ending
start = 1

password = int(input("Please enter your password(only numbers!): "))
checked = check_password(password)
if checked:
  print("Password is correct!\n")

while start:
  if checked:
    print(
      "choose an operation!\navailable operations:\n\t1-Deposit\n\t2-Payout\n\t3-Budegt information\n\t4-Change Password\n"
    )
    chosen_operation = input(
      "Press D for Deposit \n\tP for Payout \n\tB for Budget and \n\tC for changing password:\n"
    )
    #for accepting small and capital letters
    operation = chosen_operation.upper()

    #the only 4 available operations
    available_operations = ["D", "P", "B", "C"]

    match operation:
      case "D":
        deposited_value = int(input("enter the amount to be deposited: "))
        if deposited_value >= 0:
          new_budget = deposit(deposited_value)
          actuell_value = new_budget
          print(f"{deposited_value} Euro is deposited succsessfully!\n")
          print(f"actuell Budget: {actuell_value} Euro\n")
          check_input()
        else:
          print("Deposing faild, try again!\n")

      case "P":
        payedout = int(input("enter the amount to be payedout: "))
        if actuell_value >= payedout:
          new_budget = payout(payedout)
          actuell_value = new_budget
          print(f"{payedout} Euro is payedout succsessfully!\n")
          print(f"actuell Budget: {actuell_value} Euro\n")
          check_input()

        else:
          print("You don't have enough Budget!\n")
          check_input()

      case "B":
        print(f"Your Budget is {actuell_value} Euro\n")
        check_input()

      case "C":
        new_password = int(input("Enter the new password, only numbers: "))
        change_password(new_password)
        check_input()
      case _:
        print("Erorr!\n")
        check_input()

  else:
    check_input()
    password = int(input("Please enter your password: "))
    checked = check_password(password)

#mögliche Verbesserung:
#Database: Passwort verschlüsseln
#          speichern neues Passworts
#          speichern, wie viel das Passwort geändert wurde
#          Verschiedene Kontos anhand Passwort öffnen bzw. erstellen
