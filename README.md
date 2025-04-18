# MLB Hitter Modeling

## -- Project Status: Active

## Project Intro/Objective

This repository hosts various piece of work in the steps to build a fully working MLB player model similar to ZIPS. Various expoloratory steps need to be taken first before the model is made.

## Roadmap

### Broad Steps to be taken

- Exploring aging curves for the various stats of intrest
- Use K-Nearest Neighbor to find similar seasons and compare outcomes
- Devlop XGBoost model to predict median outcome for each player season
- Determine unqiue standard dev for each player season
- Use a Monte Carlo simulation to capture such std

### DIPS (4/17)

- Split into seven diffrent parts:
  - PA Model
  - WRC+ Model
  - BsR Model
  - Def Model
  - Standard Dev Predection
  - Monte Carlo Sim
- PA Model (fluid)
  - Probably most key to WAR Calc.
  - Baseball Prospectus Injury Data, combined with age and previous PA
  - xgboost model likely applied
- WRC+ Model
  - three xgboost models without PA Data
    - seperated based on data avail (02, 15, 23)
  - three nearest neighbor models split the same way
  - indiv. model predections, combinded with expected PA feed to xgboost model
  - those predections are regressed to mean (might experiment with aging curves)
- BSR / Def (fluid)
  - much less complex
  - might just be a simple regression of publicly avial. stats and age
- Std. Dev. Predection (fluid)
  - Need to predict range of outcomes for players
  - based on model confidence as well as player age
  - likely other factors to consider
- Monte Carlo Sim (fluid)
  - either run in conjunction with xgboost model
  - run after calcuating std dev?
  - approch tbd
