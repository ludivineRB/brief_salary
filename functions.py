import json
import csv

def CalcSalary(d:dict):
    """_summary_ Return a modification of the original file with the addition of a couple key-value for salary

    Args:
        d (dict): _description_ its a dict filled with keys of subsidiary and in values the list of collections of employees and employee's informations
    """
    #Parcours le dictionnaire de dictionnaire pour chaque filiale
    for subsidiary in d:
       
        #Parcours chaque dictionnaire"filiale" pour trouver chaque employé
        for employee in d[subsidiary]:
            #condition heure sup et calcul salaire
            if employee['contract_hours'] < employee['weekly_hours_worked']:
                sup_hour = employee['weekly_hours_worked']-employee['contract_hours']
                salary = (employee['hourly_rate']*employee['contract_hours'] + sup_hour * employee['hourly_rate']*1.5)*4

            #condition pas d'heure sup, calcul du salaire fonction du nombre d'heures travaillées
            else:
                salary = round((employee['hourly_rate']*employee['weekly_hours_worked']*4),2)


            #modification du fichier original pour ajouter une clé salaire avec une valeur pour chaque employé
            employee['Salary'] = salary
     
   

def stat_subsidiary(subsidiary:dict)->tuple: 
    """_summary_return the maximal salary, the minimal salary and the average salary for a subsidiary

    Args:
        subsidiary (dict): _description_ dict containing all the datas for the employees of a subsidiary

    Returns:
        tuple: _description_ tuple of the mean, max and min salary in a subsidiary
    """
    #Récupération des données
    with open('employes_data_10_2024.json')as file:
        data = json.load(file)

    #Application de la première fonction pour avoir la clé salaire
    CalcSalary(data)

    #création d'un dictionnaire contenant toutes les infos des employés d'une filiale
    data_subsidiary= data[subsidiary] 

    salary_all = []

    #création d'une liste contenant tous les salaires des employés
    for employe in data_subsidiary : 
        salary_all.append(employe["Salary"])
    
    salary_mean = sum(salary_all) / len(salary_all)
    salary_max = max(salary_all)
    salary_min = min(salary_all)

    #enregistrement des données sous forme de tuple
    return salary_mean, salary_max, salary_min

def stats_globales(data : dict)-> tuple: 
    """_summary_ return the maximal salary, the minimal salary and the average salary for a subsidiary


    Args:
        data (dict): _description_ dict filled with keys of subsidiary and in values the list of collections of employees and employee's informations

    Returns:
        tuple: _description_tuple of the mean, max and min salary in the entreprise
    """

    all_mean = []
    all_max = []
    all_min = []

    #création d'une liste contenant les filiales
    subsidiary = data.keys()
    
    #récupération des stats de chaque filiale grâce à la fonction stat_subsidiary
    for f in subsidiary : 
        all_mean.append(stat_subsidiary(f)[0])
        all_max.append(stat_subsidiary(f)[1])
        all_min.append(stat_subsidiary(f)[2])
        
    global_mean = sum(all_mean) / len(all_mean)
    max_global = max(all_max)
    min_global = min(all_min)

    #enregistrement des données sous forme de tuple
    return global_mean, max_global, min_global

def csv_creation(data):

    #Récupération des données
    with open('employes_data_10_2024.json')as file:
        data = json.load(file)

    #Application de la première fonction pour avoir la clé salaire
    CalcSalary(data)


    #creation d'un fichier csv
    with open("stat_salary.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        
        
        #Parcours le dictionnaire de dictionnaire pour chaque filiale
        for subsidiary in data:
            writer.writerow([subsidiary])
            #Parcours chaque dictionnaire"filiale" pour trouver chaque employé
            
            #les en-têtes (colonnes du CSV)
            writer.writerow(["Name", "Job", "Salary"])
        
            for employee in data[subsidiary]:
                
                writer.writerow([employee["name"],employee["job"], employee["Salary"]])
        
            # Ajout une ligne vide pour séparer les stats des employés
            writer.writerow([])
            
            # statistiques de chaque filiale
            writer.writerow(["Statistiques"])
            writer.writerow(["Salaire maximum", f"{stat_subsidiary(subsidiary)[1]:.2f}"])
            writer.writerow(["Salaire minimum", f"{stat_subsidiary(subsidiary)[2]:.2f}"])
            writer.writerow(["Salaire moyen", f"{stat_subsidiary(subsidiary)[0]:.2f}"])

            # Ajout une ligne vide pour séparer les stats des employés
            writer.writerow([])
            writer.writerow([])
            writer.writerow([])

        print(f"Fichier CSV '{"employes_data_10_2024.json"}' créé avec succès.")


