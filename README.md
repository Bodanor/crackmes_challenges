# Crackmes.one

## Commandes utiles pour GDB:

### Bon à savoir:
* Si la commande `disas main` ne fonctionne pas, alors c'est que le programme à sans doute été compilé sans les symboles
  . On peux vérifier cela grace à la commande `file <fichier executable>`. Si la commande `file` retourne *stripped*, alors l'éxécutable ne contient pas de symbole et il faut manuellement chercher les adresse de chaque fonction. Voir [lien](https://tr0id.medium.com/working-with-stripped-binaries-in-gdb-cacacd7d5a33)


* Pour debugger plus facilement, on peux demander à GDB de nous afficher le contenu de chaque registres et en même temps afficher le code assembleur de cette façon : 
    ```shell
    layout asm
  layout regs
     ```
### Afficher les registres :

```shell
info registers
ou
i r
```

### Lire une/des chaine(s) de caractère(s) à partir d'une adresse : 
``` shell
1 chaine : x/s <adresse>
2 chaines : x/2s <adresse>
...
```
### Dans le mode 

