#import
import json
import functions
import csv

#Récupération des données d'un fichier json
with open('employes_data_10_2024.json')as file:
    data = json.load(file)

#Calcul des salaires et ajout d'un couple clé-valeur dans data "Salary-nbSalary"
functions.CalcSalary(data)

for subsidiary in data : 
    print(end='\n')
    print(f"Entreprise : {subsidiary}", end='\n\n')

    #Tri descendant en fonction des valeurs des salaires
    data[subsidiary] = sorted(data[subsidiary], key=lambda x: x["Salary"], reverse=True)
    
    #Affichage des employés avec leur position et job
    for employee in data[subsidiary]:
        print(f"{employee['name']:<20} | {employee['job']:<20} | Salaire mensuel : {employee['Salary']:.2f} €")
    print(end='\n')
    print('===========================================================================')
    
    #Affichage des stats par filiale
    print(f"Statistiques des salaires pour la filiale {subsidiary}:")
    print(f"Salaire moyen: {functions.stat_subsidiary(subsidiary)[0]:.2f}")
    print(f"Salaire max: {functions.stat_subsidiary(subsidiary)[1]:.2f}")
    print(f"Salaire min: {functions.stat_subsidiary(subsidiary)[2]:.2f}", end='\n\n')
    print('===========================================================================', end='\n')

print('===========================================================================')

#Affichage des stats générales pour l'entreprise mère
print('')
print("Statistiques globales de l'entreprise :", end='\n\n')
print(f"Salaire moyen : {functions.stats_globales(data)[0]:.2f}")
print(f"Salaire max : {functions.stats_globales(data)[1]:.2f}")
print(f"Salaire moin : {functions.stats_globales(data)[2]:.2f}", end='\n\n')

print('===========================================================================')

#sauvegarde des données sous forme de fichier csv
functions.csv_creation(data)