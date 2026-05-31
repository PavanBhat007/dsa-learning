"""
2126. Destroying Asteroids [Medium]

You are given an integer mass, which represents the original mass of a planet. 
You are further given an integer array asteroids, where asteroids[i] is the mass of the ith asteroid.
You can arrange for the planet to collide with the asteroids in any arbitrary order. 

If the mass of the planet is greater than or equal to the mass of the asteroid, the asteroid is destroyed and the planet gains the mass of the asteroid. 
Otherwise, the planet is destroyed. Return true if all asteroids can be destroyed. Otherwise, return false
"""

# -------------------------------------------------------------------------------------------------

def planetCanDestroyAllAsteroids(mass, asteroids):
    # to gain mass quickly, destory smaller asteroids first
    asteroids.sort()

    for asteroid in asteroids:
        # if smaller asteroid overpowers planet,
        # then further asteroids much larger => return false when mass falls short
        if mass < asteroid:
            return False
        
        mass += asteroid
    
    return True

if __name__ == "__main__":
    planetMass = int(input("PLANET MASS: "))
    numAsteroids = int(input("NUMBER OF ASTEROIDS: "))
    asteroids = [int(ast) for ast in input("ASTEROIDS: ").split(" ")]

    answer = planetCanDestroyAllAsteroids(planetMass, asteroids)
    if answer:
        print(f"Planet of mass {planetMass} can destroy all asteroids of mass {asteroids}")
    else:
        print(f"Planet of mass {planetMass} gets destroyed by one of the asteroids with masses {asteroids}")