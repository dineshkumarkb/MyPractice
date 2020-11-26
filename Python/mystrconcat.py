import time
start_time = time.time()

s = "Python "
s1 = "is "
s2 = "a programming "
s3 = "language"

final_str = ""

final_str += s
final_str += s1
final_str += s2
final_str += s3

end_time = time.time() - start_time
print(final_str, end_time)

