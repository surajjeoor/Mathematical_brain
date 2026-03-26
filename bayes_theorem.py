def posterior_bayes_theorem(likelihood,prior,false_positive_rate):
    '''
    Parameters:
    prior:float
    P(Hypothesis):Thats the probability of hypothesis
    
    likelihood:float
    P(Evidence|Hypothesis): its the probability where the hypothesis is true.
    
    false_positive_rate:float
    P(Evidence|¬Hypothesis): its the probability of Evidence given Hypothesis is wrong.
    
    Returns
    posterior:float
    P(Hypothesis|Evidence):probability of evidence given hypothesis
    
    '''
    
    #calculating P(Evidence)
    Evidence=(likelihood*prior)+(false_positive_rate*(1-prior))
    
    posterior=(likelihood*prior)/(Evidence)
    
    return posterior
    
if __name__=="__main__":
    prior=0.01
    sensitivity=0.95
    fpr=0.05
    prob=posterior_bayes_theorem(prior,sensitivity,fpr)
    print(f"Prior probablity before test:{prior:.1%}")
    print(f"Posterior probability after testing:{prob:.1%}")
    print(f"Test increased from confidence {prior:.1%} to {prob:.1%}")
