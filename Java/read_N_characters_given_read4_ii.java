/*
The read4 API is defined in the parent class Reader4
  int read4(char[] buf4);
*/

public class solution extends Reader4 {

  private char[] buf4 = new char[4];
  private int readPos = 0;
  private int writePos = 0;

  public int read(char[] buf, int n) {

    for (int i = 0; i < n; i++) {
      // if they point to the same place we consumed all characters in the buffer
      if (readPos == writePos) {
        writePos = read4(buf4); 
        readPos = 0;
        // we read all the characters from the file
        if (writePos == 0) {
          return i;
        }
      }

      buf[i] = buf4[readPos++];

    }

    return n;

  }
}
