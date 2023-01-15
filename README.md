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


![NUC](https://user-images.githubusercontent.com/114387230/212526634-fa9e2662-7e2d-4cd7-8fd6-a6d708ddae4b.jpg)


* Scout Mini


![Scout](https://user-images.githubusercontent.com/114387230/212526637-13bc967a-cadf-4e52-9ddd-6d33388eeff4.png)


* Intel Realsense L515


![Realsense](https://user-images.githubusercontent.com/114387230/212526639-5fc386f1-2b85-421b-ad3c-71f8048e7313.png)



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




## Python코드 제작

**library used**

        1. install pyzbar
        2. install pyrealsense2
        3. install numpy
        4. install cv2
        5. install time


## Mobility Setting
● **Modified scout MINI for rail recognition**


            # Parts Used #
            ● scout MINI : 1
            ● Intel NUC 10 : 1
            ● Intel Realsense L515 : 1


![크기변환 Mobility setting](https://user-images.githubusercontent.com/114387230/212528063-eb3ad31e-fed4-4627-8ba3-b61ea4e22f63.png)


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
