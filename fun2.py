def draw_2d(r, n, char):
    for i in range(r):
        print(str(char)*n)

def pro_draw_2d(r, n, bs, fs):
    print(str(bs)*n)
    for i in range(r):
        print(str(bs) + str(fs)*(n-2) + str(bs))
    print(str(bs)*n)

