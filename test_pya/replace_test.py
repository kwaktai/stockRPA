
text = "/Users/taikwak/TaiCloud/Documents/Project/stockRPA/flie/TMF_price_test.txt"

# with open(text, "w")as f:
#     f.write(text)
# with open(text, "w")as f:

#     f.write(text)


def price_replace():
    with open(text, "r")as file:
        price_list = file.readlines()
        file.close()
    a_1 = price_list[0].replace(" ", "\n")
    a_2 = price_list[1].replace(" ", "\n")
    a_list = a_1+a_2
    with open(text, "w")as file:
        file.write(a_list)
        file.close()
#     file.write(text)


price_replace()

# print(b)
# b_list = []
# b_replace = b[0].replace(" ", "\n")
# c_replace = b[1].replace(" ", "\n")
# d_replace = b[2].replace(" ", "\n")
# b_list.append(b_replace)
# b_list.append(c_replace)
# b_list.append(d_replace)

# print(b_list)
