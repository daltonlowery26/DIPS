# MLB Hitter Modeling

## Note

All 2025 predections (wRC+, PA, Aging), will be in final predections folder in the top level of the file structure. Projections are only for players that have played an MLB game. A seperate project will focus on minor leauge player projections.

## Project Intro/Objective

This projects MLB hitter WRC+ using three diffrent K-Nearest Neighbor Models, three xgboost models and three different models to predict PA. The WRC+ models are then averaged out based on the individual accuray of each model. The three diffrent types of models are based on the data avialiable for each time period. A three year of average of data weighted in a 60, 30, 10 was fed to all models except the 2023-2024 model. This increased accuracy as well as the stability of the projections.

## Nearest Neighbor Model

The nearest neighbor model worked by finding the 8 closest player to the target player based on the fifteen to thirty different features, depending on the model. I experimented with diffrent distance calculations such as mahalanobis distance, but ended up using eculedian as it preformed just as well to my suprise. The eight players next season wrc+ was then averaged out to predict the target players wrc+. I made a custom loss function to find the best implementation of weights as well as features for the nearest neighbors model.

## Xgboost Model

I implemnted three diffrent xgboost models based on the avialability of data. Nothing was too special about the implementation of these models. I used a random search then a grid search to find the optimal hyperparameters. I manually tuned the features based on my own baseball knowledge and assumptions about model preformance. I tried using PCA but my manual tuning preformed better

## Combining all of the Models

All the models wrc+ projections were combined together and I averaged them out. I more heavily weighted the models using older data simply because there was more data in each model causing it to preform better. All the models combined helped reduce outliers and create a quality projection. An aging curve was applied following the averaging of the models based on historical aging trends. The mean, 75th percentlie, and 25th percentile were then scaled around the historical distrubtions of wrc+ which have been very stable over the past 10 years.

### Folder Structure

- major_leauge_preds | all data and models relating to MLB player projections.
  - data | all data, cleaned and uncleaned, for models
  - final_preds | wrc+ predections for each model iteration
  - predections | models used to predict various stats
  - predicted_data | indiv. predections created by each model for each stat
- minor_leauge_preds | in progress, minor leauge to MLB translations
  - data | all data cleaned and uncleaned use

### Broad Roadmap

- Exploring aging curves for the various stats of intrest
- Use K-Nearest Neighbor to find similar seasons and compare outcomes
- Devlop XGBoost model to predict median outcome for each player season
- Determine unqiue standard dev for each player season
- Use a Monte Carlo simulation to capture such std

### DIPS 

- Split into five diffrent parts:
  - PA Model
  - WRC+ Model
  - Aging Curve
- PA Model
  - Mixture of PA, Age, and Days Missed
  - Pulled Days Missed from Fangraphs Injury Tracker
  - Created three xgboost model, looking back 1, 2, 3 years
  - weighted average of predicted values based on preformance of models
  - fed back to WRC+ models
- WRC+ Model
  - three xgboost models
    - seperated based on data avail (02, 15, 23)
    - projected next_year pa fed to model
  - three nearest neighbor models split the same way
  - predections from each model are averaged then centered around 100
  - basic aging curve applied to each player
  - predections are regressed to mean
- Aging Curves
  - explored using clustering to find smaller aging trends
  - did not preform any better
  - mean aging yr/yr for players since 2002

### Contact

- Reachout to <dalton.lowery@emory.edu> with questions or comments!
