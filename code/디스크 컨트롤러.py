import heapq

def solution(jobs):
    job_list = sorted(jobs)
    heap = []
    n1, n2 = job_list.pop(0)
    _num = n1
    _now = n2
    answer = 0
    while True:
        _num += _now
        answer += _now
        if job_list == [] and heap == []:
            answer = answer // len(jobs)
            break
        while True:
            if job_list == [] or job_list[0][0] > _num:
                break
            n1, n2 = job_list.pop(0)
            heapq.heappush(heap, [n2, n1])
        if heap:
            _now1, _now2 = heapq.heappop(heap)
            _now = _now1
            answer += _num - _now2
        else:
            if job_list:
                n1, n2 = job_list.pop(0)
                _num = n1
                _now = n2
            
    return answer