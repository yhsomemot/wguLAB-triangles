#spaced out right triangle with user's character
triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))

for row in range(triangle_height + 1):
    print((triangle_char + ' ') * row)

#while version
triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print()

i = 0

while i < triangle_height:
    i += 1
    print((triangle_char + ' ') * i)

#half arrow
h = int(input())
w = int(input())
arrow_head = int(input())

while arrow_head <= w: #if more than one input for arrow_head
    arrow_head = int(input())

for base_h in range(h):
    for base_w in range(w):
        print('*', end = '')
    print()

for head_w in range(arrow_head):
    for head in range(arrow_head - head_w):
        print('*', end = '')
    print()

#justified right triangle
height = int(input())

for row in range(height):
    for space in range(height - row - 1):
        print(' ', end = ' ')
    for star in range(row + 1):
        print('*', end = ' ')
    print()

#upsidedown triangle
height = int(input())

for row in range(height):
    print('* '* (height - row))
        
