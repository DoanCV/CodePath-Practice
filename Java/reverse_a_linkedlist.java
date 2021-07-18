class ListNode {
  int value = 0;
  ListNode next;

  ListNode(int value) {
    this.value = value;
  }
}

class ReverseLinkedList {

  public static ListNode reverse(ListNode head) {
    ListNode current = head;
    ListNode previous = null;

    while (current != null) {
      ListNode temp = current.next;
      current.next = previous;
      
      previous = current;
      current = temp;
    }
    return previous;
  }
