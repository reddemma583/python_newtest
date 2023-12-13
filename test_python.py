def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Sample list
numbers = [4, 2, 7, 1, 9, 3]

# Call the bubble_sort function
bubble_sort(numbers)

# Display the sorted list
print("Sorted list:", numbers)

