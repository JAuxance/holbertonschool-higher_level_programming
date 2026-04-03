---
  # En Python, tout est un objet —
  ce que ça change vraiment

  ---

  ## Introduction

  Si tu apprends Python, tu as
  sûrement entendu cette phrase : «
  En Python, tout est un objet. »
  Mais qu'est-ce que ça veut dire
  concrètement ? Un entier est un
  objet. Une chaîne de
  caractères est un objet. Une
  liste, une fonction, même une
  classe — tout est un objet.
  Ce n'est pas une formule
  rhétorique : c'est l'architecture
  même du langage. Et comprendre
  ce principe, c'est comprendre
  pourquoi certains comportements de
   Python peuvent sembler
  surprenants, voire
  contre-intuitifs, au début. Dans
  ce billet, je vais expliquer ce
  que
  j'ai appris sur les objets en
  Python, leur identité, leur type,
  et surtout la distinction
  cruciale entre objets mutables et
  immuables — une distinction qui
  change tout à la façon
  dont on écrit du code fiable.

  ---

  ## id() et type() : l'identité et
  la nature d'un objet

  En Python, chaque objet possède
  trois caractéristiques
  fondamentales : une valeur, un
  type,
  et une identité. La fonction
  `type()` retourne le type d'un
  objet, et la fonction `id()`
  retourne son identifiant unique en
   mémoire (l'adresse mémoire sous
  CPython).

  ```python
  a = 42
  print(type(a))   # <class 'int'>
  print(id(a))     # ex :
  140245678901234

  b = "bonjour"
  print(type(b))   # <class 'str'>
  print(id(b))     # ex :
  140245679012345

  L'opérateur is compare les
  identités (id), tandis que ==
  compare les valeurs.
  C'est une différence essentielle :

  a = [1, 2, 3]
  b = [1, 2, 3]
                                    
  print(a == b)   # True  — même    
  valeur                            
  print(a is b)   # False — objets  
  différents en mémoire
                  
  Python optimise la mémoire pour   
  certains objets courants : les
  petits entiers (de -5 à 256)      
  et certaines chaînes courtes sont
  mis en cache (c'est l'interning). 
  C'est pourquoi :
                                    
  a = 5           
  b = 5                             
  print(a is b)   # True — même 
  objet en mémoire (cache des petits
   entiers)       
                                    
  x = 1000        
  y = 1000        
  print(x is y)   # False — grands 
  entiers, pas de cache             
   
  Cette subtilité explique plusieurs
   réponses dans les exercices du
  projet, notamment                 
  pourquoi is peut retourner True
  pour des entiers faibles mais     
  False pour de grands
  nombres — même si leurs valeurs   
  sont égales.    
                  
  ---
  Les objets mutables
                                    
  Un objet mutable est un objet dont
   le contenu peut être modifié     
  après sa création,
  sans changer son identité (son
  id). Les principaux types mutables
   en Python sont :
                                    
  - list          
  - dict          
  - set

  ma_liste = [1, 2, 3]
  print(id(ma_liste))   # ex:       
  140245679000000
                                    
  ma_liste.append(4)
  print(ma_liste)       # [1, 2, 3, 
  4]                                
  print(id(ma_liste))   # Même id ! 
  L'objet a été modifié en place    
                  
  Quand deux variables pointent vers
   le même objet mutable, modifier
  l'une modifie l'autre :           
                  
  a = [1, 2, 3]   
  b = a             # b pointe vers 
  le MÊME objet                     
   
  b.append(4)                       
  print(a)          # [1, 2, 3, 4] —
   a est aussi modifié !            
  print(a is b)     # True
                                    
  C'est exactement ce que montre la 
  réponse [1, 2, 3, 4] dans
  l'exercice 14.                    
  Pour éviter ça, il faut faire une
  copie explicite :                 
   
  a = [1, 2, 3]                     
  b = list(a)       # ou a[:]
                                    
  b.append(4)
  print(a)          # [1, 2, 3]  — a
   est intact                       
  print(b)          # [1, 2, 3, 4]
  print(a is b)     # False — deux  
  objets distincts                  
   
  ---                               
  Les objets immuables

  Un objet immuable est un objet
  dont le contenu ne peut PAS être
  modifié après création.
  Les principaux types immuables en
  Python sont :                     
   
  - int                             
  - float         
  - str
  - tuple
  - bool
  - frozenset

  s = "hello"
  print(id(s))   # ex:              
  140245677000000
                                    
  s = s + " world"
  print(id(s))   # Identifiant 
  différent — nouvel objet créé en  
  mémoire !
                                    
  Les chaînes de caractères semblent
   modifiables, mais chaque
  opération crée un nouvel objet.   
  De même pour les entiers :
                                    
  n = 42
  print(id(n))   # ex:              
  140245670000001                   
   
  n += 1                            
  print(n)       # 43
  print(id(n))   # Identifiant 
  différent — n pointe maintenant   
  vers un autre objet
                                    
  Les tuples aussi sont immuables —
  on ne peut pas modifier leurs
  éléments :

  t = (1, 2, 3)
  # t[0] = 99    # TypeError:       
  'tuple' object does not support   
  item assignment                   
                                    
  ---             
  Pourquoi c'est important : Python 
  traite mutables et immuables      
  différemment                 
                                    
  Cette distinction n'est pas
  anecdotique — elle a des          
  conséquences directes et
  pratiques.                        
                  
  1. L'aliasing (le partage d'objet)
   
  Avec un objet immuable, l'aliasing
   est sans risque car la valeur ne
  peut pas changer :                
                  
  a = "python"
  b = a
  b = b.upper()   # Nouveau string 
  créé                              
  print(a)        # "python" — 
  inchangé                          
                  
  Avec un objet mutable, l'aliasing 
  est un piège classique :
                                    
  a = [1, 2, 3]   
  b = a
  b[0] = 99
  print(a)   # [99, 2, 3] — modifié 
  sans le vouloir !                 
   
  2. Les clés de dictionnaire et les
   éléments de set

  Python exige que les clés de      
  dictionnaire et les éléments de
  set soient hashables,             
  c'est-à-dire immuables. Un int, un
   str ou un tuple conviennent.     
  Une list ne peut PAS être clé de
  dictionnaire :                    
                  
  d = {}                            
  d[(1, 2)] = "coordonnée"   # OK — 
  tuple immuable                    
  # d[[1, 2]] = "erreur"     # 
  TypeError: unhashable type: 'list'
                  
  3. L'optimisation mémoire         
                  
  Python réutilise les objets       
  immuables courants (petits
  entiers, certaines chaînes) pour  
  économiser de la mémoire. Cela
  n'est pas possible pour les objets
   mutables, car partager
  un objet mutable entre plusieurs  
  variables serait dangereux.       
   
  ---                               
  Le passage d'arguments aux 
  fonctions : appel par référence   
  d'objet                         
                                    
  Python utilise un modèle parfois
  appelé "pass by object reference" 
  (ou
  pass by assignment). Ce n'est ni  
  un passage par valeur, ni un      
  passage par référence
  au sens C/C++. Concrètement : la  
  fonction reçoit une référence vers
   l'objet, pas
  une copie. Mais ce que cela       
  implique dépend du type d'objet.  
   
  Avec un objet immuable : la       
  fonction ne peut pas modifier
  l'original                        
                  
  def incrementer(n):
      n += 1
      print("dans la fonction :", n)
   
  x = 10                            
  incrementer(x)  
  print("dehors :", x)   # 10 — x   
  est inchangé
                                    
  La variable n dans la fonction    
  pointe d'abord vers le même objet
  que x (l'entier 10).              
  Mais n += 1 crée un nouvel objet
  (11) et rebinde n localement. x   
  est intact.
                                    
  Avec un objet mutable : la
  fonction PEUT modifier l'original

  def ajouter_element(liste):
      liste.append(4)               
   
  ma_liste = [1, 2, 3]              
  ajouter_element(ma_liste)
  print(ma_liste)   # [1, 2, 3, 4] —
   modifié !                        
   
  La fonction reçoit une référence  
  vers la même liste. .append()
  modifie l'objet en place.         
  Le changement est visible en
  dehors de la fonction.            
   
  Mais attention à la réaffectation 
  :               
                                    
  def remplacer_liste(liste):
      liste = [99, 100]   # 
  Rebinding local — ne modifie pas  
  l'original
                                    
  ma_liste = [1, 2, 3]
  remplacer_liste(ma_liste)
  print(ma_liste)   # [1, 2, 3] —   
  inchangé
                                    
  Ici, liste = [99, 100] crée une   
  nouvelle liaison locale. La
  variable originale n'est          
  pas affectée. C'est exactement ce
  que montre la réponse [1, 2, 3]
  dans l'exercice 18.

  Résumé pratique :                 
   
  Type d'objet: Immuable (int, str…)
  Modification en place: Impossible
  Réaffectation locale: N'affecte
  pas                           
    l'original   