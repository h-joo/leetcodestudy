
def calculate_maximum(root, reports, informTime):
    if root not in reports:
        return informTime[root]
    
    return informTime[root] + max([calculate_maximum(report, reports, informTime) for report in reports[root]])

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        reports = {}
        for employee_id in range(len(manager)):
            current_manager = manager[employee_id]
            if current_manager == -1:
                continue
            if current_manager not in reports:
                reports[current_manager] = set()
            reports[current_manager].add(employee_id)
        
        return calculate_maximum(headID, reports, informTime)
