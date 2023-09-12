# Python

def busca_pais(paises, pais):
    """
    Países es un diccionario. País es la llave.
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return None
    


#Javascript


#Paises es un objeto. Pais es la llave.
#Codigo con el principio LBYL.

#function buscaPais(paises, pais) {
 # if(!Object.keys(paises).includes(pais)) {
  #  return null;
  #}

  #return paises[pais];
#}