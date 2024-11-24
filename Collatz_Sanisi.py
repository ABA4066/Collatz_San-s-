import time
n=int(input("Tam Sayı Giriniz\n"))
sayac=0
while n!=1:
    if n%2==0:
        n=n/2
        time.sleep(1)
        print("Sayımız çift olduğu için 2'ye böldük.")
        time.sleep(1)
        print("Yeni sayımız {}'dir\n".format(n))
    else:
        n=(3*n)+1
        time.sleep(1)
        print("Sayımız tek olduğu için 3'le çarpıp 1 ekledik.")
        time.sleep(1)
        print("Yeni sayımız {}'dir\n".format(n))
    sayac +=1
print("\n1'e ulaşmak {} adım sürdü\n".format(sayac))