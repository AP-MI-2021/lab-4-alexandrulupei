
print(""""
   1 ,Găsește ultimul număr prim mai mic decât un număr dat.
   2 , verifica daca un numar este palindrom.
   b ,Inapoi la meniu
   x, Iesire
   """"")
while True:

    option = input("Alegeti o optiune")

    if option == "1":
        def get_largest_prime_below(x):
            '''
            Determina cel mai mic numar prim mai mic decat n
            :param x: numar intreg
            :return: Cel mai mic numar prim mai mic decat n
            '''
            if (x == 1):
                return print("Nu exista numere prime mai mici decat 1!")
            if (x == 2):
                return 1
            for i in range(x-1, 0, -1):
                a = 0
                for j in range(2, i//2):
                    if i % j == 0:
                        a = 1
                if a == 0:
                    return i

        print ("Găsește ultimul număr prim mai mic decât un număr dat. Numarul dat este:")


        def test_get_largest_prime_below():
            assert get_largest_prime_below(6) == 5
            assert get_largest_prime_below(10) == 7
            assert get_largest_prime_below(100) == 97

        z = int(input())
        print(get_largest_prime_below(z))

    elif option == '2':
       def is_palindrome(n):
           '''
       Verifica daca un numar este palindrom
           :param n:  numar intreg
           :return: Retruneaza adevarat daca nr este palindrom si False in caz contrar
           '''
           if n < 10:
               return False
           ogl = 0
           aux = n
           while aux > 0:
               ogl = ogl * 10 + aux % 10
               aux = aux // 10
           if ogl == n:
               return True
           else: return False
       def test_is_palindrome():
           assert is_palindrome(1) is False
           assert is_palindrome(123421) is False
           assert is_palindrome(1234321) is True

       print("introduceti un numar:")
       w = int(input())
       if is_palindrome(w) is True:
           print("Este palindrom")
       else: print("Nu este palindrom")


    elif option == 'b':
        print(""""
   1 ,Găsește ultimul număr prim mai mic decât un număr dat.
   2 ,Verifica daca un numar este palindrom.
   b, Inapoi la meniu
   x, Iesire
   """"")

    elif option == 'x':
        break

    else:
        print("Nu ati ales o optiune valida")

