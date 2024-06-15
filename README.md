# Promise Class for Asynchronous-like Behavior in Python

This file provides a `Promise` class that can be used to simulate asynchronous behavior in Python using threads and callbacks.

## Installation

There's no installation required for this code. You can simply copy the `promise.py` file to your project directory and import it into your Python scripts.

## Usage

1. **Import the `Promise` class:**

   ```python
   from promise import Promise
   ```

2. **Create a `Promise` instance:**

   ```python
   promise = Promise()
   ```

3. **Define asynchronous operations:**

   - You'll need to implement your own asynchronous operations (functions that take some time to complete). These functions should return the result value when successful.

4. **Resolve the promise:**

   - Once your asynchronous operation completes, call the `resolve` method of the promise object, passing the result value as an argument. This will trigger any registered `then` callback.

   ```python
   def my_async_operation():
       # Simulate some asynchronous work (e.g., network request, file I/O)
       import time
       time.sleep(2)  # Replace with your actual asynchronous operation
       return "Asynchronous result"

   # Call the asynchronous operation and resolve the promise
   promise.resolve(my_async_operation)
   ```

5. **Handle successful completion (optional):**

   - Use the `then` method to register a callback function that will be executed when the promise is resolved. This callback function will receive the result value from the asynchronous operation.

   ```python
   promise.then(lambda result: print("Success:", result))
   ```

6. **Handle errors (optional):**

   - Use the `catch` method to register a callback function that will be executed if the promise is rejected due to an error during the asynchronous operation. This callback function will receive the error object.

   ```python
   def handle_error(error):
       print("Error:", error)

   promise.catch(handle_error)
   ```

## Example Usage:

```python
from promise import Promise

def main():
    promise = Promise()

    def my_async_operation():
        import time
        time.sleep(2)  # Simulate asynchronous work
        return "Asynchronous result"

    promise.resolve(my_async_operation)

    promise.then(lambda result: print("Success:", result))
    promise.catch(lambda error: print("Error:", error))

if __name__ == "__main__":
    main()
```

## Important Notes:

- This approach simulates asynchronous behavior using threads and callbacks. Python has built-in mechanisms for asynchronous programming using the `async`/`await` keywords, but this example demonstrates a callback-based solution.
- For complex asynchronous tasks, consider using libraries like `concurrent.futures` or third-party asynchronous libraries in Python.

## Thread Safety:

- The `threading.Lock` object is used to ensure thread-safe access to the promise's internal state. This is crucial when multiple threads might interact with the same promise object.

## Disclaimer:

- Using threads can introduce complexity to your code. Consider using higher-level abstractions for asynchronous programming in Python whenever possible.
