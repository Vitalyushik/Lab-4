def convert_to_words(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    teens = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = ['', 'одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    words = ''
    if number == 0:
        words = 'ноль'
    elif number == 10:
        words = 'десять'
    elif number < 10:
        words = units[number]
    elif 10 <= number < 20:
        words = teens[number - 10]
    elif 20 <= number < 100:
        words = tens[number // 10] + ' ' + units[number % 10]
    elif 100 <= number < 1000:
        if number % 100 == 0:
            words = hundreds[number // 100]
        else:
            words = hundreds[number // 100] + ' ' + convert_to_words(number % 100)
    elif 1000 <= number < 10000:
        if number % 1000 == 0:
            if number//1000 == 1:
                words = thousands[number//1000] + ' тысяча'
            elif 2>= number//1000 >=4:
                words = thousands[number//1000] + ' тысячи'
            else:
                words = thousands[number//1000]  + ' тысяч'
        else:
            if number//1000 == 1:
                words = thousands[number//1000] + ' тысяча ' + convert_to_words(number % 1000)
            elif 2>= number//1000 >=4:
                words = thousands[number//1000] + ' тысячи ' + convert_to_words(number % 1000)
            else:
                words = thousands[number//1000]  + ' тысяч ' + convert_to_words(number % 1000)
            
                
                
    elif 10000 <= number < 20000:
        if number % 1000 == 0:
            words = convert_to_words(number // 1000) + ' тысяч'
        else:
            words = convert_to_words(number // 1000) + ' тысяч ' + convert_to_words(number % 1000)
    elif 20000 <= number < 100000:
        if number % 1000 == 0:
            if str(number)[1] == '1':
                words = tens[number // 10000]+ ' '  + thousands[int(str(number)[1])]  + ' тысяча ' 
            elif str(number)[1] in a:
                words = tens[number // 10000]+ ' '  + thousands[int(str(number)[1])] + ' тысячи'
            else:
                words = tens[number // 10000]+ ' '  + thousands[int(str(number)[1])] + ' тысяч'
        else:
            if str(number)[1] == '1':
                words = tens[number // 10000]+ ' '  + thousands[int(str(number)[1])]  + ' тысяча ' + convert_to_words(number % 1000)
            elif str(number)[1] in a:
                words = tens[number // 10000]+ ' '  + thousands[int(str(number)[1])] + ' тысячи ' + convert_to_words(number % 1000)
            else:
                words = tens[number // 10000]+ ' '  + thousands[int(str(number)[1])] + ' тысяч ' + convert_to_words(number % 1000)  
    elif number == 100000:
        words = hundreds[number // 100000] + ' тысяч'
        
    return words

def convert_currency(number):
    number_str = str(number)
    if len(number_str) >= 2:
        if number_str[-1] == '1':
            if number_str[-2] == '1':
                return 'рублей'
            else:
                return 'рубль'
        elif number_str[-1] in a:
            return 'рубля'
        else:
            return 'рублей'
    else:
        if number_str[-1] == '1':
            return 'рубль'
        elif number_str[-1] in a:
            return 'рубля'
        else:
            return 'рублей'


    
   



