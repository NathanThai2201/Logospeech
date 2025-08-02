ascii_low = 32
ascii_high = 126
def decrypt(landing_input):
    input2 = cbb(landing_input)
    return input2
def cbb(landing_input):
    input2 = py(landing_input)
    input2 = p(input2)
    input2 = ec(input2)
    input2 = d(input2,0)
    input2.reverse()
    input2 = v(input2,g(200,seed=310673))
    input2 = d(input2,1)
    input2.reverse()
    input2 = v(input2,g(200,seed=569212))
    input2 = v(input2,g(200,seed=120562))
    input2 = v(input2,g(200,seed=198259))
    input2 = v(input2,g(200,seed=472810))
    input2 = v(input2,g(200,seed=331229))
    input2 = ps(input2)
    input2 = nc(input2,1)
    input2 = d(input2,0)
    input2 = e(input2)
    input2 = f(input2)
    input2.reverse()
    input2 = r(input2)
    input2 = ec(input2)
    input2 = d(input2,1)

    return input2
def d(t_input,index):
    for i in range(len(t_input)):
        if index == 0:
            temp = ord(t_input[i])-3
            index = 1
        else:
            temp = ord(t_input[i])+3
            index = 0
        if temp < ascii_low:
            temp += (ascii_high-ascii_low)+1
        if temp > ascii_high:
            temp -= (ascii_high-ascii_low)+1
        t_input[i]=chr(temp)
    return t_input
def f(t_input):
    fib = [0,1]
    i=2
    while fib[i-1]<len(t_input):
        fib.append(fib[i-1]+ fib[i-2])   
        index1 = fib[i] 
        i+=1
        fib.append(fib[i-1]+ fib[i-2])   
        index2 = fib[i] 
        i+=1
        if index1 < len(t_input) and index2 < len(t_input):
            temp =t_input[index1]
            t_input[index1] = t_input[index2]
            t_input[index2] = temp
    return t_input
def e(t_input):
    e = list(str(int(((1+1/10000)**10000)*10**18)))
    j=0
    for i in range(len(e)):
        j+=int(e[i])
        if j>len(t_input): break
        t_input.pop(j)
        j-=1
    return t_input
def nc(t_input,index):
    amount=5
    if index == 1:
        return t_input[amount:len(t_input)-amount]
    if index == 0:
        return t_input
def ps(t_input):
    i = 0
    j = len(t_input)-1
    while i<j:
        temp = t_input[i]
        t_input[i] = t_input[j]
        t_input[j] = temp
        i+=2
        j-=2
    return t_input
def v(t_input,key):
    out = []
    key_length = len(key)
    for i in range(len(t_input)):
        shift = ord(key[i % key_length]) - 32 
        decrypted_char = chr((ord(t_input[i]) - 32 - shift) % 95 + 32)
        out.append(decrypted_char)
    return out
def p(t_input):
    pi=list(str(31415926535897932384626433832795288419716939937515))
    j=0
    for i in range(len(pi)):
        j+=int(pi[i])
        if j>len(t_input): break
        t_input.pop(j)
        j-=1
    return t_input
def r(t_input):
    pad_const=9
    if t_input[0].isdigit():
        length = int(t_input[0])
        if length <= pad_const:
            for i in range(pad_const - length):
                t_input.pop(0)
            t_input.pop(0)
    else:
        t_input.pop(0)
    return t_input
def g(length, seed):
    newstr = []
    for a in range(length):
        seed = str(seed)
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~abcdefghijklmnop'
        for i in range(0, 6, 2):
            numstr = int(seed[i:i+2])
            newstr.append(characters[numstr])
        random_string = ''.join(map(str, newstr)) 
        seed = int(seed)
        seed = seed*4 + 184503 + (a*123) + (a%2)*468160 + (1-(a%2))*501764
    return random_string
def ec(t_input):
    if (len(t_input) % 2 == 0):
        index = len(t_input)//2
        one = t_input[:index]
        two = t_input[index:]
        final = two + one
        return final
    return t_input
def py(t_input):
    col = 1
    fake_pyramid = []
    original_input = t_input.copy()
    
    while t_input != []:
        layer = []
        for i in range(col):
            if t_input != []:
                layer.append(t_input[0])
                t_input.pop(0)
        fake_pyramid.append(layer)
        col+=1

    pyramid_indices = []
    a,b = 0,0

    for j in range(col):
        while a < col:
            try:
                temp = fake_pyramid[a][b]
                pyramid_indices.append([a,b])
            except:
                pass
            a+=1
            b+=1
        b-=1
        while b >= 0:
            try:
                temp = fake_pyramid[a][b]
                pyramid_indices.append([a,b])
            except:
                pass
            a-=1
            b-=1
        a+=2
        b+=1

    for i in range(len(original_input)):
        a_idx, b_idx = pyramid_indices[i]
        fake_pyramid[a_idx][b_idx] = original_input[i]

    t_input = [char for row in fake_pyramid for char in row]
    return t_input


def main():
    with open("in.txt", 'r') as file:
        landing_input = file.read()
    t_input = [i for i in landing_input]
    result = decrypt(t_input)
    final = ''.join(map(str, result))
    print(final)
if __name__ == "__main__":  
    main()