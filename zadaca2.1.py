converter = input("Ovo je program koji pretvara kilometre u milje! Pritisnite enter za nastavak. ")

kilometers = float(input("Upišite daljinu u kilometrima: "))

conversion_factor = 0.621371

miles = kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles} miles.")