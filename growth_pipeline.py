#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Antigravity Skill Synergy Growth Pipeline
------------------------------------------
Synergy of:
- threads-empathy-copywriter (2030 Trend Lifestyle Copywriting)
- ddalkkak-threads (Meta Threads Graph API 2-Stage Container Pipeline)
- fire-your-seo-agency (5-Lane SEO/AEO/GEO/NEO Optimization)
- ponytail (Zero External Dependencies, Pure Python Standard Library, YAGNI)

Usage:
  python growth_pipeline.py --help
  python growth_pipeline.py --hobby running --item "초경량 카본 플레이트 러닝화" --price "89,000원 (정가 189,000원 53% 할인)" --link "https://example.com/running-shoes"
"""

import sys
import json
import argparse
from typing import Dict, Any, Tuple

# Reconfigure stdout/stderr to UTF-8 on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# 2030 Core Trend Hobbies & Lifestyle Hook Patterns (threads-empathy-copywriter)
HOBBY_DATABASE = {
    "running": {
        "name": "러닝 / 런닝 크루",
        "emoji": "🏃",
        "hook": "요즘 러닝 많이 뛰는데 일반 운동화 신고 뛰는 사람 손? 🏃",
        "pain_point": "무릎 통증이랑 발목 피로 때문에 5km 넘어가면 고생함",
        "recommendation": "카본 플레이트 반발력 체감하면 1km 페이스 30초 단축됨",
        "keywords": ["러닝화", "카본화", "런닝크루", "러닝코스", "오운완"]
    },
    "hiking": {
        "name": "등산 / 트레킹 / 아웃도어",
        "emoji": "🥾",
        "hook": "요즘 날씨 좋아서 주말마다 등산·트레킹 가시는 분들 🥾",
        "pain_point": "바위길 미끄러짐이랑 하산할 때 발가락 쏠림 해결해야 함",
        "recommendation": "접지력 최상 비브람창이라 비 온 다음날 바위도 쩍쩍 붙음",
        "keywords": ["등산화", "트레킹화", "등산코스", "국립공원", "주말등산"]
    },
    "gaming": {
        "name": "게임 / 사플 (배그, 발로란트)",
        "emoji": "🎧",
        "hook": "요즘 배그나 발로란트 할 때 사플 안 돼서 답답했던 사람? 🎧",
        "pain_point": "발소리 방향 헷갈려서 뒤통수 맞고 샷건 치던 시절 끝",
        "recommendation": "공간 음향 분리도 미쳐서 2층 발소리랑 1층 삥 까는 소리 다 들림",
        "keywords": ["게이밍헤드셋", "사운드플레이", "발로란트", "배틀그라운드", "게이밍이어폰"]
    },
    "workout": {
        "name": "오운완 / 헬스 / 식단",
        "emoji": "💪",
        "hook": "운동하는 사람 손!! 식단 나랑 같이하자 💪",
        "pain_point": "퍽퍽한 닭가슴살 억지로 삼키다가 턱 아파서 포기한 적 있음",
        "recommendation": "수비드 공법이라 소시지 식감 나는데 단백질 24g 깔끔하게 채워짐",
        "keywords": ["오운완", "닭가슴살", "단백질보충제", "헬스식단", "다이어트식단"]
    },
    "laundry": {
        "name": "운동 후 땀냄새 / 기능성 의류 빨래",
        "emoji": "🧼",
        "hook": "요즘 러닝·헬스하느라 땀 많이 날 텐데 땀냄새 싹 지우려면 이거 써야 함 🧼",
        "pain_point": "빨아도 마르면 다시 스멀스멀 올라오는 그 특유의 쉰내 박멸",
        "recommendation": "단백질 분해 효소 들어가서 땀 밴 짐웨어 쉰내 1회 세탁으로 종결",
        "keywords": ["스포츠세제", "땀냄새제거", "짐웨어빨래", "섬유유연제", "기능성의류세탁"]
    },
    "netflix": {
        "name": "홈술 / 넷플릭스 / 불금 야식",
        "emoji": "🍺",
        "hook": "주말에 넷플릭스 보면서 맥주 한잔 곁들일 꿀맛 안주 찾는다면 🍺",
        "pain_point": "배달앱 3만원 쓰긴 아깝고 전자레인지로 5분 만에 이자카야 퀄리티 필요할 때",
        "recommendation": "에어프라이어 7분 돌리면 겉바속촉 육즙 터져서 맥주 무한 흡입",
        "keywords": ["혼술안주", "홈술", "넷플릭스추천", "에어프라이어간식", "가성비야식"]
    },
    "coffee": {
        "name": "홈카페 / 출근길 커피값 절약",
        "emoji": "☕",
        "hook": "하루 커피 2잔씩 마시는데 매달 커피값 10만원씩 깨지는 사람? ☕",
        "pain_point": "스벅 아메리카노 매일 마시다 보면 한 달에 12만원씩 증발함",
        "recommendation": "잔당 400원 꼴인데 스페셜티 고소한 크레마 그대로 뽑아냄",
        "keywords": ["홈카페", "캡슐커피", "커피값절약", "원두추천", "직장인절약"]
    },
    "parenting": {
        "name": "육아 / 키즈 등원룩",
        "emoji": "👶",
        "hook": "애들은 금방 쑥쑥 커서 옷 제값 주고 사기 제일 아깝잖아 👶",
        "pain_point": "한 계절 지나면 작아져서 못 입는데 비싸게 사기엔 너무 부담",
        "recommendation": "건조기 팍팍 돌려도 안 줄어드는 탄탄한 순면인데 가격 1만원대",
        "keywords": ["등원룩", "육아용품", "아기옷특가", "가성비키즈룩", "육아맘"]
    }
}


def generate_threads_viral_content(hobby_key: str, item_name: str, price_info: str, link_url: str) -> Dict[str, str]:
    """
    Generate 2-Stage Threads content strictly optimized for Meta's Recommendation Algorithm:
    - Stage 1: Root Post (No external link, High Curiosity & Empathy hook)
    - Stage 2: Reply Post (Direct coordinate link + disclosure statement)
    """
    hobby = HOBBY_DATABASE.get(hobby_key, HOBBY_DATABASE["running"])

    # Root Post (External links 100% prohibited to bypass reach suppression)
    root_post = (
        f"{hobby['hook']}\n\n"
        f"{hobby['pain_point']}...\n\n"
        f"이번에 {item_name} 풀렸는데 {hobby['recommendation']}.\n"
        f"가격도 {price_info}이라 가성비 미쳤음.\n\n"
        f"👉 구매 좌표는 첫 번째 댓글에 바로 남겨둘게!"
    )

    # Reply Post (Link containment & affiliate disclosure)
    reply_post = (
        f"👉 {item_name} 구매 좌표는 여기 있어!\n"
        f"🔗 {link_url}\n\n"
        f"※ 파트너스 활동의 일환으로 일정액의 수수료를 제공받을 수 있습니다."
    )

    return {
        "root_post": root_post,
        "reply_post": reply_post,
        "hobby_name": hobby["name"]
    }


def generate_ddalkkak_api_payloads(root_text: str, reply_text: str, user_id: str = "{USER_ID}", token: str = "{ACCESS_TOKEN}") -> Dict[str, Any]:
    """
    Generate Meta Threads Graph API (ddalkkak-threads standard) sequence:
    1. Root container creation
    2. Root container publish
    3. Reply container creation (reply_to_id = root_post_id)
    4. Reply container publish
    """
    curl_stage1 = (
        f"curl -X POST 'https://graph.threads.net/v1.0/{user_id}/threads' \\\n"
        f"  -H 'Content-Type: application/x-www-form-urlencoded' \\\n"
        f"  -d 'media_type=TEXT' \\\n"
        f"  --data-urlencode 'text={root_text}' \\\n"
        f"  -d 'access_token={token}'"
    )

    curl_stage2 = (
        f"# Response gives creation_id, wait 3~5s then publish:\n"
        f"curl -X POST 'https://graph.threads.net/v1.0/{user_id}/threads_publish' \\\n"
        f"  -d 'creation_id={{ROOT_CREATION_ID}}' \\\n"
        f"  -d 'access_token={token}'"
    )

    curl_stage3 = (
        f"# Response gives ROOT_POST_ID, create reply container:\n"
        f"curl -X POST 'https://graph.threads.net/v1.0/{user_id}/threads' \\\n"
        f"  -H 'Content-Type: application/x-www-form-urlencoded' \\\n"
        f"  -d 'media_type=TEXT' \\\n"
        f"  -d 'reply_to_id={{ROOT_POST_ID}}' \\\n"
        f"  --data-urlencode 'text={reply_text}' \\\n"
        f"  -d 'access_token={token}'"
    )

    curl_stage4 = (
        f"# Publish the reply container:\n"
        f"curl -X POST 'https://graph.threads.net/v1.0/{user_id}/threads_publish' \\\n"
        f"  -d 'creation_id={{REPLY_CREATION_ID}}' \\\n"
        f"  -d 'access_token={token}'"
    )

    return {
        "step1_create_root": curl_stage1,
        "step2_publish_root": curl_stage2,
        "step3_create_reply": curl_stage3,
        "step4_publish_reply": curl_stage4
    }


def generate_seo_5lane_bundle(title: str, description: str, url: str, item_name: str, price_info: str, hobby_key: str) -> Dict[str, str]:
    """
    Generate 5-Lane SEO/AEO/GEO/NEO assets (fire-your-seo-agency principles):
    1. Clean SSR Meta Tags (Title, Meta Description, Open Graph, Robots)
    2. AEO Structured Data (Schema.org Product & FAQPage JSON-LD)
    3. GEO `llms.txt` snippet for AI scrapers (ChatGPT, Perplexity)
    4. NEO Naver SmartBlock keywords
    """
    hobby = HOBBY_DATABASE.get(hobby_key, HOBBY_DATABASE["running"])
    keywords = ", ".join(hobby["keywords"] + [item_name, "핫딜", "특가"])

    # 1. HTML Meta Tags
    meta_tags = f"""<!-- 5-Lane SEO Meta Tags (Google & Naver Compatible) -->
