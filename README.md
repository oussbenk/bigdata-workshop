# Big Data Workshop @ FSEGN (2021)

## Arborescence
    ~
    └──formation/
        ├── code
        │   ├── mapper.py
        │   ├── reducer.py
        │   └── reducer2.py
        └── data
            ├── joboutput		(chiffres d'affaires par magasin; voir "reducer.py") 
            │   └── part-00000
            │ 
            ├── joboutput3		(magasin ayant le chiffre d'affaire max; voir "reducer2.py")
            │   └── part-00000
            └── purchases.txt       (dataset)

## A. Test des scripts MAP/REDUCE sur disque local (sans Hadoop)
Tester les deux programmes sur le disque local (avec les redirections ou *pipes*)

**Remarque :** La commande `sort` joue le rôle de *shuffle* dans Hadoop.

Seules les 50 premières lignes du dataset sont testées. On suppose que le repertoire de travail courant est `code/`
```
	head -50 ../data/purchases.txt | ./mapper.py | sort | ./reducer.py
```

## B. Utilisation de Hadoop pour MAP/REDUCE
1. Créer un répertoire "myinput" sur le HDFS de Hadoop 

	`hadoop fs -mkdir myinput`

2. Mettre le fichier sur le HDFS (rep. de travail courant `code/`)

	`hadoop fs -put ../data/purchases.txt myinput`

3. Vérifier la présence du fichier sur HDFS

	`hadoop fs -ls myinput`
	
4. Lancer le MAP/REDUCE sur Hadoop (rep. de travail courant `code/`)

	`hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.13.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input myinput -output joboutput`

5. Afficher le fichier résultat à partir de HDFS (fichier nommé par défaut `part-00000`)

	`hadoop fs -cat joboutput/part-00000`

6. Charger les fichiers résultats à partir de HDFS sur le disque local (rep. de travail courant `code/`)

**Remarque :** Les fichiers résultats sont disponibles en téléchargement sous `data/` (voir arborescence en haut)
```
  hadoop fs -get joboutput ../data/
```

## :warning: Annexes
### Description des scénarios de MAP/REDUCE
:one: **Scénario 1 :** Calculer les chiffres des ventes annuels par magasin et les afficher dans le format à 2 colonnes :

(voir programme `reducer.py` et fichier résultat `part-00000` sous `joboutput`)

```
Nom_magasin1    Ventes1
Nom_magasin2    Ventes2
Nom_magasin3    Ventes3
...             ...
```

:two: **Scénario 2 :** Calculer et afficher le chiffre des ventes du magasin ayant le plus grand chiffre d'affaire dans une seule ligne :

(voir programme `reducer2.py` et fichier résultat `part-00000` sous `joboutput3`)

```
Nom_magasin    Ventes
```

### Autres remarques
1. Il faut autoriser les programmes Python à être exécutés en leurs accordant le droit d'exécution avec `chmod` comme suit
  
    `chmod 777 mapper.py`

    `chmod 777 reducer.py`
    
2. Quelques commandes Linux ne fonctionnent pas en les rattachant avec `hadoop fs` telles que `head` et `tree` (par contre `tail` fonctionne).
