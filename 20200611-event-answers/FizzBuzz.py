for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 15 == 0:   #15の倍数の時
        string = 'FizzBuzz'
    elif num % 3 == 0:  #3の倍数の時
        string = 'Fizz'
    elif num % 5 == 0:  #5の倍数の時
        string = 'Buzz'
    else:               #その他の時
        string = num
    '''
    #上の式を三項演算子を用いて一文で記述(動作確認済み)
    string = 'FizzBuzz' if num % 15 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz'\
     if num % 5 == 0 else num
    '''
    # ここまで記述

    print(string)
