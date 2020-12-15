import math
import sys
sys.setrecursionlimit(10**7)
#競技プログラミング対整数問題のライブラリーです
class integerlib():
    def __init__(self):
        pass
    
    def primeset(self,N): #N以下の素数をsetで求める.エラトステネスの篩O(√Nlog(N))
        lsx = [1]*(N+1)
        for i in range(2,int(-(-N**0.5//1))+1):
            if lsx[i] == 1:
                for j in range(i,N//i+1):
                    lsx[j*i] = 0
        setprime = set()
        for i in range(2,N+1):
            if lsx[i] == 1:
                setprime.add(i)
        return setprime
    
    def defprime(self,N):#素数かどうかの判定、エラトステネスの篩O(√Nlog(N))
        return N in self.primeset(N)
    
    def gcd(self,N,K):#最大公約数
        return math.gcd(N,K)

    def lmc(self,N,K):#最小公倍数
        return N*K//math.gcd(N,K)
    
    def factorization(self,N):#素因数分解√N
        arr = []
        temp = N
        for i in range(2, int(-(-N**0.5//1))+1):
            if temp%i==0:
                cnt=0
                while temp%i==0:
                    cnt+=1
                    temp //= i
                arr.append([i, cnt])
        if temp!=1:
            arr.append([temp, 1])
        if arr==[]:
            arr.append([N, 1])
        return arr #[素因数、個数]

    def factorizationset(self,N):#素因数分解√N,含まれている素因数の種類
        if N == 1:
            return set()
        ls = self.factorization(N)
        setf = set()
        for j in ls:
            setf.add(j[0])
        return setf

    def divisorsnum(self,N):#約数の個数
        ls = []
        for i in self.factorization(N):
            ls.append(i[1])
        d = 1
        for i in ls:
            d *= i+1
        return d

    def Eulerfunc(self,N):#オイラー関数正の整数Nが与えられる。1,2,…,Nのうち、Nと互いに素であるものの個数を求めよ。
        ls = list(self.factorizationset(N))
        ls2 = [N]
        for i in ls:
            ls2.append(ls2[-1]-ls2[-1]//i)
        return ls2[-1]

    def make_divisors(self,N):#約数列挙O(√N)
        lower_divisors , upper_divisors = [], []
        i = 1
        while i*i <= N:
            if N % i == 0:
                lower_divisors.append(i)
                if i != N // i:
                    upper_divisors.append(N//i)
            i += 1
        return lower_divisors + upper_divisors[::-1]

    def invmod(self,a,mod):#mod逆元
        if a == 0:
            return 0
        if a == 1:
            return 1
        return (-self.invmod(mod % a, mod) * (mod // a)) % mod
        
    def cmbmod(self,n, r, mod):#nCr % mod
        inv = [0,1]
        for i in range(2, n + 1):
            inv.append((-inv[mod % i] * (mod // i)) % mod)
        cmd = 1
        for i in range(1,min(r,n-r)+1):
            cmd = (cmd*(n-i+1)*inv[i])%mod
        return cmd

    def permmod(self,n, r, mod):#nPr % mod
        perm = 1
        for i in range(n,r-1,-1):
            perm = (perm*i)%mod
        return perm

    def modPow(self,a,n,mod):#繰り返し二乗法 a**n % mod
        if n==0:
            return 1
        if n==1:
            return a%mod
        if n % 2 == 1:
            return (a*self.modPow(a,n-1,mod)) % mod
        t = self.modPow(a,n//2,mod)
        return (t*t)%mod