from PIL import Image, ImageDraw
import numpy as np
import skimage.io as skio
import skvideo.io
import sys

img_path = sys.argv[1]
grid_height = int(sys.argv[2])
grid_width = int(sys.argv[3])

if '.png' in img_path or 'jpg' in img_path:
    img = skio.imread(img_path)
elif '.mp4' in img_path:
    img = next(skvideo.io.vreader(img_path))
img_height, img_width = img.shape[:2]

img_obj = Image.fromarray(img)
img_drawer = ImageDraw.Draw(img_obj)

# Draw vertical lines.
xs = np.linspace(0, img_width, grid_width + 1)
for x in xs:
    img_drawer.line((x, 0, x, img_height), fill=0, width=3)
# Draw horizontal lines.
ys = np.linspace(0, img_height, grid_height + 1)
for y in ys:
    img_drawer.line((0, y, img_width, y), fill=0, width=3)

annotated_img = np.array(img_obj)
skio.imshow(annotated_img)
skio.show()
