def swapFileData():
    file1 = input("sample2")
    file2 = input("sample1")

    with open(file1, 'r') as a: 
        data_a = a.read()

    with open(file1, 'r') as a: 
        a.write(data_b)

    with open(file2, 'r') as a: 
        data_b = b.read()

    with open(file1, 'r') as a: 
        a.write(data_a)