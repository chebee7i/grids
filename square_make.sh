#!/usr/bin/env bash

python square_maketikz.py

pdflatex Poster_Rule90_Single.tex
pdftk Poster_Rule90_Single.pdf burst output Poster_Rule90_Single_%d.pdf
mv Poster_Rule90_Single_1.pdf Poster_Rule90_Single.pdf
mv Poster_Rule90_Single_2.pdf Poster_Rule90_Single_Solution.pdf

pdflatex Poster_Rule90_Random.tex
pdftk Poster_Rule90_Random.pdf burst output Poster_Rule90_Random_%d.pdf
mv Poster_Rule90_Random_1.pdf Poster_Rule90_Random.pdf
mv Poster_Rule90_Random_2.pdf Poster_Rule90_Random_Solution.pdf

pdflatex Poster_Rule90_Custom.tex
pdftk Poster_Rule90_Custom.pdf burst output Poster_Rule90_Custom_%d.pdf
mv Poster_Rule90_Custom_1.pdf Poster_Rule90_Custom.pdf
mv Poster_Rule90_Custom_2.pdf Poster_Rule90_Custom_Solution.pdf

