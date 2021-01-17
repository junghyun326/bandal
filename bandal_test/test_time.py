import timeit
 
start_time = timeit.default_timer() # 시작 시간 체크
 
sum = 0
 
for i in range(100000000):
    sum += i
    
terminate_time = timeit.default_timer() # 종료 시간 체크  
 
print("%f초 걸렸습니다." % (terminate_time - start_time))