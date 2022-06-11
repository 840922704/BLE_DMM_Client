package com.yscoco.wyboem.ble;

import java.util.Calendar;

public class IssuedData {
  public static final byte WRITE_FUNCTION_KEYSTROKE_OPERATION = 3;
  
  public static final byte WRITE_FUNCTION_TIME_SETTING = 4;
  
  public static byte[] keystrokeOperation(byte paramByte, byte[] paramArrayOfbyte) {
    byte[] arrayOfByte = new byte[paramArrayOfbyte.length + 1];
    arrayOfByte[0] = (byte)paramByte;
    System.arraycopy(paramArrayOfbyte, 0, arrayOfByte, 1, paramArrayOfbyte.length);
    return IssuedUtil.getSendByte((byte)3, arrayOfByte);
  }
  
  public static byte[] timeSetting() {
    Calendar calendar = Calendar.getInstance();
    int i = calendar.get(11);
    int j = calendar.get(12);
    int k = calendar.get(13);
    byte[] arrayOfByte = new byte[5];
    arrayOfByte[0] = (byte)(byte)i;
    arrayOfByte[1] = (byte)(byte)j;
    arrayOfByte[2] = (byte)(byte)k;
    return IssuedUtil.getSendByte((byte)4, arrayOfByte);
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\IssuedData.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */