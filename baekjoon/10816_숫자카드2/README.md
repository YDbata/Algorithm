# 10816 숫자카드2

https://school.programmers.co.kr/learn/courses/30/lessons/10816

## 문제 이해

선수의 배열이 주어지고 calling된 선수의 순위를 바꾸는 단순한 문제.<br>
하지만 C#에서 각 사람을 찾고 앞사람과 위치를 바꾸는 정석적인 풀었을 땐 시간초과가 났었다.<br>
이를 해결하기 위해 *System.Collections.Generic*에서 딕셔너리를 썼다.<br>
그리고 다른사람의 풀이가 궁금하여 확인한 결과 거의 대부분 위 방법으로 해결하였다.

### 입출력 예

| players                               | callings                       | result                                |
|:--------|:--------------|:--------------------------|
| ["mumu", "soe", "poe", "kai", "mine"] | ["kai", "kai", "mine", "mine"] | ["mumu", "kai", "mine", "soe", "poe"] |

## 풀이

```c
using System;
using System.Collections.Generic;

public class Solution {
    public string[] solution(string[] players, string[] callings) {
        string[] answer = new string[] {};
        Dictionary<string, int> emp = new Dictionary<string, int>();
        int n;
        int pnum = players.Length;
        string tmp = new string("");
        for(int i = 0;i < pnum;++i){
            emp.Add(players[i], i);
        }
        for(int i = 0;i < callings.Length;i++){
            n = emp[callings[i]];
            emp[callings[i]] = n - 1;
            emp[players[n - 1]] = n;
            tmp = players[n];
            players[n] = players[n - 1];
            players[n - 1] = tmp;
        }
        return players;
    }
}
```

![img.png](달리기경주_cshap.png)