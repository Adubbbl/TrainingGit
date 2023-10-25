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
- Pour **annuler un fichier que j'ai ajouté à staging area par erreur** : git restore --staged <nom du fichier>

#### Cacher des fichiers aux manipulations git : ne pas les suivre et donc ne pas envoyer sur github
Il peut y avoir des fichiers ou dossiers que je ne veux pas suivre (avec Git) : 
- Je créer alors le fichier **.gitignore** : echo type null > .gitignore
- J'y écris le nom des dossiers et fichiers que je ne souhaite par suivre.


### Création du dépôt Local
On va y stocker en quelque sorte des états de notre projet, donc créer un album. 
- Pour **passer une modification du staging area au dépôt Local**, on utilise git commit - m "On donne un nom à la photo" : Le nom est souvent un résumé de la modification que j'ai apporté # Cela revient en quelque sorte à prendre une photo de l'état actuel de mes fichiers. L'exécution peut nécessité mon identification au préalable avec : **git config --global user.email "you@example.com"** ou **git config --global user.name "you@example.com"**
- Pour visualiser **l'historique de mes photos, donc l'historique des commit** : git log --oneline (pour les avoir en une ligne). On obtient par exemple aac5fbb (HEAD -> master) add files and first notes : le code représente notre photo . Ce qui pourra être utile pour revenir en arrière
- Pour **quitter le dépôt local pour staging area** (c'est à dire annuler un commit) : git revert ou git resert 


### Github 
On veut que d'autres personnes puissent modifier notre fichier. On va mettre notre dépôt local sur github. Il faut donc créer un compte sur le site github.
- **Les branches dans github** : On peut avoir plusieurs album à partir de notre photo ainsi avoir plusieurs branches qui contiendrait des albums différentes. Pour apporter une nouvelle modification, sans casser le code actuel, on crée une nouvelle branche. Pour **afficher les branches** : git branch
- **Envoyez son projet sur github**
    1. Il faut créer un répertoire dans github :  c'est dans cela que sera uploader notre dépôt local
    2. Changer la branche "master" par défaut en "main" dans notre dépôt local (C'est ainsi qu'elle se nomme désormais ) : git branch -M main 
    3. Etablir le lien entre notre dépôt local et github : git remote add origin <lien vers le dépôt github avec .git à la fin ; par exemple https://github.com/root529/TrainingGit.git>. 
    Pour **effacer origin donc la liaison à github** : git remote remove origin
    4. Pour envoyer notre album photo ; donc notre dépôt local actuel sur github : git push -u origin main


### Mode Collaboration 
Cette fois, je veux plutôt récupérer le dépôt github sur mon PC afin d'y travailler.
1. Je fais git clone "le lien du dépôt github que j'aurai copié"
2. Ensuite avec d'apporter toute modification, je vais créer une nouvelle branche à partir de l'état actuel du dépôt ; afin d'éviter des conflits de modifications. Je ne vais donc pas travailler sur la branche main.
3. Pour **créer une nouvelle branch** j'utilise : git checkout -b <nom de la branche> : -b permet de switcher directement sur la nouvelle branche. Ainsi l'ensemble de mes modifications seront sur cette branches là.
4. . Après avoir add et commit mes modifications, je vais **push cette branche** là pour rendre accessible mes nouvelles modifications à mes collaborateurs sur github : git push origin <nom de la branche>
5. Je verrai automatiquement ma modification sur github. Je créer un pull request, en ajoutant aussi un commentaire sur mon apport pour mes collaborateurs, afin d'interpeller sur mon apport et que les autres puissent réagir dessus. Il est important pour chaque push vers github de bien travailler sur une seule fonctionnialité donc réaliser un seul commit, de bien documenter pour permettre aux collaborateurs de comprendre. 
6. Le pull request pourra être manager dans github, on peurra demander des apports de mofications. On pourra aussi merge cela si tout est ok dans la branche main. 
7. Après le merge du pull request ; je peux supprimer la nouvelle branche. 

### Mise à jour 
#### GIT PULL
- Pour mettre à jour ma branche main local par rapport à la branche main du dépôt github, je me place sur ma branche main et je fais : git pull  
- Pour **supprimer une branche** dont je n'ai plus besoin, je fais : git branch -d <nom de la branche>

#### MERGE
- On peut voir les lignes qui ont des conflits (quand par exemple plusieurs personnes ont modifié la même ligne) et accepté les modifications les plus interessantes.
- Pour voir qui a ajouté chaque ligne de mon fichier : git  blame <nom du fichier> 


#### COMMIT ULTERIEUR
- J'ai fais plusieurs commit V1, V2, V3, V4. Mais je me rends compte que V2 est mieux donc je souhaite y revenir pour l'utiliser. 
- Je fais : git checkout -b < le code du commit V2>  <nom nouvelle branche>. Cela va créer une nouvelle branche et mon état présent sera V2 à qui je pourrai apporter de nouvelles modifications sans mettre en péril les autres versions après V2
- Mes commit suivantes donc seront sur la nouvelle branche. Attention !! Si je maintien cette branche plus tard, je risque de perdre mes autres versions V3 et V4


N.B : **Invite de commande windows** :  https://www.malekal.com/les-commandes-de-base-invite-de-commande-cmd-windows/#Comment_creer_un_nouveau_repertoire_avec_une_invite_de_commande_CMD
