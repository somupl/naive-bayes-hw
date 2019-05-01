from bayescoin import BayesCoin

bd = BayesCoin()
bd.choose_coin()

for _ in range(10):
    flip = bd.flip_coin()
    bd.update_priors(flip)

print('-' * 50)
ans = max(bd.prior.keys(), key=(lambda k: bd.prior[k]))
print('experimental ans is {} and actual ans is {}'.format(ans, bd.coin))
