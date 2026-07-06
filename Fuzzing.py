import random
import string
import traceback

def fuzz_function(target_func, iterations=1000):
    crashes = []
    for i in range(iterations):
        # Generate random/malformed input
        input_type = random.choice(["string", "int", "bytes", "empty", "huge"])
        if input_type == "string":
            test_input = ''.join(random.choices(string.printable, k=random.randint(0, 50)))
        elif input_type == "int":
            test_input = random.randint(-2**31, 2**31)
        elif input_type == "bytes":
            test_input = bytes(random.getrandbits(8) for _ in range(random.randint(0, 20)))
        elif input_type == "empty":
            test_input = ""
        else:
            test_input = "A" * random.randint(1000, 10000)

        try:
            target_func(test_input)
        except Exception as e:
            crashes.append((test_input, str(e), traceback.format_exc()))

    return crashes

def example_target(data):
    if isinstance(data, str) and len(data) > 5000:
        raise MemoryError("Simulated overflow")
    return data[:10]

results = fuzz_function(example_target, iterations=500)
print(f"Found {len(results)} crashes")
for inp, err, _ in results[:3]:
    print(f"Input caused: {err}")