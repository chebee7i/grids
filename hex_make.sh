#!/usr/bin/env bash

pdflatex rule90_hexrules.tex
pdftk rule90_hexrules.pdf burst output rule90_hexrules_%d.pdf
mv rule90_hexrules_1.pdf rule90_hexrules_arrows.pdf
mv rule90_hexrules_2.pdf rule90_hexrules_noarrows.pdf
mv rule90_hexrules_3.pdf rule90_hexrules_vertical_arrows.pdf
mv rule90_hexrules_4.pdf rule90_hexrules_vertical_noarrows.pdf
pdfcrop rule90_hexrules_arrows.pdf rule90_hexrules_arrows.pdf
pdfcrop rule90_hexrules_noarrows.pdf rule90_hexrules_noarrows.pdf
pdfcrop rule90_hexrules_vertical_arrows.pdf rule90_hexrules_vertical_arrows.pdf
pdfcrop rule90_hexrules_vertical_noarrows.pdf rule90_hexrules_vertical_noarrows.pdf

python hex_maketikz.py > hexlattice.tex
pdflatex hexlattice.tex
pdftk hexlattice.pdf burst output hexlattice_%d.pdf
pdfcrop hexlattice_1.pdf hexlattice_1.pdf
pdfcrop hexlattice_2.pdf hexlattice_2.pdf

