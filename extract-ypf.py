import sys, os
from ypf import Ypf

EXTRACT_PATH = "extracted"

for i in [elem for elem in sys.argv if elem.endswith(".ypf")]:
	ypf = Ypf.from_file(i)
	
	for f in ypf.header.entries:
		fname = f.filename.holder.text.strip().replace("\\", "/")
		dname = os.path.dirname(fname)
		compressed = f.compressed
		file_type = f.file_type
		
		os.makedirs(''.join([EXTRACT_PATH, '/', dname]), exist_ok=True)
		with open(''.join([EXTRACT_PATH, '/', fname]), mode="wb") as writer:
			print(''.join([str(file_type), '\t' , EXTRACT_PATH, '/', fname]))
			if(compressed == 0):
				writer.write(f.body.body)
			elif(compressed == 1):
				writer.write(f.body.cmprsd_body)
