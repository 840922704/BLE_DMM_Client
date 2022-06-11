package com.yscoco.wyboem.util;

import com.yscoco.blue.utils.BleUtils;

public class EncryptionUtil {
  public static byte[] encByted = new byte[] { 
      65, 33, 115, 85, -94, -63, 50, 113, 102, -86, 
      59, -48, -30, -88, 51, 20, 32, 26, -86, -69 };
  
  public static byte[] enc_code(byte[] paramArrayOfbyte) {
    byte[] arrayOfByte = new byte[paramArrayOfbyte.length];
    for (byte b = 0; b < paramArrayOfbyte.length; b++)
      arrayOfByte[b] = (byte)(byte)(paramArrayOfbyte[b] ^ encByted[b % 20]); 
    return arrayOfByte;
  }
  
  public static void main(String[] paramArrayOfString) {
    byte[] arrayOfByte = enc_code(BleUtils.hexStringToByte("10 27 37 44 5c 66 7a 84 9e a0 b0 c0 d0 e0 f0"));
    System.out.println(BleUtils.toHexString(arrayOfByte));
    System.out.println(BleUtils.toHexString(enc_code(arrayOfByte)));
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboe\\util\EncryptionUtil.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */