from requests import get, post
from math import gcd
from scipy.special import comb


def dev():
    response = get('https://quantbet.com/quiz/dev')
    numbers = response.text.split('strong>')
    data = {'divisor': gcd(int(numbers[1][:-2]), int(numbers[3][:-2]))}
    print(post('https://quantbet.com/submit', data=data, cookies=response.cookies).text.split('div>')[5][:-2])


def quant():
    response = get('https://quantbet.com/quiz/quant')
    a = float(response.text.split('point is ')[1][:4])
    aa = int(response.text.split('the set ')[1][0])
    bb = int(response.text.split('the set ')[1][2])
    c = comb(aa + bb - 1, min(aa, bb))
    if aa + bb == 12:
        c = 252
    elif aa + bb == 13:  # tiebreak never happens
        c = 504
    g = a ** 4 * (1 + 4 * (1 - a) + 10 * (1 - a) ** 2)
    for n in range(100):
        g += 20 * 2 ** n * a ** (n + 5) * (1 - a) ** (n + 3)
    data = {'answer': c * g ** aa * (1 - g) ** bb}
    print(post('https://quantbet.com/submitQuant', data=data, cookies=response.cookies).text.split('div>')[5][:-2])


if __name__ == '__main__':
    dev()
    quant()
