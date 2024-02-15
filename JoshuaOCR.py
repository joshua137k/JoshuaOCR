import cv2
import numpy as np
import os

main_image = cv2.imread('imagem.png')
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

t = main_image[::]

l=[]
def rec(path, letter):
    template = cv2.imread(path)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    for loc in locations:
        bottom_right = (loc[0] + template.shape[1], loc[1] + template.shape[0])
        cv2.rectangle(t, loc, bottom_right, (0, 255, 0), 2)
        l.append(letter)


letters = {chr(letter) for letter in range(65, 91)}

for letter in letters:
    folder_path = os.path.join("ABC", letter)
    path = (folder_path + "/" + letter + ".png")
    rec(path, letter)

print(l)

cv2.imshow('Matched Image', t)
cv2.waitKey(0)
cv2.destroyAllWindows()

