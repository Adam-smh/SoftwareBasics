print("Average speed in km/h")
km = input()

print("What was the speed limit?")
limit = input()

if int(km) <= int(limit):
    print("OK")

elif int(km) > int(limit):
    points = (km-limit)/5
    print("points" + points)
