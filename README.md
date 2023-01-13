# QR코드를 인식시켜 무인이동체를 이동시키는 기술
*무인이동체를 활용한 인공지능 자율주행(K-Digital) 프로젝트"

*(gif 로딩에 다소 시간이 걸릴 수 있습니다.)*

>## ABOUT
![ssl_slam](https://user-images.githubusercontent.com/114387230/212218035-0ad2c0ae-703e-44c8-815f-914bdd07ff20.gif)

</p>
<p align="center">
  SLAM
</p>



### Tech Base


#### 1. 언어
* Python - 구현
* C, C++ - 코드참고

#### 2. 환경
* ROS (ROS1_melodic)
* Linux (Ubuntu_18.04, Debian_buster)
* Intel NUC 10


#### 3. 프로젝트 관리 도구
* git, github
  * repository 생성
  * 프로젝트, 코드 관리
  * ~~버전관리, 협업~~ (Slack, Notion으로 대체됨)
    * 버전관리 및 협업 Slack 환경에서 실시

* Slack
  * 커뮤니케이션
  * daily dev journal
  * data, code 공유



>## 기능별 분류


### 1. 실내 측위를 위한 3D맵 생성
* SLAM
  * Lidar sensor


* 좌표계
  * 위치 분석을 위한 Cartesian coordinate system과 주행 동작을 위한 Quaternions 변환



### 2. 프로젝트를 위한 초기 활동
![turtlebot3](https://user-images.githubusercontent.com/114387230/212233522-a1134c47-a621-4170-8344-1892976cc32d.gif)

* https://github.com/ROBOTIS-GIT/turtlebot3_simulations
  * 터틀봇 시뮬레이터 패키지 - 터틀심
    * 실제 기능 적용 이전 시뮬레이션 테스트
    * Node, topic, service 구조 파악
    * 가상의 무인이동체를 통해 벽 인지, 맵핑의 구조 파악


### 3. 관리자 GUI


### 4. 맵, 기준좌표, 객체 위치 좌표 저장 + ~~저장된 데이터 로딩하여 동작 구현~~ (미구현)
  #### 구현된 기능




### 5. Autonomous Mapping




### 6. 객체 인식 & 인식을 위한 분류 모델 생성
* 객체 인식
 * 
* 모델 생성

* Auto Labeling




># 프로젝트 관리
* Simulator (https://github.com/ROBOTIS-GIT/turtlebot3_simulations)
  * 코드 테스트 및 변수 관리
* Notion
* Slack - 커뮤니케이션



## Simulator (Turtlebot3_simulations)
*실제 이동체에 적용하기 전 시뮬레이션 환경에서 알고리즘 테스트 실시*




## 이슈 관리 (Notion)




## 테스크 관리 (Notion)




## 커뮤니케이션 관리 (Slack)
* 커뮤니케이션

  


># 미구현 및 개선사항

## 저장된 맵 정보를 불러온 뒤 정상적으로 작동하는 기능 구현 미완성
  * 미완성 사유

  * Try&Error

  * 기능 대체 구현

  * 향후 개선 방법








## 객체 인지 모델 정확도 부족




## git, github 기반 프로젝트 진행을 위한 개선점

    




----------

>*참고 Reference*



----------

프로젝트에 대한 리뷰, 코멘트, 피드백에 늘 배고픕니다 :heart_eyes:

Made with :fire:Maximum Effort:fire: and Python
