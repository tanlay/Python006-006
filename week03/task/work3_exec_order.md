### 标识以下SQL每个字句的执行顺序

```shell
SELECT DISTINCT player_id, player_name, count(*) as num     # 第五步
FROM player JOIN team ON player.team_id = team.team_id      # 第一步
WHERE height > 1.80                                         # 第二步
GROUP BY player.team_id                                     # 第三步
HAVING num > 2                                              # 第四步
ORDER BY num DESC                                           # 第六步
LIMIT 2                                                     # 第七步
```