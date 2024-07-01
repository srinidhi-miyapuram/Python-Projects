# Credit card validation using the Lhun's algorithm

def lunh_algorithm(cardNumber):
    # Convert card number to a list
    card_number_list = list(cardNumber)
    odd_sum = 0
    even_sum = 0
    
    # Calculate sum of digits at odd positions
    for x in range(len(card_number_list)):
        if x % 2 != 0:
            odd_sum += int(card_number_list[x])
        elif x % 2 == 0:
            digit = int(card_number_list[x]) * 2
            if digit > 9:
                digit_list = list(str(digit))
                digit_sum = sum([int(i) for i in digit_list])
                even_sum += digit_sum
            else:
                even_sum += digit
    
    # Check if the sum of digits is divisible by 10
    odd_even_sum = even_sum + odd_sum
    if odd_even_sum % 10 == 0:
        return True
    return False

if __name__ == '__main__':
    cardNumber = input("Enter card number :- ")
    valid = lunh_algorithm(cardNumber)
    if valid:
        print("Valid Card")
    else:
        print("Invalid Card")