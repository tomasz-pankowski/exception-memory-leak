import argparse
import gc
import objgraph
from time import sleep


class BigData:
    def __init__(self, size: int):
        self.data = "a" * size


def leak_exception():
    big_data = BigData(1024 * 1024)
    raise Exception("This exception will cause a memory leak")


def code_with_leak(step: int):
    error = None
    try:
        leak_exception()
    except Exception as e:
        error = e


def code_without_leak(step: int):
    error = None
    try:
        leak_exception()
    except Exception as e:
        error = e
    finally:
        del error


def count_objects():
    get_count = gc.get_count()
    print(f"BigData objects: {objgraph.count('BigData')}, "
          f"Gc count: {get_count}")


if __name__ == "__main__":
    # Add command-line argument parsing
    parser = argparse.ArgumentParser(description="Memory leak demonstration")
    parser.add_argument(
        "--mode",
        choices=["leak", "no-leak"],
        required=True,
        help="Select mode: 'leak' to demonstrate memory leak, 'no-leak' to run without leaks"
    )
    parser.add_argument(
        "--gc-enabled",
        action="store_true",
        help="Enable garbage collection (disabled by default)"
    )

    args = parser.parse_args()

    # Handle garbage collection based on args
    if not args.gc_enabled:
        gc.disable()
        print("Garbage collection disabled")
    else:
        gc.enable()
        print("Garbage collection enabled")

    # Select run mode based on args
    if args.mode == "leak":
        run_mode = code_with_leak
    else:
        run_mode = code_without_leak

    print("Running mode:", args.mode)
    print("Garbage collection enabled:", gc.isenabled())
    for s in range(10_000):
        if s % 100 == 0:
            sleep(1)
        if s % 100 == 0:
            count_objects()
        run_mode(s)
