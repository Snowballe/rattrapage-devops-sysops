def fizzBuzz(n):
    # Vérifier si n est un multiple de 3 et de 5 en premier, car c'est une exception
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    # Ensuite, vérifier si n est un multiple de 3
    elif n % 3 == 0:
        return "Fizz"
    # Ensuite, vérifier si n est un multiple de 5
    elif n % 5 == 0:
        return "Buzz"
    # Si aucune des conditions ci-dessus n'est satisfaite, retourner n sous forme de chaîne de caractères
    else:
        return str(n)

assert fizzBuzz(15) == "FizzBuzz", "Doit retourner FizzBuzz car multiple de 3 et 5"
assert fizzBuzz(5) == "Buzz", "Doit retourner Buzz car multiple de 5"
assert fizzBuzz(3) == "Fizz", "Retourne Fizz car multiple de 3"
assert fizzBuzz(8) == "8","Retourne le chiffre car non multiple des 2 chiffres"
print("tests passés")
