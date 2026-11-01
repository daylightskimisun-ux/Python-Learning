hosepower=float(input("马力:"))
weight=float(input("重量:"))
prise=float(input("价格:"))
engine_thrust_ration=hosepower/weight*1000
single_horsepower_prise=hosepower/prise
performance_tag=""
value_tag=""
if engine_thrust_ration>180:
    performance_tag= "高性能"
elif engine_thrust_ration>140:
    performance_tag= "中等性能"
else:
    performance_tag= "低性能"
if single_horsepower_prise>10:
    value_tag="高价值"
elif single_horsepower_prise>5:
    value_tag= "中等价值"
else:
    value_tag="低价值"
print(f"发动机推重比是：{engine_thrust_ration:.2f},性能等级是：{performance_tag},单马力价格是：{single_horsepower_prise:.2f}，价值等级是：{value_tag}")