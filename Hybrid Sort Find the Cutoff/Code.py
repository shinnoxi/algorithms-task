import random
import time
import matplotlib.pyplot as plt


def insertion_sort(arr, left, right):
    """ترتيب المقطع المحدد داخل المصفوفة باستخدام Insertion Sort"""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    """دمج مصفوفتين فرعيتين مرتبتين"""
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def hybrid_sort_helper(arr, left, right, k):
    """دالة الترتيب الهجين بالتبديل إلى Insertion Sort إذا كان الحجم أقل من k"""
    # إذا كان الحجم أقل من أو يساوي k، نستخدم الترتيب بالإدراج
    if (right - left + 1) <= k:
        insertion_sort(arr, left, right)
        return

    if left < right:
        mid = (left + right) // 2
        hybrid_sort_helper(arr, left, mid, k)
        hybrid_sort_helper(arr, mid + 1, right, k)
        merge(arr, left, mid, right)


def hybrid_sort(arr, k):
    arr_copy = arr.copy()
    hybrid_sort_helper(arr_copy, 0, len(arr_copy) - 1, k)
    return arr_copy


def find_best_k():
    array_size = 100000
    # تجربة قيم مختلفة للعتبة k
    k_values = [1, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100]
    trials_per_k = 5

    print(f"Testing on array of size n = {array_size}")
    print(f"{'k':<8} | {'Average Time (seconds)':<25}")
    print("-" * 38)

    average_times = []

    for k in k_values:
        total_time = 0.0
        for _ in range(trials_per_k):
            test_data = [random.randint(1, 1000000) for _ in range(array_size)]
            start = time.perf_counter()
            hybrid_sort(test_data, k)
            total_time += time.perf_counter() - start

        avg_time = total_time / trials_per_k
        average_times.append(avg_time)
        print(f"{k:<8} | {avg_time:<25.6f}")

    # تحديد أفضل قيمة لـ k
    best_k = k_values[average_times.index(min(average_times))]
    print("-" * 38)
    print(f"Optimal Cutoff Value (Best k): {best_k}")

    # رسم النتائج بيانيًا
    plt.figure(figsize=(9, 5))
    plt.plot(k_values, average_times, marker="o", color="royalblue", linewidth=2)
    plt.axvline(best_k, color="red", linestyle="--", label=f"Best k = {best_k}")
    plt.title("Finding Optimal Cutoff Threshold (k) for Hybrid Sort")
    plt.xlabel("Cutoff Size (k)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("hybrid_sort_cutoff.png")
    plt.show()


if __name__ == "__main__":
    find_best_k()