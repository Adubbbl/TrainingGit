## Dossier local -> Staging Area -> Dépôt Local -> Github

### Création du dossier local
Il s'agit de notre dossier sur notre machine physique. Il contiendra l'ensemble des dossiers et fichiers relatives à notre projet. 

### Création du staging area 
Il s'agit d'un endroit où on se prépare à prendre des états (photos) de notre projet. On y stocke temporairement nos modifications

- **Pour le créer :** git init | Cela créer un dossier caché .git dans notre projet ; ce dossier contiendra toutes les manipulations qu'on réalisera dans notre projet avec git.
- **Pour voir l'état des choses :** git status
- **Ajouter un fichier au staging area :** git add <fichier> : cela permet de quitter le dossier local pour le staging area
- **Ajouter tous les fichiers de notre projet au staging area :** git add . 
- **Enlevez l'ensemble des fichiers qui se trouvent dans le staging area :** git rm -rf --cached 

#### Cacher des fichiers aux manipulations git : ne pas les suivre et donc ne pas envoyer sur github
Il peut y avoir des fichiers ou dossiers que je ne veux pas suivre (avec Git) : 
- Je créer alors le fichier **.gitignore** : echo type null > .gitignore
- J'y écris le nom des dossiers et fichiers que je ne souhaite par suivre.



