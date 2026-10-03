# FAKE CHURCH — SHOP 실버 주얼리 썸네일 프롬프트

*무드 레퍼런스: 헤비 핸드카빙 925 실버, 블랙 산화 처리, 고딕 크로스·백합문양 계열 (King Kroach / Chrome Hearts 류의 질감)*
*모티프는 전부 FAKE CHURCH 자체 심볼(로딩 후광, FAKE 도장, 커서, 성사)로 치환*

> ⚠️ 프롬프트에 실제 브랜드명은 넣지 않는다. 넣으면 모델이 해당 브랜드의 로고·시그니처 디자인(십자 플러스, 대거 등)을 그대로 박아버려서, 실제 판매할 샵 이미지로는 쓸 수 없게 된다. 질감은 아래 공통 블록의 묘사로 충분히 나온다.

---

## 0. 썸네일 규격 (샵 그리드 통일용)

- 비율 **4:5 세로** (1080×1350) — 샵 그리드 카드용. 정사각 그리드면 1:1로만 바꿔서 같은 프롬프트 사용
- 배경 **#0a0a0a 매트 블랙** (사이트 `--bg-deep`과 일치 → 카드 테두리 없이 자연스럽게 녹음)
- 제품이 프레임의 약 60% 차지, 정중앙, 같은 앵글 → 그리드에 깔았을 때 크기·위치가 들쭉날쭉하지 않게
- 제품 1개당 3컷 권장: **① 메인 썸네일 ② 호버용 착용컷 ③ 상세페이지 매크로**

---

## 1. 공통 스타일 블록 (모든 프롬프트 뒤에 그대로 붙이기)

```
heavy hand-carved 925 sterling silver, cast gothic silverwork, deep blackened oxidized recesses contrasting with high-polish raised surfaces, slightly worn antique patina, chunky weight, visible hand-finished tool marks,
studio product photography, centered on seamless matte black background, resting on black glossy acrylic with a faint soft reflection, single hard key light from upper left, thin cool chrome rim light, deep shadows, 100mm macro lens, f/8, razor sharp detail, 4:5 vertical composition, object fills 60% of frame,
no text, no logo, no watermark, no hands, no props
```

### 네거티브 (지원 모델만)
```
gold, brass, colored gemstones, cheap plating, plastic look, blurry, extra objects, brand logo, watermark, text, cluttered background, white background, gradient background
```

---

## 2. 제품별 프롬프트 — `[PRODUCT]` 자리에 넣고 뒤에 공통 블록

### 01. HALO.LOADING — 시그넷 링
```
A thick sterling silver band ring, the band formed by eight separate curved arc segments like a loading spinner icon, one segment missing leaving a gap, each segment's edge carved with tiny gothic beaded borders, shown at three-quarter angle standing upright,
```

### 02. SEAL OF FAKE — 스탬프 시그넷 링
```
A heavy oval signet ring in sterling silver, the flat face engraved with a recessed rectangular rubber-stamp border with distressed uneven edges, a single ornate blackletter capital letter F deeply carved in the center, shoulders of the ring carved with gothic fleur-de-lis scrollwork, three-quarter angle,
```
> 글자 깨지면 face를 빈 상태로 생성 → 글자는 후보정에서 Brotheric 폰트로 합성 (사이트 폰트와 통일됨)

### 03. CURSOR CROSS — 펜던트
```
A gothic cross pendant in sterling silver, each of the four arms ending in a sharp arrowhead shaped like a computer mouse pointer, the center of the cross holds a small segmented halo ring, cross surface carved with fine gothic tracery, hanging from a thick silver bail, flat front view,
```

### 04. ROSARY OF REFRESH — 묵주 체인 목걸이
```
A long sterling silver rosary-style necklace, chain of small round silver beads alternating with tiny segmented halo rings every tenth bead, ending in a small gothic cross drop, arranged in a loose elegant loop on the surface, top-down view,
```

