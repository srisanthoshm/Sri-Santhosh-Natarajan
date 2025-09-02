try:
    a=int(input("Enter a number: "))
    if a<=0:
        print("Please enter a positive number")
    else:
        series = []
        for i in range(a):
            series.append(2*i+1)
        print("Output:", ", ".join(str(x) for x in series))
except ValueError:
    print("Invalid input! Please enter an integer.")
