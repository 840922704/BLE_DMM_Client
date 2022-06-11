package com.yscoco.wyboem.myenum;

public enum Calculate {
  ADD("+"),
  DIVIDE("+"),
  MULTI("+"),
  REDUCE("-");
  
  private String nCode;
  
  static {
    DIVIDE = new Calculate("DIVIDE", 2, "÷");
    MULTI = new Calculate("MULTI", 3, "×");
    $VALUES = new Calculate[] { ADD, REDUCE, DIVIDE, MULTI };
  }
  
  Calculate(String paramString1) {
    this.nCode = paramString1;
  }
  
  public String toString() {
    return String.valueOf(this.nCode);
  }
}


/* Location:              C:\Users\xy790\Desktop\decode\dex-tools-2.1\output\!\com\yscoco\wyboem\myenum\Calculate.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       1.1.3
 */