#A four-digit integer is given. Find the number of even digits in it.
def var_int(x):
    a=x%10
    a1=(a%2+1)%2
    x//=10

    b=x%10
    b1=(b%2+1)%2
    x//=10

    c=x%10
    c1=(c%2+1)%2
    x//=10

    d=x%10
    d1=(d%2+1)%2

    return a1+b1+c1+d1
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
print(var_int(4455))