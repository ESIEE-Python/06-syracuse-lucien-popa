#### Fonctions secondaires
"""
module pour manipuler les suites de Syracuse
"""
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    affichage suite de Syracuse
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    l = [n]
    while n!=1:
        if n%2 == 0: # n paire
            n = n//2
            l.append(n)
        else: # n impaire
            n = n*3 +1
            l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    n = len(l)
    return n

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    premier_element = l[0]
    for indice in range(1,len(l)):
        if l[indice] < premier_element:
            return indice
    return -1


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    n = max(l)
    return n

#### Fonction principale


def main():
    """
    appels des fonctions secondaires
    """
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

    #A = syracuse_l(5)
    #syr_plot(A)
    #print(temps_de_vol(A))
    #print(temps_de_vol_en_altitude(A))
    #print(altitude_maximale(A))

    #B = syracuse_l(10)
    #syr_plot(B)
    #print(temps_de_vol(B))
    #print(temps_de_vol_en_altitude(B))
    #print(altitude_maximale(B))

if __name__ == "__main__":
    main()
