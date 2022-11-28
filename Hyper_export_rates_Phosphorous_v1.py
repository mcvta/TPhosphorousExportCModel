# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:40:08 2022

@author: mcva
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 11:49:50 2022

@author: mcva
"""
import pandas as pd
import functools as ft
from hyperopt import hp
from hyperopt.plotting import main_plot_vars
from hyperopt.plotting import main_plot_history
from hyperopt.plotting import main_plot_histogram
from hyperopt import base
from pprint import pprint
from sklearn.metrics import  mean_absolute_error

df = pd.read_excel (r'G:\My Drive\Python_Projects\2  - Export rates\Hyper poly model\GitHub\p_livestock.xlsx')
data = df.set_index('Station')

soil_df = pd.read_excel (r'G:\My Drive\Python_Projects\2  - Export rates\Hyper poly model\GitHub\p_soil_use.xlsx')
soil_use = soil_df.set_index('Station')

livestock = data[['p_livestock']].copy()
observed = data[['p_observed']].copy()

#===============================================================================
# Define parameters in hyperopt
#===============================================================================


def uniform_int(name, lower, upper):
    # `quniform` returns:
    # round(uniform(low, high) / q) * q
    return hp.quniform(name, lower, upper, q=1)


parameter_space = {'Agric': hp.uniform('Agric', 0.01, 5)}





#===============================================================================
# Define function to minimize
#===============================================================================
parameters_out=[]
mae_out=[]

def model(parameters):
    parameters_out.append(parameters)
    print("Parameters:")
    pprint(parameters)
    print()    
    
    # Export Rates
    Agric = parameters['Agric']
    Artif_T = 0.0
    Past = Agric/3
    Agroforestry = Agric/1.71429
    Forest = Agric/6
    Shrubland = Agric/12
    Open_spaces = 0.0
    Wetland = 0.0
    Waterbodies = 0.0
    
    #Load calculation
    
    df1 = soil_use.apply(lambda x: x/sum(x)*100, axis=1)
    
    Exp1=df1['Artificialized_territories']*Artif_T
    Exp2=df1['Agriculture']*Agric
    Exp3=df1['Pasture']*Past
    Exp4=df1['Agroforestry']*Agroforestry
    Exp5=df1['Forest']*Forest
    Exp6=df1['Shrubland']*Shrubland
    Exp7=df1['Open_spaces']*Open_spaces
    Exp8=df1['Wetland']*Wetland
    Exp9=df1['Waterbodies']*Waterbodies
    
    df2=[Exp1,Exp2,Exp3,Exp4,Exp5,Exp6,Exp7,Exp8,Exp9]
    
    
    df3 = ft.reduce(lambda left, right: pd.merge(left, right, on='Station'), df2)
    Agr_Flo = df3.sum(axis=1)/100
    
    Agr_Flo = Agr_Flo.to_frame()
    Agr_Flo.rename( columns={0 :'Agr_Flo'}, inplace=True )
    
    result = livestock['p_livestock']+Agr_Flo['Agr_Flo']
    
    mae = mean_absolute_error(result, observed)
    mae_out.append(mae)
    return (mae)
    
#===============================================================================
# run hyperparameter optimization
#===============================================================================

import hyperopt
from functools import partial


final_df = pd.DataFrame(columns=['MAE', 'Agriculture', 'Forest','Shrubland','Pasture','Agroforestry'],dtype=object)
# Object stores all information about each trial.
# Also, it stores information about the best trial.
trials = hyperopt.Trials()

tpe = partial(
    hyperopt.tpe.suggest,

    # Sample 1000 candidate and select candidate that
    # has highest Expected Improvement (EI)
    n_EI_candidates=50,

    # Use 20% of best observations to estimate next
    # set of parameters
    gamma=0.2,

    # First 20 trials are going to be random
    n_startup_jobs=20,
)

hyperopt.fmin(
    model,

    trials=trials,
    space=parameter_space,

    # Set up TPE for hyperparameter optimization
    algo=tpe,

    # Maximum number of iterations. Basically it trains at
    # most 200 networks before selecting the best one.
    max_evals=1000,
)


domain = base.Domain(model, parameter_space)
main_plot_vars(trials, domain)
main_plot_history(trials, domain)
main_plot_histogram(trials, domain)

#===============================================================================
# Export results to .csv file
#===============================================================================

df1 = pd.DataFrame (mae_out)
df1.rename( columns={0 :'MAE'}, inplace=True )
df2 = pd.DataFrame (parameters_out)
 
result = pd.concat([df1,df2], axis=1)
result_sorted = result.sort_values(by=['MAE'], axis=0)
result_sorted .to_csv('result_only_agriculture.csv') 







