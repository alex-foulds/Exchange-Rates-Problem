# Exchange-Rates-Problem

## Introduction
Repository for implementation of the Exchange Rates Interview problem

Given 3 items: a 2d list of exchange rates, a currency to exchange from (a) and a currency to exchange to (b), work out the exchange rate going from a to b.

Example: ([["GBP", "USD", 1.36],["USD", "EUR", 0.88]] , "GBP", "EUR") would return 1.1968. Official GBP to EUR is 1.2 (07/01/22)

## Pseudo code and thoughts
### Initial Thoughts
- Use of recursion
- If currency is in the sublist[1], the exchange is 1/sublist[2]

### Pseudo Code

```
function findExchange(exchanges, currencyFrom, currencyTo)
    input currencyFrom
    input currencyTo
    input exchanges

    Loop over each exchange(sublist) in exchanges(list)

        If currencyFrom and currencyTo both in exchange
            return either exchange[2] or 1/exchange[2]
    
        Else If currencyFrom in exchange[0]
            return findExchange(exchanges, exchange[1], currencyTo)
        
        Else If currencyFrom in exchange[1]
            return findExchange(exchanges, exchange[0], currencyTo)

        Else 
            print "Currency exchange not available in input"
            return 0

```
