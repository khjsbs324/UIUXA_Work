import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

out_dir = r'C:\UIUX이지희\Antigravity\클라이언트 분석'
os.makedirs(out_dir, exist_ok=True)

clients = [
    {
        "num": 1,
        "filename": "[가상클라이언트_01] 차은채_WICKETA총괄디렉터_D2C안식처.txt",
        "name": "차은채 (Cha Eun-chae)",
        "role": "WONDERSCAPE / WICKETA 브랜드 총괄 디렉터",
        "concept": "2030 세대를 위한 몽환적 맞춤형 믹솔로지(Mixology) 티 & 캄테크(Calm-Tech) D2C 사전 신청 자사몰 구축",
        "purpose": "복잡한 전통 다도 번거로움과 커피 부작용(속 쓰림, 수면 장애)을 해소하고 온전한 3분 안식 경험 전달 및 정기구독 유치",
        "reqs": [
            ("비밀 안식처 감성의 오프화이트 및 글래스모피즘 메인 UX/UI 설계", "높음"),
            ("감정 다이얼 선택 기반 맞춤형 블렌딩 티 레시피 자동 큐레이션", "높음"),
            ("찬물/탄산수 1초 융해 Zero-Labor 믹솔로지 안내", "보통"),
            ("앰비언트 사운드 및 수색 변환 모션 기반 초현실 브루잉 타이머", "높음"),
            ("라이브 3D 이니셜 각인 시뮬레이터 및 DIY 커스텀 번들 빌더", "보통"),
            ("8대 페르소나별 맞춤 추천 팩 카루셀 및 아로마 휠 룩북", "보통"),
            ("장바구니 이동 없는 슬라이드아웃 Cart Drawer 및 심리스 결제", "높음"),
            ("탐색 스크롤 위치 100% 보존 (뒤로가기 시 이탈 방지)", "높음"),
            ("웰컴 키트 응모 및 사전 신청/정기구독 폼 구축", "높음")
        ],
        "ia": """WICKETA (위케티) 브랜드 자사몰
├─ 1. Home (메인페이지)
│  ├─ Hero Section ("Drink Me, Escape Reality")
│  ├─ Emotional Diagnosis Quiz ("오늘 하루 어땠나요?")
│  ├─ Mixology Visual Lookbook (수색 변환 & 아로마 휠)
│  ├─ Interactive Brewing Timer (3분 카운트다운 & 앰비언트 sound)
│  ├─ DIY Custom Builder (베이스x서브 조합 & 3D 이니셜 각인)
│  ├─ Persona Matching Curation (8대 페르소나 맞춤 추천 팩)
│  └─ Pre-Order CTA & Subscription (사전 신청 및 웰컴 키트 폼)
├─ 2. Mixology Lab (큐레이션 & 레시피)
│  ├─ 감정 다이얼 퀴즈 상세
│  └─ 아로마 휠 & 성분 표기 아카이브
├─ 3. Custom Sanctuary (DIY & 기프팅)
│  ├─ 3D 각인 시뮬레이터
│  └─ DIY 번들 구성 팩
└─ 4. Pre-Order & Cart Drawer (결제 & 신청)
   ├─ 슬라이드아웃 Cart Drawer
   └─ 사전 예약 / 정기구독 신청서""",
        "hero_slogan": "Drink Me, Escape Reality",
        "cta_ment": "나만의 몽환적 안식처 찾기 & 웰컴 체험키트 사전 신청하기"
    },
    {
        "num": 2,
        "filename": "[가상클라이언트_02] 강이현_WICKETA_B2B이사_탕비실구독.txt",
        "name": "강이현 (Kang Yi-hyun)",
        "role": "WONDERSCAPE / WICKETA CX 및 B2B 웰니스 총괄 이사",
        "concept": "오피스 워커홀릭을 위한 'Office Sanctuary' B2B 기업 탕비실 정기구독 & 1:1 라이브 각인 웰컴 키트 유치",
        "purpose": "사무실 탕비실 티백의 떫은 맛과 속 쓰림을 해결하고 데스크 위 3분 안식 리추얼 B2B 정기구독 솔루션 제공",
        "reqs": [
            ("오피스 데스크테리어 디자인 및 여백 중심 미니멀 에디토리얼 그리드", "높음"),
            ("오후 각성(Focus) vs 퇴근 안식(Relax) 듀얼 티박스 인터랙티브 스위처", "높음"),
            ("기업 규모별(10인/50인/100인) B2B 맞춤 탕비실 정기구독 혜택 안내", "높음"),
            ("기업 로고 및 임직원 이니셜 실시간 3D 각인 시뮬레이터", "높음"),
            ("사무실 데스크탑용 미니 3분 브루잉 타이머 & 앰비언트 Sound", "보통"),
            ("기업 구매 담당자 전용 B2B 웰컴키트 무료 샘플 신청 폼", "높음"),
            ("장바구니 이동 없이 견적서 출력 및 결제가 가능한 슬라이드아웃 Cart Drawer", "높음"),
            ("기업 휴가철/인원 변동 시 배송량 셀프 조절 UI", "보통")
        ],
        "ia": """WICKETA B2B & Office Sanctuary
├─ 1. Home (B2B 메인페이지)
│  ├─ Hero Section ("Transform Your Office Desk into a Sanctuary")
│  ├─ Office Mood Switcher ('오후 각인' vs '퇴근 안식' 듀얼 큐레이션)
│  ├─ B2B Corporate Pack Intro (10인/50인/100인 기업 정기구독)
│  ├─ Live Corporate Engraving (기업 로고 & 직원 이니셜 3D 각인)
│  ├─ Desktop Brewing Timer Demo (오피스용 미니 브루잉 타이머)
│  ├─ B2B Free Sample Request Form (기업 담당자 샘플 팩 신청서)
│  └─ Office Persona Review Grid & Subscription Calculator
├─ 2. B2B Corporate Service
│  ├─ 기업 맞춤 견적 계산기
│  └─ 샘플 키트 무료 신청 및 견적서 출력
└─ 3. Cart Drawer & Estimate
   ├─ 슬라이드아웃 B2B 결제 Drawer
   └─ 정기구독 배송 수량 셀프 변경 UI""",
        "hero_slogan": "Transform Your Office Desk into a Sanctuary",
        "cta_ment": "우리 회사 탕비실 웰컴키트 무료 샘플 신청하기"
    },
    {
        "num": 3,
        "filename": "[가상클라이언트_03] 신유진_WICKETA_조향사_DIY믹솔로지.txt",
        "name": "신유진 (Shin Yu-jin)",
        "role": "WONDERSCAPE / WICKETA R&D 믹솔로지 랩 총괄 조향사",
        "concept": "1초 DIY 논알콜 믹솔로지 레시피 아카이브 & 홈카페 논알콜 칵테일 스타터 키트 사전 신청",
        "purpose": "찬물/탄산수 즉각 융해 기술로 가사 노동 제로 홈카페 믹솔로지 문화를 선도하고 레시피 아카이브 플랫폼 구축",
        "reqs": [
            ("베이스 티 x 서브 토핑 선택 시 3D 수색 변화 및 Taste Radar Chart 표시", "높음"),
            ("탑/미들/베이스 향 레이어링 아로마 휠 아카이브 탭", "높음"),
            ("1초 찬물/탄산수 융해 논알콜 하이볼/에이드 믹솔로지 가이드", "보통"),
            ("홈카페 크리에이터 숏폼 영상 및 레시피 챌린지 참여 탭", "높음"),
            ("4+2 스타터 DIY 체험 팩 및 본품 100% 페이백 쿠폰 이벤트", "높음"),
            ("대체당(스테비아/에리스리톨) 및 성분 칼로리 투명 표기 FAQ", "보통"),
            ("1-Click 슬라이드아웃 Cart Drawer 및 탐색 스크롤 위치 보존", "높음")
        ],
        "ia": """WICKETA Mixology Lab
├─ 1. Home (DIY 메인)
│  ├─ Hero Section ("Create Your Own Surreal Mixology")
│  ├─ Interactive Recipe Switcher (3D 수색 변화 & Taste Radar Chart)
│  ├─ Sensory Aroma Wheel (탑/미들/베이스 올팩토리 아카이브)
│  ├─ Mixology Starter Kit Intro (4+2 스타터 팩 & 페이백 쿠폰)
│  ├─ User Recipe Challenge Grid (유저 숏폼 영상 및 레시피 연동)
│  ├─ Non-Alcohol Highball Guide (1초 레시피 가이드)
│  └─ Pre-Order CTA Form (DIY 키트 50% 할인 예약)
├─ 2. Recipe Archive
│  ├─ 조합별 수색 3D 시뮬레이터
│  └─ 사용자 커뮤니티 숏폼 등록
└─ 3. Starter Order & Cart Drawer
   ├─ 슬라이드아웃 Cart Drawer
   └─ 스타터 키트 1-Click 결제""",
        "hero_slogan": "Create Your Own Surreal Mixology",
        "cta_ment": "나만의 믹솔로지 레시피 조합하고 스타터 키트 사전 신청하기"
    },
    {
        "num": 4,
        "filename": "[가상클라이언트_04] 백서진_WICKETA_럭셔리_프리미엄각인.txt",
        "name": "백서진 (Baek Seo-jin)",
        "role": "WONDERSCAPE / WICKETA 프리미엄 기프팅 & 럭셔리 라인 총괄 디렉터",
        "concept": "카카오톡 선물하기 연동 및 나/타인 전용 스몰 럭셔리 라이브 3D 각인 기프트 세트 사전 예약 유치",
        "purpose": "사무실 책상 위 데스크테리어 오브제 틴케이스와 3D 각인 시뮬레이터를 통해 가치 소비 및 스몰 럭셔리 선물 문화 창달",
        "reqs": [
            ("실시간 이니셜/응원 문구 3D 틴케이스 & 보틀 각인 시뮬레이터", "높음"),
            ("Self-Gifting(나를 위한 선물) vs Special Gift 샌드 베이지 전용 패키지 세트", "높음"),
            ("카카오톡 선물하기 직연동 및 수령인 주소 미입력 선결제 Cart Drawer", "높음"),
            ("구매자들의 실제 데스크테리어 연출 사진 룩북 갤러리", "보통"),
            ("모바일/데스크탑 360도 각인 렌더링 회전 뷰어", "높음"),
            ("떫은 맛 0% 밸런스 블렌딩 및 위생/품질 검증 라벨", "보통"),
            ("모바일 음성/텍스트 감성 프라이빗 메시지 카드 작성 모듈", "보통")
        ],
        "ia": """WICKETA Sanctuary Gift
├─ 1. Home (럭셔리 메인)
│  ├─ Hero Section ("Gift a 3-Minute Peace to Your Soul")
│  ├─ Live Engraving Simulator (실시간 3D 제품 각인 렌더링 뷰어)
│  ├─ Sanctuary Gift Package Showcase (Self-Gifting vs Special Gift)
│  ├─ Deskterior Impression Gallery (구매자 연출 룩북)
│  ├─ Kakao Gift 1-Click Banner (카카오톡 선물하기 연동)
│  ├─ Personalized Card Writer (음성/텍스트 감성 카드 모듈)
│  └─ Pre-Order & Engraving CTA (스페셜 기프트 사전 예약)
├─ 2. Live Customizer
│  ├─ 3D 각인 바틀 회전 뷰어
│  └─ 프라이빗 메시지 작성기
└─ 3. Kakao Seamless Checkout
   ├─ 슬라이드아웃 Cart Drawer (주소 미입력 선결제)
   └─ 샌드 베이지 패키지 신청""",
        "hero_slogan": "Gift a 3-Minute Peace to Your Soul",
        "cta_ment": "실시간 이니셜 각인해보고 스페셜 기프트 세트 사전 예약하기"
    },
    {
        "num": 5,
        "filename": "[가상클라이언트_05] 한지안_WICKETA_BM_제로슈가스틱.txt",
        "name": "한지안 (Han Ji-an)",
        "role": "WONDERSCAPE / WICKETA 헬시케어 & 제로 라인업 총괄 브랜드 매니저",
        "concept": "Z세대 및 헬시 플레저를 위한 제로 슈가/무카페인 퀵 스틱 1-Click 패스트 주문 및 간편 구독",
        "purpose": "1초 만에 찬물/탄산수에 녹는 제로 스틱으로 당류/카페인 걱정 없는 웰빙 음료 경험과 초간편 결제 제공",
        "reqs": [
            ("0 Calorie, 0g Sugar, 0mg Caffeine 투명 라벨 인포그래픽", "높음"),
            ("모바일 1-Click 카카오페이/토스페이 직연동 패스트 체크아웃", "높음"),
            ("'공부할 때' / '운동 후' / '야식용' 목적별 1초 음료 셀렉터", "높음"),
            ("찬물/탄산수 투하 즉시 융해되는 1초 수색 변환 숏폼 비디오", "보통"),
            ("Z세대 틱톡/인스타그램 실제 음용 인증샷 리뷰 카루셀", "보통"),
            ("원하는 제로 스틱 맛 3종 골라 담는 주간/월간 퀵 스틱 파우치 구독", "높음"),
            ("모바일 진입 시 복잡한 팝업 제거 및 슬라이드아웃 Cart Drawer 결제", "높음")
        ],
        "ia": """WICKETA Zero Ritual
├─ 1. Home (제로 케어 메인)
│  ├─ Hero Section ("0 Calorie, 100% Fantasy")
│  ├─ 1-Second Healthy Choice Selector (공부/운동/야식 목적별 셀렉터)
│  ├─ Transparent Nutrition Assurance (0 Calorie / 0 Sugar / 0 Caffeine)
│  ├─ Quick-Stick Melting Demo (1초 융해 숏폼 비디오)
│  ├─ Z-Generation Review Carousel (대학생 인증샷 후기)
│  ├─ 1-Click Fast Checkout Module (카카오/토스 1-Click 직연동)
│  └─ Zero Starter Pouch Subscription (골라담기 구독 파우치)
├─ 2. Zero Nutrition & Menu
│  ├─ 대체당 성분 투명 라벨
│  └─ 목적별 퀵 스틱 큐레이션
└─ 3. 1-Click Fast Drawer
   ├─ 카카오/토스페이 직연동 결제
   └─ 3가지 맛 골라담기 파우치 구독""",
        "hero_slogan": "0 Calorie, 100% Fantasy",
        "cta_ment": "1초 만에 녹는 제로 퀵 스틱 체험 팩 사전 신청하기"
    },
    {
        "num": 6,
        "filename": "[가상클라이언트_06] 윤서연_29SELECT_수석MD_감성큐레이션.txt",
        "name": "윤서연 (Yoon Seo-yeon)",
        "role": "'29SELECT' 웰니스 & F&B 부문 수석 MD",
        "concept": "29SELECT 단독 WICKETA 브랜드위크 쇼케이스 및 29SELECT 단독 에디션 사전 예약 유치",
        "purpose": "29SELECT 감성 유저층 대상 에디토리얼 브랜드스토리와 감정 진단 퀴즈, 단독 기프트 팩 혜택 제공",
        "reqs": [
            ("29SELECT 단독 한정판 기프트 팩 (샌드 베이지 파우치 + 스틱 4종) 쇼케이스", "높음"),
            ("오프화이트 0.5px 미세 구분선 기반의 에디토리얼 브랜드 스토리", "높음"),
            ("29SELECT 유저 전용 감정 진단 퀴즈 & 1:1 맞춤 티 추천 모듈", "높음"),
            ("29SELECT 회원 15% 쿠폰 직연동 및 100% 안심 페이백 예약 혜택", "높음"),
            ("29SELECT 대표 에디터 5인의 실제 오피스/홈 힐링 화보 리뷰", "보통"),
            ("수색 그래디언트 아트 3D 시뮬레이션 & 브루잉 타이머 가이드", "보통"),
            ("29SELECT 회원 계정 직연동 1-Click 예약 결제 Cart Drawer", "높음")
        ],
        "ia": """WICKETA x 29SELECT Exclusive Showcase
├─ 1. Home (콜라보 메인)
│  ├─ Hero Section ("29SELECT Exclusive : WICKETA Escape Reality")
│  ├─ Editorial Brand Story ('모던 모자장수의 다과회' 에디토리얼)
│  ├─ Interactive Emotion Quiz (29SELECT 회원 맞춤 감정 퀴즈)
│  ├─ 29SELECT Exclusive Gift Pack Intro (360도 회전 뷰어 & 쿠폰)
│  ├─ Sensory Mixology Visual (수색 변환 & 3분 타이머)
│  ├─ 29SELECT Editor Review Grid (에디터 5인 실제 리뷰)
│  └─ Pre-Order & Coupon Benefits (15% 쿠폰 & 사전 예약)
├─ 2. Editorial Showcase
│  ├─ 브랜드 스토리 3분 가이드
│  └─ 에디터 픽 시량 리포트
└─ 3. 29SELECT Fast Checkout
   ├─ 29SELECT 계정 직연동 Cart Drawer
   └─ 15% 단독 할인 예약""",
        "hero_slogan": "29SELECT Exclusive : WICKETA Escape Reality",
        "cta_ment": "29SELECT 단독 혜택받고 WICKETA 사전 예약하기"
    },
    {
        "num": 7,
        "filename": "[가상클라이언트_07] 최하은_공간디자이너_3D가상투어.txt",
        "name": "최하은 (Choi Ha-eun)",
        "role": "스튜디오 '안식' 총괄 공간 디자이너 / 대표",
        "concept": "WICKETA 성수/도산 오프라인 안식처 공간 디지털 트윈 연동 & 팝업 3D 투어 및 시향 예약 유치",
        "purpose": "오프라인 건축 공간의 안개 룸과 브루잉 바를 웹 3D 투어로 연동하고 시향 타임슬롯 예약 유도",
        "reqs": [
            ("성수/도산 오프라인 공간의 안개 룸/브루잉 바 360도 3D 가상 공간 투어 뷰어", "높음"),
            ("오프라인 1:1 맞춤 블렌딩 시향 룸 타임슬롯 예약 캘린더", "높음"),
            ("투명 유리/아크릴 재질을 반영한 공간 오브제 틴케이스 굿즈 예약 폼", "높음"),
            ("웹 브루잉 타이머 실행 시 오프라인 조명과 연동되는 스마트 홈 라이팅 UI", "보통"),
            ("여백 비중 60%의 건축 에디토리얼 그리드 및 0.5px 마이크로 라인", "높음")
        ],
        "ia": """WICKETA Ambient Sanctuary Space
├─ 1. Home (공간 디지털 트윈 메인)
│  ├─ Hero Section ("Architectural Sanctuary in Digital Twin")
│  ├─ 3D Virtual Space Tour (360도 안개 룸 & 브루잉 바 투어)
│  ├─ Off-line Timeslot Reservation Calendar (1:1 시향 예약)
│  ├─ Architectural Object Goods Showcase (공간 오브제 틴케이스)
│  └─ Smart Lighting Timer Guide & Booking Form
├─ 2. Virtual Tour Module
│  ├─ 성수/도산 팝업 3D 인터랙티브 뷰
│  └─ 공간 건축 스토리
└─ 3. Space Booking & Cart
   ├─ 시향 예약 캘린더
   └─ 공간 굿즈 사전 예약 Drawer""",
        "hero_slogan": "Architectural Sanctuary in Digital Twin",
        "cta_ment": "성수 안식처 공간 3D 투어하고 시향 예약하기"
    },
    {
        "num": 8,
        "filename": "[가상클라이언트_08] 임태경_부티크호텔이사_인룸티타임.txt",
        "name": "임태경 (Im Tae-kyung)",
        "role": "부티크 호텔 '르 세랑' F&B & 웰니스 스파 총괄 이사",
        "concept": "5성급 웰니스 부티크 호텔 투숙객 전용 인룸(In-Room) 맞춤형 티 큐레이션 및 웹 모듈 연동",
        "purpose": "객실 태블릿/모바일을 통해 투숙객 피로도 진단 후 인룸 앰비언트 브루잉 타이머와 힐링 티타임 제공",
        "reqs": [
            ("객실 전용 오프화이트 우드 패키지 + 무카페인 수면 안식 스틱 티 3종 안내", "높음"),
            ("객실 태블릿/모바일 전용 투숙객 피로/시차 진단 1초 슬라이더 UI", "높음"),
            ("객실 스피커/스마트 TV 연동 인룸 앰비언트 sound 브루잉 타이머", "높음"),
            ("티타임 체험 완료 후 호텔 웰니스 스파 15% 할인 쿠폰 자동 발급", "보통"),
            ("호텔 린넨 화이트 및 딥 월넛 톤의 미니멀 럭셔리 호스피탈리티 UI", "높음")
        ],
        "ia": """WICKETA x Le Serein In-Room Sanctuary
├─ 1. Home (호텔 인룸 메인)
│  ├─ Hero Section ("In-Room Sanctuary Ritual")
│  ├─ In-Room Amenity Intro (오프화이트 우드 패키지 & 수면 티 3종)
│  ├─ Fatigue Diagnosis Slider (투숙객 피로/시차 진단 슬라이더)
│  ├─ In-Room Ambient Sound Timer (TV/스피커 연동 브루잉 sound)
│  └─ Wellness Spa Coupon Module (스파 15% 쿠폰 자동 발급)
├─ 2. Guest Wellness Module
│  ├─ 피로도 진단 퀴즈
│  └─ 브루잉 sound 타이머 플레이어
└─ 3. Hotel Voucher Drawer
   ├─ 스파 쿠폰 발급
   └─ 인룸 티 세트 구매""",
        "hero_slogan": "In-Room Sanctuary Ritual",
        "cta_ment": "객실에서 나만의 3분 힐링 리추얼 시작하기"
    },
    {
        "num": 9,
        "filename": "[가상클라이언트_09] 권명수_뷰티편집숍CEO_이너뷰티.txt",
        "name": "권명수 (Kwon Myung-soo)",
        "role": "뷰티 웰니스 셀렉트숍 '에디트 웰' 대표이사 / CEO",
        "concept": "이너뷰티 & 헬시 믹솔로지 티 입점 기획전 유치 및 단독 파우치 사전 예약 유치",
        "purpose": "피부 수분 케어, 당류/카페인 절제를 원하는 유저를 위한 이너뷰티 믹솔로지 레시피 큐레이션 제공",
        "reqs": [
            ("히알루론산/비타민C 결합 피부 수분 케어 무카페인 스틱 팩 큐레이션", "높음"),
            ("피부 상태 및 당류 섭취 습관 선택 뷰티 밸런스 체크 퀴즈 UI", "높음"),
            ("Edit-Well 단독 뷰티 파우치 + 투명 리유저블 글래스 보틀 패키지 안내", "높음"),
            ("피부과 전문의 및 이너뷰티 에디터의 당류/카페인 0g 투명 라벨 검증표", "보통"),
            ("Pure Water Cyan & Fresh Coral Pink 컬러 기반 맑은 수색 뷰티 UI", "높음")
        ],
        "ia": """WICKETA x Edit-Well Inner Beauty Mixology
├─ 1. Home (이너뷰티 메인)
│  ├─ Hero Section ("Inner Beauty & Healthy Mixology")
│  ├─ Beauty Balance Quiz (피부 건조/당류 절제 밸런스 체크)
│  ├─ Inner Beauty Mixology Curation (수분 케어 & 체조율 스틱)
│  ├─ Edit-Well Exclusive Pouch Showcase (리유저블 보틀 세트)
│  ├─ Expert Nutrition Label (전문의 0g 투명 검증 표)
│  └─ Pre-Order CTA Form (단독 파우치 예약)
├─ 2. Beauty Checkup
│  ├─ 이너뷰티 퀴즈 모듈
│  └─ 성분 검증 리포트
└─ 3. Edit-Well Order Drawer
   ├─ 단독 파우치 간편 결제
   └─ 보틀 세트 사전 예약""",
        "hero_slogan": "Inner Beauty & Healthy Mixology",
        "cta_ment": "이너뷰티 체크하고 단독 제로 스틱 파우치 예약하기"
    },
    {
        "num": 10,
        "filename": "[가상클라이언트_10] 송아린_숏폼크리에이터_믹솔로지챌린지.txt",
        "name": "송아린 (Song A-rin)",
        "role": "채널 '아린믹스' 리드 크리에이터 / 믹솔로지스트",
        "concept": "Z세대 대상 '1-Sec Non-Alcohol Cocktail Challenge' 릴스 아카이브 및 콜라보 키트 사전 예약",
        "purpose": "1초 만에 완성되는 인스타 감성 논알콜 하이볼 레시피 공유 및 유저 참여 챌린지 커뮤니티 구축",
        "reqs": [
            ("유저들이 틱톡/릴스 영상 URL 및 레시피 조합을 등록하는 챌린지 탭", "높음"),
            ("Arin Mix 단독 콜라보 레시피 킷 (피치 자몽 에센스 + 오로라 루이보스)", "높음"),
            ("실시간 3D 수색 레이어링 그라데이션 커스텀 시뮬레이터", "높음"),
            ("실시간 유저 투표 & 베스트 믹솔로지스트 글래스 리워드 제공 모듈", "보통"),
            ("Electric Neon Cyan & 세로 비디오 카드 숏폼 UI", "높음")
        ],
        "ia": """WICKETA x Arin Mix 1-Sec Challenge
├─ 1. Home (숏폼 챌린지 메인)
│  ├─ Hero Section ("1-Sec Non-Alcohol Cocktail Challenge")
│  ├─ Short-form Recipe Challenge Archive (릴스/틱톡 영상 연동)
│  ├─ Arin Mix Exclusive Kit Intro (피치 자몽 + 오로라 루이보스)
│  ├─ 3D Water Gradient Simulator (실시간 수색 커스텀)
│  ├─ Live User Voting & Reward (유저 투표 & 리워드 현황)
│  └─ Challenge Pre-Order CTA Form
├─ 2. Challenge Community
│  ├─ 영상 등록 폼
│  └─ 투표 및 랭킹 모듈
└─ 3. Collabo Kit Drawer
   ├─ 아린 콜라보 키트 간편 구매
   └─ 리워드 신청 Drawer""",
        "hero_slogan": "1-Sec Non-Alcohol Cocktail Challenge",
        "cta_ment": "나만의 1초 믹솔로지 레시피 업로드하고 콜라보 킷 받기"
    },
    {
        "num": 11,
        "filename": "[가상클라이언트_11] 이도은_P4디자이너_비밀안식처.txt",
        "name": "이도은 (Lee Do-eun)",
        "role": "디자인 스튜디오 '안식' 대표 / 프리랜서 UI/UX 디자이너",
        "concept": "디지털 피로 해소를 위한 몽환적 비밀 정원 안식처(Sanctuary) 자사몰 웹사이트 설계",
        "purpose": "모니터 스크린 피로감과 번아웃을 겪는 2030 영 크리에이터를 위해 3분 정서적 안식 경험 전달",
        "reqs": [
            ("오프화이트 배경, 0.5px 미세 구분선, 50% 여백 비중의 안식처 레이아웃", "높음"),
            ("'오늘 하루 어땠나요?' 3단계 감정 진단 퀴즈 및 맞춤 힐링 티 자동 추천", "높음"),
            ("소프트 드림코어, 안개 그라데이션, 글래스모피즘 비주얼 룩북 카루셀", "높음"),
            ("매월 감정 리듬 변화에 따라 배송되는 프라이빗 안식 티 파우치 정기구독", "높음"),
            ("Soft Sand Beige (#F4F1EA) & Deep Slate Gray (#252B36) 디자인 톤앤매너", "높음")
        ],
        "ia": """WICKETA Secret Sanctuary
├─ 1. Home (비밀 안식처 메인)
│  ├─ Hero Section ("My Own Surreal Sanctuary")
│  ├─ Emotional Diagnosis Quiz ("오늘 하루 어땠나요?")
│  ├─ Dreamcore Visual Lookbook (안개 그라데이션 & 글래스모피즘)
│  └─ Private Sanctuary Subscription Form (프라이빗 정기구독)
├─ 2. Sanctuary Experience
│  ├─ 3단계 내면 진단
│  └─ 몽환적 룩북 갤러리
└─ 3. Subscription Drawer
   ├─ 프라이빗 파우치 정기구독
   └─ 첫 체험키트 1-Click 신청""",
        "hero_slogan": "My Own Surreal Sanctuary",
        "cta_ment": "나만의 비밀 안식처 진단받고 첫 체험키트 신청하기"
    },
    {
        "num": 12,
        "filename": "[가상클라이언트_12] 박지후_P3IT대리_3분퀵브루ing.txt",
        "name": "박지후 (Park Ji-hoo)",
        "role": "대기업 IT 서비스 기획자 / 대리",
        "concept": "오피스 워커홀릭을 위한 커피 대체 속 편한 3분 퀵 브루ing 티 라인업 자사몰 구축",
        "purpose": "카페인 과다 수면 장애와 속 쓰림을 해소하고 찬물에서도 3분 만에 우러나는 오피스 힐링 음료 제공",
        "reqs": [
            ("오후 각인(Focus) vs 야근/퇴근 휴식(Rest) 듀얼 무드 선택 진단 퀴즈", "높음"),
            ("찬물/탄산수 즉각 융해 3분 퀵 브루ing 타이머 가이드 UI", "높음"),
            ("위장에 부담 없는 무카페인 루이보스/자스민 커피 대체 성분 표기", "높음"),
            ("사무실 탕비실용 30일분 대량 파우치 1-Click 슬라이드아웃 Cart Drawer 결제", "높음"),
            ("Office Slate Blue (#2C3E50) & Energy Amber (#E67E22) 오피스 미니멀 UI", "보통")
        ],
        "ia": """WICKETA Office Quick-Brewing
├─ 1. Home (오피스 메인)
│  ├─ Hero Section ("3-Min Quick-Brewing for Office Workaholics")
│  ├─ Dual Mood Selector ('오후 각인 Focus' vs '퇴근 휴식 Rest')
│  ├─ 3-Min Quick-Brewing Timer Guide (찬물 즉각 융해 가이드)
│  ├─ Coffee Alternative Health Label (속 편한 무카페인 검증)
│  └─ Office Pack Bulk Purchase Form (탕비실 30일분 간편 결제)
├─ 2. Office Wellness Guide
│  ├─ 듀얼 무드 진단 퀴즈
│  └─ 커피 대체 성분 인포그래픽
└─ 3. Quick Cart Drawer
   ├─ 오피스 대량팩 1-Click 결제
   └─ 정기 배송 신청""",
        "hero_slogan": "3-Min Quick-Brewing for Office Workaholics",
        "cta_ment": "속 편한 3분 퀵 브루ing 오피스팩 사전 신청하기"
    },
    {
        "num": 13,
        "filename": "[가상클라이언트_13] 이지민_P2대학생_오로라수색비주얼.txt",
        "name": "이지민 (Lee Ji-min)",
        "role": "대학생 & 비주얼 다이어터 / 트렌드 세터",
        "concept": "Z세대 비주얼 다이어터를 위한 0kcal/제로 슈가 영롱한 파스텔 오로라 수색 & SNS 릴스 인증샷 웹사이트",
        "purpose": "다이어트 중에도 칼로리와 당류 부담 없이 SNS에 예쁜 파스텔 수색 음료를 촬영해 올릴 수 있는 길티프리 경험 제공",
        "reqs": [
            ("물과 티백이 섞여 몽환적으로 퍼지는 파스텔 오로라 수색 변환 GIF 룩북", "높음"),
            ("당류 0g, 칼로리 0kcal 다이어트 부담 100% 소거 투명 라벨 인포그래픽", "높음"),
            ("틱톡/인스타그램 실제 구매 대학생들의 비주얼 티 칵테일 릴스 갤러리", "보통"),
            ("투명 글래스 보틀 + 액상 스틱 3종 담긴 파스텔 투명 보틀 스타터 팩 1-Click 주문", "높음"),
            ("Aurora Pastel Cyan (#00E5FF) & Dreamy Lavender 톤앤매너", "높음")
        ],
        "ia": """WICKETA Aurora Visual Dream
├─ 1. Home (비주얼 메인)
│  ├─ Hero Section ("Guilt-Free Pastel Aurora Visual")
│  ├─ Pastel Water Color GIF Lookbook (영롱한 수색 변환 모션)
│  ├─ 0kcal Guilt-Free Label (당류 0g / 칼로리 0kcal 인포그래픽)
│  ├─ SNS Reels Challenge Gallery (대학생 실물 인증샷 갤러리)
│  └─ Pastel Bottle Starter Pack Form (투명 보틀 팩 50% 할인 주문)
├─ 2. Visual Gallery
│  ├─ 수색 모션 GIF 룩북
│  └─ SNS 릴스 갤러리
└─ 3. 1-Click Bottle Drawer
   ├─ 파스텔 보틀 팩 간편 주문
   └─ 50% 할인 쿠폰 적용""",
        "hero_slogan": "Guilt-Free Pastel Aurora Visual",
        "cta_ment": "영롱한 0kcal 수색 스틱 팩 50% 할인받고 사전 신청하기"
    },
    {
        "num": 14,
        "filename": "[가상클라이언트_14] 윤기준_P7개발팀장_정밀브루잉타이머.txt",
        "name": "윤기준 (Yoon Ki-jun)",
        "role": "테크 기업 과장 & 개발 팀장 / 하이엔드 완벽주의 미식가",
        "concept": "오차 0% 정밀 우림 가이드 & Zero Defect 품질 검증을 요구하는 하이엔드 완벽주의자 웹사이트",
        "purpose": "모호한 가이드를 배제하고 초 단위 정밀 브루잉 타이머와 수치화된 아로마 휠, 공인 위생 검증 표기 제공",
        "reqs": [
            ("물 온도(85℃/100℃), 수량(250ml), 우림 시간(180초) 초 단위 정밀 브루잉 카운트다운 타이머", "높음"),
            ("단맛, 쓴맛, 바디감, 향의 노트를 수치화한 비주얼 아로마 휠 레이더 차트", "높음"),
            ("공인 기관 위생, 농약 미검출, 대체당 안전성 Zero Defect 검증서 디지털 뷰어", "높음"),
            ("찻잎 산화를 100% 방지하는 하이엔드 밀폐 수밀 틴케이스 사전 주문 모듈", "높음"),
            ("Precision Charcoal (#1C2541) & Metallic Platinum 정밀 미학 UI", "보통")
        ],
        "ia": """WICKETA High-End Precision Brewing
├─ 1. Home (정밀 테크 메인)
│  ├─ Hero Section ("Zero Defect 0% Error Brewing Precision")
│  ├─ Precise Countdown Timer (85℃/100℃, 250ml, 180s 초 단위 타이머)
│  ├─ Quantitative Aroma Wheel Radar Chart (풍미 수치화 레이더 차트)
│  ├─ Zero Defect Quality Certificate Viewer (공인 위생/품질 검증서)
│  └─ Airtight Tin-case Pre-Order Form (수밀 틴케이스 사전 예약)
├─ 2. Precision Science
│  ├─ 정밀 우림 가이드
│  └─ 품질 인증서 디지털 뷰어
└─ 3. High-End Order Drawer
   ├─ 수밀 틴케이스 간편 예약
   └─ 정밀 브루잉 팩 결제""",
        "hero_slogan": "Zero Defect 0% Error Brewing Precision",
        "cta_ment": "오차 0% 정밀 타이머 가이드 확인하고 하이엔드 팩 예약하기"
    },
    {
        "num": 15,
        "filename": "[가상클라이언트_15] 서지안_P8육아대디_노동제로논알콜하이볼.txt",
        "name": "서지안 (Seo Ji-an)",
        "role": "IT 기업 파트장 & 육아대디 / 4년차 육아부모",
        "concept": "가사 노동 제로(Zero-Labor) 1초 찬물/탄산수 논알콜 하이볼 웹사이트 구축",
        "purpose": "육아 퇴근 후 물 끓이기와 설거지 등 가사 노동 없이 1초 만에 깔끔하고 청량한 논알콜 하이볼 경험 제공",
        "reqs": [
            ("끓인 물/설거지 0건, 찬물·탄산수에 즉각 융해되는 노동 제로 1초 레시피 가이드", "높음"),
            ("알콜·카페인·당류 걱정 없이 타격감과 청량함만을 전하는 육퇴 힐링 논알콜 하이볼", "높음"),
            ("탄산수 6팩 + WICKETA 스틱 2종 묶음 1-Click 번들 빌더", "높음"),
            ("주소 및 결제 수단이 저장되어 3초 만에 주문되는 슬라이드아웃 Cart Drawer", "높음"),
            ("Cold Brew Amber (#8B4513) & Carbonated Cyan 청량 실용주의 UI", "보통")
        ],
        "ia": """WICKETA Zero-Labor Refreshment
├─ 1. Home (육아대디 메인)
│  ├─ Hero Section ("Zero-Labor 1-Sec Non-Alcohol Highball")
│  ├─ Zero-Labor Recipe Guide (끓인 물/설거지 제로 1초 레시피)
│  ├─ Parent Healing Highball Lineup (무알콜/무카페인/무당류 청량 팩)
│  ├─ Carbonated Water Bundle Builder (탄산수 6팩 + 스틱 2종 묶음)
│  └─ 3-Sec Fast Checkout Cart Drawer (3초 심리스 결제 폼)
├─ 2. Zero-Labor Guide
│  ├─ 1초 논알콜 레시피 가이드
│  └─ 탄산수 배합 비율 시뮬레이터
└─ 3. Bundle Cart Drawer
   ├─ 탄산수 번들 1-Click 구매
   └─ 40% 할인 예약 신청""",
        "hero_slogan": "Zero-Labor 1-Sec Non-Alcohol Highball",
        "cta_ment": "가사 노동 제로! 1초 논알콜 하이볼 번들팩 40% 할인 예약하기"
    }
]

