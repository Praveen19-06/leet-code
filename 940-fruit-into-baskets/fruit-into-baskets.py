class Solution:
    def totalFruit(self, fruits):
        a = b = -1
        count_a = count_b = 0
        left = 0
        ans = 0

        for right in range(len(fruits)):
            if fruits[right] == a:
                count_a += 1

            elif fruits[right] == b:
                count_b += 1

            else:
                while count_a > 0 and count_b > 0:
                    if fruits[left] == a:
                        count_a -= 1
                    else:
                        count_b -= 1
                    left += 1

                if count_a == 0:
                    a = fruits[right]
                    count_a = 1
                else:
                    b = fruits[right]
                    count_b = 1

            ans = max(ans, right - left + 1)

        return ans