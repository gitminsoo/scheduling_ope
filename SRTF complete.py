import json
import json_parse


def SRTF(process):
    
    # num of process
    pro_num = len(process)
    
    # total time
    running_time = 0
    
    # each process's left time
    left_time = [0] * pro_num
    
    for i in range(0,pro_num):
        left_time[i] = process[i]['burst_time']
    
    # running state's idx
    run_idx = -1
    
    # ready queue flag
    ready_flag = [0] * pro_num
    
    # shortest idx buffer
    short_buf = -1
    
    # response time array
    res = [-1] * pro_num
    
    # terminate time
    term = [0] * pro_num
    
    while(True):
        
        if(left_time[run_idx] == 0):
            ready_flag[run_idx] = -1
            term[run_idx] = running_time
        
        for i in range(0,pro_num):
            if(process[i]['arrival_time']==running_time):
                ready_flag[i]=1
                
                if(run_idx == -1):
                    run_idx = i
                    res[run_idx] = running_time
                
                else:
                    if(left_time[run_idx]>left_time[i]):
                        run_idx = i
            elif(left_time[run_idx]==0):
                
                for i in range(0,pro_num):
                    if(ready_flag[i] == 1):
                        short_buf = i
                        
                for i in range(0,pro_num):
                    if(ready_flag[i] == 1):
                        if(left_time[short_buf]>left_time[i]):
                            short_buf = i
                            
                run_idx = short_buf
        if(res[run_idx]==-1):
         res[run_idx] = running_time

        
        if(left_time[run_idx]==0):
            break
        left_time[run_idx] = left_time[run_idx]-1
        running_time = running_time +1
    
    # 반환시간은 결론적으러
    # 프로세스가 끝난시간 - 프로세스가 도착한 시간이다
    turn_time = [0]*pro_num
    avg_turn = 0
    for i in range(0,pro_num):
        turn_time[i] = term[i] - process[i]['arrival_time']
        avg_turn = turn_time[i]
    avg_turn = avg_turn / pro_num
    
    print("turn",turn_time)
    
    wait_time = [0]*pro_num
    avg_wait = 0
    for i in range(0,pro_num):
        wait_time[i] = turn_time[i] - process[i]['burst_time']
        avg_wait = wait_time[i]
    avg_wait = avg_wait / pro_num
    
    print("wait",wait_time)
    
    print("res",res)
    avg_res = 0
    for i in range(0,pro_num):
        avg_res = res[i]
    avg_res = avg_res / pro_num
    
    print("avg_turn",avg_turn,"avg_wait",avg_wait,"avg_res",avg_res)
        
    
                        
                        
   
    
    
    
with open('./process.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)
pre = json_parse.extract_preemptive(data)



SRTF(process)