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

# Il peut y avoir des fichiers ou dossiers que je ne veux pas suivre (avec Git) : 
# Je créer alors le fichier .gitignore et je les y insère

# git rm -rf --cached : Enlevez l'ensemble des fichiers qui se trouvent dans le studio

# Création dépôt Local ##########################
# Pour passer une modification du staging area au dépôt Local, on utilise git commit
# git commit - m "On donne un nom à la photo" : Le nom est souvent un résumé de la modification que j'ai apporté # Cela revient en quelque sorte à prendre une photo de l'état actuel de mes fichiers
# L'exécution peut nécessité mon identification au préalable avec : git config --global user.email "you@example.com"

# Pour visualiser l'historique de mes photos, donc l'historique de mes commit dans le dépôt local : git log --online
# On obtient par exemple :
# aac5fbb (HEAD -> master) add files and first notes : le code représente notre photo

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



# Cette fois, je veux plutôt récupérer le dépôt github sur mon PC
# 1. Je fais git clone <le lien du dépôt github que j'aurai copié>
# 2. Ensuite avec d'apporter toute modification, je vais créer une nouvelle branche à partir de l'état actuel du dépôt ; afin d'éviter des conflits de modifications. Je ne vais donc pas travailler sur la branche main.
# 3. Pour créer une nouvelle branch j'utilise : 
