package com.yscoco.wyboem.ble;

public class BleDTO {
  boolean[] allSet;
  
  byte[] bytes;
  
  double d;
  
  String mac;
  
  String num;
  
  public BleDTO(String paramString1, double paramDouble, String paramString2, boolean[] paramArrayOfboolean, byte[] paramArrayOfbyte) {
    this.mac = paramString1;
    this.d = paramDouble;
    this.num = paramString2;
    this.allSet = paramArrayOfboolean;
    this.bytes = paramArrayOfbyte;
  }
  
  public boolean[] getAllSet() {
    return this.allSet;
  }
  
  public byte[] getBytes() {
    return this.bytes;
  }
  
  public double getD() {
    return this.d;
  }
  
  public String getMac() {
    return this.mac;
  }
  
  public String getNum() {
    return this.num;
  }
  
  public void setAllSet(boolean[] paramArrayOfboolean) {
    this.allSet = paramArrayOfboolean;
  }
  
  public void setBytes(byte[] paramArrayOfbyte) {
    this.bytes = paramArrayOfbyte;
  }
  
  public void setD(double paramDouble) {
    this.d = paramDouble;
  }
  
  public void setMac(String paramString) {
    this.mac = paramString;
  }
  
  public void setNum(String paramString) {
    this.num = paramString;
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\BleDTO.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */