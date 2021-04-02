# Face Detection
## 참고자료
https://medium.com/nodeflux/performance-showdown-of-publicly-available-face-detection-model-7c725747094a
https://seongkyun.github.io/study/2019/03/25/face_detection/

모델별 추론 시간  
![](https://miro.medium.com/max/700/1*Xhhwn_y5ZL-O-alPQXLvEQ.jpeg)

Dell XPS 랩탑으로 4가지 모델 테스트:
  1. HaarCasCade model using OpenCV
     https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf
     https://www.youtube.com/watch?v=LsK-xG1cLYA
  2. DlibHOG
  3. MTCNN using TensorFlow  
     https://github.com/ipazc/mtcnn
  4. MobileNetSSD using TensorFlow

TODO: Adding technical details for each Model


---
gif images from the demo  
![broken link](source/movie/Haar.gif)  
OpenCV HaarCascade  

![broken link](source/movie/DlibHOG.gif)  
DlibHOG  

![broken link](source/movie/MTCNN.gif)  
MTCNN  

![broken link](source/movie/MobileNetSSD.gif)  
MobileNetSSD  

---
# Face Detection dataset
http://shuoyang1213.me/WIDERFACE/
