#Task: You are given a string S.Your task is to print all possible permutations of size
of the string in lexicographic sorted order.
    
Input Format:A single line containing the space separated string
and the integer value

Constraints:The string contains only UPPERCASE characters.
Output Format:Print the permutations of the string on separate lines.


from itertools import permutations
str1, int1 = input().split()

for i in sorted(permutations(str1, int(int1))):
    print (''.join(i))
    
