# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import csv
import sys
from pandas import ExcelWriter
from pandas import ExcelFile
from functions import *
import sys




# txt FILES
fp_clubs = '/home/kristijan/github/FootballEvolcion/Datas/Club_statstic.csv'
fp = '/home/kristijan/github/FootballEvolcion/Datas/testni_podaci.csv'
filePath ='/home/kristijan/github/FootballEvolcion/Datas/TEST_CSV.csv'
koef = "/home/kristijan/github/FootballEvolcion/Datas/file.txt"
data = "/home/kristijan/github/FootballEvolcion/Datas/datas.txt"
podaci = "/home/kristijan/github/FootballEvolcion/Datas/podaci.txt"
save_csv_a = '/home/kristijan/github/FootballEvolcion/Datas/Save_csv_Parsing_a.csv'
save_csv_b = '/home/kristijan/github/FootballEvolcion/Datas/Save_csv_Parsing_b.csv'
save_csv_c = '/home/kristijan/github/FootballEvolcion/Datas/Save_csv_Parsing_c.csv'



DFrame = DataFrameFunc(fp)
#DataF = DataFrameFuncClubs(fp_clubs)
## print datas and functions colls
# print("Podaci:  : ")
# print(DFrame)
# print("\n")
# print("koeficijenti : ")
# printFile(koef)
# print("\n")
#print("DataF CLubs")
#print(DataF)
a = DataFrameFuncClubs(fp_clubs)

print(a)
print("test 1: ")
print(GETDataClubs(a))
# print(GetAVGIncinterception[i] = (Expenditures[i]*koef[i])omeFORpayerDepartures(DFrame))
# print(GetDataForLeauge_AVG_Seasons(DFrame))
# print("test 2: ")
#print(GetBYyear(DFrame))
#print(GetInflationBYclubs(DataF))
#test
#print(GetDataForLeauge_AVG_Seasons(DFrame))


#print("ukupna ligaska potrošnja po igracu : ")
#print(GetAVGExpendFORpayerArrivals(DFrame))
# print("\n")
# print("ukupna ligaska Bruto zarada po igracu :: ")
# print(GetAVGIncomeFORpayerDepartures(DFrame))
# print("\n")
# print("ukupna ligaska NETTO zarada po igracu :: :")
# print(GetAVGBalanceFORpayerDepartures(DFrame))
#
# a = GetAVGExpendFORpayerArrivals(DFrame)
# b = GetAVGIncomeFORpayerDepartures(DFrame)
# c = GetAVGBalanceFORpayerDepartures(DFrame)
#
#
#
# # Write to file
# head = 'Name_of_leauge Season Nationality AvgExpend +INFLACION'
# WriteTOcsvFILE(save_csv_a,a,head)
# WriteTOcsvFILE(save_csv_b,b,head)
# WriteTOcsvFILE(save_csv_c,c,head)
