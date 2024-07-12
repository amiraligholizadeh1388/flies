#a->b b->c c-d
cities = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
flies = ['a->b' , 'b->c' , 'c->d']
def check_fly(mabda , maghsad , city , fly):
    mabdaha = [i[0] for i in flies]
    maghsadha = [i[-1] for i in flies]
    if mabda in mabdaha:
        if maghsad in maghsadha:
            if f'{mabda}->{maghsad}' in flies:
                return f'{mabda}->{maghsad}'
            else:
                b = mabda
                his = [mabda]
                while True:
                    a = maghsadha[mabdaha.index(b)]
                    his.append(a)
                    a = maghsadha[mabdaha.index(a)]
                    his.append(a)
                    if a != maghsad:
                        b = a
                    else:
                        continue
                    ticket = str(his)
                    ticket.replace('[' and ']' , '')
                    ticket.replace(',' , '->')
                    ticket.replace(' ' , '')
                    return ticket
        elif maghsad not in maghsadha:
            return 'ma hamchin parvazi nadarim'
    elif mabda not in mabdaha:
        return 'ma hamchin parvazi nadarim'
print(check_fly('a' , 'c' , cities , flies))