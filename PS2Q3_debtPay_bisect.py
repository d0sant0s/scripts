# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:08:49 2016

@author: EvanDeCastros
"""

def debtPay(balance, annualInterestRate, lowPay, highPay):
    month = 0
    newBal = balance
    guessPay = (lowPay + highPay) / 2
    while abs(guessPay - lowPay) >= 0.02 and month < 12:
        month += 1
        newBal -= guessPay
        newBal = round(newBal + (newBal * (annualInterestRate / 12)), 2)
    if month == 12 and newBal > 0:
        lowPay = guessPay
        return debtPay(balance, annualInterestRate, lowPay, highPay)
    elif month == 12 and newBal < 0:
        highPay = guessPay
        return debtPay(balance, annualInterestRate, lowPay, highPay)
    return print('Lowest Payment: ', round(guessPay, 2))

balance = 320000
annualInterestRate = 0.2
lowPay = balance / 12
highPay = (balance * (1 + (annualInterestRate/12))**12) / 12
debtPay(balance, annualInterestRate, lowPay, highPay)
