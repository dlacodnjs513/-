def display_multiplication_table():
    for i in range(2, 10):  
        print(f"{i}단")
        for j in range(1, 10):  
            print(f"{i} x {j} = {i * j:2d}")
        print()  

display_multiplication_table()
