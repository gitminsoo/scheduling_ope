import json

import json_parse

def FCFS(process) :
    
    pro_num = len(data['process'])
    
    
    waiting_time_buf = [0] * pro_num
    
    waiting_time = [0] * pro_num
    
    left_time = [0] * pro_num
    
    run_idx = -1
    
    running_time = 0
    
    res = [-1]*pro_num
    
    turn_time = [0]*pro_num
    
    for i in range(0,pro_num):
       
        left_time[i] = process[i]['burst_time']
    
    while(True):
        
        if(run_idx < 0):
            run_idx = 0
            waiting_time[run_idx] = waiting_time_buf[run_idx]
            if(res[run_idx] == -1):
                res[run_idx] = running_time
        
        
        for i in range(0,pro_num):
            if(i == run_idx):
                left_time[i] = left_time[i] - 1
            else:
                waiting_time_buf[i] = waiting_time_buf[i] + 1
        
        running_time = running_time + 1 
        
        if(left_time[run_idx] == 0):
            turn_time[run_idx] = running_time
            
            if(run_idx == (pro_num-1)):
                break
            else:
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
    
    
    ret = {}
    
    ret['num_of_process'] = pro_num
    ret['total_running_time'] = running_time
    ret['cpu_utilization'] = running_time  / running_time
    ret['throughput'] = pro_num/running_time
    ret['avg_turnaround_time'] = avg_turn
    ret['avg_waiting_time']= avg_wait
    ret['avg_response_time'] = avg_res
    
    
    return ret
    
    
        
    
   
    
    
    
        
        

with open('./process.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)

ret = FCFS(process)
    
print(ret)
