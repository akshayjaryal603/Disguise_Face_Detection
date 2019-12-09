import sys
import os
#----------------------------------------------
# taking all the images
#----------------------------------------------
import glob as g
n= g.glob('*.jpg')

for i in range(0, len(n)):
	n[i]= n[i].split('.')[0]

now=os.getcwd()
try:
    os.mkdir('Eyes')
except:
    print('already there')

try:
    os.mkdir('Lips')
except:
    print('already there')

try:
    os.mkdir('Nose')
except:
    print('already there')

for name in n:
    try:
	    #-------------------------------
	    # saving values to dataframe
	    #-------------------------------
	    import pandas as pd
	    df= pd.DataFrame(index= range(1, 69), columns= ['y', 'x'])
	    i=0
	    with open(str(name+'.68pt'),'r') as f:
		    for l in f:
			    i=i+1
			    y,x= l.split()
			    df.x[i]= int(x)
			    df.y[i]= int(y)
	    # print(df)

	    #--------------------------------
	    # Cropping the image
	    #--------------------------------
	    from PIL import Image

	    def cropLips(image_path, coords, saved_location):
		    """
		    image_path: The path to the image to edit
		    A tuple of x/y coordinates (x1, y1, x2, y2)
		    saved_location: Path to save the cropped image
		    """
		    image_obj = Image.open(image_path)
		    cropped_image = image_obj.crop(coords)
		    cropped_image = cropped_image.resize((100,30))
		    os.chdir('Lips')
		    cropped_image.save(saved_location)
		    # cropped_image.show()
		    os.chdir(now)
		
	    def cropEyes(image_path, coords, saved_location):
		    """
		    image_path: The path to the image to edit
		    A tuple of x/y coordinates (x1, y1, x2, y2)
		    saved_location: Path to save the cropped image
		    """
		    image_obj = Image.open(image_path)
		    cropped_image = image_obj.crop(coords)
		    cropped_image = cropped_image.resize((100,30))
		    os.chdir('Eyes')
		    cropped_image.save(saved_location)
		    os.chdir(now)
		
	    def cropNose(image_path, coords, saved_location):
		    """
		    image_path: The path to the image to edit
		    A tuple of x/y coordinates (x1, y1, x2, y2)
		    saved_location: Path to save the cropped image
		    """
		    image_obj = Image.open(image_path)
		    cropped_image = image_obj.crop(coords)
		    cropped_image = cropped_image.resize((40, 80))
		    os.chdir('Nose')
		    cropped_image.save(saved_location)
		    os.chdir(now)

	    if __name__ == '__main__':
		    image = name+'.jpg'
		    cropLips(image, (df.x[49]-5, df.y[51]-5, df.x[55]+5, df.y[58]+5), name+'LipsCropped.jpg')
		    cropEyes(image, (df.x[18]-5, df.y[20]-5, df.x[27]+5, df.y[29]+5), name+'EyesCropped.jpg')
		    cropNose(image, (df.x[32]-5, df.y[28]-5, df.x[36]+5, df.y[34]+5), name+'NoseCropped.jpg')
		    print("parts cropped for image "+name)
    except:
		    print('Error for ropping parts of Image '+name)
