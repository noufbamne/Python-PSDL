import cv2
from PIL import Image, ImageEnhance

# 1. Read image
img = cv2.imread("input.jpg")

# 2. Display image
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# 3. Save image with new name
cv2.imwrite("saved_image.jpg", img)

# 4. Resize image
resized = cv2.resize(img, (300, 300))
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)

# 5. Flip image
flipped = cv2.flip(img, 1)  # 1 = horizontal flip
cv2.imshow("Flipped Image", flipped)
cv2.waitKey(0)

# 6. Crop image
cropped = img[50:300, 50:300]
cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)

# 7. Convert to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)

# 8. Enhance contrast (using PIL)
pil_img = Image.open("input.jpg")
enhancer = ImageEnhance.Contrast(pil_img)
enhanced_img = enhancer.enhance(2.0)  # increase contrast
enhanced_img.save("enhanced.jpg")
enhanced_img.show()

cv2.destroyAllWindows()