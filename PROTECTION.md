
---

## ✅ `PROTECTION.md`

```markdown
# Branch Protection Justification

## Why Protect the `main` Branch?

Branch protection helps maintain the **integrity** of the codebase and prevent bugs or security issues from reaching production.

---

## Enforced Rules:

1. ✅ **Require pull request reviews**  
   At least one reviewer must approve changes before they can be merged into `main`.

2. ✅ **Require status checks to pass**  
   All CI tests must pass. If any test fails, merging is blocked.

3. 🚫 **Restrict direct pushes**  
   Developers cannot push directly to `main`. All changes must go through a pull request.

---

## Benefits

- **Quality Control**: Ensures all code is reviewed and tested.
- **Security**: Prevents accidental or malicious code from going live.
- **Team Collaboration**: Encourages team review and shared ownership of the code.
![image](https://github.com/user-attachments/assets/13de275f-939e-47cf-b58e-96bb34f68bdb)
![image](https://github.com/user-attachments/assets/53c0340b-cb19-4e44-9cfa-f4586512d3f1)

