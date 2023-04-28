import json
import json_parse


def Priority_RR(process,quantum):
    
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
    
    # last time
    quantum_check = 0
    
    # finish check
    f_check = 0
    
    # priority를 정렬하여 저장
    # 하나씩 꺼내어 사용
    
    pri_set = list()
    
    for i in range(0,pro_num):
        if process[i]['priority'] not in pri_set:
            pri_set.append(process[i]['priority'])
    
    pri_set.sort()
    
    # 멀티 큐는 우선순위가 같은 작업끼리 모아둘
    # 리스트의 리스트 -> 이중 리스트를 저장하는 변수
    multi_que = list()
    
    for i in range(0,len(pri_set)):
        que = list()
        for j in range(0,pro_num):
            if(pri_set[i] == process[j]['priority']):
                que.append(j)
        multi_que.append(que)
    
    # print(multi_que)
    
    # step은 멀티큐의 어느 단계에서 
    # 라운드 로빈을 실행하고 있는지 알려주는 변수
     
    step = 0
    
    # 우선 멀티큐의 모든 스텝을 for문으로 이어준다
    for step in range(0,len(multi_que)):
        
        cnt = len(multi_que[step])

        while(1):
            # 만약 runstate 가 비어있다면 
            # 첫 스텝의 0번 인덱스로 시작한다
            # -> 우선순위가 제일 높은 애중에 랜덤 실행
            # 또한 이 함수의 run idx는 실제 인덱스가 아닌 
            # 멀티레벨 내의 인덱스로 지정한다
            if(run_idx == -1):
                run_idx = 0
            
            print(multi_que[step][run_idx])
            
            # 런 스테이트의 남은 시간을 하나씩 줄여준다
            left_time[multi_que[step][run_idx]] = left_time[multi_que[step][run_idx]] - 1
            
            # 실제 동작 시간은 하나씩 늘리고
            running_time = running_time +1
            # 퀀텀 기준 시간도 하나씩 늘린다
            quantum_check = quantum_check +1
            
            # 퀀텀 시간을 전부 채워 한 경우
            if(quantum_check % quantum == 0):
                # 퀀텀을 0으로 돌려준다
                quantum_check = 0
                # 해당 스텝의 범위를 보면서 만약
                # 실행시간이 남은 프로세스가 있으면 런스테이트를 넘긴다
                for i in range(0,len(multi_que[step])):
                    if(multi_que[step][(run_idx + i+1)%(len(multi_que[step]))] > 0):
                        run_idx = (run_idx +1)%(len(multi_que[step]))
                        
                        break
            
            # 런 스테이트가 시간을 다 한 경우
            if(left_time[multi_que[step][run_idx]]==0):
                # 퀀텀을 0으로 돌려준다
                quantum_check = 0
                for i in range(0,len(multi_que[step])):
                    if(multi_que[step][(run_idx + i+1)%(len(multi_que[step]))] > 0):
                        run_idx = (run_idx +1)%(len(multi_que[step]))

                        
                        break
            # f_check를 이용하여 해당 step의 
            # 프로세스가 모두 끝났는지 확인한다
            # f_check로 해당 스텝의 모든 남은 시간을 더한다
            for i in range(0,len(multi_que[step])):
                f_check = f_check + left_time[multi_que[step][i]]
            if(f_check == 0):
                # 스텝이 끝난 경우 러닝스테이트를 비워주어
                # 다음 스텝에서 0번 인덱스부터 시작하게 해준다
                run_idx = -1
                break
            f_check = 0
            
    print(running_time)
                    
                
                
                        
                    
                
            
        
                
    
        
        
        
        
    
     
   
   
    
    
    
with open('./process.json','r') as f:
    data = json.load(f)

process = json_parse.make_process(data)
pre = json_parse.extract_preemptive(data)



Priority_RR(process,2)