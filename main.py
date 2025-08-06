// your code here

# Convertisseur de Température
# Challenge Python Facile - Codeurs Pro
# Surprenez nous par votre imagination et perfectionnez le code a votre guise

def celsius_to_fahrenheit(celsius):
    return ""

def fahrenheit_to_celsius(fahrenheit):
    return ""

def celsius_to_kelvin(celsius):
    return ""

def kelvin_to_celsius(kelvin):
    return ""

def afficher_menu():
    // AMELIOREZ A VOTRE GUISE
    print("=== Convertisseur de Température ===")
    print("1. Celsius vers Fahrenheit")
    print("2. Fahrenheit vers Celsius")
    print("3. Celsius vers Kelvin")
    print("4. Kelvin vers Celsius")
    print("5. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == '1':
            temp = input("Entrez la température en Celsius : ")
            try:
                temp = float(temp)
                print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")
        
        elif choix == '2':
            temp = input("Entrez la température en Fahrenheit : ")
            try:
                temp = float(temp)
                print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")
                //AJOUTEZ LES AUTRES CAS
        else:
            print("Option invalide. Veuillez choisir entre 1 et 5.")

if __name__ == "__main__":
    main()
