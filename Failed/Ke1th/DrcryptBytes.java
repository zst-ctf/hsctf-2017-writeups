import java.math.BigInteger;

public class DrcryptBytes {
    static byte[] bytes = {
        -93, 35, 23, 82, -4, 57, -128, 83, -95, -60, -100,
         73, 40, -86, 7, 73, -101, 3, 118, -66, -104, 69,
        121, 76, 1, -124, -124, -1, -64, 29, 28, 43, 2, 
        -25, 54, 52, -79, -62, 11, -43, 52, -72, -117,
         -25, -103, -55, 75, -97
    };

    public static void main(String[] argv) {
        // https://www.mkyong.com/java/how-do-convert-byte-array-to-string-in-java/
        String s = new String(bytes);
        //System.out.println("Text Decryted : " + s);
        System.out.println(s);
    }

    // https://www.mkyong.com/java/how-to-convert-hex-to-ascii-in-java/
    public static String convertStringToHex(String str){
        char[] chars = str.toCharArray();
        StringBuffer hex = new StringBuffer();
        for(int i = 0; i < chars.length; i++){
            hex.append(Integer.toHexString((int)chars[i]));
        }
        return hex.toString();
    }

}

