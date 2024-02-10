#Αλγόριθμος 7.2.2. : Γρήγορη ύψωση σε δύναμη mod m.
def Fast_Exponentiation(b , e , m):
    B = b #Base
    result = 1
    E = e #exponent
    M = m #Μodulo
    while (E > 0):
        if ((E % 2) == 1):
            result =(result * B) % M
        E = (E // 2) #Η πράξη // εκτελεί και επιστρέφει ακέραιο αποτέλεσμα ενώ η / δεκαδικό.
        B = (B ** 2) % M
    return result

print(Fast_Exponentiation(5, 77 , 19))
