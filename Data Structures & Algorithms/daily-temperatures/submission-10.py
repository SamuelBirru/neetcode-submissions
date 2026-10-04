class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [] # temp, index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackI = stack.pop()
                results[stackI] = i - stackI
            stack.append((temp, i)) 

        return results

        '''

        monotonically decreasing stack
        '''