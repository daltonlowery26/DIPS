# MLB Hitter Modeling

## Project Intro/Objective

This repository hosts various piece of work in the steps to build a fully working MLB player model similar to ZIPS. This is an indepentent project done for my own enjoyment and exploration. Currently, only WRC+ projections for players that played in the MLB in 2024 are completed. I am working to add WAR projections as well as projections for players that have yet to play.

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

### DIPS (4/27)

- Split into five diffrent parts:
  - PA Model
  - WRC+ Model
  - Aging Curve
  - BsR Model
  - Def Model
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
- BSR / Def (fluid)
  - much less complex
  - might just be a simple regression of publicly avial. stats and age

### Note

- Final Predections in final_preds folder
- Reachout to <dalton.lowery@emory.edu> with questions or comments!
