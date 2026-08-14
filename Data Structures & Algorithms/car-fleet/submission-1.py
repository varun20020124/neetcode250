class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        max_time = 0
        fleet = 0
        for pos,spd in cars:
            time = (target-pos)/spd
            if time > max_time:
                max_time = time
                fleet += 1
        return fleet 