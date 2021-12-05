import matplotlib.pyplot as plt
def percent_added(per, amount):
    val = amount * (per/100)
    final_val = amount + val
    return final_val

def ci(p, n, r, t, m):
    x1 = [0]
    graph_dict_1 = [10000]
    graph_dict_2 = [10000]
    alpha = p
    monthly_amount_investment = p
    x = t
    a = p
    c = n
    y = m*12
    h = m*6
    q = m*3
    # m = m
    d = m*12/365
    year_number = 0
    while x>0:
        while c>0:
            if n==1:
                monthly_amount_investment +=y
                a = percent_added(r, a)
                a += y
            elif n==2:   
                monthly_amount_investment +=h
                a = percent_added(r/2, a)
                a += h
            elif n==4:  
                monthly_amount_investment +=q
                a = percent_added(r/4, a)
                a += q
            elif n==12:
                monthly_amount_investment +=m
                a = percent_added(r/12, a)
                a += m
            elif n==365:
                monthly_amount_investment +=d
                a = percent_added(r/365, a)
                a += d
            # print(f"month ended value {alpha}-{a}")
            c -=1
        c = n
        x -=1
        year_number +=1
        x1.append(year_number)
        graph_dict_1.append(monthly_amount_investment)
        graph_dict_2.append(a)
        # print(f"year ended value{a}")
    # print(graph_dict)
    plt.cla()
    plt.plot(x1, graph_dict_1, label = "investment", marker='o', markersize=12)
    plt.plot(x1, graph_dict_2, label = "return", marker='o', markersize=12)
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Results')
    plt.legend()
    if __name__ == '__main__':
        
        plt.show()
    plt.savefig('static/foo.png')
    if n==1:
        pr = p+(y*n*t)
    elif n==2:
        pr = p+(h*n*t)
    elif n==4:
        pr = p+(q*n*t)
    elif n==12:
        pr = p+(m*n*t)
    elif n==365:
        pr = p+(d*n*t)
    # defining interest
    i = a - pr
    # Show results
    if __name__ == '__main__':
        print(f"Principle = {p} \nRate of interest = {r} % \nTotal amount invested= {pr} \nTotal amount got = {a}\nCompound interest = {i}")
    total_percentage(pr, i)
    tp = total_percentage(pr, i)
    api_return = {
        "":[1, 2],
        "Principle":f"{p} ₹",
        "Rate of interest":f"{r} %",
        "Total amount invested" : f"{pr} ₹",
        "Total amount received": f"{a} ₹",
        "Compound interest" : f"{i} ₹",
        "All over profit": f"{tp} %",
        "Data for graph preparation": monthly_amount_investment
    }
    return(api_return)



def total_percentage(p, i):
    p = float(p)
    i = float(i)
    percentage = i/p*100
    if __name__ == '__main__':
        print(f"Total profit = {percentage} %")
    return percentage

if __name__=="__main__":
    p = int(input("Enter Princilpe Value:-\n"))
    r = float(input("Enter rate of interest per annum:-\n"))
    # n = int(input("Enter number of times compound in a tenure:-\n"))
    t = int(input("Enter number of years:-\n"))
    abc = input("Enter 'y' for yearly deposits and 'm' for monthly deposits")
    if abc == "m":
        m = float(input("Enter monthly contributions:-\n"))
    elif abc == "y":
        m = float(input("Enter yearly contributions:-\n"))
        m = m/12
    xyz = input("Enter 'y' for yearly, 'h' for half yearly, 'q' for quarterly, 'm' for monthly, 'd' for daily compoundation")
    if xyz == "y":
        n = 1
    elif xyz =="h":
        n = 2
    elif xyz =="q":
        n = 4
    elif xyz =="m":
        n = 12
    elif xyz =="d":
        n = 365
    
    ci(p, n, r, t, m)
