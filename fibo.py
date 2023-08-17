import asyncio as a
import random

from pip._vendor.distlib.compat import raw_input


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


async def calculate_fibonacci_async_with_delay(n, order):
    delay = random.uniform(0.0, 1)
    await a.sleep(delay)
    result = fib(n)
    print(f"Fibonacci of number {n} = {result}, finished {order}")
    return n, result


async def main():
    num1 = int(raw_input("Enter First Integer Number!\n"))
    num2 = int(raw_input("Enter Second Integer Number!\n"))
    if num1 < 0 or num2 < 0:
        print("Please enter a positive integer")
    else:
        tasks = [calculate_fibonacci_async_with_delay(num1, "first"), calculate_fibonacci_async_with_delay(num2, "second")]

        completed_tasks = []
        for task in a.as_completed(tasks):
            completed_task = await task
            completed_tasks.append(completed_task)

        first_completed_task = completed_tasks[0]
        print(f"Fibonacci of number {first_completed_task[0]} finished first with result {first_completed_task[1]}")


if __name__ == "__main__":
    a.run(main())
