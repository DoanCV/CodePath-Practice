struct ListNode {
  int val;
  ListNode *next;

  ListNode(): val(0), next(nullptr) {}
  ListNode(int x): val(x), next(nullptr) {}
  ListNode(int x, ListNode *next): val(x), next(next) {}
};

class solution {
private:
  ListNode* reverse_linked_list(ListNode *head){
    ListNode *prev = NULL;
    ListNode *curr = head;

    while (curr) {
      ListNode *temp = curr->next;
      curr->next = prev;

      prev = curr;
      curr = temp;

    }

    return prev;
  }

};
