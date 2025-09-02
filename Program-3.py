try:
    a=int(input("Enter a number: "))
    if a<=0:
        print("Please enter a positive number")
    else:
        s=[]
        if a % 2==0:
            limit=a-1
        else:
            limit=a
        for i in range(1, limit + 1):
            s.append(2 * i - 1)
        print("Output:", ", ".join(str(x) for x in s))
except ValueError:
    print("Invalid input! Please enter an integer.")
