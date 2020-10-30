def array_check(num):

    for i in range(len(num)-2):


         if (num[i] == 1):
            if (num[i + 1] == 2):
               if (num[i + 2] == 3):
                  return True


    return False


#print(array_check([1,1,2,4,1]))

def  string_bits(mystring):

   #Logic 1

   result = ""
   for i in range(0,len(mystring),2):
      result+=mystring[i]

   print(result)


   #Logic 2

   print(mystring[::2])


string_bits("hello")




def end_other(a,b):

   a = a.lower()
   b = b.lower()

   print (a.endswith(b) or b.endswith(a))

   print(a[-(len(b)):] == b or b[-len(a):] == a)


end_other("hiabc","abc")


def double_char(mystring):

   result = ""

   for i in mystring:
      result+=i*2

   print(result)


double_char("dinesh")



# def no_teen_sum(a,b,c):
#
#    if(a in range(13,20) and not fix_teen(a)):
#       a = 0
#    elif(b in range(13,20) and not fix_teen(b)):
#       b = 0
#    elif(c in range(13,20) and not fix_teen(c)):
#       c = 0
#
#    return a+b+c
#
# def fix_teen(val):
#
#    if(val == 15 or val == 16):
#       return True


def no_teen_sum(a,b,c):

   return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):

   if n in [13,14,17,18,19]:
      n = 0

   return n


print(no_teen_sum(2,13,1))


def count_evens(nums):

   even_count = 0

   for i in nums:
      if i%2 == 0:
         even_count+=1

   return even_count


print(count_evens([1,3,5]))