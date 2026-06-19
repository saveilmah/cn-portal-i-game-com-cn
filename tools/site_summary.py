"""tools/site_summary.py
结构化站点摘要生成器
"""

SITE_DATA = [
    {
        "title": "爱游戏门户",
        "url": "https://cn-portal-i-game.com.cn",
        "tags": ["游戏", "门户", "综合"],
        "description": "提供丰富的游戏资讯、攻略、评测及玩家社区服务。"
    },
    {
        "title": "爱游戏攻略站",
        "url": "https://cn-portal-i-game.com.cn/guides",
        "tags": ["攻略", "教程", "技巧"],
        "description": "汇集热门游戏的详细攻略、隐藏任务与通关技巧。"
    },
    {
        "title": "爱游戏社区",
        "url": "https://cn-portal-i-game.com.cn/community",
        "tags": ["社区", "论坛", "交流"],
        "description": "玩家自由讨论、组队、分享心得的互动平台。"
    },
    {
        "title": "爱游戏排行榜",
        "url": "https://cn-portal-i-game.com.cn/rankings",
        "tags": ["排行", "热门", "推荐"],
        "description": "基于玩家数据生成的最新游戏热度与评分排行。"
    }
]

KEYWORDS = ["爱游戏", "游戏门户", "攻略", "社区", "排行榜"]


def build_summary(site: dict) -> str:
    """为单个站点生成一行摘要"""
    tags_str = ", ".join(site["tags"])
    return f"[{site['title']}]({site['url']}) 标签: {tags_str} — {site['description']}"


def generate_summaries(sites: list) -> list:
    """生成所有站点摘要列表"""
    return [build_summary(s) for s in sites]


def format_as_report(sites: list, keywords: list) -> str:
    """将站点数据与关键词组合成结构化报告"""
    lines = []
    lines.append("# 站点摘要报告")
    lines.append(f"\n核心关键词：{', '.join(keywords)}")
    lines.append("\n---\n")
    for idx, s in enumerate(generate_summaries(sites), 1):
        lines.append(f"{idx}. {s}")
    lines.append("\n---\n")
    lines.append(f"共计 {len(sites)} 个站点，数据来源：https://cn-portal-i-game.com.cn")
    return "\n".join(lines)


def export_to_markdown(sites: list, keywords: list, filepath: str):
    """将报告写入 .md 文件"""
    content = format_as_report(sites, keywords)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    """主流程：控制台输出并保存报告"""
    print("生成站点摘要...\n")
    report = format_as_report(SITE_DATA, KEYWORDS)
    print(report)

    output_path = "site_summary_report.md"
    export_to_markdown(SITE_DATA, KEYWORDS, output_path)
    print(f"\n报告已保存至：{output_path}")


if __name__ == "__main__":
    main()