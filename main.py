import dot
import line
import triangle
dot1 = dot.dot(5, 9)
dot2 = dot.dot(3, 9)
dot3 = dot.dot(3, 5)
x = triangle.triangle(dot1, dot2, dot3)
print(x.area)