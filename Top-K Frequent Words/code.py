import heapq
import time
import re


def count_words(text):
    """الخطوة 1: استخراج الكلمات وحساب تكرار كل كلمة في Dictionary"""
    words = re.findall(r'\b[a-z]+\b', text.lower())
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def get_top_k_words(word_counts, k):
    """الخطوتان 2 و 3: استخدام Min-Heap بحجم k للاحتفاظ بأعلى الكلمات فقط"""
    if k <= 0 or not word_counts:
        return []

    min_heap = []

    for word, count in word_counts.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (count, word))
        elif count > min_heap[0][0]:
            heapq.heapreplace(min_heap, (count, word))

    # الخطوة 4: ترتيب النتيجة تنازلياً من الأكبر للأصغر
    return sorted(min_heap, key=lambda x: x[0], reverse=True)


def run_tests():
    """تشغيل اختبارات بسيطة ومباشرة للتأكد من صحة الكود"""
    print("--- 1. Basic Test Cases ---")
    
    tests = [
        ("to be or not to be", 2),
        ("apple banana apple orange banana apple", 2),
        ("code test code python code test", 1)
    ]

    for text, k in tests:
        counts = count_words(text)
        top_k = get_top_k_words(counts, k)
        result = [(word, count) for count, word in top_k]
        print(f"Text: '{text}' | k = {k} -> Top {k}: {result}")


def run_benchmark():
    """اختبار الأداء والسرعة على نص كبير بأرقام واضحة"""
    print("\n--- 2. Performance Benchmark ---")
    
    # تكوين نص كبير بتكرارات معروفة مسبقاً:
    # كلمة heap تتكرر 10000 مرة، algorithm تتكرر 8000 مرة، python تتكرر 5000 مرة، وباقي الكلمات 1000 مرة
    words_list = (
        ["heap"] * 10000 +
        ["algorithm"] * 8000 +
        ["python"] * 5000 +
        ["data"] * 1000 +
        ["sort"] * 1000 +
        ["tree"] * 1000
    )
    
    large_text = " ".join(words_list)
    k = 3

    start_time = time.perf_counter()
    counts = count_words(large_text)
    top_k = get_top_k_words(counts, k)
    elapsed_time = time.perf_counter() - start_time

    print(f"Total words processed: {len(words_list)}")
    print(f"Top {k} most frequent words:")
    for rank, (count, word) in enumerate(top_k, 1):
        print(f"  {rank}. '{word}' -> {count} times")

    print(f"Execution Time: {elapsed_time:.6f} seconds")


if __name__ == "__main__":
    run_tests()
    run_benchmark()