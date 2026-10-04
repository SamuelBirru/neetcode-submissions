class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # [temp, index]
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([temp,i])
        return result
                

        '''
        i = day

        temperatures[i] = temp at i day

        result[i] = # of days after i before a warmer day

        temperatures[i + k] > temperatures [i]

        result[i] = k - i


        '''