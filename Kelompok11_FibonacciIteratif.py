from timeit import default_timer as waktu

# Fibonaci Iteratif
def fibiter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


start = waktu()
fibiter(10)
end = waktu()
print("Waktu eksekusi fibonacci iteratif (n = 10) = ", "{:f}".format(end-start))

start = waktu()
fibiter(20)
end = waktu()
print("Waktu eksekusi fibonacci iteratif (n = 20) = ", "{:f}".format(end-start))

start = waktu()
fibiter(40)
end = waktu()
print("Waktu eksekusi fibonacci iteratif (n = 40) = ", "{:f}".format(end-start))

start = waktu()
fibiter(45)
end = waktu()
print("Waktu eksekusi fibonacci iteratif (n = 45) = ", "{:f}".format(end-start))