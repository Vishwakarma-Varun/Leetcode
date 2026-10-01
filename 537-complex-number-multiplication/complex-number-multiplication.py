class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.replace("i","j")
        num2 = num2.replace("i","j")
        if "+-" in num1 or "+-" in num2:
            num1 = num1.replace("+-","-")
            num2 = num2.replace("+-","-")
        ans = complex(num1)*complex(num2)
        if ans.real == 0:
            return f"0+{int(ans.imag)}i"
        if ans.imag < 0:
            return f"{str(int(ans.real))}+{int(ans.imag)}i"
        ans = str(ans)
        ans = ans.replace("j","i")

        if "(" in ans or "-" in ans:
            ans = ans.replace("(","")
            ans = ans.replace(")","")
        return ans