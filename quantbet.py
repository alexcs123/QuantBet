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
    p, s = float(response.text.split('point is ')[1][:4]), [int(n) for n in response.text.split('the set ')[1][0:3:2]]
    g = p ** 4 * (1 + 4 * (1 - p) + 10 * (1 - p) ** 2) + sum([20 * 2 ** n * p ** (n + 5) * (1 - p) ** (n + 3) for n in range(100)])
    data = {'answer': (comb(sum(s) - 1, min(s)) if sum(s) < 12 else 252) * g ** s[0] * (1 - g) ** s[1]}
    print(post('https://quantbet.com/submitQuant', data=data, cookies=response.cookies).text.split('div>')[5][:-2])


if __name__ == '__main__':
    dev()
    quant()
