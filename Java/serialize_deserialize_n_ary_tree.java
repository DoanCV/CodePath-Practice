import java.util.*;

class Node {
  public int val;
  public List<Node> children;

  public Node() {}

  public Node(int _val) {
    val = _val;
  }

  public Node(int _val, List<Node> _children) {
    val = _val;
    children = _children;
  }

};

class Codec {

  public String serialize(Node root){
    // empty tree
    if (root == null){
      return "x";
    }

    StringBuilder result = new StringBuilder();

    Queue<Node> queue = new LinkedList<>();
    queue.offer(root);
    queue.offer(null); // we may need a flag to indicate the end of the level so we can add null
    // i believe we do not need it since this is just BFS and we know the size of the queue before we add the children

    while (!queue.isEmpty()) {
      int level_size = queue.size();

      for (int i = 0; i < level_size; i++){
        Node curr_node = queue.poll();
        if (curr_node == null) {
          result.append("x");
          result.append(",");
          break;
        }
        
        for (Node child: curr_node.children) {
          queue.offer(child);
        }

        queue.add(null);
        result.append(curr_node.val);
        result.append(",");
      }

    }

    // we always have an extra comma so get rid of it
    result.deleteCharAt(result.length() - 1);
    System.out.println(result.toString());
    return result.toString();
  }


  public Node deserialize(String data) {
    String[] data_arr = data.split(",");

    if (data_arr[0] == "x") {
      return null;
    }

    Node root = new Node(Integer.parseInt(data_arr[0]));

    Queue<Node> queue = new LinkedList<>();
    queue.offer(root);

    int i = 2; // the root is the only node at its depth and so we need to skip the first x
    while (i < data_arr.length){
      Node curr_node = queue.poll();

      // the children are a list of nodes so get them and set .children to that list
      List<Node> kids = new LinkedList<>();

      while (data_arr[i] != "x") {
        Node child = new Node(Integer.parseInt(data_arr[i++]));
        kids.add(child);
        queue.offer(child);
      }

      i++;
      curr_node.children = kids;

    }

    return root; 
  }
}


class Main {
  public static void main(String[] args) {
    
    Node root = new Node(1);
    Node two = new Node(2);
    Node three = new Node(3);
    Node four = new Node(4);
    Node five = new Node(5);
    Node six = new Node(6);

    List<Node> kids_1 = new ArrayList<>();
    kids_1.add(three);
    kids_1.add(two);
    kids_1.add(four);
    List<Node> kids_2 = new ArrayList<>();
    kids_2.add(five);
    kids_2.add(six);

    root.children = kids_1;
    three.children = kids_2;

    Codec test = new Codec();
    test.deserialize(test.serialize(root));
    System.out.println("Done");
  }
}
