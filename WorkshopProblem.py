from PIL import Image
im = Image.open('wafer_image_1.png', 'r')
pix_val = list(im.getdata())
d = {}
for i in pix_val:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
    '''
    if i != (255,255,255) and i != (128,128,128):
    	print(i)
    '''
print(sorted(d))
#print(pix_val)
