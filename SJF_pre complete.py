import json
import json_parse


def SJF_pre(process):
    
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
                    if(process[run_idx]['burst_time']>process[i]['burst_time']):
                        run_idx = i
            elif(left_time[run_idx]==0):
                
                for i in range(0,pro_num):
                    if(ready_flag[i] == 1):
                        short_buf = i
                        
                for i in range(0,pro_num):
                    if(ready_flag[i] == 1):
                        if(process[short_buf]['burst_time']>process[i]['burst_time']):
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
    for i in range(0,pro_num):
        turn_time[i] = term[i] - process[i]['arrival_time']
    
    print(turn_time)
    
    wait_time = [0]*pro_num
    for i in range(0,pro_num):
        wait_time[i] = turn_time[i] - process[i]['burst_time']
    
    print(wait_time)
    
    print(res)
    
                        
                        
   
    
    
    
with open('./process.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)
pre = json_parse.extract_preemptive(data)



SJF_pre(process)