### 05. TITHE COIN — 코인 메달리온 펜던트
```
A thick hand-hammered sterling silver coin medallion pendant, raised relief of a segmented loading-spinner halo in the center radiating thin light rays, coin edge reeded with fine ridges, outer ring carved with gothic beaded border, heavy bail on top, flat front view,
```

### 06. CONFESSION — 스피커 그릴 스터드 이어링 (페어)
```
A pair of round sterling silver stud earrings, each face perforated with tiny holes arranged like a speaker grille forming a gothic rose window pattern, domed and heavy, blackened inside the holes, pair placed side by side slightly angled,
```

### 07. CROWN OF CABLES — 뱅글
```
A thick sterling silver bangle bracelet shaped like a crown of thorns made from twisted braided cables, small sharp thorns protruding along the braid, one thin cable end terminating in a tiny connector plug, standing upright at three-quarter angle,
```

### 08. STILL WORSHIP — 와이드 커프
```
A wide sterling silver cuff bracelet, surface deeply carved with gothic cathedral window tracery and a flowing scroll banner ribbon across the center, scroll left blank, edges with raised beaded borders, standing upright at three-quarter angle showing the opening,
```
> 배너에 "STILL WORSHIP" 각인은 후보정 합성

### 09. BELIEVER № — 신도 번호 태그 목걸이
```
A thick rectangular sterling silver dog tag pendant with rounded corners, a raised gothic border frame, deeply stamped serial number "No. 0001" in the center, small segmented halo ring engraved above the number, on a silver ball chain arranged in a curve, flat front view,
```

### 10. PEW KEY — 열쇠 키링/월렛체인 참
```
An ornate antique church key in sterling silver, the bow (handle) shaped like a gothic quatrefoil with a segmented halo ring inside, the shaft long and twisted, the key bit replaced by a flat USB connector shape, hanging from a heavy silver ring with a short curb chain, flat front view at slight angle,
```

### 11. LITTLE HALO — 드롭 이어링 (싱글)
```
A single sterling silver drop earring, a small gothic cross dangling beneath a tiny segmented halo ring, attached to a thick silver hoop, hanging vertically, flat front view,
```

### 12. SACRAMENT CHALICE — 펜던트
```
A small chalice-shaped pendant in sterling silver, the cup surface etched with fine circuit board traces that resolve into gothic tracery near the rim, heavy stem and base, hanging from a thick bail, three-quarter angle,
```

---

## 3. 호버용 착용컷 (썸네일 위에 마우스 올리면 바뀌는 2번째 이미지)

```
Close-up of [PRODUCT, worn on finger / around neck / on wrist / on ear], model's skin pale with cool tone, wearing black clothing, face cropped out of frame, dark moody chiaroscuro lighting, single hard side light, matte black background, 35mm film grain, desaturated palette with deep black and bone white, 4:5 vertical, no text, no logo
```

## 4. 상세페이지 매크로 (디테일 컷)

```
Extreme macro close-up of the carved surface of [PRODUCT], showing hand-carved tool marks, blackened oxidized crevices and polished raised edges, shallow depth of field, raking side light emphasizing texture, matte black background, no text
```

---

## 5. 생성 팁

- **1번 제품을 먼저 뽑고 그 결과를 레퍼런스 이미지로 고정** → 나머지 11개는 "match the lighting, background and silver finish of the reference image" 한 줄 추가. 이게 그리드 톤 통일에 가장 효과 큼
- 각인 텍스트(F, STILL WORSHIP, № 0001)는 모델이 거의 다 뭉갬 → 빈 면으로 생성 후 Brotheric으로 합성 추천
- 실버가 너무 새것처럼 반짝이면 `heavily oxidized, darker patina` 추가 / 너무 탁하면 `more mirror polish on raised areas`
- 배경이 순흑이 아니게 나오면 썸네일 후보정에서 #0a0a0a로 레벨 맞추기 (사이트 배경과 1px 경계 안 생기게)
