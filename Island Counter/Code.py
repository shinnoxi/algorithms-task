import time
from collections import deque
import numpy as np


def bfs_flood_fill(grid, start_r, start_c):
    """غمر الجزيرة بالكامل وتحويل خلاياها من 1 إلى 0 لعدم زيارتها مرة أخرى"""
    rows, cols = grid.shape
    queue = deque([(start_r, start_c)])
    grid[start_r, start_c] = 0

    # الاتجاهات الأربعة: أعلى، أسفل، يسار، يمين
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 1:
                grid[nr, nc] = 0
                queue.append((nr, nc))


def count_islands(grid):
    """حساب إجمالي عدد الجزر في الشبكة"""
    # أخذ نسخة لعدم تعديل الشبكة الأصلية
    working_grid = grid.copy()
    rows, cols = working_grid.shape
    island_count = 0

    for r in range(rows):
        for c in range(cols):
            if working_grid[r, c] == 1:
                island_count += 1
                bfs_flood_fill(working_grid, r, c)

    return island_count


def run_tests():
    """تشغيل حالات اختبار واضحة للتأكد من صحة الكود"""
    print("--- 1. Basic Test Cases ---")

    # اختبار 1: شبكة تحتوي على 3 جزر منفصلة
    grid1 = np.array([
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ])
    print(f"Test 1 (Expected: 3) -> Result: {count_islands(grid1)} islands")

    # اختبار 2: جزيرة واحدة متصلة
    grid2 = np.array([
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1]
    ])
    print(f"Test 2 (Expected: 1) -> Result: {count_islands(grid2)} island")

    # اختبار 3: ماء فقط (بدون جزر)
    grid3 = np.zeros((3, 3), dtype=int)
    print(f"Test 3 (Expected: 0) -> Result: {count_islands(grid3)} islands")


def run_benchmark():
    """اختبار الأداء على شبكة كبيرة باستخدام numpy"""
    print("\n--- 2. Performance Benchmark ---")
    
    # توليد شبكة بحجم 500x500 (250,000 خلية) بنسبة يابسة 30%
    np.random.seed(42)
    large_grid = np.random.choice([0, 1], size=(500, 500), p=[0.7, 0.3])

    start_time = time.perf_counter()
    total_islands = count_islands(large_grid)
    elapsed_time = time.perf_counter() - start_time

    print(f"Grid Size      : 500 x 500 (250,000 cells)")
    print(f"Islands Found  : {total_islands}")
    print(f"Execution Time : {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    run_tests()
    run_benchmark()