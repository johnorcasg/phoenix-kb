# wrong_number_or_misc.md  

## Purpose  
Provides Phoenix with fallback responses for wrong numbers, misc callers, and off-topic inquiries.  
Goal: **end gracefully** or **redirect if relevant**.  

---

## 1. Wrong Number – Polite Exit  
- “Got it, thanks for letting me know — I’ll update my notes.”  
- “No worries at all, I’ll take you off my list here.”  
- “Appreciate you clarifying, I’ll make sure we don’t bother you again.”  

**Tag:** WRONG_CONTACT → exit.  

---

## 2. Not the Owner but Knows Owner  
- “Understood — are you connected with them, or should I try another way?”  
- “Thanks for that. If you think they’d want to chat, would you mind passing along my info?”  

**Tag:** LEAD_REFERRAL if they offer a connection.  

---

## 3. Non-Seller Caller (Lender, Vendor, Misc)  
- “Got it, thanks for reaching out. What’s the best way to categorize this — lender, vendor, or other?”  
- “I appreciate you calling in. Let me note this down as not related to a property.”  

**Tag:** OTHER.  

---

## 4. Hostile or Spam Accusation  
- “Understood — I’ll mark this down as not a fit.”  
- “Got it, I’ll make sure to close this out.”  
- “I hear you, thanks for being direct. I’ll note that down.”  

**Tag:** DEAD.  

---

## Rules of Use  
1. If **wrong contact** → exit quickly, keep it polite.  
2. If **knows owner** → attempt referral, but don’t push.  
3. If **misc category** → tag as OTHER.  
4. If **hostile** → tag DEAD and end calmly.  

---
