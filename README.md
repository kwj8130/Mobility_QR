# QR코드를 인식시켜 무인이동체를 이동시키는 것을 목표로 진행
*무인이동체를 활용한 인공지능 자율주행(K-Digital) 프로젝트"

*(gif 로딩에 다소 시간이 걸릴 수 있습니다.)*

>## ABOUT




### Tech Base


#### 1. 언어
* Python - 구현
* C, C++ - 코드참고

#### 2. 환경
* ROS (ROS1_melodic)
* Linux (Ubuntu_18.04)


#### 3. 프로젝트 관리 도구
* git, github
  * 프로젝트, 코드 관리
  * 버전관리 및 협업을 Slack 환경에서 실시
    
* Slack
  * 팀원들과의 커뮤니케이션
  * data, code 공유


#### 4. 사용 도구
* Intel Nuc 10
  * Scout Mini에 장착
  * 제작한 코드들을 활용하기 위한 장치


![크기변환 nuc-10_5_57a91428-c654-4ff7-9075-35a9e791f070_1200x1200_crop_center](https://user-images.githubusercontent.com/114387230/212526484-4df0efd5-7497-4847-ab3c-e7bed49e8739.jpg)

  
* Scout Mini
  * 프로젝트에 활용하기 위한 Mobility

![176610886-aa75f777-31e0-460b-a51e-7033cd9d9cd2](https://user-images.githubusercontent.com/114387230/212524406-5d35fcac-543c-43ae-815d-d73e4825e9ce.png)




* Intel Realsense L515

  * LiDAR 기능을 활용
  * Camera 기능이 포함되어 Mobility의 벽 타기 및 QR인식

![176611606-8a1c7cfc-bb6c-4fce-a34e-f3d8a8edf493](https://user-images.githubusercontent.com/114387230/212524370-3d61dd0d-dd90-422f-a7b1-46a323462c0c.png)




>## 프로젝트 진행


### 1. 프로젝트를 위한 초기 활동
![turtlebot3](https://user-images.githubusercontent.com/114387230/212233522-a1134c47-a621-4170-8344-1892976cc32d.gif)

* https://github.com/ROBOTIS-GIT/turtlebot3_simulations
  * 터틀봇 시뮬레이터 패키지 - 터틀심
  
* 터틀봇 시뮬레이터 사용법 튜토리얼
    * 실제 기능 적용 이전 시뮬레이션 테스트
    * Node, topic, service 구조 파악
    * 가상의 무인이동체를 통해 벽 인지, 맵핑 방식을 파악


### 2. 프로젝트에 사용된 패키지 설치
* Ubuntu 18.04 Installation

1. ROS Installation
2. Reference Site 
<<https://wiki.ros.org/melodic/Installation/Ubuntu>> 1.2 ~ 1.6.1 Installation

3. scout_mini SDK Installation
Reference Site 
<<https://github.com/agilexrobotics/ugv_sdk>>

4. scout_mini Package installation
Reference Site
<<https://github.com/agilexrobotics/scout_ros>>

5. intel Realsense L515 SDK installation 
     **Ubuntu 18.04**
         
         $ sudo add-apt-repository "deb http://librealsense.intel.com/Debian/apt-repo bionic main" -u
         $ sudo apt-get install librealsense2-dkms
         $ sudo apt-get install librealsense2-utils
         $ sudo apt-get install librealsense2-dev
         $ sudo apt-get install librealsense2-dbg
         
         ## test
         $ realsense-viewer

6. SLAM Package

     **Reference Site**
        <<https://github.com/wh200720041/ssl_slam>>
        
        
### 3. 맵, 기준좌표, QR인식 확인
  #### 구현된 기능
  
  1. SLAM


  ![ssl_slam](https://user-images.githubusercontent.com/114387230/212218035-0ad2c0ae-703e-44c8-815f-914bdd07ff20.gif)
  
  
  
  2. QR 인식 & 인식을 위한 분류 모델 생성



  * QR 인식 테스트


  ![QR Test](https://user-images.githubusercontent.com/114387230/212525835-f2900dcd-9cab-41ae-8cab-58ddfa539769.gif)
  
  
  
  * QR & Mobility


  
  ![QR Depth (1)](https://user-images.githubusercontent.com/114387230/212526322-944bd03c-8781-4733-9a94-5832b912331e.gif)






># 프로젝트 관리
* Simulator 1 (https://github.com/ROBOTIS-GIT/turtlebot3_simulations)
* Simulator 2 (https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)
  * 실제 이동체에 적용하기 전 시뮬레이션 환경에서 알고리즘 테스트 실시
  
* Visual Studio Code, Python
  * 코드 작성 및 참고
  
* Slack - 팀원들과의 커뮤니케이션




## 이슈 관리 (Notion)




## 테스크 관리 (Notion)

  


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
