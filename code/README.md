# Face Detection test with webcam
4 models
1. Haar Cascade
2. Dlib HOG
3. MTCNN
4. MobileNetSSD

## run_webcam.py
Perform Face Detection with webcam.

## run_image.py
(Under construction) Face Detection on the images from WIDER FACE

## MTCNN
is from this github repo: https://github.com/ipazc/mtcnn

## MTCNN speed improvement
modify mtcnn.mtcnn.mtcnn.py file
* Line293 outputs a list of pyramid size and this is used for P-Net. By
reducing this list, speed can be improved.
* Line296 selects O-Net skipping. It is for speed-up but almost no effects.