import sys
import os
import io
import numpy as np
import dlib 
from PIL import Image

class FaceCropper():
    def __init__(self):
        self.face_detector = dlib.get_frontal_face_detector()
    
    def crop(self, in_path, out_path):
        files = os.listdir(in_path)
        for file in files:
            try:
                img = Image.open(in_path + file)
                np_img = np.array(img)
                faces = self.face_detector(np_img)

                print(f'{len(faces)} faces are detected in {file}.')

                cnt = 0
                for f in faces:
                    crop_img = np_img[f.top():f.bottom(), f.left():f.right()]
                    crop_img = Image.fromarray(crop_img)
                    if len(faces) == 1:
                        crop_img.save(out_path + file)
                    elif len(faces) > 1:
                        crop_img.save(out_path + str(cnt) + '_' + file)
                        cnt += 1
            except Exception as e:
                print(f'{file} failed')
                print(e)

if __name__ == '__main__':
    in_path = sys.argv[1]
    out_path = sys.argv[2]
    
    cropper = FaceCropper()
    cropper.crop(in_path, out_path)