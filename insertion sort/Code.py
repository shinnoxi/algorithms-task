import random
import time
import matplotlib.pyplot as plt


def insertion_sort(arr):
    """
    يقوم بترتيب المصفوفة باستخدام Insertion Sort
    ويرجع: (المصفوفة المرتبة، عدد المقارنات، عدد الإزاحات)

    """
    arr = arr.copy()
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        
        # إذا انتهى التكرار بسبب j < 0، لا نحسب مقارنة إضافية
        arr[j + 1] = key

    return arr, comparisons, shifts


def measure_time(sort_fn, data):
    """قياس وقت التنفيذ بالثواني"""
    start = time.perf_counter()
    sort_fn(data)
    end = time.perf_counter()
    return end - start


def run_experiment():
    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]

    times_sorted = []
    times_reverse = []
    times_random = []

    print(f"{'Size (n)':<10} | {'Sorted (s)':<12} | {'Reverse (s)':<12} | {'Random (s)':<12}")
    print("-" * 52)

    for n in sizes:
        # تجهيز البيانات
        sorted_data = list(range(n))
        reverse_data = list(range(n, 0, -1))
        random_data = [random.randint(1, n) for _ in range(n)]

        # قياس الوقت
        t_sorted = measure_time(insertion_sort, sorted_data)
        t_reverse = measure_time(insertion_sort, reverse_data)
        t_random = measure_time(insertion_sort, random_data)

        times_sorted.append(t_sorted)
        times_reverse.append(t_reverse)
        times_random.append(t_random)

        print(f"{n:<10} | {t_sorted:<12.6f} | {t_reverse:<12.6f} | {t_random:<12.6f}")

    # رسم النتائج ومقارنتها بالمنحنيات النظرية
    plot_results(sizes, times_sorted, times_reverse, times_random)


def plot_results(sizes, t_sorted, t_reverse, t_random):
    plt.figure(figsize=(10, 6))

    # البيانات التجريبية
    plt.plot(sizes, t_sorted, label="Best Case (Sorted)", marker="o")
    plt.plot(sizes, t_random, label="Average Case (Random)", marker="s")
    plt.plot(sizes, t_reverse, label="Worst Case (Reverse)", marker="^")

    # منحنيات نظرية للمقارنة (scaled للرسم)
    
    max_t = max(t_reverse)
    max_n = max(sizes)
    theoretical_n2 = [(n ** 2) / (max_n ** 2) * max_t for n in sizes]
    theoretical_n = [n / max_n * (max(t_sorted) if max(t_sorted) > 0 else 0.001) for n in sizes]

    plt.plot(sizes, theoretical_n2, "--", color="gray", label="Reference O(n²)")
    plt.plot(sizes, theoretical_n, ":", color="black", label="Reference O(n)")

    plt.title("Empirical Analysis of Insertion Sort")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("insertion_sort_analysis.png")
    plt.show()


if __name__ == "__main__":
    run_experiment()