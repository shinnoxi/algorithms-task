import heapq
import time
import re


def count_words(text):
    """الخطوة 1: حساب تكرار الكلمات باستخدام Dictionary"""
    words = re.findall(r'\b[a-z]+\b', text.lower())
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def get_top_k_words(word_counts, k):
    """الخطوتان 2 و 3: الاحتفاظ بأعلى k كلمات باستخدام Min-Heap بحجم k"""
    min_heap = []

    for word, count in word_counts.items():
        if len(min_heap) < k:
            # إذا لم يمتلئ الـ Heap بعد، نضيف العنصر
            heapq.heappush(min_heap, (count, word))
        elif count > min_heap[0][0]:
            # إذا كان تكرار الكلمة أكبر من الجذر (أصغر عنصر في الـ Heap)، نستبدله
            heapq.heapreplace(min_heap, (count, word))

    # الخطوة 4: ترتيب محتويات الـ Heap تنازلياً حسب التكرار للطباعة
    return sorted(min_heap, key=lambda x: x[0], reverse=True)


def run_project():
    # تجربة أولى على المثال المذكور في الصورة
    sample_text = "to be or not to be"
    k_sample = 2
    counts = count_words(sample_text)
    top_sample = get_top_k_words(counts, k_sample)

    print("--- Example Test ---")
    print(f"Text: '{sample_text}' | k = {k_sample}")
    print(f"Word Counts: {counts}")
    print(f"Top {k_sample} Words: {[(word, count) for count, word in top_sample]}\n")

    # تجربة ثانية على نص كبير وقياس الوقت
    print("--- Large Text Benchmark ---")
    large_words = ["algorithm", "heap", "sort", "data", "tree", "graph", "code", "python"]
    # توليد نص كبير (100,000 كلمة) بتكرارات متفاوتة
    large_text = " ".join(
        [large_words[i % len(large_words)] for i in range(100000)]
        + ["heap"] * 5000
        + ["algorithm"] * 3000
        + ["python"] * 2000
    )

    k = 3
    start_time = time.perf_counter()

    large_counts = count_words(large_text)
    top_k = get_top_k_words(large_counts, k)

    elapsed_time = time.perf_counter() - start_time

    print(f"Top {k} most frequent words:")
    for rank, (count, word) in enumerate(top_k, 1):
        print(f"{rank}. '{word}' -> {count} times")

    print(f"\nExecution Time: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    run_project()