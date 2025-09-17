# Name
# CIS 3330
# CODE 1 - Weather Assistant
# Conversion formula: (Temperature in °F - 32) * .5556
# Note that the message to user should be the following
# "What is the temperature outside: "

def main():
    user_temperature = int(input("What is the temperature outside: "))
    #print(user_temperature)
    temp_in_c = ((user_temperature-32)*0.5556)
    #print(temp_in_c)

    if temp_in_c > 20:
        print("\nWear a hat")
    elif temp_in_c < 10:
        print("\nWear a heavy jacket")
    elif temp_in_c < 20:
        print("\nWear a light jacket")

    

if __name__ == "__main__":
    main()
