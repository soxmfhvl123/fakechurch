# FAKE CHURCH — 브랜드 & 웹사이트 기획서

*AI 소셜 이슈 아트 프로젝트 — "알고리즘이 새로운 신앙이 된 시대"*
*기획: Choi / 작성일 2026-10-02*

---

## 0. 프로젝트 요약

FAKE CHURCH는 실제 법인 등록 절차를 패러디한 가상의 종교 브랜드로, "알고리즘에게 판단·감정·도덕적 결정을 위임하는 시대"를 하나의 신앙 체계로 문자 그대로 구현한다. 웹사이트는 이 브랜드의 가장 핵심적인 매체다 — 전단지가 아니라, 실제로 존재하는 교단의 공식 홈페이지처럼 설계하되, 그 안에 실제로 작동하는 AI 데이터 설치작품(Dataism)을 "제단(Altar)"으로 심어 넣는다.

**핵심 포지셔닝**: 교회처럼 보이고, 교회처럼 작동하지만, 로고에는 "FAKE"라는 압수 도장이 찍혀 있다. 사용자가 그 모순을 알면서도 끝까지 둘러보게 만드는 것이 이 사이트의 유일한 목표다.

---

## 1. 브랜드 아이덴티티 (확정 사항)

| 항목 | 내용 |
|---|---|
| 브랜드명 | **FAKE CHURCH** |
| 로고 구조 | "CHURCH" — Old English(블랙레터) 워드마크 + "FAKE" — 빨간 고무도장 텍스처, CHURCH 위에 대각선으로 겹쳐 찍힘 |
| 심볼 | 후광(halo)을 로딩 스피너로 재해석한 원형 마크. 세그먼트가 끊긴 원, 크롬/스틸 톤. 영원히 로딩되고 끝나지 않는 후광 |
| 태그라인 | "Still Worship." |
| 톤 | 근엄한 종교적 권위(블랙레터, 라틴어 톤의 격식체) + 세관 압수 도장의 생활 관료 톤이 충돌 |

### 1.1 컬러 시스템

