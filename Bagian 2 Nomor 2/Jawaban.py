fibs = [0,1]
num = input("masukan jumlah deret fibbonacci: ")

num = int(num)
    if num < 3:
print("minimal 3 deret")
      else:

    for i in range (num-2):

    fibs.append (fibs[-2]+fibs[-1])

    print (fibs)