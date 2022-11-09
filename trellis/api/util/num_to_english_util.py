ref = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'one hundred'
}

h = 100
k = 1000
m = k * k
b = m * k
t = b * k
q = t * k
z = q * k
s = z * k

labels = {
    h: 'hundred',
    k: 'thousand',
    m: 'million',
    b: 'billion',
    t: 'trillion',
    q: 'quadrillion',
    z: 'quintillion',
    s: 'sextillion'
}


def get_previous_scale(scale):
    if scale == k:
        return h
    return int(scale / k)


def get_greater_and_label():
    greater = list(labels.keys())[-1]
    label = labels[greater]
    return greater, label


def to_english(num):
    if num < 0:
        raise Exception('numbers less than 0 are not allowed')

    max_number, label = get_greater_and_label()
    if num > max_number:
        raise Exception('numbers greater than one ' + label + ' are not allowed')

    if num in ref:
        return ref[num]

    if num < h:
        if num % 10 == 0:
            return ref[num]

        return ref[num // 10 * 10] + '-' + ref[num % 10]

    for scale in labels.keys():
        if not num < scale:
            continue

        p_scale = get_previous_scale(scale)
        label = labels[p_scale]

        partial_result = to_english(num // p_scale) + ' ' + label + ' '
        if num % p_scale == 0:
            return partial_result

        return partial_result + to_english(num % p_scale)

    raise Exception('samething is wrong')
