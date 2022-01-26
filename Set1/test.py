width = 5
height = 6

ct_lines3 = [[None]*width]*height
print(ct_lines3)

print(ct_lines3)

for j in range(height):
    for i in range(width):        
        ct_lines3[j][i] = j,i
        
print(ct_lines3)