# Python Promise Library

A lightweight, thread-safe Promise implementation for Python that brings JavaScript-style Promise functionality to your Python applications.

## Overview

This library provides a Promise class that represents a value which may be available now, or in the future, or never. It follows the same conceptual model as JavaScript Promises, allowing for cleaner asynchronous code without deeply nested callbacks.

## Features

- Thread-safe implementation using locks
- Chainable API with `then()` and `catch()` methods
- Automatic error propagation
- Support for asynchronous value resolution
- Minimal dependencies (only uses Python's standard `threading` module)

## Installation

```bash
# Coming soon to PyPI
pip install python-promise
```

## Usage

### Basic Usage

```python
from promise import Promise

# Create a new promise
promise = Promise()

# Define success and error handlers
def on_success(value):
    print(f"Success: {value}")

def on_error(error):
    print(f"Error: {error}")

# Register callbacks
promise.then(on_success).catch(on_error)

# Resolve the promise
promise.resolve(lambda: "Hello, World!")
```

### Asynchronous Operations

```python
import time
from promise import Promise

def fetch_data():
    # Simulate network request
    time.sleep(2)
    return {"data": "Some important data"}

# Create and immediately start resolving a promise
promise = Promise()
promise.resolve(fetch_data)

# The callback will be executed once the data is available
promise.then(lambda data: print(f"Received: {data}"))

print("Fetching data in background...")
# Continue doing other work while the promise resolves
```

### Error Handling

```python
from promise import Promise

def risky_operation():
    # This will raise an exception
    return 1 / 0

promise = Promise()
promise.then(lambda value: print(f"This won't run: {value}"))
promise.catch(lambda error: print(f"Caught an error: {error}"))

# The error will be caught and handled
promise.resolve(risky_operation)
```

## API Reference

### `Promise()`

Creates a new Promise object.

### `Promise.then(callback)`

Registers a callback to be called when the promise is resolved.

- **Parameters:**
  - `callback`: A function that takes the resolved value as its single parameter
- **Returns:** The promise object (for chaining)

### `Promise.catch(callback)`

Registers a callback to be called when the promise is rejected.

- **Parameters:**
  - `callback`: A function that takes the error as its single parameter
- **Returns:** The promise object (for chaining)

### `Promise.resolve(value)`

Resolves the promise with a given value.

- **Parameters:**
  - `value`: A function that returns the value to resolve the promise with

### `Promise.reject(error)`

Rejects the promise with a given error.

- **Parameters:**
  - `error`: The error to reject the promise with

## Implementation Details

The Promise implementation uses Python's threading module to handle asynchronous operations:

- Each promise has a thread lock to ensure thread safety
- Resolution is handled in a separate thread to avoid blocking
- Callbacks are executed immediately if the promise is already resolved/rejected when they're registered

## Limitations

- Unlike JavaScript Promises, this implementation does not support `Promise.all()` or `Promise.race()` yet
- Promises are resolved in separate threads rather than an event loop
- The value provided to `resolve()` must be callable (a function or lambda)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
