import java.util.*;

class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
};

class LevelOrderTraversal {
  public static List<List<Integer>> traverse(TreeNode root) {
    List<List<Integer>> result = new ArrayList<List<Integer>>();
    if (root == null) {
      return result;
    }

    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);

    while (!queue.isEmpty()) {
      int queue_size = queue.size();
      List<Integer> curr_level = new ArrayList<>();

      for (int i = 0; i < queue_size; i++) {
        TreeNode curr_node = queue.poll();
        curr_level.add(curr_node.val);

        if (curr_node.left != null) {
          queue.offer(curr_node.left);
        }

        if (curr_node.right != null) {
          queue.offer(curr_node.right);
        }
      }
      result.add(curr_level);
    }
    return result;
  }


  public static void main(String[] args) {
    TreeNode root = new TreeNode(12);
    root.left = new TreeNode(7);
    root.right = new TreeNode(1);
    root.left.left = new TreeNode(9);
    root.right.left = new TreeNode(10);
    root.right.right = new TreeNode(5);
    List<List<Integer>> result = LevelOrderTraversal.traverse(root);
    System.out.println("Level order traversal: " + result);
  }
}
