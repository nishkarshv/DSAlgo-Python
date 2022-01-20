def numberToWords( num):
    onedict = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    twolessdict = {
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }
    tendict = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }
    def two(num):
        if not num:
            return ''
        elif num<10:
            return onedict[num]
        elif num<20:
            return twolessdict[num]
        else:
            tens = num//10
            res = num - tens*10
            return tendict[tens] + ' ' + onedict[res] if res else tendict[tens]
    def three(num):
        hundred = num//100
        res = num-hundred*100
        if hundred and res:
            return onedict[hundred] + ' Hundred ' + two(res)
        elif not hundred and res:
            return two(res)
        elif hundred and not res:
            return onedict[hundred] + ' Hundred'

    billion = num//1000000000
    million = (num-billion*1000000000)//1000000
    thousand = (num-billion*1000000000-million*1000000)//1000
    res = num - billion*1000000000-million*1000000-thousand*1000
    if not num:
        return 'Zero'
    result = ''
    if billion:
        result = three(billion) + ' Billion'
    if million:
        result += ' ' if result else ''
        result += three(million) + ' Million'
    if thousand:
        result += ' ' if result else ''
        result += three(thousand) + ' Thousand'
    if res:
        result += ' ' if result else ''
        result += three(res)
    return result

print(numberToWords(128888888883))
