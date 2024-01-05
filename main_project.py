import config
import pprint
from rech_books import Search
from ajout_books import Ajout
from supprimer_books import Delete

client = config.client
db = config.db


class Nav_and_view(object):

    def __init__(self):
        pass

    # Menu principale
    def run(self):
         
        while True :
         print("--------------------------------------------------------------------------------------------------------")
         accueil_menu = input("Bienvenue en Bibiothèque ! Souhaitez-vous faire : recherche (1), ajout (2), supprimer (3), statistiques (4) des documents ? / Quitter (quit) : ")

         if accueil_menu =="1":
             self.mode_recherche()
         elif accueil_menu =="2":
              self.ajout_book()
         elif accueil_menu =="3":
              self.mode_suppression()
         elif accueil_menu=="4":
              self.statistics()
         elif accueil_menu =="quit":
             break

    # Mode de recherche ( filtrage ou classique )
    def mode_recherche(self):
         mode_rech = input("Indiquer si vous faites une recherche filtré (1) ou classique (2), Retour (retour) : ")

         if mode_rech == "1":
             self.choix_filtrage()
         elif mode_rech =="2":
             self.classique()
         elif mode_rech == "retour" :
             self.run()

    # Mode filtrage de recherche 
    def choix_filtrage(self):
        filter_choice = input("Quel filtrage ? type (1), titre (2), année (3), catégorie (4), auteur (5). Retour : (retour) : ")

        if filter_choice =="retour":
             self.mode_recherche()
        elif filter_choice=="1":
             self.filtrage_type()
        elif filter_choice=="2":
             self.filtrage_titre()
        elif filter_choice=="3":
             self.filtrage_annee()
        elif filter_choice=="4":
             self.filtrage_categorie()
        elif filter_choice=="5":
             self.filtrage_auteur()

    # Filtrage recherche type        
    def filtrage_type(self):
          filtrage_type = input("indiquer le type : ")
          result_filt_type = list(Search.filter_type(filtrage_type))
          exist_type = len(result_filt_type)
          if exist_type > 0 :
            for b in result_filt_type:
                    pprint.pprint(b)
                    print("\n")
                    print("-----------------------------------------------")
          else :
               print("le document est introuvable. ")   

    # Filtrage recherche titre
    def filtrage_titre(self):
          filtrage_titre = input("indiquer le titre : ")
          result_filt_titre = list(Search.filter_title(filtrage_titre))
          exist_titre = len(result_filt_titre)
          if exist_titre >0:
            for b in result_filt_titre :
                  pprint.pprint(b)
                  print("\n")
                  print("-----------------------------------------------")
          else :
               print("le document est introuvable. ")                

    # Filtrage recherche année
    def filtrage_annee(self):
          filter_annee = int(input("indiquer l'année : "))
          result_filt_annee = list(Search.filter_year(filter_annee))
          exist_annee = len(result_filt_annee)
          #exist_annee = Search.count_docs(filter_annee)
          if exist_annee > 0 :
               for b in result_filt_annee :
                    pprint.pprint(b)
                    print("\n")
                    print("-----------------------------------------------")
          else :
               print("le document est introuvable. ")   

    # Filtrage recherche catégorie
    def filtrage_categorie(self):
          filter_cat = input("indiquer la catégorie : ")
          result_filt_cat = list(Search.filter_booktitle(filter_cat))
          exist_cat = len(result_filt_cat)
          if exist_cat > 0 :
               for b in result_filt_cat :
                    pprint.pprint(b)
                    print("\n")
                    print("-----------------------------------------------")
          else :
               print("le document est introuvable. ")   

    # Filtrage recherche auteur
    def filtrage_auteur(self):
          filter_auteur = input("indiquer l'auteur : ")
          result_filt_auteur = list(Search.filter_authors(filter_auteur))
          exist_auteur = len(result_filt_auteur)
          if exist_auteur > 0 :
            for b in result_filt_auteur :
                print("\n")
                pprint.pprint(b)
                print("\n")
                print("-----------------------------------------------")
          else:
               print("le document est introuvable. ")   
    
    # Recherche classique
    def classique(self):
         rech_class = input("Indiquez votre recherche : ")
         result_rech = list(Search.rech_classique(rech_class))
         exist_doc = len(result_rech)
         if exist_doc > 0 :
           for b in result_rech:
                print("\n")
                pprint.pprint(b)
                print("\n")
                print("-----------------------------------------------") 
         else :
              print("le document est introuvable. ")

    # Ajout de document
    def ajout_book(self):
         # On va insérer le type, le titre, l'année, la catégorie et l'auteur(s) dans le document
         liste_auteurs = []
         ajout_type = input(" Insertion document (1/5) : Ecrire le type : ")
         ajout_title = input(" Insertion document (2/5) : Ecrire le titre : ")
         ajout_year = int(input(" Insertion document (3/5) : Ecrire l'année : "))
         ajout_cat = input(" Insertion document (4/5) : Ecrire la catégorie : ")
          # Possibilité d'ajouter plusieurs auteurs
         add_auteur="oui"
         while add_auteur == "oui":
              ajout_new_auteur = input (" Insertion document (5/5) : Ecrire l'auteur : ")
              liste_auteurs.append(ajout_new_auteur)
              add_auteur = input("Continuer d'ajouter des auteurs ? (oui)/(non) : ")
              if add_auteur =="non":
               break
             
         result_ajout = Ajout.ajout_book(ajout_type,ajout_title,ajout_year,ajout_cat,liste_auteurs)
         print(f"Le document - {ajout_title} - a été ajouté à votre bibliothèque !")

     # Mode de suppression
    def mode_suppression(self):
         mode_delete = input("Indiquer si c'est une suppression classique (oui), ou par critère (non). Retour : (retour) : ")

         if mode_delete=="oui":
              self.supp_classique()
         elif mode_delete=="non":
              self.supp_par_critere()
         elif mode_delete=="retour":
              self.run()

     # Suppression classique
    def supp_classique(self):
         supp_class = input("Indiquer votre suppression : ")
         result = Delete.Supp_classique(supp_class)
         print(f"Document(s) - {supp_class} - supprimé de votre bibliothèque !")

     # Suppression par critère
    def supp_par_critere(self):
         crit_supp = input("Supprimer par (type) / (titre) / (année) / (catégorie) / (auteur) ? Retour : (retour) : ") 
         if crit_supp=="retour":
              self.mode_suppression()
         elif crit_supp=="type":
              self.supp_par_type()
         elif crit_supp=="titre":
              self.supp_par_titre()
         elif crit_supp=="année":
              self.supp_par_annee()
         elif crit_supp=="catégorie":
              self.supp_par_cat()
         elif crit_supp=="auteur":
              self.supp_par_auteur()

     # suppression par type
    def supp_par_type(self):
         supp_type = input("Supprimer quel type : ")
         result = Delete.supp_type(supp_type)
         print(f"Document(s) de type - {supp_type} - supprimé de votre bibliothèque !")
       
     # suppression par titre
    def supp_par_titre(self):
         supp_title = input("Supprimer le titrre : ")
         result = Delete.supp_title(supp_title)
         pprint(f"Document(s) de titre - {supp_title} - supprimé de votre bibliothèque !")

     # suppression par année
    def supp_par_annee(self):
         supp_annee = int(input("Supprimer l'année : "))
         result = Delete.supp_year(supp_annee)
         pprint(f"Document(s) de titre - {supp_title} - supprimé de votre bibliothèque !")

     #suppression par catégorie
    def supp_par_cat(self):
         supp_cat = input("Supprimer la catégorie : ")
         result = Delete.supp_cat(supp_cat)
         pprint(f"Document(s) de titre - {supp_title} - supprimé de votre bibliothèque !")

    def supp_par_auteur(self):
         tas_auteurs = []
         add_author ="oui"
         while add_author=="oui":
              supp_author = input("Supprimer l'auteur : ")
              tas_auteurs.append(supp_author)
              add_author = input("Continuer à supprimer des auteurs ? (oui)/(non) : ")
              if add_author=="non":
                   break
              
         supp_tot_authors = Delete.supp_auteur(tas_auteurs)
         print(f"La/Les auteur(s) {tas_auteurs} supprimé de la bibliothèque !")

     # Statistiques
    def statistics(self):
         choix_stat = input(" Afficher ? Nombre de publications par année (1), leur moyenne des années (2), leur total par type (3) : ") 

         if choix_stat=="1":
              choix_year = int(input("Indiquer l'année : "))
              post_per_year = db["books"].aggregate([
                   {"$match":{"year":{"$eq":choix_year}}},
                   {"$group":{"_id":"$year","nb":{"$sum":1}}},
                   {"$sort":{"_id":1}}
                   ])
              for b in post_per_year:
                 pprint.pprint(b)
                 print("-----------------------------------------------")

         elif choix_stat=="2":
              choix_moy_year = input("Indiquer le type ( Article, Book, Phd, ...) : ")
              result = db["books"].aggregate([
                   {"$match":{"type":{"$eq":choix_moy_year}}},
                   {"$group":{"_id":"$type","moyenneAnnees":{"$avg":"$year"}}}
                   ])
              for b in result:
                   pprint.pprint(b)
                   print("-----------------------------------------------")

         elif choix_stat=="3":
              result = db["books"].aggregate([{"$group":{"_id":"$type","nb":{"$sum":1}}}])
              for b in result :
                   pprint.pprint(b)
                   print("-----------------------------------------------")
                         
              
# Activation méthodes Nav_and_view
nav_instance = Nav_and_view()
nav_instance.run()        
nav_instance.mode_recherche()
nav_instance.choix_filtrage()
nav_instance.filtrage_type()
nav_instance.filtrage_titre()
nav_instance.filtrage_annee()
nav_instance.filtrage_categorie()
nav_instance.filtrage_auteur()
nav_instance.classique()
nav_instance.ajout_book()
nav_instance.mode_suppression()
nav_instance.supp_classique()
nav_instance.supp_par_critere()
nav_instance.supp_par_type()
nav_instance.supp_par_titre()
nav_instance.supp_par_annee()
nav_instance.supp_par_cat()
nav_instance.supp_par_auteur()
nav_instance.statistics()






