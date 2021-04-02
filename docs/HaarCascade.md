# Haar Cascade
미리 정해진 필터를 이용해 이미지를 스캔, 해당 필터의 패턴이 이미지에 존재하는지 여부를 검출<br>

필터 예시
<p align="center">
<img src="https://docs.opencv.org/3.4.1/haar_features.jpg">
</p>

이미지와 필터를 통한 패턴 검출 예시 
<p align="center">
<img src="https://docs.opencv.org/3.4.1/haar.png">
</p>

Haar Cascade에서 중요한 요소 3가지
1. Integral image  
2. AdaBoost
3. Cascade

## 1. Integral image
패턴이 있는지 없는지 확인하는 방법은 간단하다. 단순히 필터의 흰색부분에 해당하는
픽셀값의 합에서 어두운 부분의 픽셀값의 합을 빼주면 된다. 이 값이 일정 기준을 넘으면 해당 패턴이
있다고 판단. 근데 이걸 하려면 필터의 2차원 배열을 읽어야 하는데 O(width * height) 만큼의 시간이 필요하다. 
이 시간을 O(1)으로 단축 가능하게 하는 technique이 integral image.
######  
아래 그림을 보자

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/b/bd/Integral_image_application_example.svg" height=400>
</p>


1번 그림은 본래 이미지 배열. 2번은 본래 이미지의 적분영상 (integral image) 배열.
적분영상의 각각의 셀 값은 본래 이미지의 (0,0) 원점부터 구하고자 하는 해당 셀까지의 사각형에
포함되는 셀 값들의 합이다. 예로 그림 1의 빨간색 선((0,0)부터 (2,3)까지의 사각형)의 합은 101로
2번 그림의 (2,3)셀에 나타난다.
다음으로 이 integral image를 이용해서 임의의 사각형에서의 픽셀 합을 구하려면 그림 2 아래의 방법
을 사용하면 된다. 수식은 위키를 참고.

## 2. AdaBoost
[link](Ensemble_Learning.md)
## 3. Cascade


## 참고 사이트
https://docs.opencv.org/3.4.1/  
https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf  
https://www.codeproject.com/Articles/441226/Haar-feature-Object-Detection-in-Csharp  
https://en.wikipedia.org/wiki/Summed-area_table  

