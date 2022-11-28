# TPhosphorousExportCModel
This repository includes the python code of two models that can be used to predict total phosphorous export coefficients from a system of linear equations.
The system of linear equations is solved with the implementation of the Bayesian optimization algorithm (Hyperopt)(Bergstra et al 2013, Bergstra et al 2013). 

The results of this study are described in the following manuscript: 
**Almeida, M.C., Rodrigues, A.C. and Coelho P.S.: A methodology to improve the accuracy of Total Phosphorous diffuse loads estimates from agroforestry watersheds**:


## Input data
Model 1 - Hyper_export_rates_Phosphorous_v1.py - Only agricultural export coefficients are optimized;
Model 2 - Hyper_export_rates_Phosphorous_v2.py - All land uses export coefficients are optimized.

## Input data

In the folder Input data we have included 2 input files:

1) p_livestock.xlsx - with the following 3 columns:
Station - Watershed station number;
p_livestock - Total P livestock export coefficient (kg/ha.year)
p_observed - Total P observed export coefficient (kg/ha.year).

2) p_soil_use.xlsx - with the following 10 columns:
Station - Watershed station number;
Artificialized_territories - 	land use area, km<sup>2</sup>;
Agriculture - land use area, km<sup>2</sup>;
Pasture - land use area, km<sup>2</sup>;
Agroforestry - land use area, km<sup>2</sup>;
Forest - land use area, km<sup>2</sup>;
Shrubland - land use area, km<sup>2</sup>;
Open_spaces - land use area, km<sup>2</sup>;
Wetland	Waterbodies - land use area, km<sup>2</sup>.


## Hyperparameter optimization
In the following table we have included the Hyperopt parameters

#### Table1. Model parameters and optimization range
Parameter|	Optimization range
---- | ------------------ |
Parameter search space   |[0.01, 5]
n_EI_candidates   |50
gamma   |0.2
n_startup_jobs   |20
max_evals  |1000

## How to run the hyperoptimization algorithm
1. Install neupy from the [neupy webpage](http://neupy.com/pages/installation.html);
2. Create an empty folder;
3. In this folder place the python code file (e.g. Hyper_export_rates_Phosphorous_v1.py) and the input files (e.g. p_livestock.xlsx; p_soil_use.xlsx);
4. Run the code. The output includes a file (e.g. resuls_all.csv) with the following columns:
Station - Watershed station number;
Agric - Total P agricultural export coefficient (kg/ha.year);
Agroforestry - Total P agroforestry export coefficient (kg/ha.year);
Forest - Total P forest export coefficient (kg/ha.year);	
Past - Total P pasture export coefficient (kg/ha.year);
Shrubland - Total P shrubland export coefficient (kg/ha.year).


## References
Almeida, M.C. and Coelho P.S.: Modeling river water temperature with limiting forcing data,...

Bergstra, J. S., Bardenet, R., Bengio, Y. and Kegl, B.: Algorithms for hyper-parameter optimization, in Advances in Neural Information Processing Systems, 2011, 2546–2554, 2011.

Bergstra, J., Yamins, D., Cox, D. D.: Making a Science of Model Search: Hyperparameter Optimization in Hundreds of Dimensions for Vision Architectures. TProc. of the 30th International Conference on Machine Learning (ICML 2013), 115-23, 2013.

