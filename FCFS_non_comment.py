import json
# json파싱을 위한 import

import json_parse

import pandas as pd


def FCFS(process) :
    
    ret = list()
    
    # number of process
    pro_num = len(process)
    
    # waiting_time_buf를 저장할 배열을 만들어준다
    waiting_time_buf = [0] * pro_num
    
    # waiting_time을 저장할 배열을 만들어준다
    waiting_time = [0] * pro_num
    
    # left_time을 저장할 배열을 만든다
    left_time = [0] * pro_num
    
    # run_idx 를 만들어 runnig의 idx를 바꾸어준다
    # 초기 스테이트를 음수로 주어 시작을 알린다
    run_idx = -1
    
    # 총 running time
    running_time = 0
    
    # response time buf
    # -1 을 준 이유는 -1이면 업데이트가 한번도 되지 않음을 주어서
    # 업데이트 후 res로 넘기기 위함
    res = [-1]*pro_num
    
    # turnaround time 저장할 배열
    turn_time = [0]*pro_num
    
    # 각 프로세스의 인덱스와 버스트 타임을 넣어주고 숫자로 변형
    for i in range(0,pro_num):  
        
        # 각 idx 별 burst time 은 진행해야할 남은 시간
        left_time[i] = process[i]['burst_time']
    
    while(True):
        
        # 초기 스테이트의 값을 지정
        if(run_idx < 0):
            run_idx = 0
            waiting_time[run_idx] = waiting_time_buf[run_idx]
            if(res[run_idx] == -1):
                res[run_idx] = running_time
        
        
        for i in range(0,pro_num):
            if(i == run_idx):
                # run_idx의 남은 시간을 -1씩
                left_time[i] = left_time[i] - 1
            else:
                # 나머지는 대기시간 증가
                waiting_time_buf[i] = waiting_time_buf[i] + 1
        
        # 위의 행동을 실행하면 실질적으로 1초를 체크 한것이므로 running +1
        running_time = running_time + 1 
        
        if(left_time[run_idx] == 0):
            turn_time[run_idx] = running_time
            
            # 런스테이트의 남은 시간이 0이 되면 실행
            if(run_idx == (pro_num-1)):
                # 러닝 스테이트의 인덱스가 마지막이라면 브레이크
                break
            else:
                # 다음 런 스테이트로 이동
                run_idx = run_idx + 1
                waiting_time[run_idx] = waiting_time_buf[run_idx]
                if(res[run_idx] == -1):
                    res[run_idx] = running_time
        
    # 평균 반환시간 구하기
    total_turn = 0
    avg_turn = 0
    
    for i in range(0,pro_num):
        total_turn = total_turn + turn_time[i]
    
    avg_turn = total_turn / pro_num
    
    # 평균 대기시간 구하기
    total_wait = 0
    avg_wait = 0
    
    for i in range(0,pro_num):
        total_wait = total_wait + waiting_time[i]
    
    avg_wait = total_wait/pro_num
    
    # 평균 응답시간 구하기
    total_res = 0
    avg_res = 0
    
    for i in range(0,pro_num):
        total_res = total_res + res[i]
    
    avg_res = total_res/pro_num
    
    
    print("number of process is",pro_num)
    print("total running time",running_time)
    print("1. cpu utilization is",running_time/running_time)
    print("2. througput is",pro_num/running_time)
    print("3. each turnaround time",turn_time)
    print("3_a. average turnaround time",avg_turn)
    print("4. waiting time", waiting_time)
    print("4_a. average waiting time", avg_wait)
    print("5. response time is",res)
    print("5_a. average response time is",avg_res)
    
        
        

with open('./process.json','r') as f:
    data = json.load(f)
# json 파일 안의 모든 내용을 data에 저장장

process = json_parse.make_process(data)

FCFS(process)
# 중앙처리장치 이용률
    # running time / (runningtime + idle_time)
# 처리율
    # 프로세스의 갯수 / 총시간 
# 반환시간, 소요시간(turnaround time)
    # 종료시간 - 도착시간 
# 대기시간
    # 레디큐에서 기다린 시간
# 응답시간
    # 작업이 처음 시작한 시간 
    
    
