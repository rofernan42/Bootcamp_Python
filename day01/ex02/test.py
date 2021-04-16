from vector import Vector

vec1 = Vector([2.0, 1.0, 6.0, 4.5])
print("vec1: ", vec1, "size:", len(vec1))
vec2 = Vector(6)
print("vec2: ", vec2, "size:", len(vec2))
vec3 = Vector(range(3, 7))
print("vec3: ", vec3, "size:", len(vec3))

print("")

v1 = vec1 + 5
print("vec1 + 5: ", v1)
v1 = 5 + vec1
print("5 + vec1: ", v1)
v1 = vec1 + vec2
print("vec1 + vec2: ", v1)
v1 = vec1 + vec3
print("vec1 + vec3: ", v1)

print("")

v2 = vec1 * 6
print("vec1 * 6: ", v2)
v2 = 6 * vec1
print("6 * vec1: ", v2)
v2 = vec1 * 6.7
print("vec1 * 6.7: ", v2)
v2 = vec1 * vec2
print("vec1 * vec2: ", v2)
v2 = vec1 * vec3
print("vec1 * vec3: ", v2)

print("")

v3 = vec1 - 7
print("vec1 - 7: ", v3)
v3 = 7 - vec1
print("7 - vec1: ", v3)
v3 = vec1 - vec2
print("vec1 - vec2: ", v3)
v3 = vec1 - vec3
print("vec1 - vec3: ", v3)

print("")

v4 = vec1 / 6
print("vec1 / 6: ", v4)
v4 = 6 / vec1
print("6 / vec1: ", v4)
v4 = vec1 / 6.7
print("vec1 / 6.7: ", v4)
v4 = vec1 / vec2
print("vec1 / vec2: ", v4)
v4 = vec1 / vec3
print("vec1 / vec3: ", v4)