def compound_interest(p,t,r):
    ci = p*(pow((1 +r /100),t))
    print("The compound interest is:",ci)
    return ci
compound_interest(12,9,8)