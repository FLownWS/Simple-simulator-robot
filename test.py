import model

m = model.Model ()

print("##TEST 1##")
m.m1.speed = 10
m.m2.speed = 10

print("Premier model : {}".format(m))

linear_speed, rotational_speed = m.dk()
print("Model : {}".format(m))
if linear_speed == 10 and rotational_speed == 0:
    print("\nTEST 1 OK")
else:
    print("\nTEST 1 KO")

print("\n##TEST 2##")
m.m1.speed, m.m2.speed = m.ik(10, 0)

print("Model : {}".format(m))
if m.m1.speed == 10 and m.m2.speed == 10:
    print("\nTEST 2 OK")
else:
    print("\nTEST 2 KO")

