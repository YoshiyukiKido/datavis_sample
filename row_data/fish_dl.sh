#!/bin/bash

for y in 2015 2016 2017 2018 2019 2020 2021 2022
#for y in 2019 2020
do
    for m in 01 02 03 04 05 06 07 08 09 10 11 12
    do
        wget https://www.market.jafic.or.jp/file/sanchi/$y/01_tukibetu_$y\_$m.xlsx
        #echo $y $m
    done
done