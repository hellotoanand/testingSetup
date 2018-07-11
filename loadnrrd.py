import numpy as np
from PIL import Image
import nrrd

readdata, options = nrrd.read("zc_Segmentation1.1.seg.nrrd")

print(" nrrd file read ")
print(" The file dimensions are ",readdata.shape)

for i in range(readdata.shape[0]):
	mysegment = readdata[i]
	
	mysegment1 = np.transpose(mysegment, (2,0,1))
	print ("The individual segment dimensions are ", mysegment1.shape)
	#exit()
	count = 0;
	for x in range(mysegment1.shape[0]):
		mys1 = mysegment1[x]
		


	#	print ("The image dimensions are ", mys1.shape, " count ", count)
	#	exit()
		mys1filename = "Lobe\Lobe_" +str(i)+ "_" +str(x)+ ".jpg"
	#	mys1file = open(mys1filename,"w")
		temp = np.array(mys1)
	#	temp = temp * 255
		tempImage = Image.fromarray((temp*255).astype(np.uint8))
		tempImage.save(mys1filename);



	#	exit()
	#	print ("temp shape is ",temp.shape)
	#
	#	for y in range(mys1.shape[1]):
	#		mys2 = mys1[y]
	#		print (" The row dimensions are ", mys2.shape)
	#		for z in range(mys2.shape[0]):
	#			mys3 = mys2[z]
	#			if mys3 == 1:
	#				count = count + 1
	#
	#			mys1file.write(str(mys3))
	#			mys1file.write(" ")
	#		mys1file.write("\n")
	#	mys1file.close()

	#	print(" File ",x," written \n")


#	#result_filename = "Lobe_" + str(i) + ".txt"
#	mysegmentfilename = "Lobe_" + str(i) + ".txt"
#	mysegmentfile = open(mysegmentfilename, "wb")
#	mysegmentfile.write(mysegment1)

	print (" Total voxels written ", count)
print (options)
myoptionsfile = open("LobeOptions_", "w")
myoptionsfile.write(str(options))


