# carbon-growth-fitting

creating spatially explicit natural forest carbon growth images is a multi step process that involves:
 
1. generate growth function data from chart images.
2. fit the growth curve (chapman-richards) to the generated data to derive the coefficients.
3. create a map that is the combination of two geographic ranges (continental regions, and climatic regions) and calculate forest carbon growth for N years using the coefficients for each spatially explicit area.

A completed version of the carbon json is provided (`cabon_completed.json`). The codes represent the combination of continental  regions and FAO Global Ecological Zones that have been grouped into humid and dry areas.

## 1. generate growth function data from chart images.

Growth curve charts were found in the appendix of Blanca et al. 2018. These images were then converted into csv's representing the data using [automeris.io](https://apps.automeris.io/wpd/).

## 2. fit the growth curve (chapman-richards) to the generated data to derive the coefficients.

Using `./notebooks/carbon_loop.py` will fit the chapman-richards function to each csv and write out a json file with the coefficients and name of the region of natural forest growth (e.g. "Natural Asia Dry")

Note: This json is only partly complete. It is edited in the following step to incorporate the continental and climatic regions.

## 3. create a map that is the combination of two geographic ranges (continental regions, and climatic regions) and calculate forest carbon growth for N years using the coefficients for each spatially explicit area.

Using `./notebooks/curves_to_fc.py` follow the directions to update the json file for the unique region based on continental and climatic region. 

