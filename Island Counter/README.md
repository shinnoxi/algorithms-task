# Island Counter

مشروع لحساب عدد الجزر في شبكة ثنائية الأبعاد (2D Grid) مكونة من يابسة (1) وماء (0) باستخدام لغة Python ومكتبة numpy مع خوارزمية البحث بالعرض (BFS Flood Fill).

## فكرة الخوارزمية
الجزيرة هي مجموعة من خلايا اليابسة (1) المتصلة أفقيا أو رأسيا. نمر على جميع خلايا الشبكة، وعند العثور على خلية قيمتها 1، نزيد عداد الجزر بمقدار 1 ثم نطلق خوارزمية Flood Fill باستخدام طابور (Queue - BFS) لتحويل هذه الخلية وجميع خلايا اليابسة المتصلة بها إلى 0 حتى لا يتم عدها مرة أخرى. التعقيد الزمني والمكاني للخوارزمية هو O(R * C) حيث R عدد الصفوف و C عدد الأعمدة.

## Pseudocode

```text
COUNT-ISLANDS(grid)
    island_count = 0
    for r = 0 to rows - 1
        for c = 0 to cols - 1
            if grid[r][c] == 1
                island_count = island_count + 1
                BFS-FLOOD-FILL(grid, r, c)
    return island_count


BFS-FLOOD-FILL(grid, start_r, start_c)
    queue = empty Queue
    ENQUEUE(queue, (start_r, start_c))
    grid[start_r][start_c] = 0

    while queue is not empty
        (r, c) = DEQUEUE(queue)
        for each (nr, nc) in adjacent neighbors (up, down, left, right)
            if (nr, nc) is inside grid and grid[nr][nc] == 1
                grid[nr][nc] = 0
                ENQUEUE(queue, (nr, nc))
```

## شرح الكود

* **bfs_flood_fill(grid, start_r, start_c)**: تستقبل موقع بداية الجزيرة وتستخدم طابور (deque) لزيارة كل الخلايا المتصلة بها أفقيا ورأسيا وتحويل قيمتها إلى 0.
* **count_islands(grid)**: تأخذ نسخة من مصفوفة numpy وتمر على خلاياها لحساب عدد الجزر الكلي.
* **run_tests()**: تختبر الكود على 3 شبكات معلومة النتائج مسبقا (3 جزر، جزيرة واحدة، وشبكة فارغة).
* **run_benchmark()**: تولد شبكة عشوائية كبيرة بحجم 500x500 باستخدام numpy وتقيس وقت التنفيذ بالثواني.