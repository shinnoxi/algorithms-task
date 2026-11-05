# Empirical Analysis of Insertion Sort

هذا الكود يقوم بتنفيذ خوارزمية Insertion Sort وتحليل أدائها عملياً من خلال قياس وقت التنفيذ على أحجام وأنواع مختلفة من البيانات.

## Pseudocode

```text
InsertionSort(A)
    comparisons = 0
    shifts = 0
    
    for i = 1 to length(A) - 1
        key = A[i]
        j = i - 1
        
        while j >= 0
            comparisons = comparisons + 1
            if A[j] > key
                A[j + 1] = A[j]
                shifts = shifts + 1
                j = j - 1
            else
                break
                
        A[j + 1] = key
        
    return A, comparisons, shifts
```

## شرح الكود

يتكون الكود من أربع دوال رئيسية:

1. `insertion_sort(arr)`:
تقوم بترتيب المصفوفة المدخلة، وتعتمد على أخذ كل عنصر ومقارنته بالعناصر التي قبله لوضعه في مكانه الصحيح. الدالة ترجع المصفوفة بعد الترتيب، بالإضافة إلى عدد المقارنات (comparisons) وعدد الإزاحات (shifts) التي تمت.

2. `measure_time(sort_fn, data)`:
تستخدم مكتبة `time.perf_counter` لحساب الوقت الفعلي بالثواني الذي تستغرقه دالة الترتيب لتنفيذ مهمتها على البيانات المدخلة.

3. `run_experiment()`:
تجهز بيانات بأحجام مختلفة تبدأ من 100 وتصل إلى 5000 عنصر. لكل حجم، يتم إنشاء ثلاث مصفوفات: مرتبة، معكوسة، وعشوائية. بعد ذلك تقيس وقت ترتيب كل حالة وتطبع النتائج في جدول، ثم تستدعي دالة الرسم.

4. `plot_results(sizes, t_sorted, t_reverse, t_random)`:
تستخدم مكتبة `matplotlib` لرسم النتائج العملية التي تم قياسها ومقارنتها بالمنحنيات النظرية $O(n)$ و $O(n^2)$، وفي النهاية تحفظ الرسم البياني في صورة باسم `insertion_sort_analysis.png`.

## التشغيل

لتثبيت المكتبة المطلوبة وتشغيل الكود:

```bash
pip install matplotlib
python main.py
```