"""
Script to generate TeX files for posters.

"""


import pycelle
import numpy as np

template_document = r"""\documentclass{article}
\usepackage[a0paper, landscape, margin=.5in, top=.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric}
\colorlet{color0}{gray!50}
\colorlet{color1}{black}
\pagestyle{empty}
\begin{document}
%s
\end{document}
"""

template_poster = r"""\begin{center}
%s

\vspace{2in}
%s
\end{center}
"""

template_grid = r"""
\begin{tikzpicture}[scale=3.7]
%s
\end{tikzpicture}"""

template_rule = r"""
\scalebox{8}{Rule %s}\\[1in]
\begin{tikzpicture}[scale=3.3]
  \def\i{0}
  \draw[fill=color1] (\i + 0, 0) rectangle (\i + 1, 1);
  \draw[fill=color1] (\i + 1, 0) rectangle (\i + 2, 1);
  \draw[fill=color1] (\i + 2, 0) rectangle (\i + 3, 1);
  \draw[fill=%s] (\i + 1,-1) rectangle (\i + 2, 0);

  \def\i{4}
  \draw[fill=color1] (\i + 0, 0) rectangle (\i + 1, 1);
  \draw[fill=color1] (\i + 1, 0) rectangle (\i + 2, 1);
  \draw[fill=color0] (\i + 2, 0) rectangle (\i + 3, 1);
  \draw[fill=%s] (\i + 1,-1) rectangle (\i + 2, 0);

  \def\i{8}
  \draw[fill=color1] (\i + 0, 0) rectangle (\i + 1, 1);
  \draw[fill=color0] (\i + 1, 0) rectangle (\i + 2, 1);
  \draw[fill=color1] (\i + 2, 0) rectangle (\i + 3, 1);
  \draw[fill=%s] (\i + 1,-1) rectangle (\i + 2, 0);

  \def\i{12}
  \draw[fill=color1] (\i + 0, 0) rectangle (\i + 1, 1);
  \draw[fill=color0] (\i + 1, 0) rectangle (\i + 2, 1);
  \draw[fill=color0] (\i + 2, 0) rectangle (\i + 3, 1);
  \draw[fill=%s] (\i + 1,-1) rectangle (\i + 2, 0);

  \def\i{16}
  \draw[fill=color0] (\i + 0, 0) rectangle (\i + 1, 1);
  \draw[fill=color1] (\i + 1, 0) rectangle (\i + 2, 1);
  \draw[fill=color1] (\i + 2, 0) rectangle (\i + 3, 1);
  \draw[fill=%s] (\i + 1,-1) rectangle (\i + 2, 0);

  \def\i{20}
  \draw[fill=color0] (\i + 0, 0) rectangle (\i + 1, 1);
  \draw[fill=color1] (\i + 1, 0) rectangle (\i + 2, 1);
  \draw[fill=color0] (\i + 2, 0) rectangle (\i + 3, 1);
  \draw[fill=%s] (\i + 1,-1) rectangle (\i + 2, 0);

  \def\i{24}
  \draw[fill=color0] (\i + 0, 0) rectangle (\i + 1, 1);
  \draw[fill=color0] (\i + 1, 0) rectangle (\i + 2, 1);
  \draw[fill=color1] (\i + 2, 0) rectangle (\i + 3, 1);
  \draw[fill=%s] (\i + 1,-1) rectangle (\i + 2, 0);

  \def\i{28}
  \draw[fill=color0] (\i + 0, 0) rectangle (\i + 1, 1);
  \draw[fill=color0] (\i + 1, 0) rectangle (\i + 2, 1);
  \draw[fill=color0] (\i + 2, 0) rectangle (\i + 3, 1);
  \draw[fill=%s] (\i + 1,-1) rectangle (\i + 2, 0);
\end{tikzpicture}
"""

def ruleset(rule):
    """
    Returns a tikzpicture environment for an ECA ruleset.

    """
    x  = pycelle.ECA(rule, (10, 10))
    subs = map(x.eval_int, range(7,-1,-1))
    subs = ['color1' if sub else 'color0' for sub in subs]
    subs = (rule,) + tuple(subs)
    return template_rule % subs

def grid(rule, gridsize, ic, solution=False):
    """
    Returns a tikzpicture environment for an ECA.

    Parameters
    ----------
    rule : int
        The ECA rule.
    gridsize : tuple
        A 2-tuple specifying the grid size. The first element is the number
        of columns and the second is the number of rows.
    ic : str, array
        The initial condition of the ECA. This should be 'single' or 'random'.
        It may also be an array with length equal to the number of columns.
        The elements of the array specify that value of the cell.

    """
    x  = pycelle.ECA(rule, gridsize, ic=ic)
    x.evolve(draw=False)
    lines = get_lines(x._sta, initial=not solution)

    env = template_grid % ('\n'.join(lines),)

    return env

def get_lines(sta, initial=False):
    square0 = r"\filldraw[fill=color0] ({}, {}) rectangle ({}, {});"
    square1 = r"\filldraw[fill=color1] ({}, {}) rectangle ({}, {});"
    square  = r"\draw ({}, {}) rectangle ({}, {});"

    lines = []
    for i in range(sta.shape[0]):
        for j in range(sta.shape[1]):
            if i > 0 and initial:
                line = square
            else:
                if sta[i,j] == 1:
                    line = square1
                else:
                    line = square0

            x0 = j
            y0 = -i
            x1 = j + 1
            y1 = -i - 1
            lines.append(line.format(x0, y0, x1, y1))

    return lines

def poster(rule, gridsize, ic, solution=False):

    the_rules = ruleset(rule)
    the_grid  = grid(rule, gridsize, ic, solution=solution)
    poster = template_poster % (the_rules, the_grid)
    return poster

def grid_and_solution(rule, gridsize, ic, filename):
    x = pycelle.ECA(rule, gridsize, ic)
    poster1 = poster(rule, gridsize, x._sta[0], solution=False)
    poster2 = poster(rule, gridsize, x._sta[0], solution=True)

    content = r'\newpage'.join([poster1, poster2])
    doc = template_document % (content,)

    with open(filename, 'w') as f:
        f.write(doc)

def large_demos():
    rule = 90
    gridsize = (65,110)

    runs = [
        ('single', 'Poster_Rule90_DemoSingle.tex'),
        ('random', 'Poster_Rule90_DemoRandom.tex'),
    ]
    np.random.seed(123)
    for ic, filename in runs:
        content = poster(rule, gridsize, ic, solution=True)
        content = content.replace('[scale=3.7]', '[scale=1]')
        doc = template_document % (content,)
        with open(filename, 'w') as f:
            f.write(doc)

def triplet(rule):
    basename = "Poster_Rule{0}".format(rule)
    grid_and_solution(rule, (16,31), 'single', basename + '_Single.tex')
    np.random.seed(123)
    grid_and_solution(rule, (17,31), 'random', basename + '_Random.tex')

    ic = np.zeros(31)
    ic[7:10] = 1
    ic[21:24] = 1
    grid_and_solution(rule, (17,31), ic, basename + '_Custom.tex')

def main():
    triplet(90)
    triplet(106)
    triplet(150)

def rulesets_only():
    tikz = []
    for rule in [45, 90, 105, 110, 150]:
      tikz.append(r"\begin{center}%s\end{center}" % (ruleset(rule),) )
    content = '\\newpage\n'.join(tikz)
    final = template_document % (content,)
    with open('rules.tex', 'w') as f:
      f.write(final)


if __name__ == '__main__':
    #main()
    pass
    #large_demos()
    rulesets_only()
