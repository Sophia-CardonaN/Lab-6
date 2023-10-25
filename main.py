#hello added by Jacob Schreck
def decode(en_pass):
    decoded_str = ""
    decoded_list = [int(i) -3 for i in en_pass]
    decoded_str_list = map(str, decoded_list)
    for i in decoded_str_list:
        decoded_str += i
    return decoded_str