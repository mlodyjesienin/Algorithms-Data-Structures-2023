'''TRESC:
Podczas Twoich praktyk zawodowych w biurze śledczym otrzymałeś zadanie dostania się do
pewnego zabezpieczonego hasłem laptopa. Jedyną podpowiedzią jaką zostawił przestępca
był pewien ciąg cyfr wyrażony jako string S. Odkryto już, że w rzeczywistości podpowiedź
pozostawiona przez przestępcę była pewną tajną wiadomością, która została zakodowana
poprzez zamienienie liter na znaki (tak np. A = 1, B = 2, …, Z = 26) oraz, że hasło ustawione
przez przestępcę to tak naprawdę liczba wyrażająca całkowitą liczbę różnych wiadomości,
które mogą ukrywać się pod zakodowanym ciągiem. Twoim zadaniem jest napisanie
algorytmu, który zwróci poprawne hasło niezbędne do zalogowania się do laptopa. Możesz
przyjąć, że pusty ciąg ma tylko 1 rozwiązanie, a niepoprawne wiadomości 0 rozwiązań
(przez niepoprawne można uznać np. takie, które posiadają dwa zera pod rząd, z których nie
da się odczytać żadnej litery)
'''

from zad6ktesty import runtests 

def haslo ( S ):
    n = len(S) 
    if n==0:
        return 1

    T = [0 for _ in range(n)] 
    T[0] = 1
    a = 10*int(S[0]) + int(S[1]) 
    if 0<a and a<27:
        T[1] = 2 
    else:
        T[1] = 1
    for i in range(2,n):
        if S[i] == '0':
            if S[i-1] == '1' or S[i-1] == '2':
                T[i] = T[i-2]
            else:
                return 0
        else:
            a = 10*int(S[i-1]) + int(S[i]) 
            if 10 < a and a<27 :
                T[i] = T[i-1] + T[i-2] 
            else:
                T[i] = T[i-1] 
        
    return T[n-1]

runtests ( haslo )