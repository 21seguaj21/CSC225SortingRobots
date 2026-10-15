# CSC 225 — Sorting Robot Lottery: Results

**Random seed:** ____3____  
**Algorithm 1:** ____Selection____  
**Algorithm 2:** ____Heap____

The driver generates **50 random lists of 100 integers each**. Both algorithms receive the same list for each run. Paste the 50 comparison counts from the program for each algorithm below (rather than filling in a 50-row table).

**Algorithm 1 counts (50 runs):**

```text
   1 Selection             336
   1 Heap                 1017
   2 Selection             313
   2 Heap                 1032
   3 Selection             309
   3 Heap                 1022
   4 Selection             298
   4 Heap                 1030
   5 Selection             290
   5 Heap                 1023
   6 Selection             337
   6 Heap                 1008
   7 Selection             332
   7 Heap                 1011
   8 Selection             342
   8 Heap                 1016
   9 Selection             299
   9 Heap                 1024
  10 Selection             335
  10 Heap                 1018
  11 Selection             309
  11 Heap                 1027
  12 Selection             271
  12 Heap                 1005
  13 Selection             344
  13 Heap                 1023
  14 Selection             310
  14 Heap                 1025
  15 Selection             302
  15 Heap                 1017
  16 Selection             330
  16 Heap                 1010
  17 Selection             316
  17 Heap                 1019
  18 Selection             305
  18 Heap                 1028
  19 Selection             309
  19 Heap                 1045
  20 Selection             326
  20 Heap                 1038
  21 Selection             285
  21 Heap                 1028
  22 Selection             290
  22 Heap                 1031
  23 Selection             302
  23 Heap                 1031
  24 Selection             331
  24 Heap                 1023
  25 Selection             296
  25 Heap                 1025
  26 Selection             295
  26 Heap                 1029
  27 Selection             289
  27 Heap                 1019
  28 Selection             314
  28 Heap                 1021
  29 Selection             312
  29 Heap                  999
  30 Selection             326
  30 Heap                 1022
  31 Selection             336
  31 Heap                 1037
  32 Selection             302
  32 Heap                 1035
  33 Selection             360
  33 Heap                 1036
  34 Selection             290
  34 Heap                 1041
  35 Selection             323
  35 Heap                 1038
  36 Selection             332
  36 Heap                 1021
  37 Selection             326
  37 Heap                 1021
  38 Selection             327
  38 Heap                 1022
  39 Selection             321
  39 Heap                 1022
  40 Selection             344
  40 Heap                 1025
  41 Selection             342
  41 Heap                 1037
  42 Selection             315
  42 Heap                 1036
  43 Selection             330
  43 Heap                 1025
  44 Selection             300
  44 Heap                 1031
  45 Selection             320
  45 Heap                 1023
  46 Selection             312
  46 Heap                 1013
  47 Selection             329
  47 Heap                 1030
  48 Selection             351
  48 Heap                 1027
  49 Selection             317
  49 Heap                 1017
  50 Selection             304
  50 Heap                 1032
```

**Algorithm 2 counts (50 runs):**

```text

```

| Statistic | Algorithm 1 | Algorithm 2 |
|---|---:|---:|
| Average | 316.69 | 1024.7 |
| Median | 315.5 | 1024.5 |
| Minimum | 271 | 999 |
| Maximum | 360 | 1045 |
| Population standard deviation | 18.98 | 9.32 |

**Which algorithm used fewer comparisons across the 50 runs?**

Selection

**One interesting observation:**
Heap had a smaller SD, so on average it did close to the same number of steps as selection 
