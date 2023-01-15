#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pyrealsense2 as rs
from os import system
from geometry_msgs.msg import Twist
import numpy as np
import rospy
import cv2
import pyzbar.pyzbar as pyzbar
import time 
import os

cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
# img_pub = rospy.Publisher('chatter', String, queue_size = 10)
height = 0
width = 0

Find_QR = 'Waiting'
Check_QR = ''
latest_QR = ''
check_mod = 1

print_count = 0
QR_count = 0

check_path = True
check_result = 0 # 0 직진 1 좌 2 우

speed = 0   #msg.linear.x
angle = 0      #msg.angular.z
turn = 0.1

t1 = 0
t2 = 0
millis = 0
def Direction(LEFT_MEAN, FRONT_MEAN, RIGHT_MEAN):
    global speed, angle, turn, check_result, check_path, check_mod, Find_QR, Check_QR, latest_QR, t1

    os.system('clear')
    # print(f'speed : {speed}, angle : {angle}')
    # print('check_result : ',check_result)
    print(f'L: {LEFT_MEAN}, F: {FRONT_MEAN}, R: {RIGHT_MEAN}')
    # print('check_path : ', check_path)
    print(f'찾을 QR : {Find_QR}')
    # print(f'check_mod : {check_mod}')
    print(f'현재 인식되는 QR : {Check_QR}')
    # print(f'millis : {millis}')
    
    if check_mod == 2:
        speed = 0.06
        angle = 0
        if check_path == True:
            if FRONT_MEAN <= 95 and Find_QR == Check_QR :
                latest_QR = Check_QR
                speed = 0
                angle = 0
                t1 = 0
                check_mod = 1
                Find_QR = 'Waiting'
                # print(f'{Check_QR}을 찾았습니다.')

            if FRONT_MEAN <= 55 and LEFT_MEAN <= 55 and RIGHT_MEAN <= 55:
                speed = 0
                angle = 0
                check_path = False

            if FRONT_MEAN >= 65 and check_result == 0:
                speed = speed
                angle = 0
            
            if RIGHT_MEAN + 15 <= FRONT_MEAN or LEFT_MEAN + 15 <= FRONT_MEAN :       
                if ((RIGHT_MEAN <= 45 or LEFT_MEAN <= 45) or FRONT_MEAN < 85) and check_result == 0:
                    check_LR()
                
            if check_result == 1:
                speed = speed
                angle = -0.1    
                check_result = 0
        
            if check_result == 2:
                speed = speed
                angle = 0.1
                check_result = 0
                
        if check_path == False:
            speed = 0
            angle = turn
            if FRONT_MEAN >= 150:
                if RIGHT_MEAN >= 70 and LEFT_MEAN >= 70:
                    check_path = True
                    turn = turn * -1 


def check_LR(): # 좌우 ㅇㅇ 
    global check_result
    if LEFT_MEAN > RIGHT_MEAN:
        check_result = 2
    elif LEFT_MEAN < RIGHT_MEAN:
        check_result = 1

# speedm angle 값 넘겨주는 부분 
def Moving():
    global speed, angle
    msg = Twist()
    msg.linear.x = speed
    msg.angular.z = angle
    cmd_pub.publish(msg)

# lader_sensor 키면 초반 설정 함수
def Ladar_setting():
    # Configure depth and color streams
    pipeline = rs.pipeline()
    config = rs.config()

    # Get device product line for setting a supporting resolution
    pipeline_wrapper = rs.pipeline_wrapper(pipeline)
    pipeline_profile = config.resolve(pipeline_wrapper)
    device = pipeline_profile.get_device()
    device_product_line = str(device.get_info(rs.camera_info.product_line))

    found_rgb = False
    for s in device.sensors:
        if s.get_info(rs.camera_info.name) == 'RGB Camera':
            found_rgb = True
            break
    if not found_rgb:
        print("The demo requires Depth camera with Color sensor")
        exit(0)

    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

    if device_product_line == 'L500':
        config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
    else:
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    # Start streaming
    pipeline.start(config)
    
    return pipeline

def display(pipeline):
    global LEFT_MEAN, FRONT_MEAN, RIGHT_MEAN, width, height

    # This call waits until rec new coherent set of frames is available on rec device
    # Calls to get_frame_data(...) and get_frame_timestamp(...) on rec device will return stable values until wait_for_frames(...) is called
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    color_frame = frames.get_color_frame()

    if not depth_frame or not color_frame:
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())

    depth_colormap_dim = depth_image.shape

    height = depth_colormap_dim[0]
    width  = depth_colormap_dim[1]

    resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
            
    LEFT =  depth_image[(height//2)+40 : (height//2)+80, 0:40]
    FRONT = depth_image[(height//2)+40 : (height//2)+80, (width//2-20) : (width//2)+20]
    RIHGT = depth_image[(height//2)+40 : (height//2)+80, width-40 : width]

    LEFT_MEAN  = round(np.mean(LEFT)/40) 
    FRONT_MEAN = round(np.mean(FRONT)/40)
    RIGHT_MEAN = round(np.mean(RIHGT)/40)

    return resized_color_image, depth_image

def QR_OPENCV(color_image, depth_image):
    global check_mod, speed, Find_QR, Check_QR, latest_QR, QR_count, t1, t2, millis
    gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)
    t2 = int(round(time.time())) 
    text = ''
    x, y, w, h = 0, 0, 0, 0
    if not decoded == [] :
        for Dcode in decoded :
            x, y, w, h = Dcode.rect
            barcode_data = Dcode.data.decode("utf-8")
            barcode_type = Dcode.type
            text = '%s (%s)' % (barcode_data, barcode_type)
            if check_mod == 1 and Find_QR == 'Waiting' and barcode_data != latest_QR:
                t1 = int(round(time.time()))
                QR_count = QR_count + 1
                Find_QR = barcode_data
                print(f'QR 인식 {QR_count}번째 : {Find_QR}')
            Check_QR = barcode_data
    else:
        Check_QR = '인식되는 QR 없음'
    millis = t2 - t1
    if millis >= 3 and not t1 == 0:
        check_mod = 2

    cv2.rectangle(depth_image, (0, (height//2)+40),             (40, (height//2)+80),            (255))
    cv2.rectangle(depth_image, ((width//2-20), (height//2)+40), ((width//2)+20, (height//2)+80), (255))
    cv2.rectangle(depth_image, (width-40, (height//2)+40),      (width, (height//2)+80),         (255))

    cv2.putText(color_image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.rectangle(color_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

if __name__ == "__main__":
    try:
        rospy.init_node("Path_Finder", anonymous = True)
        pipeline = Ladar_setting()
        while True:
            color_image, depth_image = display(pipeline) 
            Direction(LEFT_MEAN, FRONT_MEAN, RIGHT_MEAN)
            Moving()
            QR_OPENCV(color_image, depth_image)

            cv2.imshow("color_image", color_image)
            cv2.imshow("depth_image", depth_image)
            key = cv2.waitKey(30)
            if key == 27:
                break            
    
    except rospy.ROSInterruptException:
        print('error')
        pass