credit_score = int(input('Enter credit score'))
if credit_score < 400 or credit_score > 850:
    print('Invalid Credit Score')
else:
    if 400 <= credit_score < 600:
        print('Silver Card')
    elif 600 <= credit_score < 800:
        print('Gold Card')
    else:
        print('Platinum Card')
