class SeatManager:

    def __init__(self, n: int):
        self.available_seats = [i for i  in range(1, n+1)]
        heapq.heapify(self.available_seats)

    def reserve(self) -> int:
        return heappop(self.available_seats)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.available_seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)