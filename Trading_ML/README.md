# Trading_ML

### Plan 1

* Models  ---> how can I apply boosting to all models?
   * XGBoost (or Gradient Boosted Trees)
   * Microsoft's LightGBT
* Process
   * pipeline
   * GridSearchCV or RandomSearchCV of:
      * feature selection
      * feature parameters (stochastic smoothing, etc)
* Metrics
   * Recall, Neg Log Loss, F1, AUC or RMSE/RMAE

#### Action plan
* either use 30 second cadence - done
* test what time of day the biggest moves occur - done
* train model(s) using `Process`
* potentially create an emsamble of the models - meaning take their predictions and average them out

#### Features
* Open, High, Low, Close, <all indicators> - for each 30 second period and for every period going back 30 minutes

#### Target
* % change 5 or 10 minunites in the future



### Future tweaks to try out
* build BB off of particular second's data assigning it to the next second (aka the BB for particular second is fixed at the start, rather than fluctuating during the second)
