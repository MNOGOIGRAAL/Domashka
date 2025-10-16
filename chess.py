from PIL import Image, ImageDraw

one_cell = 50
board_size = 400

img = Image.new('RGB', (board_size, board_size), 'white')

draw = ImageDraw.Draw(img)

for row in range(9):
    for col in range(9):
        if (row + col) % 2 == 0:
            color = 'white'
        else:
            color = 'black'
        x1 = col * one_cell
        y1 = row * one_cell
        x2 = x1 + one_cell
        y2 = y1 + one_cell
        draw.rectangle([x1, y1, x2, y2], fill=color)

img.save('chessboard.png')