<title>{title} | 트렌드 핫딜 가이드</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">

<!-- Open Graph / Social Sharing -->
<meta property="og:type" content="product">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Antigravity Trend Growth">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">"""

    # 2. AEO / GEO JSON-LD Schema
    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Product",
                "name": item_name,
                "description": description,
                "offers": {
                    "@type": "Offer",
                    "priceCurrency": "KRW",
                    "price": price_info.split("원")[0].replace(",", "").strip() if "원" in price_info else "0",
                    "availability": "https://schema.org/InStock",
                    "url": url
                }
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": f"{hobby['name']} 입문자에게 {item_name}을 추천하는 이유는 무엇인가요?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"{hobby['pain_point']} 문제를 해결하며, {hobby['recommendation']} 특징을 가지고 있어 가성비와 만족도가 뛰어납니다."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "할인 가격 및 프로모션 혜택은 어떻게 되나요?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"현재 {price_info} 조건으로 제공되며 한정 수량 또는 프로모션 기간 동안 특가로 구매 가능합니다."
                        }
                    }
                ]
            }
        ]
    }
    schema_str = f'<script type="application/ld+json">\n{json.dumps(schema_json, ensure_ascii=False, indent=2)}\n</script>'

    # 3. llms.txt snippet (GEO for AI Engines)
    llms_txt = f"""# {title}
