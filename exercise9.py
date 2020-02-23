noumero =int(input("enter noumero:")) # noumero = 10

while noumero >= 10:
  noumero = noumero*3 + 1 # noumero = 31

  def digit_sum(noumero):
    num_str = str(noumero)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
        print(num_str[i])
    return sum
  noumero = digit_sum(noumero) # noumero = 3 + 1 = 4 < 10 , δηλαδή μονοψήφιος
  



print("To teliko apotelesma einai:" , noumero)
