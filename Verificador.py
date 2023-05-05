path = input("Digite el nombre del archivo original")
with open(f"./{path}.txt", 'rb') as file1, open("./descomprimido_elmejorprofesor.txt", 'rb') as file2:
    text1 = file1.read()
    text2 = file2.read()
    print("Ok") if text1 == text2 else print("Nok")
       
