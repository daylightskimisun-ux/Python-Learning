ptn = str(input("请输入蛋白粉名称："))
ppw = float(input("请输入蛋白粉质量（克）："))
pc = float(input("请输入蛋白质占比（百分比）："))
pp = float(input("请输入蛋白粉价格（元）："))
wp = ppw * (pc/100)
spp = pp / wp
value_tag = ""
type_tag = ptn.strip()
match type_tag:
    case "分离蛋白":
        if 0.25 <= spp < 0.45:
            value_tag = "高性价比"
        elif spp >= 0.45:
            value_tag = "性价比一般"
        elif spp < 0.25:
            value_tag = "警惕"
    case "乳清蛋白":
        if 0.12 <= spp < 0.28:
            value_tag = "高性价比"
        elif spp >= 0.28:
            value_tag = "性价比一般"
        elif spp < 0.12:
            value_tag = "警惕"
    case "多重蛋白":
        if 0.20 <= spp < 0.35:
            value_tag = "高性价比"
        elif spp >= 0.35:
            value_tag = "性价比一般"
        elif spp < 0.20:
            value_tag = "警惕"
    case _:
        value_tag = "未知类型"
print(f"蛋白粉名称是：{ptn}，蛋白质含量是：{wp}克，单位价格是：{spp:.3f}元/克，性价比评价是：{value_tag}")            