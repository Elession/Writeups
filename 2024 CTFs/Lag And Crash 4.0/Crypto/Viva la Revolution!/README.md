## Writeup

- Difficulty: Easy
- Description: Viva la Revolution my friend! we shall overtake the government!
- Flag: `LNC24{pR1m3s_4eva!}`

We are provided with the source code and the output.txt file.

`p` and `q` values suggest that this is RSA cryptography.

```python
def X9sm_4sF(zWQ):
    p, q = 0, 0
    while not isPrime(p):
        p = random.getrandbits(zWQ) + random.getrandbits(zWQ // 20)
    while not isPrime(q):
        q = random.getrandbits(zWQ) + random.getrandbits(zWQ // 10)
    return p, q
```

This function generates p and q values which will always be prime.

Since `N = z * Z`, or better known as `N = p * q`, we can go to [factordb.com](http://factordb.com), a site that can help us solve for the `p` and `q` values.

![](./images/img1.png)

Great! We can directly solve for `phi` value and decipher the cipher text with our solve script.

For better clarity, in order to decrypt RSA,

1. We must find the private exponent (d), which satisfies the following:

`de ≡  1 mod ϕ(n)`

2. To decrypt RSA ciphertext:

`M = C**d mod n`
