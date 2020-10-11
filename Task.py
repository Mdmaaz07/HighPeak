goodies = []
#f = open("input.txt", "rt")

def StoreGoodies():
    #f = open("C:\Users\moham\Desktop\input.txt", "rt")
    #print(f)
    n = int(input("Enter number of goodies: "))#taking input from the user 
    for i in range(n):
        goodie = input("\nGoodie Name: ")
        price = int(input("price: "))
        goodies.append([goodie, price])
# the below loop calculates the difference between the chosen goodie with highest price and the lowest price
    for i in range(n):
        for j in range(n):
            if goodies[i][1] < goodies[j][1]:
                temp = goodies[i]
                goodies[i] = goodies[j]
                goodies[j] = temp
# The below loop shows the answer
def ShowGoodies(n_goodies):
    for goodie in goodies[:n_goodies]:
        print(goodie[0] + ": " + str(goodie[1]))# Below gives the required answer

    print("And the difference between the chosen goodie with highest price and the lowest price is " + str(goodies[n_goodies - 1][1] - goodies[0][1]))


StoreGoodies()
n_employee = int(input("\n\nNumber of employee: "))
ShowGoodies(n_employee)
