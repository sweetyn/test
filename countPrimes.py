"""204. Count Primes
Count the number of prime numbers less than a non-negative number, n.
"""
import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        aaa=0

        #option2
        # divNum = [2,3,5]
        # if n <= 2:
        #     return 0
        #
        # #Count the prime #
        # else:
        #     count = 0
        #     for j in range(2, n):
        #         isPrime = True
        #
        #         if j <= 1:
        #             isPrime = False
        #             continue
        #         elif j in divNum:
        #             count += 1
        #             continue
        #         else:
        #             i = 0
        #             while i < len(divNum):
        #                 if j % divNum[i] == 0:
        #                     isPrime = False
        #                     break
        #
        #                 # print(j, divNum[i])
        #                 i += 1
        #
        #
        #
        #
        #             # for i in divNum:
        #             #     if j % i == 0 and isPrime == True:
        #             #         print(j, i)
        #             #         isPrime = False
        #             #         break
        #             #     else:
        #             #         print("prime:", j, i)
        #
        #
        #         if isPrime == True:
        #             if j not in divNum:
        #                 divNum.append(j)
        #                 # print(divNum)
        #             count += 1
        #
        # return count




        #option1
        # if n <= 2:
        #     return 0
        #
        # #Count the prime #
        # else:
        #     i = 1
        #     count = 0
        #
        #     while n-i >= 2:
        #         isPrime = True
        #
        #         for j in range(n-i):
        #
        #             if j > 1 and isPrime == True:
        #                 # print(n-i, j, (n-i) % j)
        #
        #                 if (n-i) % j == 0:
        #                     # print("no")
        #                     isPrime = False
        #                     break
        #
        #         if isPrime == True:
        #             # print("prime", n-i)
        #             count += 1
        #
        #         i += 1
        #
        # return count


        # option 3
        # prime_nums = []
        #
        # if n <= 2:
        #     return 0
        #
        # elif n == 3:
        #     prime_nums.append(n-1)
        #
        # else:
        #     for i in range(3, n, 2):
        #         j=0
        #         # print(i)
        #         while j < len(prime_nums):
        #             if i % prime_nums[j] == 0:
        #                 break
        #             j += 1
        #         else:
        #             prime_nums.append(i)
        #
        #     prime_nums.insert(0,2)
        #
        # print(prime_nums)
        #
        # return len(prime_nums)


        # option 4
        prime_nums = []

        if n <= 2:
            return 0

        elif n == 3:
            prime_nums.append(2)

        elif n >= 4:
            prime_nums.append(2)

            for i in range(3, n, 2):
                # print("1:", i)
                j = 0
                # while int(i ** 0.5) >= prime_nums[j]:
                while int(math.sqrt(i)) >= prime_nums[j]:
                    if i % prime_nums[j] == 0:
                        break

                    j += 1
                else:
                    prime_nums.append(i)
                    x = False

        return len(prime_nums)




test1 = Solution()
#test cases
# print (test1.countPrimes(2))    #expected 0
# print (test1.countPrimes(3))    #expected 1
# print (test1.countPrimes(4))    #expected 2
# print (test1.countPrimes(5))    #expected 2
# print (test1.countPrimes(6))    #expected 3
# print (test1.countPrimes(1000))    #expected 168
# print (test1.countPrimes(10000))    #expected 1229
print (test1.countPrimes(499979))    #expected 133329
