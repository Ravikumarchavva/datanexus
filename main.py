def main():
    print("Hello from datanexus!")

def big_function_to_test_ruff():
    # This function is intentionally long to test Ruff's performance
    # and to see if it can handle large files without issues.
    for i in range(1000):
        print(f"Processing item {i}")
        if i % 100 == 0:
            print(f"Still working on item {i}...")
    print("Finished processing all items. Now doing something else. This is a placeholder for a big function that does something complex and time-consuming. It might involve a lot of calculations, data processing, or even network requests. The goal is to simulate a real-world scenario where the function takes a significant amount of time to complete. This is important for testing purposes, especially when we want to ensure that our code is optimized and doesn't have any performance bottlenecks. We might also want to check if Ruff can handle this without any issues or if it raises any warnings or errors during the process.")

if __name__ == "__main__":
    main()
