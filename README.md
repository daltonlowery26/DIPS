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

### Model Plan 4/7 (very fluid)

- I want to pull many regression methods together to try to find mean
- xgboost model to predict mean preformance for player
- use nearest neighbor to find closest 5 neighbors and then compare next season preformance
- combine these two methods together with cleaver weighting to try to find a mean (need to create mult models for each bc of lack of stat avial)
- only use these two models to predict rate stats, not PA, Def, or BSR
- then create a diffrent model to predict PA
- then calculate batting run value (can you calc straight from wOBA or do you need a model?)
- then add Def and BSR value
- need to predict std for each player season and project precentile outcomes
- monte carlo simulation to find mean projected value
- Predicted WAR
