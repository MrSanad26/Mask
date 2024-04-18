## before running

'''
!git clone https://github.com/ultralytics/yolov5  # clone
%cd yolov5
%pip install -qr requirements.txt  # install

pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt

'''

import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='bestfinal.pt', force_reload=True)

image='testmask1.jpg'
results = model(image)
print(results)
results.show()