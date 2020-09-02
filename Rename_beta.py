import os

print("RENAME HELPS CHANGE SAME NAMES OR EXTENSIONS OF MULTIPLE FILES AT ONCE")
while True:
    print("TYPE 'Y' TO MOVE TO THE NEXT FOLDER OR 'N' TO STOP AT THAT FOLDER")
    rootPath = "C:/Users"
    os.chdir(rootPath)
    print(rootPath)
    do = input("Do you want to go further: ").upper()
    while do == "Y":
        lis = os.listdir(rootPath)
        n = 1
        for x in lis:
            print(n, "-", x)
            n += 1
        k = int(input("What number of file do you want to enter: "))
        r = k-1
        add = str(lis[r])
        if "." in add:
            print("Sorry, Can't go any further")
            exit()
        else:
            newPath = rootPath + "/" + add
            print(newPath)
            os.chdir(newPath)
            print(os.listdir(newPath))
            rootPath = newPath
            do = input("Do you still want to go further: ")

    print(rootPath)
    nlist = os.listdir(rootPath)

    old = input("What do you want to change: ")
    new = input("To what: ")

    for n in nlist:
        os.rename(n, n.replace(old, new))
    print("YOUR OPERATION HAS BEEN COMPLETED\nCHECK YOUR FOLDER")
