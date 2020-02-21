def card_check(card_number):
    sum=0
    digits=len(card_number)
    odd=num_digits&1
    for i in range(0,digits):
        digit=int(card_number[i])
        if not ((i&1)^odd):
            digit=digit*2
        if digit>9:
            digit=digit-9
        sum=sum+digit
    print ((sum%10)==0)
                  
    
