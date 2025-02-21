import numpy as np
def getBondPrice(y, face, couponRate, m, ppy=1):
    couponPayment = face * couponRate / ppy
    mppy = m * ppy
    t = np.arange(1, mppy + 1)
    pv = 1 / (1 + y/ppy) ** t

    cf = np.full(mppy, couponPayment)
    cf[-1] += face

    pvcf = cf * pv

    price = np.sum(pvcf)

    return price
