#hàm kiểm tra số nguyên tố
def check_prime_number(n):

    flag = 1
    if (n <2):
        flag = 0
        return flag  
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break 
    return flag

check_prime_number(11)

def check_min_2_prime(a):
    
  count=0
  for i in range(0,len(a)):
    if(check_prime_number(a[i])==1):  # nếu a[i ] là số nguyên tố
     count=count+1 # tăng biến đếm
  if count>=2:
    return True
  else :
    return False


#mảng không có số nguyên tố
a=[1,4,6,8]
res=check_min_2_prime(a)
res

#mảng có 1 số nguyên tố
a=[1,2,4,6]
res1=check_min_2_prime(a)
res1

#mảng  nhiều hơn  2 số nguyên tố
a=[1,2,3,5]
res2=check_min_2_prime(a)
res2