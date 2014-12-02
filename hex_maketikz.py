import pycelle


template = r"""\documentclass{article}
\usepackage[a0paper, landscape, margin=.5in, top=.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric}
\begin{document}

\pagestyle{empty}

%% Adapted from:
%%   http://tex.stackexchange.com/questions/6019/drawing-hexagons
%%
%% x=3*(minimum size)/2
%% y=\sqrt{3/4}*(minimum size)/2
%%

\definecolor{color0}{RGB}{178,223,138}
\definecolor{color2}{RGB}{166,206,227}
\definecolor{color1}{RGB}{31,120,180}

\tikzset{
  box/.style={
    regular polygon,
    regular polygon sides=6,
    minimum size=10mm,
    inner sep=0mm,
    outer sep=0mm,
    rotate=90,
  draw=gray!50,
  ultra thin
  }
}

\scalebox{1.5}{%%
\begin{tikzpicture}[x=4.330127mm,y=7.5mm]
%s
\end{tikzpicture}
}

\newpage

\scalebox{1.5}{%%
\begin{tikzpicture}[x=4.330127mm,y=7.5mm]
%s
\end{tikzpicture}
}

\end{document}
"""


#grid = (64,96-1)
#x = pycelle.ECA(90, grid, 'single')

grid = (64, 64)
x = pycelle.ECA(6, grid, radius=.5)
x.hex_onehalf = True

#x._sta[0,:] = 0
#x._sta[0,-1] = 1
x.evolve(draw=False)

hex0 = r"\node[box,fill=color0] at ({}, {}) {{}};"
hex1 = r"\node[box,fill=color1] at ({}, {}) {{}};"
hex_empty = r"\node[box] at ({}, {}) {{}};"

def get_lines(sta, initial=False):
    lines = []
    for i in range(sta.shape[0]):
        for j in range(sta.shape[1]):



            if i > 0 and initial:
                line = hex_empty
            else:
                if sta[i,j] == 1:
                    line = hex1
                else:
                    line = hex0

            x = 2 * j
            y = -i
            if i % 2 == 1:
                x += 1

            lines.append(line.format(x, y))
    return lines

initial_grid = '\n'.join(get_lines(x._sta, initial=True))
final_grid = '\n'.join(get_lines(x._sta, initial=False))

out = template % (initial_grid, final_grid)
print out
