import random

main_numbers = []
main_numbers_count=0


while main_numbers_count<10:
    number=random.randint(1,70)
    if number not in main_numbers:
         main_numbers.append(number)
         main_numbers_count+=1
print(main_numbers)

        
