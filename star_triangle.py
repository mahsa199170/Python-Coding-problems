# Write a program in Python to produce Star triangle.



# *
# ***
# *****
# *******
# *********

# for i in range(1,11,2):
#
#         print( i * "*")

# ---------------------------------------------


# * * * *
# * * * *
# * * * *
# * * * *


# for i in range(4):
#     for j in range(4):
#         print("*", end = " ")
#     print()
#


# ---------------------------------------------

# *
# * *
# * * *
# * * * *

#
# for i in range(1,5):
#         print(i * " *")
# ---------------------------------------------

# *
# * *
# * * *
# * * * *

# for i in range(4):   #column
#     for j in range(i+1):   #row
#         print("*", end = " ")
#     print()

# ---------------------------------------------

#
# * * * *
# * * *
# * *
# *

# for i in range(4):
#     for j in range(i,4):
#         print("*", end = " ")
#     print()

# ---------------------------------------------
#        *
#      * *
#    * * *
#  * * * *

#
# for i in range(4):
#         for j in range(i,4):
#                 print(" ", end = " ")
#         for j in range(i+1):
#                 print("*",end = " ")
#         print()


# the print() statement with no arguments is used to print a newline character at the end of each row, which moves the output to the next line.

# ---------------------------------------------


#    *
#   * *
#  * * *
# * * * *

# for i in range(4):
#     for j in range(i,4):
#         print(" ", end = "")
#     for j in range(i+1):
#         print("*", end = " ")
#     print()
#

# ---------------------------------------------

# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(5):
#     for j in range(i,5):
#         print("*", end = " ")
#     print()

# ---------------------------------------------


 # * * * * *
 #   * * * *
 #     * * *
 #       * *
 #         *

# for i in range(5):
    # for j in range(i):
    #     print(" ", end = " ")
    # for j in range(i,5):
    #     print("*", end = " ")
    # print()

# ---------------------------------------------

# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(5):
#     for j in range(i+1):
#         print(" ", end = " ")
#     for j in range(i,5):
#         print("*", end = " ")
#     print()

# ---------------------------------------------
#          *
#        * * *
#      * * * * *
#     * * * * * * *
#    * * * * * * * * *

# for i in range(5):
#     for j in range(i,5):
#         print(" ", end = " ")
#     for j in range(i+1):
#         print("*" , end = " ")
#     for j in range(i):
#         print("*", end = " ")
#     print()

# ---------------------------------------------

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# for i in range(5):
#     for j in range(i):
#         print(" ", end = " ")
#     for j in range(i,5):
#         print("*", end = " ")
#     for j in range(i,4):
#         print("*", end = " ")
#     print()
# ---------------------------------------------


     #       *
     #     * * *
     #   * * * * *
     # * * * * * * *

# for i in range(4):
#     for j in range(i,5):
#         print(" ", end = " ")
#     for j in range(i):
#         print("*" , end = " ")
#     for j in range(i+1):
#         print("*", end = " ")
#     print()
## ---------------------------------------------


  # * * * * * * * * *
  #   * * * * * * *
  #     * * * * *
  #       * * *
  #         *

# for i in range(5):
#     for j in range(i+1):
#         print(" ", end = " ")
#     for j in range(i,4):
#         print("*", end = " ")
#     for j in range(i,5):
#         print("*", end = " ")
#
#     print()
#
# ---------------------------------------------

# *       *
# *       *
# *       *
# *       *
# *       *


# for i in range(5):
#     for j in range(5):
#         if j == 0 or j == 4 :
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

## ---------------------------------------------

#
#     *
#     *
# * * * * *
#     *
#     *

#
# for i in range(5):
#     for j in range(5):
#         if i == (5//2) or j == (5//2) :
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

# ---------------------------------------------


# *       *
#   *   *
#     *
#   *   *
# *       *
#
# for i in range(5):
#     for j in range(5):
#         if i == j or i+j == 5 -1 :
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
# ---------------------------------------------


# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# for i in range(5):
#     for j in range(5):
#         if i == 0 or j == 0 or i == 5-1 or j == 5-1:
#             print("*", end = " ")
#         else:
#             print(" ", end = " ")
#     print()
