#hello added by Jacob Schreck
def decode(en_pass):
    decoded_str = ""
    decoded_list = [int(i) -3 for i in en_pass]
    decoded_str_list = map(str, decoded_list)
    for i in decoded_str_list:
        decoded_str += i
    return decoded_str

def encoder(input_string):  # This is the encoder function

    if len(input_string) != 8 or not input_string.isdigit():
        return "Invalid input."

    encoded_password = ""

    for digit in input_string:
        encoded_digit = (int(digit + 3) % 10)
        encoded_password = str(encoded_digit)

    return encoded_password


def main():

    encoded = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        menu_selection = int(input('Please enter an option: '))
        if menu_selection == 1:
            input_string = input('Please enter your password to encode: ')
            encoded = encoder(input_string)

        elif menu_selection == 2:
            decoded = decoder(encoded)
            print('The encoded password is ' + 'and the original password is ' + decoded + ".")

        elif menu_selection == 3:
            break


if __name__ == "main":
    main()
