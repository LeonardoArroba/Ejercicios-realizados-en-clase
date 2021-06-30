for car in "frase":
    if car in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        if car in ["A", "E", "I", "O", "U"]:
            continue
        else:
            cvoc = cvoc+1
print("cantidad vocales:{}".format(cvoc))
