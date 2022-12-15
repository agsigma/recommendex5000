# Rescalex & recommendex 5000

## Overview

System designed to:

* Convert data regarding movies ratings to individual scales showing level of interest of particular user in given category. E.g. for user `Amy` we would like to know how high she is placed on `Science fiction` scale and be able to compare her score to scores of other users.
* Find users similar to selected user using only data about scales scores, not individual ratings given to movies.
* Recommend movies basing on top picks from similar users (so information about scores is not removed from data, we only decide to not use it during finding similar users)   

## General remarks

Rule: **All scripts must be run from repo root**.

## Data

* Data was downloaded from `https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset`. Archive must be placed in `data/` directory.
* `./scripts/prepare_data.sh`

