class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and a < 0:
                if stack[-1] + a < 0:
                    stack.pop()
                    continue
                elif stack[-1] + a > 0:
                    alive = False
                elif stack[-1] + a == 0:
                    stack.pop()
                    alive = False
            if alive:
                stack.append(a)
        return stack