from timeit import default_timer as waktu

# Fibonaci Rekursif
def fibrekur(n):
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    else :
        return (fibrekur(n-2) + fibrekur(n-1))

#test = int(input("Masukkan N : "))

start = waktu()
fibrekur(10)
end = waktu()
print("Waktu eksekusi fibonacci rekursif (n = 10) = ", "{:f}".format(end-start))

start = waktu()
fibrekur(20)
end = waktu()
print("Waktu eksekusi fibonacci rekursif (n = 20) = ", "{:f}".format(end-start))

start = waktu()
fibrekur(40)
end = waktu()
print("Waktu eksekusi fibonacci rekursif (n = 40) = ", "{:f}".format(end-start))

start = waktu()
fibrekur(45)
end = waktu()
print("Waktu eksekusi fibonacci rekursif (n = 45) = ", "{:f}".format(end-start))