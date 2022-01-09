#Exchange rates problem

def main():

    exchanges = [["GBP","USD",1.3572132],["GBP","EUR",1.196638],["JPY","USD",0.0086445116]];
    currencyFrom = "EUR";
    currencyTo = "JPN";

    exchange = findExchange(exchanges,currencyFrom,currencyTo);
    if exchange:
        print("Exchange Rate from {} to {} is: {}".format(currencyFrom, currencyTo,exchange));
    else:
        print("Error in the request. Currency combination invalid: {} , {}".format(currencyFrom, currencyTo));

def findExchange(exchanges, currencyFrom, currencyTo, avoidRepeat=None):
    #adding avoidRepeat to skip past troublesome exchanges which leads to recursion error
    try:
        for exchange in exchanges:

            if currencyFrom == exchange[0]:
                #If the exchange rate exists perfectly in the list
                if currencyTo == exchange[1]:
                    return exchange[2];
                
                #If the exchange exists. Call to see if 'new currency' can exchange to currencyTo
                elif exchange[1]!=avoidRepeat:
                    return exchange[2]*findExchange(exchanges,exchange[1],currencyTo, exchange[0]);
                
                elif exchange[1]==avoidRepeat:
                    continue;

                else:
                    #If currency combination is not found
                    return False;

            elif currencyFrom == exchange[1]:
                #If the exchange rate exists, but reversed, in the list
                if currencyTo == exchange[0]:
                    return 1/exchange[2];

                #If the exchange exists reversed. Call to see if 'new currency' can exchange to currencyTo
                elif exchange[0]!=avoidRepeat:
                    return (1/exchange[2])*findExchange(exchanges,exchange[0], currencyTo, exchange[1]);
                
                elif exchange[0]==avoidRepeat:
                    continue;

                else:
                    #If currency combination is not found
                    return False;
    except TypeError as err:
        print("Unrecognised currency. It does not exist in the exchanges.")
        return False;
    
main();