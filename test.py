'''
변수 모음
car_controls.steering : 핸들 (1~ -1) + 면 오른쪽
car_controls.throttle : 전진 (1~ -1) + 전진
car_controls.brake : 브레이크 (0~ 1)
self.half_road_limit : 도로 폭의 반과 차 폭의 반을 더한 값 ( 5 + 1.25 = 6.25)
sensing_info.to_middle  :  차와 중앙차선과의 거리 (+ 면 오른쪽, -면 왼쪽)
sensing_info.collided  :  충돌, True
sensing_info.speed  :  차량 속도
sensing_info.moving_forward  :  앞으로 가는지
sensing_info.moving_angle  :  차와 중앙차선과의 각도
sensing_info.track_forward_angles  :  앞의 10개 구간 차와 중앙차선의 각도
sensing_info.distance_to_way_points  :  앞의 10개 구간 차와 중앙차선과의 거리
sensing_info.lap_progress : 골인
sensing_info.track_forward_obstacles  :  앞의 장애물의 정 가운데가 중앙차선과 떨어져있는 위치 정보 (장애물크기 2m)
'''

car_controls.throttle = 1
car_controls.brake = 0

if sensing_info.track_forward_obstacles:
    if (sensing_info.track_forward_obstacles[0] - 1) <= sensing_info.to_middle <= (sensing_info.track_forward_obstacles[0] + 1):
        car_controls.steering = -0.5


if sensing_info.moving_angle > 0:
    car_controls.steering = -0.5

if sensing_info.moving_angle < 0:
    car_controls.steering = 0.5

if sensing_info.to_middle >= self.half_road_limit:
    car_controls.steering = -0.5

if -(sensing_info.to_middle) >= self.half_road_limit:
    car_controls.steering = 0.5

if sensing_info.collided == True:
    car_controls.steering = -0.9

if sensing_info.to_middle == 4:
    car_controls.steering = 0
elif sensing_info.to_middle < 4:
    car_controls.steering = 0.1
else:
    car_controls.steering = -0.1

if sensing_info.moving_forward == False:
