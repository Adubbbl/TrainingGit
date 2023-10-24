# https://www.malekal.com/les-commandes-de-base-invite-de-commande-cmd-windows/#Comment_creer_un_nouveau_repertoire_avec_une_invite_de_commande_CMD
# Invite de commande windows
print("Hello")

# On a : Dossier local -> Staging Area -> Dépôt Local -> Github

# Création du dossier local ##########################""
# il s'agit de notre dossier sur notre machine physique

# Création du staging area (studio de photos) ###########################""
# git init > cela créé un dossier caché .git

# git status : voir l'état des choses

# Ajouter un fichier au studio de photos : git add <fichier> : cela permet de quitter le dépôt local pour le staging area
# Ajouter tous les fichiers au staging area : git add . 

# Il peut y avoir des fichiers ou dossiers que je ne veux pas suivre (avec Git) : 
# Je créer alors le fichier .gitignore et je les y insère. Ces fichiers n'iront donc pas sur github

# git rm -rf --cached : Enlevez l'ensemble des fichiers qui se trouvent dans le studio

# Création dépôt Local ##########################
# Pour passer une modification du staging area au dépôt Local, on utilise git commit
# git commit - m "On donne un nom à la photo" : Le nom est souvent un résumé de la modification que j'ai apporté # Cela revient en quelque sorte à prendre une photo de l'état actuel de mes fichiers
# L'exécution peut nécessité mon identification au préalable avec : git config --global user.email "you@example.com"

# Pour visualiser l'historique de mes photos, donc l'historique des commit : git log --oneline (pour les avoir en une ligne)
# On obtient par exemple :
# aac5fbb (HEAD -> master) add files and first notes : le code représente notre photo . Ce qui pourra être utile pour revenir en arrière

# Github ##################
# on veut que d'autres personnes puissent modifier notre fichier. On va mettre notre dépôt local sur github
# Les branches dans github : On peut avoir plusieurs album à partir de notre photo ainsi avoir plusieurs branches qui contiendrait différentes version de notre photo.
# Il faut créer un répertoire dans github :  c'est dans cela que sera stocké notre dépôt local
# Deuxième chose à faire : changer la branche "master" par défaut en "main" (C'est ainsi qu'elle se nomme désormais ) :
# git branch -M main
# Pour afficher mes branches : git branch
# Pour établir le lien entre notre dépôt local et github : git remote add origin <lien vers le dépôt github avec .git à la fin ; par exemple https://github.com/root529/TrainingGit.git>
# To remove origin donc la liaison à github : git remote remove origin
# Pour envoyer notre album photo ; donc notre dépôt local actuel sur github : git push -u origin main


########################################################
###########################################################
# Mode COLLABORATIOn
# Cette fois, je veux plutôt récupérer le dépôt github sur mon PC
# 1. Je fais git clone <le lien du dépôt github que j'aurai copié>
# 2. Ensuite avec d'apporter toute modification, je vais créer une nouvelle branche à partir de l'état actuel du dépôt ; afin d'éviter des conflits de modifications. Je ne vais donc pas travailler sur la branche main.
# 3. Pour créer une nouvelle branch j'utilise : git checkout -b <nom de la branche> : -b permet de switcher directement sur la nouvelle bfranche
# 4. Ainsi l'ensemble de mes modifications seront sur ces branches là. Après avoir add et commit mes modifications, je vais push cette branche là pour rendre accessible mes nouvelles modifications à mes collaborateurs sur github : git push origin <nom branch>
# 5. Je verrai automatiquement ma modification sur github : Et je créer un pull request ; ajouter un commentaire sur mon apport pour mes collaborateurs. 
# 6. Il est important pour chaque push vers github de bien travailler sur une seule fonctionnialité donc réaliser un seul commit, de bien documenter pour permettre aux collaborateurs de comprendre. 
# 7. Le pull request pourra être manager dans github, on peurra demander des apports de mofications. On pourra aussi merge ma modification dans la branche main. 
# 8. Après le merge du pull request ; je peux supprimer la nouvelle branche. 


################ GIT PULL
## Pour mettre à jour ma branche main par rapport à la branche main du dépôt github, je fais : git pull  
## Pour supprimer la branche dont je n'ai plus besoin, je fais : git branch -d <nom branch>

################ MERGE CONFLIT
# On peut voir les lignes qui ont des problèmes et accepté ce qui m'interesse 
# Pour voir qui a ajouté chaque ligne de mon fichier : git  blame <nom fichier> : Il renvoie chaque ligne avec le nom de l'auteur

# J'ai ajouté un fichier à staging area par erreur (C'est à dire qu'en réalité, je ne souhaite pas envoyer ce fichier sur github). 
# Pour annuler cela, je fais : git restore --staged <nom fichier>

# Pour quitter le dépôt local pour staging area (c'est à dire annuler un commit) : git revert ou git resert 

################# COMMIT ULTERIEUR
# J'ai fais plusieurs commit V1, V2, V3, V4. Mais je me rends compte que V2 est mieux donc je souhaite y revenir pour l'utiliser. 
# Je fais : git checkout -b < le code du commit V2>  <nom new branch > - 
# Cela va créer une nouvelle branche et mon état présent sera V2 à qui je pourrai apporter de nouvelles modifications sans mettre en péril les autres versions après V2
# Mes commit suivantes seront sur la nouvelle branche
# Attention je maintien cette branche plus tard, je risque de perdre mes autres versions V3 et V4