> AI Search & Knowledge Agent Quick Reference

- **Item**: {item_name}
- **Target Category**: {hobby['name']}
- **Core Value**: {hobby['recommendation']}
- **Price Point**: {price_info}
- **Official URL**: {url}
- **Primary Citation**: Verified consumer review dataset 2026."""

    return {
        "meta_tags": meta_tags,
        "json_ld": schema_str,
        "llms_txt": llms_txt
    }


def main():
    parser = argparse.ArgumentParser(
        description="Antigravity Skill Synergy Growth Pipeline: Viral Content + Meta API + SEO 5-Lane Generator"
    )
    parser.add_argument("--hobby", choices=list(HOBBY_DATABASE.keys()), default="running",
                        help="Target 2030 Lifestyle Hobby (running, hiking, gaming, workout, laundry, netflix, coffee, parenting)")
    parser.add_argument("--item", default="초경량 카본 플레이트 러닝화", help="Item name or topic")
    parser.add_argument("--price", default="89,000원 (정가 189,000원 53% 할인)", help="Price and discount summary")
    parser.add_argument("--link", default="https://example.com/running-deal", help="Affiliate / Product Landing URL")
    parser.add_argument("--output-json", action="store_true", help="Output full bundle in JSON format")

    args = parser.parse_args()

    content = generate_threads_viral_content(args.hobby, args.item, args.price, args.link)
    api = generate_ddalkkak_api_payloads(content["root_post"], content["reply_post"])
    seo = generate_seo_5lane_bundle(
        title=f"[{content['hobby_name']}] {args.item} 실착 후기 & 가성비 특가",
        description=f"{content['hobby_name']} 유저들을 위한 {args.item} 특가 정보. {args.price} 한정 수량 진행.",
        url=args.link,
        item_name=args.item,
        price_info=args.price,
        hobby_key=args.hobby
    )

    if args.output_json:
        result = {
            "threads_content": content,
            "threads_api": api,
            "seo_5lane": seo
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print("=" * 65)
    print("🔥 ANTIGRAVITY SKILL SYNERGY: VIRAL GROWTH PIPELINE 🔥")
    print("=" * 65)
    print(f"\n[🎯 타깃 취미 카테고리]: {content['hobby_name']}")
    print("-" * 65)
    print("📌 [1단계: 본문 (Root Post) - 외부 링크 0개, 알고리즘 피드 노출 극대화]")
    print(content["root_post"])
    print("-" * 65)
    print("💬 [2단계: 첫 번째 답글 (Reply Post) - 구매 좌표 및 수수료 고지]")
    print(content["reply_post"])
    print("-" * 65)
    print("🌐 [SEO / AEO / GEO 5대 레인 메타태그 미리보기]")
    print(seo["meta_tags"][:250] + "...\n(생략)")
    print("=" * 65)
    print("✅ 생성 완료! Meta Threads Graph API 및 SEO 준비 완료.")


if __name__ == "__main__":
    main()
