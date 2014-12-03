#!/usr/bin/env bash

# Sooo ugly.

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


pdflatex Poster_Rule150_Single.tex
pdftk Poster_Rule150_Single.pdf burst output Poster_Rule150_Single_%d.pdf
mv Poster_Rule150_Single_1.pdf Poster_Rule150_Single.pdf
mv Poster_Rule150_Single_2.pdf Poster_Rule150_Single_Solution.pdf

pdflatex Poster_Rule150_Random.tex
pdftk Poster_Rule150_Random.pdf burst output Poster_Rule150_Random_%d.pdf
mv Poster_Rule150_Random_1.pdf Poster_Rule150_Random.pdf
mv Poster_Rule150_Random_2.pdf Poster_Rule150_Random_Solution.pdf

pdflatex Poster_Rule150_Custom.tex
pdftk Poster_Rule150_Custom.pdf burst output Poster_Rule150_Custom_%d.pdf
mv Poster_Rule150_Custom_1.pdf Poster_Rule150_Custom.pdf
mv Poster_Rule150_Custom_2.pdf Poster_Rule150_Custom_Solution.pdf



pdflatex Poster_Rule106_Single.tex
pdftk Poster_Rule106_Single.pdf burst output Poster_Rule106_Single_%d.pdf
mv Poster_Rule106_Single_1.pdf Poster_Rule106_Single.pdf
mv Poster_Rule106_Single_2.pdf Poster_Rule106_Single_Solution.pdf

pdflatex Poster_Rule106_Random.tex
pdftk Poster_Rule106_Random.pdf burst output Poster_Rule106_Random_%d.pdf
mv Poster_Rule106_Random_1.pdf Poster_Rule106_Random.pdf
mv Poster_Rule106_Random_2.pdf Poster_Rule106_Random_Solution.pdf

pdflatex Poster_Rule106_Custom.tex
pdftk Poster_Rule106_Custom.pdf burst output Poster_Rule106_Custom_%d.pdf
mv Poster_Rule106_Custom_1.pdf Poster_Rule106_Custom.pdf
mv Poster_Rule106_Custom_2.pdf Poster_Rule106_Custom_Solution.pdf

