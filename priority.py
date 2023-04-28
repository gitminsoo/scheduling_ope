import json

import json_parse

def Priority(process) :
    
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
    
    # response time array
    res = [-1] * pro_num
    
    # terminate time
    term = [0] * pro_num
    
    f_check = 0
    
    hi_pri = process[0]['priority']
    
    done = [0] * pro_num
    
    
    
    while(True):
        
        if(run_idx == -1):
            for i in range(0,pro_num):
                if(process[hi_pri]['priority']>process[i]['priority']):
                    hi_pri = i
            run_idx = hi_pri
            res[run_idx]= running_time
            
            
        
        if(left_time[run_idx] == 0):
            term[run_idx] = running_time
            done[run_idx] = 1
            for i in range(0,pro_num):
                if(done[i] == 0):
                    hi_pri = i
            for i in range(0,pro_num):
                if(done[i] == 0):
                    if(process[hi_pri]['priority']>process[i]['priority']):
                        hi_pri = i
            
            run_idx = hi_pri
            if(res[run_idx] == -1):
                res[run_idx] = running_time
            
            
        
        left_time[run_idx] = left_time[run_idx] -1
        running_time = running_time +1
        
        for i in range(0,pro_num):
            f_check = f_check + left_time[i]
        
        if(f_check == 0):
            term[run_idx] = running_time
            break
        f_check = 0
        
    print(term)
    print(res)
                        
            
    

    
        
        

with open('./process.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)

ret = Priority(process)
    
