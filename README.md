# Algorithms Tasks

يحتوي هذا المستودع على تنفيذ عملي وتحليل لأربع خوارزميات أساسية باستخدام لغة Python. كل مشروع مفصول في مجلد خاص به مع الكود وشرح الخوارزمية والـ Pseudocode.

---

## 1. [Insertion Sort](./insertion%20sort/Code.py)
* تنفيذ خوارزمية الترتيب بالإدراج وحساب عدد المقارنات والإزاحات، ومقارنة وقت التنفيذ عمليا بين الحالات الثلاث (Sorted, Random, Reverse).

![Insertion Sort Analysis](./insertion%20sort/insertion_sort_analysis.png)

---

## 2. [Hybrid Sort: Find the Cutoff](./Hybrid%20Sort%20Find%20the%20Cutoff/Code.py)
* دمج خوارزميتي Merge Sort و Insertion Sort، وإجراء تجربة عملية لتحديد أفضل قيمة للعتبة (Cutoff k) لتحقيق أسرع وقت تنفيذ.

![Hybrid Sort Cutoff](./Hybrid%20Sort%20Find%20the%20Cutoff/hybrid_sort_cutoff.png)

---

## 3. [Top-K Frequent Words](./Top-K%20Frequent%20Words/code.py)
* استخراج أكثر k كلمات تكرارا في نص باستخدام القاموس (Hash Map) وهيكل بيانات الكومة الصغرى (Min-Heap) بتعقيد زمني O(N + U log k).

---

## 4. [Island Counter](./Island%20Counter/Code.py)
* حساب عدد الجزر في شبكة ثنائية الأبعاد (2D Grid) باستخدام مكتبة numpy وخوارزمية البحث بالعرض (BFS Flood Fill).

---