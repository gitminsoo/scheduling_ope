import json
# json파싱을 위한 import

def extract_preemptive(data):
    pre = data['preemptive']['preemptive']
    
    return pre

def make_process(data):
    # 파싱 한 후 숫자로 변환
    
    pro_num = len(data['process'])
    
    process = list()
    
    for i in range(0,pro_num):
        process.append(data['process'][i])
        process[i]['process_idx'] = int(process[i]['process_idx'])
        process[i]['burst_time'] = int(process[i]['burst_time'])
        process[i]['arrival_time']=int(process[i]['arrival_time'])
        process[i]['priority']=int(process[i]['priority'])
        
    
    return process

    
    


