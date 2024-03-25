def product_of_values(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

test_date = int(input("Masukkan tanggal tes hari ini: "))

print("Hasil perkalian dari 1 hingga", test_date, "adalah:", product_of_values(test_date))