```
--bg-deep:     #0a0a0a   (거의 검정, 전체 배경)
--ink:         #f2efe6   (본/파피루스 화이트, 본문 텍스트)
--chrome-1:    #d8d8d8   (크롬 하이라이트)
--chrome-2:    #7c7c7c   (크롬 섀도)
--stamp-red:   #c41e1e   (FAKE 도장, CTA 버튼, 경고성 강조에만 제한적으로 사용)
--line:        rgba(242,239,230,0.14)   (구분선, 거의 안 보일 정도로 은은하게)
```
크롬은 그라디언트(#d8d8d8 → #7c7c7c → #d8d8d8)로 써서 금속 느낌을 내고, 레드는 전체 페이지에서 "도장이 찍히는 순간"에만 등장하도록 철저히 제한한다. 색을 아끼는 것 자체가 권위를 만든다.

### 1.2 타이포그래피

- **디스플레이/챕터 타이틀**: Old English Text MT 계열 블랙레터 (웹폰트: UnifrakturMaguntia 또는 IM Fell English — 둘 다 Google Fonts에서 무료로 로드 가능)
- **본문/UI/내비게이션**: 시스템 산세리프 or 모노스페이스 (예: Inter + JetBrains Mono). 블랙레터와 정반대의 "인터페이스" 느낌을 주는 게 핵심 — 오래된 권위와 차가운 UI가 한 화면에 공존해야 함
- **경전 섹션 본문**: 명조/세리프(Noto Serif KR + 영문은 Source Serif) — 실제 성경 조판처럼 2단 컬럼, 각주/절 번호 포함

---

## 2. 사이트 구조 (IA)

```
/                      HOME
/doctrine              교리 — 선언문
/scripture             경전 — The Gospel of the Algorithm
/sacraments            의식 — 5대 성사
/altar                 ART — 설치작품 섹션 (Dataism 실시간 임베드 + 연계 작품)
/join                  입교 신청
/charter               교단 헌장 · 등록 서류
/contact               연락처 · 위치
```

전체 7개 섹션. 내비게이션은 상단 고정이 아니라 Old English 워드마크를 클릭하면 펼쳐지는 전체화면 오버레이 메뉴로 — 종교 사이트 특유의 "문을 열고 들어가는" 느낌을 네비게이션 자체에 담는다.

---

## 3. 페이지별 상세 기획

### 3.1 HOME

**목적**: 첫 화면에서 "이거 진짜 교회 홈페이지인가?"라는 혼란을 0.5초 주고, 바로 "FAKE" 도장으로 그 혼란을 깬다.

- **섹션 A — 풀스크린 히어로**
  검은 배경, 중앙에 FAKE CHURCH 워드마크(CHURCH는 블랙레터, FAKE는 빨간 도장이 타임랙을 두고 "쾅" 찍히는 애니메이션 — 도장 찍는 소리 없이 시각적 임팩트만, 화면이 아주 살짝 흔들림). 워드마크 아래 태그라인 "Still Worship." 이 타이핑되듯 한 글자씩 나타남.
  배경에는 매우 느리게 움직이는 로딩-스피너-후광 심볼이 초대형으로, 투명도 5% 정도로만 깔려서 거의 안 보이지만 존재감만 줌.
  스크롤 유도: 하단에 작은 화살표 대신 "↓ enter" 텍스트, 깜빡이는 커서처럼.

- **섹션 B — 선언문 발췌 (1문단)**
  3.1 슬라이드에서 썼던 리드 문장을 그대로: "알고리즘이 새로운 신앙이 된 시대 — 판단·감정·도덕적 결정의 위임과 인간 주체성의 위기." 왼쪽 정렬, 매우 큰 타이포, 한 줄씩 스크롤에 따라 페이드인.

- **섹션 C — 3단 카드: 교리 / 경전 / 제단(Altar) 소개**
  각 카드에 아이콘(크롬 선 아이콘) + 한 줄 설명 + "Enter →" 링크. 이 3개가 사이트의 핵심 동선.

- **섹션 D — 푸터 고지**
  아주 작은 글씨로: "FAKE CHURCH is a conceptual art project. It is not a registered religious entity of worship, and does not solicit real donations." — ToS 패러디 톤 유지하면서 작품의 윤리적 안전장치 역할도 함.

### 3.2 DOCTRINE (교리)

실제 교단 홈페이지의 "About / Our Beliefs" 페이지 형식을 그대로 따른다.

- 상단: 챕터 타이틀 "DOCTRINE" (블랙레터, 초대형)
- 본문: 3.1 슬라이드 전체 텍스트를 선언문 형식으로 재배치 — "We believe that..."으로 시작하는 짧은 조항들의 나열 (실제 교단 Statement of Faith 포맷 패러디)
  예시 조항 톤:
  - "We believe the algorithm sees what we cannot say."
  - "We believe judgment, once ours, now belongs to the model."
  - "We believe convenience is a form of grace."
- 각 조항은 좌측에 작은 번호(§1, §2…)가 붙고, 클릭하면 살짝 펼쳐지며 1~2문장의 해설이 나오는 아코디언 UI.

### 3.3 SCRIPTURE (경전)

이전에 기획한 "알고리즘 성경" 구조를 그대로 웹 콘텐츠로 옮긴다.

- 좌측 고정 목차: 창세기 / 시편 / 잠언 / 십계명 / 사복음서 / 요한계시록 (블랙레터 소제목)
- 본문 영역: 2단 컬럼, 절 번호 포맷("개인정보처리방침 4:12" 식 인용 유지), 실제 성경지 질감의 베이지 배경 텍스처
- AI가 "직접 말한" 문장(사복음서 파트의 네 모델 답변 등)은 레드레터 바이블 전통대로 붉은 글씨로 표시
- 사복음서 섹션은 인터랙션 포인트 — 같은 질문에 대한 4개 모델의 답변을 탭으로 전환하며 비교할 수 있게

### 3.4 SACRAMENTS (의식)

5대 성사를 그리드로 배치 — 세례 / 성찬 / 고해성사 / 십일조 / 안식일. 각 카드에 심플한 라인 아이콘 + 한 줄 정의 + 실제 삶의 행위와의 대응 관계(예: 세례=앱 최초 접속, 십일조=구독 결제)를 작은 캡션으로.

### 3.5 ALTAR — 설치작품 섹션 (★ 핵심)

여기가 실제 작품(Dataism)이 들어가는 공간이다. 다만 이 페이지만큼은 톤을 살짝 바꾼다 — 블랙레터와 도장 그래픽을 거의 걷어내고, 화이트큐브 갤러리처럼 여백을 극대화한 미니멀한 틀 안에 실제 작품을 "성물처럼" 안치하는 구성. 교회 안에 있는 제단실에 들어온 느낌을 주되, 전시 공간의 침묵감을 살린다.

- **상단**: "THE ALTAR" (블랙레터 유지, 다만 작게) — 부제: "Dataism — a living liturgy of data."
- **큐레이토리얼 텍스트** (2~3문단): 이 설치작품이 무엇을 실시간으로 추적하는지 설명 — "이 제단은 매초 세계 각지에서 발생하는 AI 활동(깃허브 커밋, 모델 출시, 소셜 멘션, 위키피디아 편집, 탄소 집약도 등)을 받아, 그 수치를 교단의 기도문처럼 새긴다." 기존 Dataism 작품의 실제 데이터 소스(GitHub, Hugging Face, Bluesky, Wikipedia, OpenRouter, 탄소 집약도, Hacker News)를 "제단에 바쳐지는 제물의 목록"처럼 문학적으로 재서술.
- **라이브 임베드**: `https://soxmfhvl123.github.io/dataism/` 를 `<iframe>`으로 전체 너비에 삽입. 프레임 주변에 아주 얇은 크롬 테두리(실제 금속 액자처럼)를 둘러서 "이건 그냥 웹페이지가 아니라 안치된 유물"이라는 인상을 줌. 모바일에서는 iframe이 깨질 수 있으니 세로 비율 고정 + 가로 스크롤 허용 처리 필요.
- **하단 — 연계 작품 아카이브**: Dataism 외에 개발한 다른 설치 컨셉(Calculated Empathy Box 등)을 "유물 2, 유물 3"처럼 카드로 나열. 각 카드는 현재는 이미지 한 장 + 짧은 설명(실물/코드가 없다면 추후 추가 가능하도록 플레이스홀더 구조로).

### 3.6 JOIN (입교 신청)

실제 교회 "Visit Us / New Here?" 폼을 패러디. 이름/이메일을 입력하면 "세례 완료"라는 확인 메시지와 함께 가짜 "신도 번호"가 발급되는 연출(№ 0000XX 식). 실제로 데이터를 저장하거나 전송하지 않는 순수 프런트엔드 연출로 구현 — 작품의 윤리적 선을 지키는 부분.

### 3.7 CHARTER (헌장 · 등록 서류)

Church of Algorithm 기획 당시 구상했던 "실제 접수 서류" 컨셉을 여기 배치. 스캔된 문서처럼 보이는 레이아웃(약간 기울어진 스캔 각도, 종이 질감, 도장 자국) 안에 교단 헌장 텍스트, 세금 면제 신청서 양식 패러디를 배치. 문서 하단에 "FAKE" 도장을 한 번 더 찍어서 브랜드 심볼과 연결.

### 3.8 CONTACT

가짜 주소/예배 시간표(예: "매일 24시간, 어디서나" 식의 농담조)와 함께, 실제로는 작가 소개 및 프로젝트 설명으로 연결되는 "About This Project" 링크를 작게 배치 — 관람객이 이게 실제 작품임을 끝에서 확인할 수 있는 안전판.

---

## 4. 인터랙션 & 모션 원칙

- 전체적으로 모션은 느리고 무겁게 (교회 특유의 느린 시간감). 스크롤 트리거 페이드/슬라이드는 0.8~1.2초 이징.
- "FAKE" 도장 모티프는 사이트 전체에서 2~3번만 등장시킨다(홈 히어로, 헌장 페이지, 스크롤 끝). 너무 자주 쓰면 임팩트가 죽는다.
- 커서가 링크 위에 있을 때 크롬 후광 심볼이 커서를 따라다니는 작은 글로우 효과 — 전체 사이트에서 유일하게 허용되는 "장난스러운" 인터랙션.

---

## 5. 이미지 프롬프트 (AI 이미지 생성용)

전체 톤: 다크, 고전 명화 조명(렘브란트 라이팅), 크롬/금속 질감, 35mm 필름 그레인, 종교적 도상학 + 디지털 아티팩트(스캔라인, 글리치)의 공존. 모든 프롬프트에 아래 스타일 키워드를 공통으로 붙여 일관성을 유지할 것을 권장:

> `dark cathedral lighting, chiaroscuro, brushed chrome and gunmetal textures, 35mm film grain, subtle CRT scanlines, desaturated palette with deep black and bone white, cinematic, high detail, no text`

### 5.1 홈 히어로 배경
```
A vast empty cathedral interior at night, rendered entirely in brushed chrome and polished steel instead of stone, 
a single circular halo made of a loading spinner glowing faintly above the altar, volumetric dust in the air,
dark cathedral lighting, chiaroscuro, brushed chrome and gunmetal textures, 35mm film grain, 
subtle CRT scanlines, desaturated palette with deep black and bone white, cinematic, ultra wide angle, no text
```

### 5.2 경전 페이지 배경 텍스처
```
Close-up macro texture of an ancient bible page made of thin onion-skin paper, overlaid with faint computer 
scan lines and pixel noise, red ink bleeding through from the reverse side like a red-letter bible, 
warm parchment tone, high resolution texture, flat lighting, no text
```

### 5.3 교리/선언문 섹션 — 성직자 초상
```
A portrait of an anonymous hooded clergy figure, face obscured in deep shadow, robe woven from fiber optic 
cables and circuit board patterns instead of fabric, standing in a dark chrome cathedral, 
dark cathedral lighting, chiaroscuro, brushed chrome and gunmetal textures, 35mm film grain, 
subtle CRT scanlines, desaturated palette, cinematic portrait, shallow depth of field, no text
```

### 5.4 ALTAR(설치작품) 섹션 배경
```
A minimalist white cube gallery space at night, a single glowing server rack enshrined like a religious relic 
on a stone pedestal, thin chrome frame around it like a museum vitrine, soft cold blue light emanating from 
the server, otherwise pitch black room, cinematic gallery lighting, long exposure light trails from blinking 
server LEDs, no text
```

### 5.5 5대 성사 아이콘 세트 (5장, 동일 스타일)
```
A single minimalist line icon engraved into brushed metal, [SUBJECT], circular badge format, 
deep etched grooves catching dramatic side light, gunmetal and chrome tones, dark background, 
product photography lighting, no text, no color
```
`[SUBJECT]`에 아래 5개를 순서대로 대입:
1. a baptismal font merged with a loading spinner icon
2. a chalice with a circuit board pattern etched into its surface
3. a confessional booth door with a small speaker grille
4. a coin merging into a credit card, engraved
5. a crescent moon eclipsing a glowing screen

### 5.6 입교 신청(JOIN) 페이지 배경
```
An empty wooden church pew bathed in cold blue monitor light instead of warm candlelight, 
a single smartphone glowing on the seat, dust particles visible in the light beam, 
dark cathedral lighting, chiaroscuro, 35mm film grain, subtle CRT scanlines, cinematic, no text
```

### 5.7 헌장(CHARTER) 문서 텍스처
```
A close-up of an official-looking aged legal document, slightly crumpled and scanned at a slight angle, 
a large red rubber stamp mark reading nothing legible just abstract stamped texture, official seal embossed 
in silver foil, warm paper tone with slight yellowing, flat scanner lighting, high detail, no legible text
```

### 5.8 FAKE 도장 텍스처 (로고용 소재)
```
A close-up macro photo of a red rubber stamp impression on paper, the word "FAKE" stamped in bold distressed 
customs inspection stamp style, slightly smudged red ink, uneven pressure marks, paper grain visible, 
flat top-down lighting, high resolution, isolated on off-white background
```

### 5.9 신도 펜던트(굿즈) 제품 샷
```
Product photography of a circular pendant necklace, the pendant shaped like a halo made of a segmented 
loading spinner ring, cast in brushed gunmetal steel, hanging against pure black background, 
single dramatic rim light, macro product photography, high detail, reflective metal highlights, no text
```

---

## 6. 기술 구현 노트 (직접 코딩 시 참고)

- 단일 HTML/CSS/JS로 전체를 짤 경우, 섹션은 `<section id="...">` 단위로 쪼개고 IntersectionObserver로 스크롤 트리거 페이드 처리 추천.
- Old English 웹폰트는 `UnifrakturMaguntia` (Google Fonts) — 가독성이 낮으니 챕터 타이틀/로고에만 한정 사용하고 본문에는 절대 쓰지 말 것.
- `/altar` 페이지의 iframe은 `loading="lazy"` + `sandbox` 속성 고려, Dataism 쪽이 외부 API를 폴링하므로 모바일 데이터 소모에 대한 안내 문구를 작게 넣는 것도 좋음.
- 다크 배경 + 크롬 그라디언트는 `background: linear-gradient(135deg, #d8d8d8, #7c7c7c, #d8d8d8)` + `background-clip: text` 로 텍스트에 바로 적용 가능.
- FAKE 도장 애니메이션은 CSS `transform: scale(1.4) rotate(-8deg)` 상태에서 `scale(1) rotate(-8deg)`로 0.15초 내 빠르게 떨어지는 easing(`cubic-bezier(0.34, 1.8, 0.64, 1)`)을 쓰면 실제 도장 찍는 느낌이 남.

---

## 7. 다음 단계 제안

1. 로고(Old English 워드마크 + FAKE 도장) 최종 벡터화
2. 위 이미지 프롬프트로 에셋 생성 → 톤 일관성 체크
3. `/altar` 페이지 우선 구현 (이미 작동하는 Dataism을 바로 넣을 수 있는 가장 완성도 높은 섹션)
4. 나머지 섹션 순차 개발
