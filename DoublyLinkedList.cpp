struct LinkedListNode {
    int val;
    LinkedListNode *next;
    LinkedListNode *prev;
    LinkedListNode(int val): val (val), next(nullptr), prev(nullptr) {}
};

void appendToLinkedList(LinkedListNode* tail, LinkedListNode* nodeToAdd) {
    nodeToAdd->next = tail;
    nodeToAdd->prev = tail->prev;
    tail->prev->next = nodeToAdd;
    tail->prev = nodeToAdd;
}

void printLinkedListReverse(LinkedListNode* head, LinkedListNode* tail) {
    LinkedListNode* dummy = tail->prev;
    
    while(dummy!= head) {
        cout << dummy->val << " ";
        dummy = dummy->prev;
    }
}

void printLinkedList(LinkedListNode* head, LinkedListNode* tail) {
    LinkedListNode* dummy = head->next;
    
    while(dummy != tail) {
        cout << dummy->val << " ";
        dummy = dummy->next;
    }
}

int main() {
    // Write your code here
    // Try creating 1 <-> 2 <-> 3
    // Test with cout
    LinkedListNode* head = new LinkedListNode(0);
    LinkedListNode* tail = new LinkedListNode(0);
    head->next = tail;
    tail->prev = head;
    head->prev = nullptr;
    tail->next = nullptr;
    
    appendToLinkedList(tail, new LinkedListNode(1)); 
    appendToLinkedList(tail, new LinkedListNode(2)); 
    appendToLinkedList(tail, new LinkedListNode(3)); 
    
    printLinkedList(head, tail);
    cout << endl;
    printLinkedListReverse(head, tail);
}

