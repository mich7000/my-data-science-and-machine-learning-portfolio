
# tuning using bayesian method
import optuna
from optuna.samplers import TPESampler


def obj_fun(trial):

    # set the parameters
    max_depth= trial.suggest_int('max_depth', 1, 100)
    max_features= trial.suggest_int('max_features', 1, 20)
    max_leaf_nodes= trial.suggest_int('max_leaf_nodes', 2, 8)

    #  inject the parameters in the learner.
    regr = DecisionTreeRegressor( 
                                     max_depth=max_depth, 
                                     max_features=max_features,  
                                     max_leaf_nodes=max_leaf_nodes 
                                     )

    """
    You can add use pipeline here.
    """
    
    #pipe.fit(X_train, y_train)
    #val_acc = pipe.score(X_test, y_test)
    
    return val_acc 
