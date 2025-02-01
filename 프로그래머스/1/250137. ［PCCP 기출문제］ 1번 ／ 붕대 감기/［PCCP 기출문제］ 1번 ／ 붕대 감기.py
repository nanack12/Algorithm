def solution(bandage, max_health, attacks):
    skill_time = bandage[0]
    heal_per_sec = bandage[1]
    extra_heal = bandage[2]
    cur_health = max_health
    # 시뮬레이션 여기서 돌림
    prev_t = 0
    for attack in attacks:
        cur_t = attack[0]
        dmg = attack[1]
        # 핵심 로직 START
        time_passed = cur_t - prev_t - 1
        total_heal_amount = 0
        total_heal_amount += time_passed * heal_per_sec 
        total_heal_amount += extra_heal * (time_passed // skill_time)
        cur_health = min(cur_health + total_heal_amount, max_health)
        cur_health -= dmg
        
        if cur_health <= 0:
            break
    
        # 핵심 로직 END
        prev_t = cur_t
        
        
        # 연속성공이 ++ 됨. 그 값이 extra_heal 과 같을 경우 cur_health +=
    # 시뮬레이션 끝
    return cur_health if cur_health > 0 else -1