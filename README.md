# gravity-simulator


0. Background

vectortools 와 atom 라이브러리를 사용함.

https://github.com/junobonnie/vectortools-and-atom

softening length를 도입함. (http://www.scholarpedia.org/article/N-body_simulations_(gravitational))



1. gravity-simulator demo video(모바일 재생 불가):

https://user-images.githubusercontent.com/60418809/126363251-b521883b-ae18-4127-aae7-f07725278017.mp4



2. 시스템의 운동 에너지와 퍼텐셜 에너지의 시간 그래프:

![image](https://user-images.githubusercontent.com/60418809/126363312-3b4a1494-a6cb-4aab-9403-798d3ee06906.png)

퍼텐셜 에너지의 시간 평균이 운동 에너지의 시간 평균의 -2배라는 것을 보여준다(\<U> = -2\<K>). 이는 비리얼 정리의 결과이다.



3. 다양한 분포 그래프:
  
![image](https://user-images.githubusercontent.com/60418809/126363344-bf51f346-a118-4752-87ab-4b618eb24140.png) ![image](https://user-images.githubusercontent.com/60418809/126363373-ad6442a4-974c-45af-8ced-915a325ddc39.png)

![image](https://user-images.githubusercontent.com/60418809/126363401-2024f174-dc03-4735-be7c-0a137ae93e22.png) ![image](https://user-images.githubusercontent.com/60418809/126363417-d586ed6f-b9b2-4496-bacf-252aaea3cf40.png)
  
질량이 무거운 e2입자가 가벼운 e1입자보다 원점과의 거리가 작다. 이는 에너지 등분배의 결과로, 질량이 큰 입자가 침전 되었다고도 볼 수 있다.
  
또한 입자의 위치 히스토그램이 지수함수적으로 감소하는 것은 볼츠만 분포의 결과이다. (n(r) ~ e^-E/kT)




+)
4. 입자간의 충돌 상호작용

https://user-images.githubusercontent.com/60418809/129376320-4365e127-fa65-4dec-9516-9ff98bbbd069.mp4

![image](https://user-images.githubusercontent.com/60418809/129375716-3ce734c7-1f7c-4e56-9e7c-903562e3b7da.png)



5. 입자간의 완전비탄성충돌(+합체)

https://user-images.githubusercontent.com/60418809/129376279-577cc5af-f65f-42ef-94dc-7fc80ffdc5c7.mp4

![image](https://user-images.githubusercontent.com/60418809/129375763-b9a3c5d5-92ba-4697-bc47-a99c095c4a99.png)
![image](https://user-images.githubusercontent.com/60418809/129375810-2f7c2fd1-0156-4b16-829c-0d296905f383.png)
