#Exchange rates problem

def main():

    exchanges = [["GBP","USD",1.3572132],["GBP","EUR",1.196638],["JPY","USD",0.0086445116]];
    currencyFrom = "EUR";
    currencyTo = "JPY";

    print(findExchange(exchanges,currencyFrom,currencyTo));

def findExchange(exchanges, currencyFrom, currencyTo):
    
    for exchange in exchanges:

        if currencyFrom == exchange[0]:
            #If the exchange rate exists perfectly in the list
            if currencyTo == exchange[1]:
                return exchange[2];
            
            #If the exchange exists. Call to see if 'new currency' can exchange to currencyTo
            else:
                return exchange[2]*findExchange(exchanges,exchange[1],currencyTo);

        elif currencyFrom == exchange[1]:
            #If the exchange rate exists, but reversed, in the list
            if currencyTo == exchange[0]:
                return 1/exchange[2];

            #If the exchange exists reversed. Call to see if 'new currency' can exchange to currencyTo
            else:
                return (1/exchange[2])*findExchange(exchanges,exchange[0], currencyTo);
        
        else:
            print("Error, exchange rate does not exist in exchanges -", currencyFrom);
main();