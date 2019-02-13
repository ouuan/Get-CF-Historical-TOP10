# Get CF Historical TOP10

## How to use?

Run `getHandles.py`, `getCountries.py`, `getData.py` and `dataToCsv.py` in order (or run `runall.bat` in Windows), then you will get `data.csv` in the format which fits [Jannchie](https://github.com/Jannchie)/[**Historical-ranking-data-visualization-based-on-d3.js**](https://github.com/Jannchie/Historical-ranking-data-visualization-based-on-d3.js)

## How does it work?

It gets the rating history of each user **who is in the top5000 now** by Codeforces API. So if a user was in the top10 but is not in the top5000 now, he will not be included in the historical top10s.

## Something else...

I have manually changed **<font color="black">w</font><font color="red">xhtxdy</font>**(Du Yuhao)'s country from Samoa to China in `countries.json`.