"""По пять задач с ошибками для каждого уровня сложности."""

TASKS = {
    "Лёгкий": [
        {
            "id": "even", "title": "Чётное число",
            "text": "Верни True для чётного целого n, иначе False. Пример: solve(4) → True.",
            "code": "def solve(n):\n    return n % 2 == 1",
        },
        {
            "id": "sum", "title": "Сумма от 1 до n",
            "text": "Найди сумму целых чисел от 1 до n включительно. n >= 1. Пример: solve(3) → 6.",
            "code": "def solve(n):\n    total = 0\n    for i in range(1, n):\n        total += i\n    return total",
        },
        {
            "id": "positive", "title": "Положительные числа",
            "text": "Посчитай строго положительные числа в списке numbers. Ноль не считается. Пример: solve([-1, 0, 2]) → 1. Пустой список допустим.",
            "code": "def solve(numbers):\n    count = 0\n    for n in numbers:\n        if n >= 0:\n            count += 1\n    return count",
        },
        {
            "id": "reverse", "title": "Разверни строку",
            "text": "Верни строку text в обратном порядке. Пример: solve('кот') → 'ток'. Пустая строка допустима.",
            "code": "def solve(text):\n    return text[::1]",
        },
        {
            "id": "square", "title": "Квадрат числа",
            "text": "Верни квадрат целого числа n. Примеры: solve(3) → 9, solve(-2) → 4.",
            "code": "def solve(n):\n    return n * 2",
        },
    ],
    "Средний": [
        {
            "id": "maximum", "title": "Максимум списка",
            "text": "Найди максимум непустого списка целых чисел numbers. Числа могут быть отрицательными. Пример: solve([-5, -2]) → -2.",
            "code": "def solve(numbers):\n    result = 0\n    for n in numbers:\n        if n > result:\n            result = n\n    return result",
        },
        {
            "id": "average", "title": "Среднее арифметическое",
            "text": "Верни среднее арифметическое непустого списка numbers, сохранив дробную часть. Пример: solve([1, 2]) → 1.5.",
            "code": "def solve(numbers):\n    return sum(numbers) // len(numbers)",
        },
        {
            "id": "factorial", "title": "Факториал",
            "text": "Найди факториал целого n от 0 до 10. Факториал нуля равен 1. Пример: solve(4) → 24.",
            "code": "def solve(n):\n    result = 0\n    for i in range(1, n + 1):\n        result *= i\n    return result",
        },
        {
            "id": "contains", "title": "Поиск семёрки",
            "text": "Верни True, если в списке numbers есть 7, иначе False. Пример: solve([1, 7]) → True. Для пустого списка ответ False.",
            "code": "def solve(numbers):\n    for n in numbers:\n        if n == 7:\n            return True\n        else:\n            return False\n    return False",
        },
        {
            "id": "vowels", "title": "Английские гласные",
            "text": "Посчитай английские гласные a, e, i, o, u в строке text независимо от регистра. Пример: solve('Apple') → 2.",
            "code": "def solve(text):\n    count = 0\n    for letter in text:\n        if letter in 'aeiou':\n            count += 1\n    return count",
        },
    ],
    "Сложный": [
        {
            "id": "binary_search", "title": "Бинарный поиск",
            "text": "Аргумент data — пара (numbers, target). numbers — список различных целых чисел по возрастанию. Верни индекс target или -1, если его нет. Пустой список допустим. Пример: solve(([1, 3, 5], 3)) → 1. Проверь, всегда ли цикл завершается.",
            "code": "def solve(data):\n    numbers, target = data\n    left = 0\n    right = len(numbers) - 1\n    while left <= right:\n        middle = (left + right) // 2\n        if numbers[middle] == target:\n            return middle\n        if numbers[middle] < target:\n            left = middle\n        else:\n            right = middle - 1\n    return -1",
        },
        {
            "id": "prime", "title": "Простое число",
            "text": "Верни True, если целое n простое, иначе False. Простое число больше 1 и делится только на 1 и на себя. Примеры: solve(2) → True, solve(9) → False, solve(1) → False.",
            "code": "def solve(n):\n    if n < 2:\n        return False\n    for divisor in range(2, int(n ** 0.5)):\n        if n % divisor == 0:\n            return False\n    return True",
        },
        {
            "id": "brackets", "title": "Правильные скобки",
            "text": "Строка text содержит только '(' и ')'. Верни True для правильной скобочной последовательности, иначе False. Пустая строка правильная. Примеры: solve('(())') → True, solve(')(') → False.",
            "code": "def solve(text):\n    balance = 0\n    for symbol in text:\n        if symbol == '(':\n            balance += 1\n        else:\n            balance -= 1\n    return balance == 0",
        },
        {
            "id": "second_maximum", "title": "Второй различный максимум",
            "text": "Верни второе по величине РАЗЛИЧНОЕ число в списке numbers. Если разных чисел меньше двух, верни None. Примеры: solve([5, 5, 3]) → 3, solve([2, 2]) → None. Пустой список допустим.",
            "code": "def solve(numbers):\n    if len(numbers) < 2:\n        return None\n    ordered = sorted(numbers)\n    return ordered[-2]",
        },
        {
            "id": "merge", "title": "Слияние списков",
            "text": "Аргумент data — пара списков (first, second), каждый отсортирован по неубыванию. Объедини их в отсортированный список, сохранив повторы. Списки могут быть пустыми. Пример: solve(([1, 3], [2, 4])) → [1, 2, 3, 4].",
            "code": "def solve(data):\n    first, second = data\n    result = []\n    i = 0\n    j = 0\n    while i < len(first) and j < len(second):\n        if first[i] <= second[j]:\n            result.append(first[i])\n            i += 1\n        else:\n            result.append(second[j])\n            j += 1\n    return result",
        },
    ],
}
