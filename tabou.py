from typing import List
import random 

def voyageur_de_commerce(distances: List[List[int]], n: int, tabou_length: int, max_iter: int) -> List[int]:
    # Initialiser la liste tabou et la meilleure solution trouvée jusqu'à présent
    tabou_list = []
    best_solution = []
    best_distance = float("inf")
    # Initialise le compteur d'itérations
    iter_count = 0
    
    while True:
        # Générer une solution aléatoire
        solution = generate_random_solution(n)
        
        # Calculer la distance de la solution
        distance = calculate_distance(solution, distances)
        
        # Si la distance de la solution est meilleure que la meilleure solution trouvée jusqu'à présent,
        # mettre à jour la meilleure solution
        if distance < best_distance:
            best_solution = solution
            best_distance = distance
        
        # Ajouter la solution à la liste tabou
        tabou_list.append(solution)
        
        # Si la liste tabou a atteint sa longueur maximale, retirer le premier élément de la liste
        if len(tabou_list) > tabou_length:
            tabou_list.pop(0)
    
        # Incrémente le compteur d'itérations et vérifie si le nombre maximal d'itérations a été atteint
        iter_count += 1
        if iter_count >= max_iter:
            break
    
    return best_solution
    
def generate_random_solution(n: int) -> List[int]:
    # Générer une solution aléatoire en mélangeant les villes
    cities = list(range(n))
    random.shuffle(cities)
    return cities
    
def calculate_distance(solution: List[int], distances: List[List[int]]) -> int:
    # Calculer la distance totale de la solution en parcourant chaque ville
    distance = 0
    for i in range(len(solution) - 1):
        distance += distances[solution[i]][solution[i + 1]]
    return distance


# Créer la matrice de distances à partir des données fournies
distances = [
    [0, 12, 13, 15, 23, 25, 56, 27, 38, 29, 60, 32],
    [12, 0, 23, 22, 34, 56, 24, 78, 79, 34, 23, 24],
    [13, 23, 0, 25, 23, 19, 18, 42, 25, 23, 26, 33],
    [15, 22, 25, 0, 12, 24, 38, 27, 38, 49, 69, 29],
    [23, 34, 23, 12, 0, 54, 36, 71, 81, 19, 100, 22],
    [25, 56, 19, 24, 54, 0, 16, 27, 26, 37, 105, 72],
    [56, 24, 18, 38, 36, 16, 0, 18, 23, 24, 25, 26],
    [27, 78, 42, 27, 71, 27, 18, 0, 18, 19, 30, 53],
    [38, 79, 25, 38, 81, 26, 23, 18, 0, 29, 23, 22],
    [29, 34, 23, 49, 19, 37, 24, 19, 29, 0, 22, 42],
    [60, 23, 26, 69, 100, 105, 25, 30, 23, 22, 0, 36],
    [32, 24, 33, 29, 22, 72, 26, 53, 22, 42, 36, 0]]

print(voyageur_de_commerce(distances, 12, 12, 1000))
