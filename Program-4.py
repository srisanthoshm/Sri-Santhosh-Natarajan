try:
    nums=[1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    result={}
    for i in range(1, 10):
        count=0
        for n in nums:
            if n % i==0:
                count+=1
        result[i]=count
    print(result)
except Exception as e:
    print("Error:", e)
