# Hybrid Sort: Find the Cutoff

هذا الكود يقوم بتنفيذ خوارزمية ترتيب هجينة تدمج بين Merge Sort و Insertion Sort، ويهدف إلى إيجاد أفضل قيمة للحد الفاصل ($k$) التي تحقق أسرع وقت تنفيذ.

## Pseudocode

```
HybridSort(A, left, right, k)
    if (right - left + 1) <= k
        InsertionSort(A, left, right)
        return

    if left < right
        mid = (left + right) // 2
        HybridSort(A, left, mid, k)
        HybridSort(A, mid + 1, right, k)
        Merge(A, left, mid, right)
```

## شرح الكود

يتكون الكود من خمس دوال رئيسية:

1. `insertion_sort(arr, left, right)`:
   تقوم بترتيب جزء محدد من المصفوفة يبدأ من الفهرس `left` وينتهي عند `right` باستخدام خوارزمية Insertion Sort.

2. `merge(arr, left, mid, right)`:
   تدمج نصفي المصفوفة المرتبين (`left` إلى `mid` ومن `mid + 1` إلى `right`) في مصفوفة واحدة مرتبة.

3. `hybrid_sort_helper(arr, left, right, k)`:
   الدالة الأساسية التي تطبق فكرة الخوارزمية الهجينة؛ إذا كان حجم المصفوفة الفرعية أصغر من أو يساوي $k$ يتم استدعاء `insertion_sort`، وإلا تستمر في تقسيم المصفوفة باستخدام منطق Merge Sort.

4. `hybrid_sort(arr, k)`:
   تأخذ نسخة من المصفوفة الأصلية للحفاظ عليها من التعديل المباشر، وتبدأ عملية الترتيب باستدعاء الدالة المساعدة.

5. `find_best_k()`:
   تجري التجربة العملية على مصفوفة بحجم 100,000 عنصر عبر تجربة قيم مختلفة للمتغير $k$. لكل قيمة، يتم حساب متوسط وقت التنفيذ لـ 5 محاولات، ثم يتم تحديد القيمة الأفضل ($k$) التي سجلت أقل وقت ورسم النتائج بيانياً في ملف `hybrid_sort_cutoff.png`.

## التشغيل

لتثبيت المكتبة المطلوبة وتشغيل الكود:

```
pip install matplotlib
python main.py
```