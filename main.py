#a->b b->c c-d
cities = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
flies = ['a->b' , 'b->c' , 'c->d' , 'd->e' , 'e->f']
def check_fly(mabda , maghsad , city , fly):
    mabdaha = [i[0] for i in flies]
    maghsadha = [i[-1] for i in flies]
    if mabda in mabdaha:
        if maghsad in maghsadha:
            if f'{mabda}->{maghsad}' in flies:
                return f'{mabda}->{maghsad}'
            else:
                
                his = [mabda]
                a = mabda
                while a != maghsad:
                    a = maghsadha[mabdaha.index(a)]
                    if a not in his:
                        his.append(a)
                    else:
                        his = his[0 : his.index(a)+1]
                ticket = str(his)
                ticket = ticket.replace('[' , '')
                ticket = ticket.replace(']' , '')
                ticket = ticket.replace(',' , '->')
                ticket = ticket.replace(' ' , '')
                ticket = ticket.replace("'" , '')
                return ticket
        elif maghsad not in maghsadha:
            return 'ma hamchin parvazi nadarim'
    elif mabda not in mabdaha:
        return 'ma hamchin parvazi nadarim'
print(check_fly('a' , 'd' , cities , flies))