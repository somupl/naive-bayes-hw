import random


class BayesCoin:
    # ------------------------------------------------------------ #
    def __init__(self):
        self.coins = {1:0.3, 2:0.45, 3:0.75}
        self.prior = {coin: (1/3) for coin in self.coins.keys()}
    # ------------------------------------------------------------ #

    def choose_coin(self):
        self.coin = random.choice(list(self.coins.keys()))
        print('Our belief before starting the experiment is equally distributed', self.prior)
        print('-' * 50)
        print('selected coin is {}, we dont know this, we need to find through experiment and verify'.format(self.coin))
        print('-' * 50)
    # ------------------------------------------------------------ #

    def flip_coin(self):
            if random.random()<=self.coins[self.coin]:
                return 'H'# if flip is head, return 1
            else:
                return 'T' 
    # ------------------------------------------------------------ #

    def update_priors(self, flip):
        evidence = list(map(lambda coin: (self.coins[coin] if flip == 'H' else (1 - self.coins[coin]))* self.prior[coin], self.coins.keys()))
        self.prior = {i+1: individual_evidence / sum(evidence) for i, individual_evidence in enumerate(evidence)}
        self.debug(flip, evidence)
    # ------------------------------------------------------------ #

    def debug(self, flip, evidence):
        print('flip a coin')
        print('flip:', flip)
        print('evidence of getting {} based on our belief is: {}'.format(flip, evidence))
        print(' ')
        print('updating our belief based on evidence', self.prior)
        print('-' * 50)
    # ------------------------------------------------------------ #
