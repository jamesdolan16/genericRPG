import random
import time

class Rng:
    def __init__(self):
        pass
    
    def randomNumber(self, centre, inaccuracy, change):
        """sampled triangular distribution"""
        sample = inaccuracy
        centreProbability = 0.5
        # say inaccuracy is 300, then the chance of getting the centre
        # is 1/3, if it's 500, it's 1/5, etc.
        amountOfSamples = sample * 2 + 1
        # so it's an odd number of samples
        """smallestProbability = (1 - sample * centreProbability
                               ) / (sample + 1)
        probabilityDifference = (amountOfSamples * centreProbability
                                 - 1) / (sample ** 2 + sample)"""
        probabilityDifference = centreProbability / sample
        probabilityCurve = [centreProbability - i * probabilityDifference
                            for i in range(sample + 1)]
        probabilities = [i for i in probabilityCurve[1:-1][::-1]]
        probabilities += [i for i in probabilityCurve[:-1]]
        mappedProbabilities = []
        mappedProbabilities += map(lambda x: x / sum(probabilities), probabilities)
        MAX_RANDOM = 10000
        randNumber = random.randint(0, MAX_RANDOM)
        probabilitySoFar = 0
        randomIndex = 0
        for i in range(len(mappedProbabilities)):
            probabilitySoFar += mappedProbabilities[i]
            if randNumber < MAX_RANDOM * probabilitySoFar:
                randomIndex = i
                break
        return centre + (sample - randomIndex - 1) * change





