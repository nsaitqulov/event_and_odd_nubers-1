#A four-digit integer is given. Find the sum of even digits in it.
def var_int(x):
    a=(x%10%2+1)%2*x%10
    x//=10

    b=(x%10%2+1)%2*x%10
    x//=10

    c=(x%10%2+1)%2*x%10
    x//=10

    d=(x%10%2+1)%2*x%10

    return a+b+c+d
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
print(var_int(8933))