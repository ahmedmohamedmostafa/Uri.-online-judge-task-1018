N=int(input())
N100=N//100
R=N%100
N50=R//50
R=R%50
N20=R//20
R=R%20
N10=R//10
R=R%10
N5=R//5
R=R%5
N2=R//2
R=R%2
N1=R//1
R=R%1
print(N)
print(N100,"nota(s) de R$ 100,00")
print(N50,"nota(s) de R$ 50,00")
print(N20,"nota(s) de R$ 20,00")
print(N10,"nota(s) de R$ 10,00")
print(N5,"nota(s) de R$ 5,00")
print(N2,"nota(s) de R$ 2,00")
print(N1,"nota(s) de R$ 1,00")