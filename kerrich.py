from random import randrange

def cointoss (toss_ct=1):
    """ Tosses toss_ct number of fair coins.
        Returns number of tails and heads in a tuple. """
    tails = 0
    heads = 0
    for i in range(toss_ct):
        result = randrange(2)
        if result == 0:
            tails = tails + 1
        else:
            heads = heads + 1
    return (tails, heads)



def lawofaverages ( round_ct=1, toss_ct=1):
    """ In round_ct number of rounds, tosses toss_ct number of coins.
        Reports cumulative results in rows. """
    tot_tails = 0
    tot_heads = 0
    col_len = len(str(round_ct * toss_ct)) + 2
    if col_len < 6:
        col_len = 6 # columns must fit header

    print('{n:<{c}} {n:<{c}} {e1:<{c}}\n'.format(
                n='Num.', e1='Chance', c=col_len)
          + '{t:<{c}} {h:<{c}} {e2:<{c}}'.format(
                t='tosses', h='heads', e2='error', c=col_len))

    for i in range(round_ct):
        rnd_tails, rnd_heads = cointoss(toss_ct)
        tot_tails = tot_tails + rnd_tails
        tot_heads = tot_heads + rnd_heads

        tot_tosses = tot_heads + tot_tails
        tot_error = tot_heads - (tot_tosses/2) # is a float

        print('{t:>{c}} {h:>{c}} {e:>{c}.1f}'.format(
            t=tot_tosses, h=tot_heads, e=tot_error, c=col_len ))



def lawofaverages_ ( round_ct=1, toss_ct=1):
    """ Silent version, returns results in tuple of tuples, """
    tot_tails = 0
    tot_heads = 0
    results = []
    for i in range(round_ct):
        rnd_tails, rnd_heads = cointoss(toss_ct)
        tot_tails = tot_tails + rnd_tails
        tot_heads = tot_heads + rnd_heads

        tot_tosses = tot_heads + tot_tails
        tot_error = tot_heads - (tot_tosses/2)

        rnd_result = (tot_tosses, tot_heads, tot_error)
        results.append(rnd_result)
    return tuple(results)

        

def test ():
    lawofaverages(100, 10000)



def test_ ():
    return lawofaverages_(100, 10000)
