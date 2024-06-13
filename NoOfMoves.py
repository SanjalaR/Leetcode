# Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = 0
        for i in range(len(students)):
            moves += abs(seats[i]-students[i])
        return moves
