
# tuning using bayesian method

import optuna
from optuna.samplers import TPESampler


def obj_fun(trial):
    
    max_depth= trial.suggest_int('max_depth', 1, 100)
    max_features= trial.suggest_int('max_features', 1, 20)
    max_leaf_nodes= trial.suggest_int('max_leaf_nodes', 2, 8)
    
    regr = DecisionTreeRegressor(max_depth=max_depth,
                                max_features=max_features,
                                max_leaf_nodes=max_leaf_nodes
                                )
    cat = ['transaction_year', 
           'transaction_month', 
           'transaction_dayname', 
           'number of convenience stores',
           'house age bins',
           'dist of MRT bins'
      ]
    num = ['house age', 'dist to nearest MRT', 'latitude', 'longitude']

    ohe = OneHotEncoder()
    sc = StandardScaler()

    col_trans = ColumnTransformer([('encoder', ohe, cat), 
                               ('scaler',sc, num)])

    pipe= Pipeline(steps=[('column_transformer', col_trans), ('regressor', regr)])
    
    pipe.fit(X_train, y_train)
    val_acc = pipe.score(X_test, y_test)
    
    return val_acc 