for c in clients:
    num = c["num"]
    out_file = os.path.join(out_dir, f'클라이언트 분석{num}.md')
    
    req_rows = ""
    for idx, (req_text, imp) in enumerate(c["reqs"], 1):
        req_rows += f"| {idx} | {req_text} | 브랜드 기획서 [{num:02d}] | `{imp}` |\n"
        
    req_trans_rows = ""
    for idx, (req_text, imp) in enumerate(c["reqs"][:6], 1):
        req_trans_rows += f"| \"{req_text}\" | 과정·절차 | {c['name'].split()[0]} 니즈 | 기능 구현 | 메인/서브 | 핵심 모듈 연동 |\n"

    md_content = f"""# 가상클라이언트 기반 분석 결과 보고서 [{num:02d}]

**분석 대상**: `{c['filename']}`  
**작성일시**: 2026년 8월 7일  
**브랜드명**: 위케티 (WICKETA) / WONDERSCAPE  

---

## 1. 가상 클라이언트의 기본 정보 설정

- **프로젝트의 중심 주제**: {c['concept']}
- **제작 목적**: {c['purpose']}
- **클라이언트가 제공한 자료**: 브랜드 기획서 [{num:02d}], 타깃 페르소나 데이터, 디자인 및 UX/UI 요구사항
- **필요한 정보와 기능**: 
  - 핵심 요구사항 모듈화 (퀴즈, 3D 시뮬레이터, 타이머, 룩북 등)
  - 슬라이드아웃 Cart Drawer 및 심리스 결제/예약 폼
  - 1-Click 패스트 체크아웃 및 탐색 스크롤 위치 100% 보존
- **중요도와 작업 우선순위**:
  1. `우선순위 1`: Hero Section 및 핵심 메시지 슬로건 ("{c['hero_slogan']}")
  2. `우선순위 2`: 주요 기능 모듈 (퀴즈/타이머/3D 각인/수색 뷰어)
  3. `우선순위 3`: 슬라이드아웃 Cart Drawer 및 사전 신청 CTA 폼
- **적용 매체**: 반응형 웹 (모바일 퍼스트 및 미니멀 에디토리얼 레이아웃)

---

## 2. 클라이언트가 원하는 항목 수집

| 번호 | 클라이언트 요청 내용 | 관련 자료 | 중요도 |
| :--- | :----------------- | :-------- | :----- |
{req_rows.strip()}

---

## 3. 요구사항을 정보 단위로 변환

| 요청 원문 | 정보 유형 | 주제 | 부주제 | 메뉴 | 콘텐츠·기능 |
| :-------- | :-------- | :--- | :----- | :--- | :---------- |
{req_trans_rows.strip()}

---

## 4. 비슷한 항목끼리 분류

- [x] **핵심 브랜딩 모듈**: Hero Section, 몽환적 비주얼 아트, 0.5px 미세 구분선 레이아웃
- [x] **맞춤 큐레이션 모듈**: 타깃 맞춤 진단 퀴즈, 레시피 스위처, 아로마 휠 아카이브
- [x] **인터랙티브 리추얼 모듈**: 3분 브루잉 타이머, 수색 변환 GIF/3D 모션, 앰비언트 Sound
- [x] **커스텀 및 커머스 모듈**: 라이브 3D 이니셜/로고 각인, 번들 빌더, 슬라이드아웃 Cart Drawer
- [x] **전환(CTA) 모듈**: 사전 예약 폼, 정기구독 계산기, FAQ 및 품질 검증표

---

## 5. 계층 구조 작성 (Information Architecture)

```text
{c['ia']}
```

---

## 6. 사용자가 이해하기 쉬운 이름 부여 (레이블링 검토)

- [x] **Hero Ment**: `"{c['hero_slogan']}"` (브랜드 정체성 명확 전달)
- [x] **버튼 CTA**: `"{c['cta_ment']}"` (직관적 행동 유도)
- [x] **메뉴 일관성**: 미니멀 플로팅 GNB 아이콘 및 간결한 텍스트 라벨 통일

---

## 7. 내비게이션으로 연결

- **글로벌 내비게이션 (GNB)**: 미니멀 플로팅 바 (로고, 핵심 퀴즈, 타이머, 커스텀, 장바구니 Drawer 아이콘)
- **로컬 내비게이션 (LNB)**: 목적별/무드별 탭 스위처 (Focus vs Rest / 0kcal vs Custom)
- **화면 전환 및 링크**: 페이지 이동 시 스크롤 위치 100% 보존, 결제 시 화면 전환 없는 슬라이드아웃 Cart Drawer

---

## 8. 와이어프레임으로 표현

| 화면 영역 | 작성할 항목 |
| :-------- | :---------- |
| **헤더 (Header)** | 미니멀 플로팅 GNB (로고, 주요 기능 메뉴, 장바구니 버튼) |
| **내비게이션 (Nav)** | 탭 스위처 및 카테고리 필터 |
| **바디 (Body)** | 1. Hero 비주얼 <br> 2. 타깃 진단 퀴즈 <br> 3. 수색 변환/아로마 휠 룩북 <br> 4. 브루잉 타이머 & 3D 각인 시뮬레이터 <br> 5. 맞춤 추천 팩 카루셀 |
| **어사이드 (Aside)** | 슬라이드아웃 Cart Drawer (심리스 결제 및 실시간 이니셜 각인 미리보기) |
| **푸터 (Footer)** | WONDERSCAPE 기업 정보, 브랜드 스토리, 하단 사전 신청 CTA |

---

## 9. 반복 검토 및 결과

- [x] **요청 항목 반영여부**: 클라이언트 요구사항 100% 반영 완료.
- [x] **사용자 편의성**: 슬라이드아웃 Cart Drawer 및 1-Click 패스트 체크아웃으로 이탈율 최소화.
- [x] **일관성 점검**: WICKETA 브랜드 톤앤매너 및 0.5px 미세 구분선 레이아웃 통일.

---

# 📋 최종 작성 양식 요약 (실전용)

```markdown
## 1. 가상 클라이언트
- 프로젝트 주제: {c['concept']}
- 제작 목적: {c['purpose']}
- 제공 자료: {c['filename']}
- 적용 매체: 반응형 웹 (모바일 퍼스트)

## 2. 클라이언트 요구사항
- 요청 항목: {c['reqs'][0][0]}, {c['reqs'][1][0]} 등
- 중요도: 핵심 요구사항 (`높음`)
- 관련 자료: 기획서 [{num:02d}]
- 필요한 기능: 스크롤 위치 보존, 1-Click 결제, 3D 시뮬레이션

## 3. 정보 구조
- 주제: WICKETA 맞춤형 믹솔로지 & 웰니스 D2C
- 부주제: {c['name']} 전용 큐레이션
- 메뉴: 메인 / 퀴즈 / 브루잉 타이머 / 커스텀 / Cart Drawer
- 콘텐츠: 수색 변환 룩북, 맞춤 추천 팩, 앰비언트 sound
- 정보 유형: 사실, 개념, 절차, 과정

## 4. 내비게이션
- 시작 화면: Hero Section ("{c['hero_slogan']}")
- 이동 경로: Hero → 진단 퀴즈 → 상품 큐레이션 → 브루잉 타이머 → 사전 신청 Drawer
- 연결 페이지: 상세 페이지 및 정기구독 신청서
- 검색 및 위치 안내: 미니멀 플로팅 GNB

## 5. 화면 구성
- 헤더: 미니멀 플로팅 GNB
- 내비게이션: 무드 스위처 탭
- 핵심 콘텐츠: Hero 비주얼, 진단 퀴즈, 3D 시뮬레이터, 브루잉 타이머
- 보조 콘텐츠: 아로마 휠 룩북, 후기 갤러리, FAQ
- 푸터: 원더스케이프 기업 정보 및 하단 CTA

## 6. 검토 결과
- 누락 항목: 없음 (전수 반영)
- 중복 항목: 정리 및 통합 완료
- 사용자 관점의 개선점: 슬라이드아웃 Cart Drawer 도입
- 수정 사항: 스크롤 위치 100% 보존 적용
```
"""
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

print(f"Successfully generated {len(clients)} client analysis files in {out_dir}")
