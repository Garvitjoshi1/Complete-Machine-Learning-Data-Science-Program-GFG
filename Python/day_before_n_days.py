d = int(input("Enter the day: "))
n = int(input("Enter the before n_days: "))
list  = ['Sunday', 'Monay', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
a = (d-n)%7
print(list[a])
