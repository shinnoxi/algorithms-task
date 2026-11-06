# Top-K Frequent Words

تنفيذ خوارزمية استخراج أكثر k كلمات تكرارا في نص باستخدام القاموس (Hash Map) وهيكل بيانات الكومة الصغرى (Min-Heap).

## فكرة الخوارزمية
بدلا من ترتيب كل الكلمات الفريدة البالغ عددها U بتعقيد O(U log U)، يتم إنشاء Min-Heap بحجم ثابت k. نمر على الكلمات، وإذا كان تكرار الكلمة أكبر من أصغر عنصر في الـ Heap (الجذر) نستبدله. بذلك يصبح التعقيد الزمني O(N + U log k) واستهلاك الذاكرة للـ Heap هو O(k) فقط.

## Pseudocode

```text
TOP-K-WORDS(text, k)
    counts = empty Hash Map
    for each word in text
        counts[word] = counts[word] + 1

    min_heap = empty Min-Heap
    for each (word, count) in counts
        if size(min_heap) < k
            HEAPPUSH(min_heap, (count, word))
        else if count > min_heap[0].count
            HEAPREPLACE(min_heap, (count, word))

    return SORT-DESCENDING(min_heap)
```

## شرح الكود

* **count_words(text)**: تحول النص إلى أحرف صغيرة وتستخرج الكلمات، ثم تحسب تكرار كل كلمة داخل Dictionary.
* **get_top_k_words(word_counts, k)**: تنشئ Min-Heap بحجم k للاحتفاظ بأعلى الكلمات تكرارا فقط، ثم ترتب النتيجة النهائية تنازليا.
* **run_tests()**: تختبر الكود على 3 جمل قصيرة ومباشرة للتأكد من صحة استخراج الكلمات الأكثر تكرارا.
* **run_benchmark()**: تختبر سرعة الكود على نص مكون من 26,000 كلمة بتكرارات محددة مسبقا (10000 و 8000 و 5000 و 1000) وتطبع النتيجة مع وقت التنفيذ بالثواني.