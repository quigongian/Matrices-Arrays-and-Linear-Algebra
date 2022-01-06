#Question 1
from numpy import array, matrix
import numpy
from numpy.linalg import linalg, norm
a = array([3, 1, 2]) #Here we are coding the array using the numpy array function.
print ("The array is: ")
print(a) #Here we are printing the array to the user.
print("\n")
normOfA = norm(a) #Here we are calculating the norm of the array using the norm() function from numpy.
print ("The norm is: ")
print(normOfA) #Here we are printing the norm to the user.
print("\n")

#Question 2
matrix1 = numpy.array([[4, -2, 1],[5 ,7, -1]]) #Here we are coding the 2 by 3 matrix.
print ("The first matrix is: ")
print (matrix1.T) #Here we are printing the first matrix to the user.
print ("\n")
matrix2 = numpy.array([[2],[3]]) #Here we are coding the array or 1 by 1.
print ("The array is: ")
print (matrix2) #Here we are printing the array or 1 by 1 to the user.
#print(mat2.T)
print ("\n")
res = numpy.dot(matrix1.T,matrix2) #Here we are calculating the resolution (product) of both matrixes.
print ("The product is: ")
print(res) #Here we are printing the solution to the user.
print("\n")

#Question 3
matrix1a = numpy.array([[3, 4, 3], [-1, 9, -1], [7, 2, 7]]) #Here we are coding a 3 by 3 matrix.
print("The Matrix is: ")
print (matrix1a) #Here we are printing the first matrix to the user.
print ("\n")
det = numpy.linalg.det(matrix1a) #Here we are calculating the determinant using linalg.det function from numpy.
print("The Determinant of the given Matrix is: ")
print (det) #Here we are printing the determinant to the user.
print ("\n")

#Question 4
matrix1b = numpy.array([[7, 3, 6],[2 ,2, -1]]) #Coding a 2 by 3 matrix.
print ("The first matrix is: ")
print (matrix1b) #Here we are printing the first matrix to the user.
print ("\n")
matrix2b = numpy.array([[2, 4],[3, 5], [-2,1]]) #Coding a 3 by 2 matrix.
print ("The second matrix is: ")
print (matrix2b) #Here we are printing the second matrix to the user.
print ("\n")
res = numpy.dot(matrix1b.T,matrix2b.T) #Here we are multiplying both matrixes with numpy.dot function.
print ("The product is: ")
print(res) #Here we are printing the resolution to the user.
print("\n")

#Question 5
print("The system of equations transformed into matrix form is: ")
matrix1c = numpy.array([[2, 2, 6], [2, -2, -2], [4, 2, -4]]) #Coding a system of equations but into matrix form (3 by 3).
matrix2c = numpy.array([[24],[0],[6]]) #Here we are coding everything AFTER the equals sign into matrix form as well.
print (matrix1c) #Here we are printing the first matrix to the user.
print ("\n")
print (matrix2c) #Here we are printing the second matrix to the user.
print("\n")
print("The solution to the system of equations is: ")
solution = numpy.linalg.solve(matrix1c,matrix2c) #Here we are calculating the soultion using the linalg.solve function from numpy.
print (solution) #Here we are printing the solution to the user.