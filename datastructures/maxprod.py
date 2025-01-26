
def maxsubarrayproduct(A):
    n = len(A)
    global_max_pos = 0
    global_max_neg = 0
    pos_atual = 1
    neg_atual = 1

    for i in range(0, n):

        if A[i] > 0:
            pos_atual = pos_atual * A[i]
            if neg_atual != 1:
                neg_atual = neg_atual * A[i]

        else:
            if A[i] < 0:
                if neg_atual == 1:
                    neg_atual = pos_atual * A[i]
                    pos_atual = 1
                else:
                    pos_atual, neg_atual =  swap(pos_atual, neg_atual)
            else:
                pos_atual  = 1
                neg_atual =  1

        if pos_atual > global_max_pos:
            global_max_pos = pos_atual

        if neg_atual < global_max_neg:
            global_max_neg = neg_atual

        if pos_atual < 1:
            pos_atual = 1

    return global_max_pos

def swap(t1, t2):
    return t2, t1

for case in [2,5,-1,-2,-4], [1,2,0,-4,5,6,0,7,1], [1,2,0,-4,5,6,-1,-1,0,10,10]:
    print maxsubarrayproduct(case)

