func generateParenthesis(n int) []string {
    var result []string // слайс для хранения результатов
    var backtrack func(int, int, string)
    
    backtrack = func(open, close int, sequence string) {
        if len(sequence) == n*2 { // базовый случай: если скобочная последовательность имеет нужную длину, добавляем ее в результат
            result = append(result, sequence)
            return
        }
        
        if open < n { // проверяем условие для добавления открывающей скобки
            backtrack(open+1, close, sequence+"(")
        }
        
        if close < open { // проверяем условие для добавления закрывающей скобки
            backtrack(open, close+1, sequence+")")
        }
    }
    
    backtrack(0, 0, "") // запускаем рекурсивную функцию, начинаем с 0 открытых и закрытых скобок и пустой последовательности
    
    return result
}
