def magic(n):
    # declare matrix python style
    A = [[0 for x in range(n)] for y in range(n)]
    # matrix eh l, c
    numero = 1
    l = 0
    tamanho = n * n
    c = n / 2

    while numero < tamanho:

        A[l][c] = numero
        numero += 1

        if l == 0:  # topo nao da pra ir para cima
            if c == n - 1: # ultima coluna
                l += 1
            else:
                l = n-1
                c += 1

        else:  # nao eh topo, da pra subir
            if c == n - 1:  # ultima coluna
                l -= 1
                c = 0
            else:
                if (A[l-1][c+ ] == 0):
                    l -= 1
                    c += 1
                else:
                    l += 1

    print(A)
    print('\nAll sum to magic number %i' % ((n * n + 1) * n // 2))


for n in (3, 5):
    print('\nOrder %i\n=======' % n)
    magic(n)


