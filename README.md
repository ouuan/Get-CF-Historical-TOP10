# Get CF Historical TOP10

## How to use it?

Run `getHandles.py`, `getInactiveHandles`, `getCountries.py`, `getData.py` and `dataToCsv.py` in order (or run `runall.bat` in Windows), then you will get `data.csv` in the format which fits [Jannchie](https://github.com/Jannchie)/[**Historical-ranking-data-visualization-based-on-d3.js**](https://github.com/Jannchie/Historical-ranking-data-visualization-based-on-d3.js)

## How does it work?

I get the rating history of each user **who is in the top10000 either of the active or the inactive now** by Codeforces API. So if a user was in the top10 but is in neither the top10000 of the active nor the inactive now, he will not be included in the historical top10s.

See the codes for more details. (However, I'm not good at python, so the codes may be a little ugly.)

## See the video!

The video is uploaded [here](https://www.bilibili.com/video/av43450831/). Also [on YouTube](https://youtu.be/nfAnKzyiKTo), uploaded by [Anguei](https://github.com/Anguei). 