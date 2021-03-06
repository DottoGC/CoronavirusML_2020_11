'''
Contagios diarios COVID-19 China
22/01/2020 - 10/11/2020
Luis Fernando Lizama -201602656
'''
#Covid
import numpy as np
import matplotlib.pyplot as pyplot
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

#Covid

china = [
     0,   548,   95,  277,  486,  669,  802, 2632,  578, 2054, 1661,
  2089,  4739, 3086, 3991, 3733, 3147, 3523, 2704, 3015, 2525, 2032,
   373, 15136, 6463, 2055, 2100, 1921, 1777,  408,  458,  473, 1451,
    21,   219,  513,  412,  434,  328,  428,  576,  204,  125,  125,
   151,   153,   80,   53,   37,   27,   34,   11,   13,   32,   26,
    30,    25,   44,   54,   94,   55,  130,   63,   93,   70,  121,
   115,   102,  123,   76,   81,   82,   71,   79,   32,   59,   63,
    53,    91,   74,   58,   73,  120,   79,   93,   50,   47,  357,
    27,    18,   12,   36,   15,   16,   15,   10,    3,    6,   22,
     4,    12,    3,    0,    5,    2,    2,    2,    5,    1,   14,
    20,     1,    7,    6,    5,    9,    6,   10,    9,    0,    0,
     0,    18,    3,   11,    7,    1,    3,    0,   17,    5,   18,
     8,     7,   -1,   11,    6,    9,    5,    4,    3,   11,    7,
    12,    58,   49,   43,   44,   36,   36,    0,   59,   19,   52,
    29,    20,   28,   24,   18,   14,   23,    5,   31,   14,    8,
    19,    14,   18,   28,   33,   42,    0,   79,   46,    0,  109,
    20,    81,   75,   16,   85,  119,   86,  198,  139,  157,  179,
   189,   213,  207,  223,  276,  166,  172,  158,  114,  107,  122,
   132,   120,   92,  121,  113,   52,   87,   99,   70,   65,   96,
    66,    53,   33,   40,   49,   38,   41,   23,   34,   32,   30,
    22,    27,   32,   19,   19,   20,   33,   22,   17,   33,   20,
     9,    13,   27,   18,   23,   29,   22,   16,   18,   41,   17,
    23,    35,   12,   18,   10,   15,   17,   15,   27,   22,   23,
    17,    22,   17,   20,   25,   23,   15,   20,   41,   23,   27,
    34,    18,   28,   11,   36,   20,   30,   17,   34,   16,   22,
    29,    35,   20,   23,   24,   47,   49,   28,   40,   27,   31,
    55,    26,   31,   43,   39,   31,   43,   28,   26
]
italy = [
      0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     2,
      0,     0,     0,     0,     0,     0,     1,     0,     0,     0,     0,
      0,     0,     0,     0,     0,     0,     0,     0,     0,    17,    42,
     93,    74,    93,   131,   202,   233,   240,   566,   342,   466,   587,
    769,   778,  1247,  1492,  1797,   977,  2313,  2651,  2547,  3497,  3590,
   3233,  3526,  4207,  5322,  5986,  6557,  5560,  4789,  5249,  5210,  6203,
   5909,  5974,  5217,  4050,  4053,  4782,  4668,  4585,  4805,  4316,  3599,
   3039,  3836,  4204,  3951,  4694,  4092,  3153,  2972,  2667,  3786,  3493,
   3491,  3047,  2256,  2729,  3370,  2646,  3021,  2357,  2324,  1739,  2091,
   2086,  1872,  1965,  1900,  1389,  1221,  1075,  1444,  1401,  1327,  1083,
    802,   744,  1402,   888,   992,   789,   875,   675,   451,   813,   665,
    642,   652,   669,   531,   300,   397,   584,   593,   516,   416,   333,
    200,   318,   321,   177,   518,   270,   197,   280,   283,   202,   379,
    163,   346,   338,   301,   210,   328,   331,  -148,   264,   224,   221,
    113,   577,   296,   255,   175,   174,   126,   142,   182,   201,   223,
    235,   192,   208,   137,   193,   214,   276,   188,   234,   169,   114,
    162,   230,   231,   249,   218,   190,   128,   280,   306,   252,   274,
    254,   168,   202,   288,   382,   379,   295,   238,   159,   190,   384,
    401,   552,   347,   463,   259,   412,   476,   522,   574,   629,   477,
    320,   401,   642,   840,   947,  1071,  1209,   953,   876,  1366,  1409,
   1460,  1444,  1365,   996,   975,  1326,  1397,  1732,  1694,  1296,  1150,
   1369,  1430,  1597,  1616,  1501,  1456,  1008,  1229,  1452,  1583,  1907,
   1637,  1587,  1350,  1391,  1640,  1786,  1912,  1869,  1766,  1494,  1647,
   1850,  2548,  2499,  2843,  2578,  2257,  2677,  3677,  4458,  5372,  5724,
   5456,  4619,  5898,  7332,  8803, 10009, 10925, 11705,  9337, 10871, 15199,
  16078, 19143, 19640, 21273, 17007, 21989, 24988, 26829, 31079, 31756, 29905,
  22253, 28241, 30548, 34502, 37802, 39809, 32614, 25269, 35090
]

def plotCovid(y_data, title):
    #Creacion de datasets
    X = np.asarray(range(len(y_data)))
    Y = np.asarray(y_data)
    X = X[:, np.newaxis]
    Y = Y[:, np.newaxis]
    
    # Creacion de la regresion    
    pipeline = make_pipeline(PolynomialFeatures(6), LinearRegression())
    pipeline.fit(X, Y)

    #Graficas
    seq = np.linspace(X.min(), X.max()).reshape(-1, 1)    
    pyplot.scatter(X, Y)
    pyplot.plot(seq, pipeline.predict(seq), color="orange")
    pyplot.title(title)
    pyplot.show()


plotCovid(china, "Covid-19 - Daily cases in China")
plotCovid(italy, "Covid-19 - Daily cases in Italy")
