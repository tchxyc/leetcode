# import threading
# import itertools
# import time, math
# from threading import Thread, Event
# import multiprocessing

# n = 5_000_111_000_222_021

# import asyncio


# async def spin(msg: str) -> None:
#     for char in itertools.cycle(r"\|/-"):
#         status = f"\r{char} {msg}"
#         print(status, flush=True, end="")
#         try:
#             await asyncio.sleep(0.1)
#         except asyncio.CancelledError:
#             break
#     blanks = " " * len(status)

#     print(f"\r{blanks}\r", end="")


# async def slow() -> int:
#     await asyncio.sleep(3)
#     # time.sleep(3)
#     return 42


# async def supervisor() -> int:
#     spinner = asyncio.create_task(spin("thinking!"))
#     print(f"spinner object: {spinner}")
#     result = await slow()
#     spinner.cancel()
#     return result


# def main():
#     result = asyncio.run(supervisor())
#     print(f"Answer: {result}")


# # async def is_prime(x: int) -> bool:
# #     if x < 2:
# #         return False
# #     i = 2
# #     while i * i <= x:
# #         if x % i == 0:
# #             return False
# #         i += 1
# #     return True


# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False

#     root = math.isqrt(n)
#     for i in range(3, root + 1, 2):
#         if n % i == 0:
#             return False
#     return True


# if __name__ == "__main__":
#     # main()
#     # cur = time.time()
#     print(multiprocessing.cpu_count())
#     # print(time.time() - cur)

import leetcode
