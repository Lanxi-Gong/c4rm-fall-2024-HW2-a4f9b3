import numpy as np

def getBondDuration(y, face, couponRate, m, ppy):
    coupon = (couponRate * face) / ppy
    t = np.arange(1, m * ppy + 1) / ppy
    discount_factors = (1 + y / ppy) ** (-t * ppy)
    
    pv_coupons = coupon * discount_factors
    pv_face = face * discount_factors[-1]
    pv_total = np.sum(pv_coupons) + pv_face
    
    weighted_time = np.sum(t * pv_coupons) + t[-1] * pv_face
    
    duration = weighted_time / pv_total
    
    return duration
