package com.yscoco.wyboem.myenum;

public enum UnitType {
  A,
  CELSIUS,
  F,
  FAGOT,
  HZ,
  OHM,
  V("v");
  
  private String type;
  
  static {
    A = new UnitType("A", 1, "A");
    F = new UnitType("F", 2, "F");
    CELSIUS = new UnitType("CELSIUS", 3, "℃");
    FAGOT = new UnitType("FAGOT", 4, "℉");
    OHM = new UnitType("OHM", 5, "Ω");
    HZ = new UnitType("HZ", 6, "Hz");
    $VALUES = new UnitType[] { V, A, F, CELSIUS, FAGOT, OHM, HZ };
  }
  
  UnitType(String paramString1) {
    this.type = paramString1;
  }
  
  public String getType() {
    return this.type;
  }
  
  public void setType(String paramString) {
    this.type = paramString;
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\myenum\UnitType.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */