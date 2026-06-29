from job import Job

def sortJobsAndGetPreAndMemo_(jobs: list[Job]):
    jobs.sort(key=lambda job: job.finish)

    # Get jobs' pre index
    lenJobs = len(jobs)
    pre: list[int] = [0] * lenJobs
    for i in range(0, lenJobs):
        pre[i] = -1
        for j in range(lenJobs):
            if jobs[j].finish > jobs[i].start:
                break
            else:
                pre[i] = j
    
    memo: list[float] = [0] * (lenJobs + 1)
    for i in range(1, lenJobs + 1):
        # Custo incluindo na solução
        incl = jobs[i-1].weight + memo[pre[i-1] + 1]
        # Custo não incluindo na solução
        excl = memo[i-1]
        memo[i] = max(incl, excl)

    return (pre, memo)

def findSolution_(jobs: list[Job], pre: list[int], memo: list[float]):
    result: list[Job] = []
    i = len(jobs)

    while i > 0:
        # Se incluir o Job i-1 dá o mesmo valor que memo[i], então ele foi escolhido
        if jobs[i-1].weight + memo[pre[i-1] + 1] > memo[i-1]:
            result.insert(0, jobs[i-1])
            i = pre[i-1] + 1   # pular para o índice do Job compatível anterior
        else:
            i -= 1             # caso contrário, apenas andar para trás

    return result

def weightedIntervalScheduling(jobs: list[Job]):
    (pre, memo) = sortJobsAndGetPreAndMemo_(jobs)
    return findSolution_(jobs, pre, memo)