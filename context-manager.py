import time


class Timer:
   def __enter__(self):
       self.start_time = time.time()
       return self

   def __exit__(self, exc_type, exc_value, traceback):
       self.end_time = time.time()
       elapsed_time = self.end_time - self.start_time
       print(f"Elapsed time: {elapsed_time} seconds")


# Example usage
if __name__ == "__main__":
   with Timer() as timer:
       # Code block to measure the execution time
       time.sleep(2)  # Simulate some time-consuming operation
       raise Exception()
# Elapsed time: 2.002082347869873 seconds

# Function based approach

# import time
# from contextlib import contextmanager


# @contextmanager
# def timer():
#    start_time = time.time()
#    yield
#    end_time = time.time()
#    elapsed_time = end_time - start_time
#    print(f"Elapsed time: {elapsed_time} seconds")


# # Example usage
# if __name__ == "__main__":
#    with timer():
#        time.sleep(2)
# Elapsed time: 2.0020740032196045 seconds
