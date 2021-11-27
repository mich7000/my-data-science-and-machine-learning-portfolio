
# adjusted mean absolute percentage error

def smape(pred, target):
    import numpy as np

    n = len(pred)
    masked_array= ~((pred==0) &(target==0))
    pred, target = pred[masked_array], target[masked_array]

    numerator= np.abs(pred-target)
    denominator= np.abs(pred) + np.abs(target)

    smape_val= (200 * np.sum(numerator/denominator))/n 

    return smape_val

def lgbm_smape(pred, train_data):

    labels= train_data.get_label()
    smape_val=smape(np.expm1(pred), np.expm1(labels))

    return 'SMAPE', smape_val, False
