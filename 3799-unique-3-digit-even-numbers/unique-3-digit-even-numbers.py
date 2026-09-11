class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        num = []
        for i in range(len(digits)):
            for j in range(len(digits)):
                if i == j or digits[i] == 0:
                    continue
                else:
                    for k in range(len(digits)):
                        if j == k or i == k:
                            continue
                        else:
                            if (digits[i]*100+digits[j]*10+digits[k]) % 2 == 0:
                                num.append(digits[i]*100+digits[j]*10+digits[k])
        num = set(num)
        num = list(num)
        return len(num)