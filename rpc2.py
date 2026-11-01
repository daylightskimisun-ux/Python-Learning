while True:
    ptn = str(input("请输入蛋白粉名称："))
    ppw = float(input("请输入蛋白粉重量（克）："))
    pc = float(input("请输入蛋白质占比（百分比）："))
    pp = float(input("请输入蛋白粉价格（元）："))
    wp = ppw * (pc/100)
    spp = pp / wp
    value_tag = ""
    type_tag = ptn.strip()
    match type_tag:
        case "乳清蛋白":
            if 0.12 <= spp < 0.28:
                value_tag = "高性价比"
            elif spp >= 0.28:
                value_tag = "性价比一般"
            elif spp < 0.12:
                value_tag = "警惕"
        case "分离蛋白":
            if 0.25 <= spp < 0.45:
                value_tag = "高性价比"
            elif spp >= 0.45:
                value_tag = "性价比一般"
            elif spp < 0.25:
                value_tag = "警惕"
        case "多重蛋白":
            if 0.20 <= spp < 0.35:
                value_tag = "高性价比"
            elif spp >= 0.35:
                value_tag = "性价比一般"
            elif spp < 0.20:
                value_tag = "警惕"
    print(f"蛋白粉名称：{ptn}，蛋白粉重量：{ppw}克，蛋白质占比：{pc}%，蛋白粉价格：{pp}元，蛋白质含量：{wp:.2f}克，性价比：{spp:.2f}元/克，性价比标签：{value_tag}")
    answer = input("是否继续输入？（按下回车继续，按下任意键退出）：")
    if answer != "":
        break