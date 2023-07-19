print("Hallöchen!\nDieser Rechner wurde mit Python geschrieben!\n")

#Rechner mit switch

start=1
while start:
  option=input("Eined der Operationen +-*/ auswählen: ")
  x=int(input("Gib die erste Zahl ein: "))
  y=int(input("Gib die zweite Zahl ein: "))

  options_list=["+","*","-","/"]
  match option:
    case "+":
      result=x+y
  
    case "*":
      result=x*y
  
    case "-":
      result=x-y
  
    case "/":
      result=x/y
  
    case _:
      result=00000
      print("Error!\n")
  
  print(f"Das Ergebnis von ({option})-Verfahren ist: {result}")
  start=int(input("Für weitere Nutzung die 1 drücken, sonst 0 zum Beenden!\n"))
  if start==0: print("Der Rechner wurde geschlossen, Tschüss!\n")
