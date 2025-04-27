# MLB Hitter Modeling

## Project Intro/Objective

This repository hosts various piece of work in the steps to build a fully working MLB player model similar to ZIPS. Various expoloratory steps need to be taken first before the model is made.

## Roadmap

### Broad Steps to be taken

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
  - three xgboost models without PA Data
    - seperated based on data avail (02, 15, 23)
  - three nearest neighbor models split the same way
  - indiv. model predections, combinded with expected PA feed to xgboost model
  - predections are averged based on indiv. model preformance
  - applied basic aging curves based on player preformance change season to season
  - centered predections around 100 (mean wrc+)
- Aging Curves
  - explored using clustering to find smaller aging trends
  - did not preform any better
  - mean aging yr/yr for players since 2002
- BSR / Def (fluid)
  - much less complex
  - might just be a simple regression of publicly avial. stats and age
