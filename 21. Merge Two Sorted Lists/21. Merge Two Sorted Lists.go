func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    // Обработка базовых случаев
    if list1 == nil {
        return list2
    }
    if list2 == nil {
        return list1
    }
    
    // Определение головы объединенного списка
    var head *ListNode
    if list1.Val <= list2.Val {
        head = list1
        list1 = list1.Next
    } else {
        head = list2
        list2 = list2.Next
    }
    
    // Указатель для обхода объединенного списка
    current := head
    
    // Слияние списков
    for list1 != nil && list2 != nil {
        if list1.Val <= list2.Val {
            current.Next = list1
            list1 = list1.Next
        } else {
            current.Next = list2
            list2 = list2.Next
        }
        current = current.Next
    }
    
    // Добавление оставшихся узлов list1 или list2
    if list1 != nil {
        current.Next = list1
    } else {
        current.Next = list2
    }
    
    return head
}
