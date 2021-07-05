# Trustee-gov-pairing
Pairing software for governors and trustees for circle k international

please run on python 3

## How to use:
1) ensure all files and the .py file are in the same folder
2) Ensure that all files are in CSV format
3) run the following command:
```python3
python3 pairing.py "gov.csv" "trustee.csv"
``` 
>note that "gov.csv" & "trustee.csv" can be any named files, the order is all that matters

## Output data
* The output of all the analysis will be in a subfolder from your current directory called "output"
* Each assement score on personalized analyzes will be out of a maxiumum of 100 points
  + District scores are representive of the need in the district
  + Trustee scores represent their overall strength in the area
* The pairing output sheet ranks all available trustees on overall matching in over 16 areas
>1 being most compatible ---- 6 being least compatible.
