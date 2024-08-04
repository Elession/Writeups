## Writeup

- Description: Tired of storing passwords? No worries! This super secure website is passwordless! Author: NoobMaster
- Flag: `n00bz{1337-13371337-1337-133713371337-1337}`

![](./images/img1.png)

We are presented with the source code and the site.

![](./images/img2.png)

We look at the `/<uid>` page, in which the condition checks for uuid ver. 5 of the `leet` variable and the user `admin123`.
This can be solved using a simple script.

![](./images/img3.png)

With that, we can access the webpage with the flag.

![](./images/img4.png)