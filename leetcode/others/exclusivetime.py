'''
Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.

Example 2:

Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
Output: [8]
Explanation:
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls itself again.
Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.
'''
def exclusiveTime(n,logs):
    res = [0]*n
    stack = []
    prev = 0
    for log in logs:
        fn,typ, time = log.split(":")
        fn,time = int(fn), int(time)
        if typ == "start":
            if stack:
                res[stack[-1]] += time - prev
            stack.append(fn)
            prev = time
        else:
            res[stack.pop()] += time-prev+1
            prev = time+1
    return res
def exclusiveTime_not_so_efficient(n, logs):
    st = []
    res = [0]*n
    slist = logs[0].split(":")
    
    st.append(slist[0])
    i = 1
    time = int(slist[2])
    while i < len(logs):
        
        s = logs[i].split(":")
        while time < int(s[2]):
            j = int(st[len(st)-1])
            res[j]+=1
            time+=1
        if s[1] == "start":
            st.append(s[0])
        else:
            j = int(st[len(st)-1])
            res[j]+=1
            time+=1
            st.pop()
        i+=1
    return res

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(exclusiveTime(n,logs))
        