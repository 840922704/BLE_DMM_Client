package com.yscoco.wyboem.ble;

public class BleByteBean {
  byte b;
  
  boolean isHigh;
  
  public BleByteBean() {}
  
  public BleByteBean(byte paramByte, boolean paramBoolean) {
    this.b = (byte)paramByte;
    this.isHigh = paramBoolean;
  }
  
  public byte getB() {
    return this.b;
  }
  
  public boolean isHigh() {
    return this.isHigh;
  }
  
  public void setB(byte paramByte) {
    this.b = (byte)paramByte;
  }
  
  public void setHigh(boolean paramBoolean) {
    this.isHigh = paramBoolean;
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\ble\BleByteBean.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */