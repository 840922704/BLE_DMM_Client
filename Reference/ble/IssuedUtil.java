package com.yscoco.wyboem.ble;

public class IssuedUtil {
  public static final byte HEAD_INDEX = -85;
  
  public static final byte HEAD_INDEX_TWO = -51;
  
  public static byte[] getSendByte(byte paramByte, byte[] paramArrayOfbyte) {
    byte[] arrayOfByte;
    if (paramArrayOfbyte == null) {
      arrayOfByte = new byte[5];
    } else {
      arrayOfByte = new byte[paramArrayOfbyte.length + 5];
    } 
    boolean bool = false;
    arrayOfByte[0] = (byte)-85;
    arrayOfByte[1] = (byte)-51;
    arrayOfByte[2] = (byte)paramByte;
    if (paramArrayOfbyte != null)
      System.arraycopy(paramArrayOfbyte, 0, arrayOfByte, 3, paramArrayOfbyte.length); 
    int i = 0;
    for (paramByte = bool; paramByte < arrayOfByte.length - 2; paramByte++)
      i += arrayOfByte[paramByte] & 0xFF; 
    arrayOfByte[arrayOfByte.length - 2] = (byte)(byte)(i / 256);
    arrayOfByte[arrayOfByte.length - 1] = (byte)(byte)(i & 0xFF);
    return arrayOfByte;
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\IssuedUtil.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */